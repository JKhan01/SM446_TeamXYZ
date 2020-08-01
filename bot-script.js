
const SOCKETIO_URL = 'http://localhost:4000';
const socket = io.connect(SOCKETIO_URL, {});
const initSocket = function() {
    socket.on('connect', () => {
        console.log('socket connected');
    });
    
    socket.on('disconnect', () => {
        console.log('socket disconnected');
    });
    
    socket.on('recognize', (results) => {
        console.log('recognized:', results);
    });
}



const addBotMessage = function(message) {
    var template = `<div class="message-container"><div class="message bot-message">${message}</div></div>`
    var messageContainer = document.getElementById('chatcontainer');
    messageContainer.innerHTML = messageContainer.innerHTML + template;
}

const addHumanMessage = function(message) {
    var template = `<div class="message-container"><div class="message human-message">${message}</div></div>`

    var messageContainer = document.getElementById('chatcontainer');
    messageContainer.innerHTML = messageContainer.innerHTML + template;
}

const enterListener = function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        var inputData = document.getElementById("inputbox");
        if (inputData.value !== "") {
            addHumanMessage(inputData.value);
        }
        inputData.value = "";
    }
}

let shouldStop = true;
let stopped = true;



const handleSuccess = function(stream) {
    initSocket();
    let recordButton = document.getElementById('mic');
    let downloadLink = document.getElementById('download');
    const options = {
        mimeType: 'audio/webm'
    }
    const recordedChunks = [];
    const mediaRecorder = new MediaRecorder(stream, options);

    mediaRecorder.addEventListener('dataavailable', function(e) {
        if (e.data.size > 0) {
            socket.emit('stream-data', e.data);
            recordedChunks.push(e.data);
        }
    });

    mediaRecorder.addEventListener('stop', function() {
        downloadLink.href = URL.createObjectURL(new Blob(recordedChunks));
        downloadLink.download = 'ffff.wav';
        console.log('stopped');
    });
    recordButton.onclick = function () {
        
        if (mediaRecorder.state === "inactive") {
            console.log('start');
            mediaRecorder.start(1000)
            document.getElementById('micicon').className="fa fa-stop";
        } else {
            console.log('stop');
            socket.emit('stream-reset');
            mediaRecorder.stop();
            document.getElementById('micicon').className="fa fa-microphone";
        }
    }
}

const startRecording = function() {
    shouldStop = false;
    stopped = true;
}

const stopRecording = function() {
    shouldStop = true;
    stopped = false;
}

navigator.mediaDevices.getUserMedia({
    audio: true,
    video: false
}).then(handleSuccess);



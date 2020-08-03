
const SOCKETIO_URL = 'http://localhost:4000';
const CHAT_BASE_URL = 'http://localhost:5000';
const DOWNSAMPLING_WORKER = './downsampling_worker.js';
// const socket = io.connect(SOCKETIO_URL, {});

// const initSocket = function() {
//     socket.on('connect', () => {
//         console.log('socket connected');
//     });
    
//     socket.on('disconnect', () => {
//         console.log('socket disconnected');
//     });
    
//     socket.on('recognize', (results) => {
//         console.log('recognized:', results);
//         addBotMessage(results.text)
//     });
// }



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

const doTextRequest = function(message) {
    return axios.post(`${CHAT_BASE_URL}/chat`, {
        query: message
    });
}

const enterListener = function(e) {
    if (e.keyCode === 13) {
        // e.preventDefault();
        var inputData = document.getElementById("inputbox");
        if (inputData.value !== "") {
            addHumanMessage(inputData.value);
            doTextRequest(inputData.value)
            .then(function (res) {
                console.log(res);
                res.data.forEach(printFunction);  
                function printFunction(value,index,array)
                {
                    addBotMessage(value.reply);    
                };
                
            }).catch(function (err) {
                console.error('Something went wrong');
                console.error(err);
            });
        }
        inputData.value = "";
    }
}

let shouldStop = true;
let stopped = true;


// const createAudioProcessor = function(audioContext, audioSource) {
//     let processor = audioContext.createScriptProcessor(4096, 1, 1);
//     const sampleRate = audioSource.context.sampleRate;
//     let downsampler = new Worker(DOWNSAMPLING_WORKER)
//     downsampler.postMessage({
//         command: "init",
//         inputSampleRate: sampleRate
//     });
//     downsampler.onmessage = (e) => {
//         if (socket.connected) {
//             socket.emit('stream-data', e.data.buffer);
//         }
//     }
//     processor.onaudioprocess = (event) => {
//         var data = event.inputBuffer.getChannelData(0);
//         downsampler.postMessage({
//             command: "process",
//             inputFrame: data
//         });
//     }

//     processor.shutdown = () => {
//         processor.disconnect();
//     }

//     processor.connect(audioContext.destination);

//     return processor;
// }

// initSocket();
// started = false;

// const recordButton = document.getElementById('mic');
// var audioContext;
// recordButton.onclick = function () {
    
//     var mediaStream;
//     var mediaStreamSource;
//     var streamProcessor;
        
//     if (started === false) {
//         audioContext = new AudioContext();
//         started = true;
//         const success = function(stream) {
//             mediaStream = stream;
//             mediaStreamSource = audioContext.createMediaStreamSource(mediaStream);
//             streamProcessor = createAudioProcessor(audioContext, mediaStreamSource)
//             mediaStreamSource.connect(streamProcessor);   
//         }
//         const fail = (e) => {
//             console.log('recording failure', e);
//         }
//         if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
// 			navigator.mediaDevices.getUserMedia({
// 				video: false,
// 				audio: true
// 			})
// 			.then(success)
// 			.catch(fail);
// 		}
// 		else {
// 			navigator.getUserMedia({
// 				video: false,
// 				audio: true
// 			}, success, fail);
// 		}
//         document.getElementById('micicon').className="fa fa-stop";
//     } else {
//         started = false;
//         if (mediaStream) {
//             mediaStream.getTracks()[0].stop();
//         }
//         if (mediaStreamSource) {
//             mediaStreamSource.disconnect();
//         }
//         if (streamProcessor) {
//             streamProcessor.shutdown();
//         }
//         if (audioContext) {
//             audioContext.close();
//         }
//         document.getElementById('micicon').className="fa fa-microphone";
//     }
// }

// const startRecording = function() {
//     shouldStop = false;
//     stopped = true;
// }

// const stopRecording = function() {
//     shouldStop = true;
//     stopped = false;
// }




# Jarvis (software robot assistant) for corporations [SM446]
The developed software is a Python-based web application(Flask) which acts as an assistant to corporate firms or as an Intelligent Product Manager (IPM). The software’s input interface is a microphone and its output interfaces are a speaker and email. The software provides a voice controlled interface that executes numerous tasks that are carried out in corporate offices on a daily basis. 

### Technical Details 
#### Abstract Architecture diagram of the project.
##### Architecture diagram for chat:
<div align="center">
  <img src="https://github.com/DeftNinja/SIH2020/blob/master/IMG-20200803-WA0007.jpg"><br><br>
</div>


## Getting Started


### Prerequisites
All the dependencies required to run the app are available in [reqirements.txt](https://github.com/JKhan01/SM446_TeamXYZ/blob/master/backend/requirements.txt).

The application also requires a Redis server for session storage and a MongoDB server which is our primary database.

You can choose a hosted service for both these requirement, or you can choose to host them yourself.
Download links and hosting information is available at the following links:
- [Redis](https://redis.io/)
- [Mongo](https://www.mongodb.com/)

The application also requires a browser and python(>3) to function.
Python can be downloaded from [link](https://www.python.org/), installation instructions are also provided at the link.

### Installing
To install the dependencies:
1. Navigate to backend directory
2. Open a terminal and enter `pip3 install -r requirements.txt`

## Deployment
To start the backend service:
1. Navigate to backend directory.
2. Create a file with the name .env
3. Add the following lines of code<br>
```
SECRET_KEY=
MONGO_URL=
REDIS_URL=
```
4. Set the variables (there should be no space after '='). SECRET_KEY can be any randomly generated string. MONGO_URL and REDIS_URL give the URL's to the MongoDB and Redis services respectively.
5. Start the server with `flask run`

To host the frontend:
1. Navigate to frontend directory.
2. Open a terminal and run `python3 -m http.server`. By default the service will start on port 8000.
3. Navigate to `http://localhost:8000/jarvis.html` to access the bot.

## Built With
- [Python](https://www.python.org/) -  The software is based on Python.
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Additionally it also uses Javascript.
- Atlassian APIs:
  - [JIRA API](https://developer.atlassian.com/server/jira/platform/rest-apis/) -  Used to access and execute tasks on the JIRA board.
  - [Bitbucket API](https://developer.atlassian.com/bitbucket/api/2/reference/) - Used to access the company’s Bitbucket repository.
  - [Confluence API](https://docs.atlassian.com/atlassian-confluence/REST/6.6.0/) - Used to access and execute tasks on the Confluence board.
- [Gmail API](https://developers.google.com/gmail/api) - Used to access and send the company’s email.
- [Web Speech API](https://wicg.github.io/speech-api/) - Used for speech recognition and speech to text.
- [Redis](https://redis.io/documentation) - Used for session management. 
- [Rasa](https://rasa.com/docs/) - A chatbot framework used to understand, interpret end-user queries and appropriately fetch response data over REST and scraping.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) -  It is a python micro-framework which will be used to provide a web interface. 


## Authors
#### Team XYZ:
* Shritej Patil
* Jamaluddin Khan
* Pooja More
* Nikunj Gaonkar
* Om Rao
* Rohit Kadam
#### Mentors:
* Tanmay Gujar
* Dylan Dsouza

## License
This project is licensed under the Apache-2.0 License - see the [LICENSE.txt](https://github.com/JKhan01/SM446_TeamXYZ/blob/master/LICENSE.txt) file for details.

## Acknowledgments
* [Font Awesome](https://cdnjs.com/libraries/font-awesome)
* [Choose a license](https://choosealicense.com/community/) 
* [Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/)
* [JacobLett](https://codepen.io/JacobLett/pen/QrpJEp)
* [Purplebooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)


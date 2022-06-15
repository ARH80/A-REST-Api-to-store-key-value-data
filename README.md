# A REST Api to store key-value data

A simple example of using REST API and http client in Python. This project contains a service providing REST API and a command line tool that uses the service.

## Preconditions:

- Python 3
## Server:
The server contains two python files, the api file has a class that stores the data inside a dictionary. This dictionary saves value and history for each key, the value is the last one which is set and the history is an array of all values from the time the server started. Each element of history array has a  value and a timestamps that helps us to find out when a specific value was set. The Api class has some functions to handle requests using that dictionary.
In the main file we use the functions in api file and a package named fastapi to recieve GET and POST requests and send back the response.
## Steps to run server:
### Clone the project

```
git clone https://github.com/ARH80/A-REST-Api-to-store-key-value-data.git
```

### Install dependencies
In the project directory run the command below.
```
pip install -r requirements.txt
```

### Run server
Please run the following command in the project directory. this will run the server on localhost on port 8000.

```
uvicorn server.main:app --reload
```
By the time you run the server, you can open http://127.0.0.1:8000/docs to see details about this REST api and test all of the methods.
## Client
The client communicates with server on 127.0.0.1:8000 and has these commands.
- set key1 value1 : This command sends a POST request to server and server adds this record to history and sets the value.
- get key1 : This command sends a GET request to server and server returns its latest value.
- history key1 : This command sends a GET request to server and server returns the history of key.
- quit : Use this command to terminate the program.

### Run client
Move to client directory and run the main file. Then enter commands as mentioned above.

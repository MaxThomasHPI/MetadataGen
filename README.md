# MetadataGen
This is a generator for metadata according to the MOOChub format.

## Install

### Prerequisites

The application is made to be run un Ubuntu 22.04.
Make sure the system is up-to-date.

```
sudo apt update && sudo apt upgrade
```

The source code can be cloned using Git.

```
sudo apt install git
```

The application is a Docker image. 
Docker can be installed via snap.

```
sudo snap install docker
```

### Get data from source

Get the data from the GitHub repository:


```
git clone https://github.com/MaxThomasHPI/MetadataGen.git
```

### Set environment variables

Make sure to set all environment variables in the .env file before build/start the docker containers.
 
#### Gemini key

Since the program uses the Gemini-API from Google, a valid key for this application needs to be provided.
It needs to be stored in an environment variable called "GEMINI_KEY".
The key has to work with the gemini-2.5-flash model.
Add the key in the .env variable at the root level.

```
# .env
GEMINI_KEY=<Your Gemini-API key>
```

#### Postgres

There is a database running in the background to log input data and the suggestions made.
The database is set up in a local bind and will take environment variables as provided in the .env file.
This includes a username for the database as well as a password.
A default database called "suggestions" will be set up as well. 
Please do not change the name of the database.

````
# .env
POSTGRES_USER=<your-psql-username>
POSTGRES_PASSWORD=<your-psql-password>
POSTGRES_DB=suggestions  # the default database to be created at startup, do not change!
````

### Setup and run docker container

The repository contains a Dockerfile and a docker-compose.yml for setting up an image.
Go to the directory containing the Dockerfile/docker-compose.yml and run:

```
sudo docker compose up --build
```

The application should start but can also be started with:

```
sudo docker compose up
```

after successfully building the image.


### Configuration

The application will run by default on Port 5000 (default Flask).
Port 80 will be exposed as stated in the Dockerfile.
In the docker-compose.yml the mapping (80:5000) is configured.
Also, the nginx.conf contains the mapping.
If you prefer another configuration make sure to update these files accordingly.
With this setup the application frontend can be reached via accessing http://localhost in the browser.

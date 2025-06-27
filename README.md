# MetadataGen
This is a generator for metadata according to the MOOChub format.

## Install

### Prerequisites

The application is made to be run un Ubuntu 22.04.
Make sure the system is up-to-date.

```
sudo apt update && sudo apt upgrade
```

The source code can be cloned using git.

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
https://github.com/MaxThomasHPI/MetadataGen

```
git clone https://github.com/MaxThomasHPI/MetadataGen.git
```

### Set environment variable - Gemini key

Since the program uses the Gemini-API from Google, a valid key for this application needs to be provided.
It needs to be stored in an environment variable called "GEMINI_KEY".
The key has to work with the gemini-1.5-flash model.
Add the key in the .env variable at the root level.

```
# .env
GEMINI_KEY=<Your Gemini-API key>
```

### Setup and run docker container

The repository contains a Dockerfile and a docker-compose.yml for setting up an image.
Go to the directory containing the Dockerfile/docker-compose.yml and run:

```
sudo docker-compose up --build
```

The application should start but can also be started with:

```
sudo docker-compose up
```

after successfully building the image.

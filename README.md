# MetadataGen
This is a generator for metadata according to the MOOChub format

## Install

### Prerequisites

The application is made to be run un Ubuntu 22.04.
Make sure the system is up to date.

```
sudo apt update && sudo apt upgrade
```

The source code can be cloned using git.

```
sudo apt install git
```

The application is a Docker image. 
Docker can be install via snap.

```
sudo snap install docker
```

### Get data from source

Get the data from the GitHub repository:
https://github.com/MaxThomasHPI/MetadataGen

```
git clone https://github.com/MaxThomasHPI/MetadataGen.git
```

### Setup docker container

The repository contains a Dockerfile for setting up an image.
Go to the directory containing the Dockerfile and run.

```
sudo docker build .
```

---
layout: default
nav_order: 2
title: Installing Bento on Your Local Machine - DEMO Mode
---

# Installing Bento on Your Local Machine - DEMO Mode


## Introduction
This describes how to install Bento on your local machine in DEMO mode. DEMO mode ... 

The Bento-Local environment is designed to run directly within Docker on a user’s workstation. This allows users to create and deploy their local copy of Bento with minimal changes to their local environment and allows a configuration that can be used with different workstation operating systems. 
Bento-local consists of 3 components hosted within Docker containers and a separate Dataloader container that will be shut down after running the dataloader scripts. Depending on configuration options the build can take several minutes. When the build is complete the Bento components will be configured as follows:


**Front End:**

* Local URL:	http://localhost/
* Note: The Frontend container will make requests to the backend over port 8080. This container is built using a local checkout of the bento-frontend repository.

**Back End:**  

* Local URL:	http://localhost:8080/
* Note: The Backend container will make requests to Neo4j over port 7474 and pass requested data to the Frontend. This container is built using a local checkout of the bento-backend repository.

**Neo4j:**

* Local URL:	http://localhost:7474/
* Note: The Neo4j container holds the graph database for the Bento system and will return data to the Backend when requested

**Dataloader:**

* Note: The Dataloader container will load a locally stored data set into the graph database hosted
within the Neo4j container. This container will not continue running after data has been
loaded.

## Installing Docker
To install Docker choose from the following options: Windows/Mac or Linux

**Install Docker Desktop for Windows/Mac:**

Docker Desktop is an application for MacOS and Windows machines for the building and sharing of containerized applications and microservices. It can be downloaded from: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

Once Docker Desktop has been installed docker commands can be run from Powershell or terminal windows.

**Install Docker on Linux:**

On Linux the following commands can be used to install required Docker components. 
NOTE: all Linux commands in this document were tested on CentOS 7 and may require changes if used on other Linux distributions

First, install docker:

```bash
curl -fsSL https://get.docker.com/ | sh
```

Then, install docker-compose:

```bash
curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
```


## Installing Bento

After installing Docker perform the following tasks from the command line to finish setting up Bento:

### Get the Bento-local scripts:

The bento-local scripts can be found in Github at: [https://github.com/CBIIT/bento-local](https://github.com/CBIIT/bento-local) NOTE: these scripts are available on the master branch

You can pull these onto your local workstation using any git client you have installed.

### Configure Environment settings for your local instance

The bento-local scripts require defining a `.env` file alongside the bento-local `docker-compose.yml`. This file will be pulled as part of the Git repo and should be updated with the following settings:

```
FRONTEND_SOURCE_FOLDER=<value>  set to your local copy of the frontend code
NOTE: this folder MUST be located within the bento-local folder
BACKEND_SOURCE_FOLDER=<value>  set to your local copy of the backend code
NOTE: this folder MUST be located within the bento-local folder
NEO4J_USER=<value>  the user name to set for Neo4j
NEO4J_PASS=<value>  the password to set for Neo4j
```

Note that the location of the FRONTEND_SOURCE_FOLDER and BackEND_SOURCE_FOLDER is important. The bento-local scripts will only have access to files located within the root of your bento-local checkout.

### Run the Bento-local Environment

The docker-compose files for bento-local have been written to make use of Buildkit and the Docker CLI. The commands used for docker-compose should set these options as active by passing environment variables as:

***Windows (powershell):***

```
$Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose <command>
```

***Linux/Mac:***

```
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose <command>
```


For the purposes of this document the Linux/Mac version of this command will be used.

### Commands for running Bento-local services:

To build and load bento infrastructure (from the root of the Bento-local project):

	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up -d

To rebuild an individual container (NOTE: The available containers for this command are: bento-backend, bento-frontend, neo4j):

	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up -d --no-deps --build <service_name>

To build and run the dataloader container:

	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose -f dataloader.yml up --build bento-dataloader

To stop a container:

	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down <service_name>

To stop all bento-local containers:

	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down

To clean docker objects for all stopped containers (this command can be used to return to a clean system and start over with new configurations):

	docker system prune -a

To clean all docker volumes (NOTE: this will remove any data loaded into Neo4j):

	docker system prune --volumes

To attach a shell to a running container:

	docker exec -it <container name> /bin/bash   (use /bin/ash for frontend and backend containers as they are based on alpine)


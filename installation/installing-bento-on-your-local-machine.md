---
layout: default
nav_order: 1
title: Installing Bento on Your Local Machine 
---

# Installing Bento on Your Local Machine

## Introduction
The Bento-Local environment is designed to run directly within Docker on a user’s workstation. This allows users to create and deploy their local copy of Bento with minimal changes to their local environment and allows a configuration that can be used with different workstation operating systems. 

The scripts for this project are separated into folders for its three different modes:
* Build Mode:  this will create production ready Docker containers for the frontend and backend bento projects. This mode requires users to have local copies of the bento-frontend and bento-backend repositories. Note that when using build mode there are no changes made to the source code made during the build process, any changes or configurations made to the user's local copy of the source code will be reflected in the build.
* Dev Mode:  this will create Docker containers for the frontend and backend bento projects suitable for local development. Note that in this mode configuration changes will be made during the build process to set configurations to local resources and the frontend website will reflect live changes made in the user's local copy of the source code.
* Demo Mode: this will load pre-configured bento Docker containers pulled from Docker Hub.

The bento-local environment should be launched from within the folder of the desired run mode and all local copies of source code and configuration files should reside within that folder as well.


Bento-local consists of three components hosted within Docker containers and a separate Dataloader container that will be shut down after running the dataloader scripts. Depending on configuration options the build can take several minutes. When the build is complete the Bento components will be configured as follows:


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

* The Dataloader container will load a locally stored data set into the graph database hosted within the Neo4j container. This component requires local copies of the bento-backend and bento-model repositories as well as a local copy of the data to be loaded. This container will not continue running after data has been loaded.

## Installing Docker
To install Docker choose from the following options:

**Install Docker Desktop:**

Docker Desktop is an application for MacOS and Windows machines for the building and sharing of containerized applications and microservices. It can be downloaded from: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

Once Docker Desktop has been installed docker commands can be run from Powershell or terminal windows.

**Install Docker Engine:**

Instructions for installing Docker Engine can be found at: [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

If choosing this option docker-compose will need to be installed separately. Instructions for installing docker-compose can be found at: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)


## Installing Bento

After installing Docker perform the following tasks from the command line to finish setting up Bento:

### Get the Bento-local scripts:

The bento-local scripts can be found in Github at: [https://github.com/CBIIT/bento-local](https://github.com/CBIIT/bento-local) NOTE: these scripts are available on the master branch

You can pull these onto your local workstation using any git client you have installed.

### Get the Bento Source code:

The bento-local scripts require local checkouts of the bento-frontend and bento-backend repositories. These should be cloned into folders within the root of the project you are building - for dev_mode this should be located at bento-local/dev_mode/bento-frontend and bento-local/dev_mode/bento-backend. Note that the name of the folder you clone the repo to can change, but the repo MUST be within the root of the project.
The Bento repositories are located at:

* bento-frontend: https://github.com/CBIIT/bento-frontend.git
* bento-backend: https://github.com/CBIIT/bento-backend.git

You can pull these onto your local workstation using any git client you have installed. Note that the bento-local build will use the actual code you have pulled locally when it builds - if you require features from a specific branch you must clone that branch specifically. For a vanilla install of Bento the master branch will be sufficient.

### Configure Environment settings for your local instance

The bento-local scripts require defining a `.env` file alongside the bento-local `docker-compose.yml`. This file will be pulled as part of the Git repo and should be updated with the following settings:

```
FRONTEND_SOURCE_FOLDER=<value>  set to your local copy of the frontend code
NOTE: this folder MUST be located within the bento-local folder
BACKEND_SOURCE_FOLDER=<value>  set to your local copy of the backend code
NOTE: this folder MUST be located within the bento-local folder
BENTO_DATA_MODEL=<value>  set to your local copy of the bento data model. used only by the bento-dataloader
NOTE: this folder MUST be located within the bento-local folder
NEO4J_USER=neo4j  the user name to set for Neo4j - this should remain as the default value of "neo4j" for local neo4j containers
NEO4J_PASS=<value>  the password to set for Neo4j
```

Note that the location of the FRONTEND_SOURCE_FOLDER, BACKEND_SOURCE_FOLDER, and BENTO_DATA_MODEL is important. The bento-local scripts will only have access to files located within the root of your bento-local checkout.

### Run the Bento-local Environment

***docker-compose environment variables:***

The docker-compose files for bento-local have been written to make use of Buildkit and the Docker CLI. The commands used for docker-compose should set these options as active by passing environment variables as:

* Windows: ```$Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1;```

* Linux/Mac: ```COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1```

For the commands listed in this document these variables will be shown as "<env_vars>", when running docker-compose commands replace this string with the correct version of the environment variables for your system .

### Commands for running Bento-local services:

To build and load bento infrastructure (from the root of the Bento-local project):

	<env_vars> docker-compose up -d

To rebuild an individual container (NOTE: The available containers for this command are: bento-backend, bento-frontend, neo4j):

	<env_vars> docker-compose up -d --no-deps --build <service_name>
	
To stop all running bento-local containers:

	<env_vars> docker-compose down

To stop a single running container:

	<env_vars> docker-compose down <service_name>
	
To clean docker objects for all stopped containers (this command can be used to return to a clean system and start over with new configurations):

	docker system prune -a

To clean all docker volumes (NOTE: this will remove any data loaded into Neo4j):

	docker system prune --volumes

To attach a shell to a running container:

	docker exec -it <container name> /bin/bash   (use /bin/ash for frontend and backend containers as they are based on alpine)


### Commands for running the Bento-local dataloader:
Note that the dataloader requires the following local resources:
* A local copy of the bento-backend source code. This will be used to supply schema files. The location of this folder must be within the root folder of the version of bento-local you are using and its location is set by the BACKEND_SOURCE_FOLDER variable in .env.
* A local copy of the bento-model source code. This will be used to supply data model files. The location of this folder must be within the root folder of the version of bento-local you are using and its location is set by the BENTO_DATA_MODEL variable in .env.
* A local copy of the data you intend to load. This data must be configured to match the Bento data model and schema and located in a folder named "data" within the bento-local project (ex. "bento-local/dev_mode/data").
* A properly configured copy of the dataloader configuration file located at dataloader/bento-local.yml. This file should not require any changes from the version in Github and will use the neo4j credentials and folder locations defined in the .env file.

To start the bento-dataloader container and load data:

	<env_vars> docker-compose -f dataloader.yml up --build bento-dataloader

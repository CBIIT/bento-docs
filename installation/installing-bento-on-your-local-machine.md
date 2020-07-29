---
layout: default
nav_order: 1
title: Installing Bento on Your Local Machine 
---

# Installing Bento on Your Local Machine

## Introduction
The Bento-Local environment is designed to run directly within Docker on a user’s workstation. This allows users to create and deploy their local copy of Bento with minimal changes to their local environment and allows a configuration that can be used with different workstation operating systems. 

The scripts for Bento-Local are separated into folders for its three different modes:
* Build Mode:  this will create production ready Docker containers for the frontend and backend bento projects. This mode requires users to have local copies of the bento-frontend and bento-backend repositories. Note that when using build mode there are no changes made to the source code made during the build process, any changes or configurations made to the user's local copy of the source code will be reflected in the build.
* Dev Mode:  this will create Docker containers for the frontend and backend bento projects suitable for local development. Note that in this mode configuration changes will be made during the build process to set configurations to local resources and the frontend website will reflect live changes made in the user's local copy of the source code.
* Demo Mode: this will load pre-configured bento Docker containers pulled from Docker Hub.

The bento-local environment you build will be specific to the folder of the mode you choose. All local copies of source code and configuration files used for your environment must reside within the root of this folder. For example, if you are building in Dev Mode your source code folder would be located at "bento-local/dev_mode/[source folder]".


Bento-local consists of three components hosted within Docker containers and a separate Dataloader container that will run the Bento dataloader scripts. Depending on configuration options the build can take several minutes. When the build is complete the Bento components will be configured as follows:


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

* The Dataloader container will load a local data set into the graph database hosted within the Neo4j container. This component requires local copies of the bento-backend and bento-model repositories as well as a local copy of the data to be loaded. This container will not continue running after data has been loaded.

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

You can pull these onto your local workstation using any git client you have installed. When the source code is cloned it will be saved in two new folders created within your Bento-Local project, "bento-backend" and "bento-frontend".

Note that the bento-local build will use the actual code you have cloned locally when it builds - if you require features from a specific branch you must clone that branch specifically. For a vanilla install of Bento the master branch from the bento-frontend and bento-backend repositories will be sufficient.

### Configure Environment settings for your local instance

The bento-local scripts require a `.env` file to be present alongside the bento-local `docker-compose.yml`. This file will be created with default values when cloning the Bento-Local Git repository. It should be possible to use default settings in the .env file to fully build the Bento-Local environment, however these can be changed if the folder names of your local copies of the source code have changed or if you want to set a different Neo4j password (Note that the username for Neo4j should remain as "neo4j"). The default values for this file are:

```
FRONTEND_SOURCE_FOLDER=bento-frontend
# Set to your local copy of the frontend code - the default value for this is "bento-frontend". NOTE: this folder MUST be located within the folder specific to the project you are building

BACKEND_SOURCE_FOLDER=bento-backend
# Set to your local copy of the backend code - the default value for this is "bento-backend". NOTE: this folder MUST be located within the folder specific to the project you are building

BENTO_DATA_MODEL=bento-model
# Set to your local copy of the Bento data model - the default value for this is "bento-model". NOTE: this folder MUST be located within the folder specific to the project you are building

NEO4J_USER=neo4j
# The user name to set for Neo4j - this should remain as the default value of "neo4j" for local neo4j containers

NEO4J_PASS=neo4j_pass
# The password to set for Neo4j. This can be changed if desired
```

Note that the locations of the FRONTEND_SOURCE_FOLDER, BACKEND_SOURCE_FOLDER, and BENTO_DATA_MODEL are important. These values are relative paths and must be within the folder of the build mode you are using.

### Run the Bento-local Environment

***docker-compose environment variables:***

The docker-compose files for bento-local have been written to make use of Buildkit and the Docker CLI. The commands used for docker-compose should set these options as active by passing environment variables as:

* Windows: ```$Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1;```

* Linux/Mac: ```COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1```

Many of the commands listed in this document will need to be appended to this variable declaration. Choose the correct command for the system you are running on.

### Commands for running Bento-local services:
* NOTE: all commands must be run from within the root of the folder corresponding to the build mode you are using. For dev mode this would be "bento-local/dev_mode"

To build the bento-local infrastructure and start all containers:

	* Windows:    $Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose up -d
	* Linux/Mac:  COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up -d

To rebuild an individual container (NOTE: The available containers for this command are: bento-backend, bento-frontend, neo4j):

	* Windows:    $Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose up -d --no-deps --build <service_name>
	* Linux/Mac:  COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up -d --no-deps --build <service_name>
	
To stop all running bento-local containers:

	* Windows:    $Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose down
	* Linux/Mac:  COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down

To stop a single running container:

	* Windows:    $Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose down <service_name>
	* Linux/Mac:  COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down <service_name>
	
To clean docker objects for all stopped containers (this command can be used to return to a clean system and start over with new configurations):

	docker system prune -a

To clean all docker volumes (NOTE: this will remove any data loaded into Neo4j):

	docker system prune --volumes

To attach a shell to a running container:

	docker exec -it <container name> /bin/bash   (use /bin/ash for frontend and backend containers as they are based on alpine)


### Commands for running the Bento-local dataloader:
Note that the dataloader requires the following local resources:
* A local copy of the bento-backend source code. This will be used to supply schema files. The location of this folder must be within the root folder of the version of bento-local you are using and its location is set by the BACKEND_SOURCE_FOLDER variable in .env.
* A local copy of the bento-model source code. This will be used to supply data model files. The location of this folder must be within the root folder of the version of bento-local you are using and its location is set by the BENTO_DATA_MODEL variable in .env. The Bento data model can be found at:  https://github.com/CBIIT/bento-model.git
* A local copy of the data you intend to load. This data must be configured to match the Bento data model and schema and located in a folder named "data" within the bento-local project (ex. "bento-local/dev_mode/data").
* A properly configured copy of the dataloader configuration file located at dataloader/bento-local.yml. This file should not require any changes from the version in Github and will use the neo4j credentials and folder locations defined in the .env file.

To start the bento-dataloader container and load data:

	* Windows:    $Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose -f dataloader.yml up --build bento-dataloader
	* Linux/Mac:  COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose -f dataloader.yml up --build bento-dataloader

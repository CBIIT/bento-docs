# BENTO LOCAL :bento:

The Bento-Local environment is designed to run directly within Docker on a user’s workstation. This allows users to create and deploy their local copy of Bento with minimal changes to their local environment and allows for a configuration that can be used with different workstation operating systems.

<!-- ## Requirements
- Docker
- Git
- Admin or Sudo Access on the system on which bento-local is getting installed 

## Optional 
- Docker Desktop  -->

# Getting Started
To get started with Bento-Local, follow these steps:
1. Clone or Download Bento-local Scripts
2. Initalize Project
3. Build & Run Docker containers 

> **Warning**: If you have previously cloned and initialized bento-local and wish to obtain a new build version of any service, it is essential to follow these steps:
>  1. Stop all running containers associated with the services.
>  2. Perform a Docker system prune to remove any unused containers, networks, or images.
>  
> For comprehensive instructions on changing the build version of the desired service, please refer to the "[Additional Steps > Changing Build version](#changing-build-version-of-either-of-the-services)" section.
> Please ensure that you follow these steps carefully to avoid any conflicts or issues during the build process.

## 1. Cloning Bento-Local on the system. 
Clone the "Bento-Local" repository to your local system using Git. The following command clones the master branch, which always contains the latest released version of Bento:
```
git clone https://github.com/CBIIT/bento-local.git
```

If you need an unreleased or older version of Bento, specify the branch or version number:
```
# Example for an unreleased version
git clone -b 4.0.0 https://github.com/CBIIT/bento-local.git

# Example for an older version
git clone -b 3.9.0 https://github.com/CBIIT/bento-local.git
```

Change to the "bento-local" directory:
```
cd bento-local/
```

## 2. Initializ Project
> **Warning**: The initialization scripts are location-specific and should only be run inside the corresponding directory:  ``initialization/mac_linux`` for Mac/Linux or ``initialization/windows/`` for Windows. Running the scripts from any other location may not work.

To initialize Bento-Local, follow these steps:
 1.  Change to the appropriate directory for your host operating system:
     - Mac/Linux: ```cd initialization/mac_linux/```
     - Windows: ```cd initialization/windows/```
 2. Execute the initialization script:
    - Mac/Linux: ```sh ./init.sh```
    - Windows: ```init.bat```
 3. During script execution, you will be prompted with a few questions. If you're unsure, default values are provided as well:
    - use demo data [default=yes]: (options are ``` yes | no ```)
    - set bento-backend repository [default=https://github.com/CBIIT/bento-RI-backend.git]: 
    - set bento-backend branch [default=4.10.0]:
    - set bento-frontend repository [default=https://github.com/CBIIT/bento-frontend.git]:
    - set bento-frontend branch [default=4.0.0]:
    - set bento-model repository [default=https://github.com/CBIIT/BENTO-TAILORx-model.git]:
    - set bento-model branch [default=master]:
    > **Note**: Pressing the "return" key without providing any input will use the default value. 

## 3. Build & Run Docker containers 
> **Note**: All commands must be run from within the root of the Bento-Local project.

If you are currently in the initialization directory, change to the root folder:

```
cd ../../
```

### 3.1 Build and run the Docker containers, use the following command:
 - Mac/Linux: ```COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up -d```
 - Windows: ```$Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose up -d```

### 3.2 rebuild an individual container, you can use the following command:
> **Note**: The rebuild option is available for _bento-backend, bento-frontend, bento-files, bento-os, neo4j_.
 - Mac/Linux: ```COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up -d --no-deps --build <service_name>```
 - Windows: ```$Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose up -d```

### 3.3 stop all running Bento-Local containers, use the following command:
 - Mac/Linux: ```COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down```
 - Windows: ```$Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose down```

Here are some additional commands for managing Docker containers:
```
# To find the CONTAINER ID of running containers
docker ps

# Print out logs of a specific container using its CONTAINER ID
docker logs <CONTAINER_ID>

# To attach a shell to a running container (useful for verifying configurations or troubleshooting)
docker exec -it <CONTAINER_ID> /bin/sh

```

# Additional Steps: 
## Changing Build version of either of the Services. 
Here are few steps needs to be taken to jump between different build/versions of services (includes Bento-frontend and Bento-Backend)
1. Stop the all running container. Refer [Section 3.3](#33-stop-all-running-bento-local-containers-use-the-following-command) under [ Build & Run Docker containers](#3-build--run-docker-containers)
2. Perform a Docker system prune to remove any unused containers, networks, or images using [Cleaning Bento-Local Project](#cleaning-bento-local-project) steps.
3. Run the build script from [Section 3.1](#31-build-and-run-the-docker-containers-use-the-following-command)

## Cleaning Bento-Local Project
To remove the Docker cache and return your system to a clean state, you can use the following commands. It's important to note that these commands will only remove unused objects. If you want to completely remove all cached objects, you need to stop all running Docker containers by running docker-compose down first.

To clean Docker objects for all stopped containers and return to a clean system:
```
docker system prune -a
```

To clean all Docker volumes (Note: This will remove any data loaded into Neo4j):
```
docker system prune --volumes
```

## Running the Bento-Local Dataloader
To run the Bento-Local dataloader, please make sure you have the following local resources available:

1. A local copy of the bento-frontend source code: This is used to supply schema files and should be located within the root folder of the version of Bento-Local you are using. The location of this folder is set by the FRONTEND_SOURCE_FOLDER variable in the .env file, which can be obtained by running the initialization script.

2. A local copy of the bento-model source code: This is used to supply data model files and should also be located within the root folder of the Bento-Local version you are using. The location of this folder is set by the BENTO_DATA_MODEL variable in the .env file. You can obtain the Bento data model from the following repository: https://github.com/CBIIT/bento-model.git. This can be obtained by running the initialization script.

3. A local copy of the data you want to load: This data should be configured to match the Bento data model and schema. Place the data in a folder named "data" within the Bento-Local project (e.g., "bento-local/dev_mode/data").

4. A properly configured copy of the dataloader configuration file: The configuration file should be named bento-local.yml and located in the dataloader folder. This file does not require any changes from the version in the GitHub repository and will use the Neo4j credentials and folder locations defined in the .env file.

To start the Dataloader container and load data to Neo4j, use the following command:

For Linux/Mac:
```
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose -f dataloader.yml up --build bento-dataloader
```
For Windows:
```
$Env:COMPOSE_DOCKER_CLI_BUILD=1; $Env:DOCKER_BUILDKIT=1; docker-compose -f dataloader.yml up --build bento-dataloader
```
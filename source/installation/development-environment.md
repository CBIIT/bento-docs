# Setup A Development Environment

## Backend Development Environment

There are several microservices and a group of scripts used in Bento backend:
- bento-backend: GraphQL metadata service [GitHub repo](https://github.com/CBIIT/bento-backend)
- bento-files: File service [GitHub repo](https://github.com/CBIIT/bento-files)
- bento-auth: Authentication service [GitHub repo](https://github.com/CBIIT/bento-auth)
- data-loader: Scripts for loading data [GitHub repo](https://github.com/CBIIT/icdc-dataloader)

To set up a backend development environment, following tools are needed:
- Neo4j
- OpenSearch
- Redis
- Java
- NodeJS
- Python

### Pre-requisites
#### Mac
1. To install Homebrew on your Mac
    ```
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
2. To make sure Homebrew up to date
    ```
    brew update
    ```

### Neo4j
Bento backend needs Neo4j version 4.2.x.

#### Mac
1. Download the version of 4.2.X from https://neo4j.com/download-center/#community in your local machine

2. Extract the contents of the archive, using command
    ```
    tat -xf <filename>
    ```
3. Download apoc-4.2.0.10-core.jar into the $neo4j/plugins
    ```
   https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/4.2.0.10/apoc-4.2.0.10-core.jar
    ```
4. Change the targeted directory & run Neo4j:
   ```
   cd $neo4j
   ```
   ```
   ./bin/neo4j console
   ```
After the command, logs are printed in the console.

#### Windows

### OpenSearch

#### Mac
1. Pull the OpenSearch Docker image
    ```
   docker pull opensearchproject/opensearch:1.2.4
    ```
2. To run the docker image for the Opensearch without security plugin
    ```
    docker run -p 9200:9200 -p 9600:9600 \n -e "discovery.type=single-node" -e "DISABLE_SECURITY_PLUGIN=true" opensearchproject/opensearch:1.2.4
    ```
   
#### Windows


### Redis

#### Mac
To run the docker image in the background for redis-server
   ```
   docker run --name redis-server -d redis
   ```

#### Windows


### Java
Bento backend needs Java JDK 11.

#### Mac
To install the JDK on macOS
1. Download the JDK .dmg file from
   ```
   https://www.oracle.com/java/technologies/downloads/#java11
   ```
2. Double-click the downloaded .dmg file

3. Enter the Administrator username and password and click Install Software

#### Windows


### NodeJS
Bento-files and bento-auth need NodeJS version 16.x.

#### Mac
To install node.js 16.x
   ```
   brew install node@16
   ```

#### Windows


### Python
Bento data-loader needs Python3.x.

#### Mac
1. To install Python3
   ```
   brew install python3
   ```
2. To install virtualenv via pip run(pip3 installed with Python3)
   ```
   pip3 install virtualenv
   ```
3. Create of Bento virtual environment
   ```
   virtualenv bento --python=python3
   ```
5. Deactivate the virtual environment
   ```
   deactivate
   ```
   
#### Windows



## Frontend Development Environment
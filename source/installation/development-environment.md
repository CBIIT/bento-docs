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
1. Download the latest version of Neo4j Desktop for Mac from https://neo4j.com/download/ in your local machine

2. Double-click the Neo4j .dmg file

3. After installation, you can add the desired Neo4j version recommending 4.2.X for Bento framework.
 
4. After creating your database, by going into the Manage screen, and then click to install the APOC box in the Plugins tab.

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
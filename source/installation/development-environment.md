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
#### Windows
Download and install Docker Desktop: [Docker Desktop installation instructions](https://docs.docker.com/desktop/windows/install/)

1. Download the Docker Desktop installer from the link above

2. Run installer with administrator/elevated privileges

3. When the installer displays the configuration options, ensure that ```Install required Windows components for WSL 2``` is selected

4. Verify that the installation was successful by launching Docker Desktop and then checking to see if Docker Engine is running. This can be done via any of the below methods:
   
      * In the Docker Desktop window, verify that the bar in the bottom left is green and shows ```Engine Running``` when the mouse pointer hovers over it
   
      * Right click the Docker taskbar icon and verify that menu displays a green circle next to the text ```Docker Desktop is running```
   
      * In Command Prompt, run the command:
      ```
      docker version
      ```
      and verify that the docker version information is displayed

### Neo4j
Bento backend needs Neo4j version 4.2.x.

#### Mac
1. Download the latest version of Neo4j Desktop for Mac from https://neo4j.com/download/ in your local machine

2. Double-click the Neo4j .dmg file

3. After installation, you can add the desired Neo4j version recommending 4.2.X for Bento framework
 
4. After creating your database, by going into the Manage screen, and then click to install the APOC box in the Plugins tab

#### Windows
Download and install Neo4j Dekstop: [Neo4j Desktop installation instructions](https://neo4j.com/docs/desktop-manual/current/installation/)

1. Download the latest version of [Neo4j Desktop for Windows](https://neo4j.com/download-center/)

2. If you do not already have one, copy the Neo4j Desktop Activation Key from the download page

2. Run installer with administrator/elevated privileges

4. If prompted, allow Neo4j access through the Windows firewall

5. Launch Neo4j Desktop and, when prompted, enter your Neo4j Desktop Activation Key

3. After installation, you can create a new project and add the desired Neo4j version (version 4.2.X is recommended for the Bento framework)
 
4. After creating your database, click on your project and install te ```APOC``` plugin from the ```Plugins``` tab

### OpenSearch

#### Mac/Windows
1. Verify that the Docker engine is running

2. Pull the OpenSearch Docker image
   ```
   docker pull opensearchproject/opensearch:1.2.4
   ```

3. To run the docker image for the Opensearch without security plugin
    ```
    docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" -e "DISABLE_SECURITY_PLUGIN=true" opensearchproject/opensearch:1.2.4
    ```

4. Run the command:
   ```
   docker ps
   ```
   to show the list of running containers and then verify that a container using the ```opensearchproject/opensearch:1.2.4``` image is now running

### Redis

#### Mac/Windows
1. Verify that the Docker engine is running

2. Pull the Redis Docker image
   ```
   docker pull redis
   ```

3. To run the docker image in the background for redis-server
   ```
   docker run --name redis-server -d redis
   ```

4. Run the command:
   ```
   docker ps
   ```
   to show the list of running containers and then verify that a container using the ```redis``` image is now running

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
Download and install JDK 11: [JDK 11 installation instructions](https://docs.oracle.com/en/java/javase/11/install/installation-jdk-microsoft-windows-platforms.html)

1. Download the [JDK 11 installer](https://www.oracle.com/java/technologies/downloads/#java11)

2. Run the downloaded installer

3. In Command Prompt, verify the installation by running the command:
   ```
   java -version
   ```
   and verify that the Java version is displayed to check that the Java installation was successful

### NodeJS
Bento-files and bento-auth need NodeJS version 16.x.

#### Mac
To install node.js 16.x
   ```
   brew install node@16
   ```

#### Windows
1. Download the latest [NodeJS installer](https://nodejs.org/en/download/)

2. Run the downloaded installer

3. In Command Prompt, run the command:
   ```node -v```
   and verify that the NodeJS version is displayed to check that the installation was successful

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
4. Deactivate the virtual environment
   ```
   deactivate
   ```
   
#### Windows
Download and install Python 3: [Python 3 installation instructions](https://docs.python.org/3/using/windows.html#installation-steps)

1. Download the lastest [Python 3.x installer](https://www.python.org/downloads/)

2. Run the downloaded installer

3. The "Install now" installation option can be used. If running a custom install, then ensure that pip is included and installed

4. In Command Prompt, run the command:
   ```python --version```
   and verify that the Python version is displayed to check that the Python installation was successful

5. In Command Prompt, run the command:
   ```pip3 --version```
   and verify that the pip version is displayed to check that the pip installation was successful

7. In Command Prompt, create the Bento virtual environment
   ```
   python -m venv bento_venv
   ```

8. The Bento virtual environment can be activaed with the following command in Command Prompt:
   ```
   bento_venv\Scripts\activate.bat
   ```

8. The Bento virtual environment can be activaed with the following command in Command Prompt:
   ```
   deactivate
   ```

## Frontend Development Environment
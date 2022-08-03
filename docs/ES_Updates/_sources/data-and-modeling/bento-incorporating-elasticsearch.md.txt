# Bento Backend Configuration Guide - Elasticsearch
This document for the Bento Backend outlines the architecture and configuration required to include Elasticsearch in the Bento framework.



## Introduction

The Bento Backend Framework is used in conjunction with the Bento Frontend Framework and by default is set up using a Neo4j database running the GraphQL plugin as its datasource. To increase the efficiency of backend queries this framework can be extended to use Elasticsearch for Bento queries including:

* Facet filtering queries (including widgets and stats bar)
* Table/pagination queries
* Local and global search

With Elasticsearch added to the Bento Framework the system architecture is configured as follows:


<img src="../assets/Architecture/backend-architecture-es.png" width="750"/>


The Bento Backend can be found in this Github Repository: [Bento Backend](https://github.com/CBIIT/bento-backend)


## Pre-requisites

* Java 11 or newer installed on the server hosting the Bento Backend
* The Neo4j database containing the Bento data has been initialized and is running
* Elasticsearch has been installed and is running in a location accessible from the backend instance


## Configuration

The following file will need to be updated to configure the Bento Backend Code to work with Elasticsearch:

**````src/main/resources/application.properties````**

Add the following environment variables to the container running Bento Backend in your environemnt:

* ES_HOST: set this to the Elasticsearch endpoint you will use
* ES_FILTER_ENABLED: set this to 'true' to enable using the Elasticsearch filter with your Bento backend


## Loading Data to Elasticsearch
Before enabling Elasticsearch in your environment data will need to be loaded from Neo4j using the Bento Dataloader. This Python application reads data from Neo4j and creates indices in Elasticsearch (it will delete and recreate these indices if they already exist).
The Dataloader should be run whenever data in Neo4j changes or whenever any indices need to be created or updated.


## Pre-requisites

* Python3 and pip installed in the location where the dataloader will be run
* The Neo4j database used and the Elasticsearch endpoint should be accessible from the location where the dataloader will be run
* The Bento Dataloader repository (https://github.com/CBIIT/icdc-dataloader) should be downloaded to run the dataloader
* The following configuration files from the dataloader repository should be updated for the environment where data is to be loaded:
  * config/es_indices.example.yml
  * config/es_loader.example.yml


### Usage Example
Below is an example command to run the Elasticsearch Loader:
````
python3 es_loader.py config/es_indices_<project>.yml config/es_loader_<project>.yml
````

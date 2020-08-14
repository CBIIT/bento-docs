---
layout: default
nav_order: 2
title: Overview
---

# Overview

Bento is a software framework being built to support NCI’s [Cancer Research Data Commons](https://datascience.cancer.gov/data-commons) projects, including Integrated Canine Data Commons (ICDC), and Clinical Trial Data Commons (CTDC).
<br>This site provides you with the background and instructions you need to set up your own data sharing platform using Bento. 

## Introduction
Bento is an open-source software framework for data sharing platforms that allow users to store, manage, share and analyze large-scale data according to the [FAIR](https://www.go-fair.org/fair-principles/) principles.
<br>Bento is built on three organizing principles:
<br>1. **Bento is data agnostic.** You can use Bento to develop data sharing platforms for data types of your choice. The framework is built to support the sharing of any kind of large scale biological data, be it next-generation sequencing, , proteomics, flow-cytometry or single-cell sequencing data sets.
<br>2. **Bento is modular.** The Bento architecture separates the front-end code, back-end code and the underlying graph database into three separate modules. This modularity allows users to separately update each module. For example, the database model may be updated and the resulting database will work with the other modules to form a functioning application, or the front-end code may be updated to provide a different user interface, without modifying the back-end or database modules. We believe this modularity allows Bento-enabled data sharing platforms to be scaled up and out to keep pace with the platform custodian’s evolving needs.
<br>3. **Bento is cloud enabled.** We have built Bento to be deployed on your on-premise servers as well as on the Amazon Web Services and Google Cloud platforms. 
<br>[This](http://dev.bento-tools.org/) data sharing platform was built as a reference implementation of Bento. You can explore it to better understand the capabilities of the framework. 


## Bento Architecture

## Bento Tech Stack and Infrastructure

Components

Description about guides to install and configure Bento

### API

### Neo4J

### UI
Description of the web interface/front end.

## Bento Data Model 
The Bento Core Data Model is a graphical data model that has been designed to address the data storage needs of clinical trials and research programs; it can be adapted to most data generation workflows. Graphical data models organize data in the form of a graph. The Bento Core Data Model models key components of a data generation workflow as nodes, and the relationships among them as edges. Both nodes and edges can store data in the form of properties.
It is based on the Aggregated Data Model developed by the [Center for Cancer Data Harmonization](https://datascience.cancer.gov/data-commons/center-cancer-data-harmonization-ccdh). The Aggregated Data Model synthesizes core concepts from three data sharing platforms- the [Genomic Data Commons](https://gdc.cancer.gov/); the [Proteomic Data Commons](https://proteomic.datacommons.cancer.gov/pdc/) and the [Integrated Canine Data Commmons](https://caninecommons-dev.cancer.gov/).
This model allows you to set up a <i>minimal</i> but <i>functioning</i> data sharing platform, where users can navigate from a selected clinical trial or program to a set of files of their choice. 
<br>Being schema-less, graphical data models can be easily extended, to include additional node and relationship types, without breaking the existing model. This feature allows you to expand the Bento Core Data Model to suit the evolving needs of your data sharing platform.
<br>You can access the Bento Core Data Model [here](https://github.com/CBIIT/bento-model.git). We have extended the core data model to build the reference implementation; the extended BENTO_TAILORx data model can be found [here](https://github.com/CBIIT/BENTO-TAILORx-model).



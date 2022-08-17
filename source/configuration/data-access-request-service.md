# Data Access Request (DAR) Service

## Introduction
The Bento Framework supports a user-driven data access request workflow that enables authenticated users to request access to a specific dataset or resource (ie. arm, study, project, program, etc.) and allows system administrators to review, approve, and reject data access requests submitted by users. System triggered emails are generated at each definitive point in the workflow. Admins can navigate the data access request workflow using the Bento Admin Portal. 

![Data Access Request (DAR) Workflow](../assets/dar-workflow.png)

![Data Access Request (DAR) Example page](../assets/dar-example-page.png)

<p>&nbsp;</p>


## Prerequisites
1. The files that specify the configuration parameters for the DAR service are stored in the GitHub repository `https://github.com/CBIIT/bento-frontend`. Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration parameters for node-level access can be specified in the file: `$(src)/bento-frontend/src/bento/siteWideConfig.js`.

3. Configuration parameters for DAR elements can be specified in the file: `$(src)/bento-frontend/src/bento/requestAccessData.js`.

<p>&nbsp;</p>     

## Configuring Node-Level Access 
Access to data can be specified and controlled at the node-level and requires configuration of the following parameters:
1. Edit file: `$(src)/bento-frontend/src/bento/siteWideConfig.js`
2. Update fields: node_level_access, node_name, and node_label

#### Node-Level_Access
    * Acceptable values are True or False. The default value is True.
    * If value is True, data access is controlled at the node-level and the node Node Name and Node Displayed Label parameters must be specified
    * If value is False, there is no ability to control data access at the node-level and instead users will either have access to all of the data or none of the data based upon authentication and authorization

#### Node_Name
    * The node in the data model that is used to govern the granularity of data access
    * Acceptable values are any node in the data model (ie. Program, project, study, trial, etc.). The default is Arm.

#### Node_Label
    * The value displayed on the user interface that is used to govern the granularity of data access
    * Acceptable values are any string with a max length of 30 characters. The default is Study Arm(s).

3. Example:

```javascript
// Node level access
export const NODE_LEVEL_ACCESS = true;
export const NODE_NAME = 'Arm';
export const NODE_LABEL = 'Study Arm';
```
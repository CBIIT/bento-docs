# Authorization

## Introduction
The Bento Framework supports role-based access control (RBAC) as a method of restricting access to protected or controlled data to authorized users based upon an ascribed role. This enables systematic and reproducible assignment of permissions to facilitate auditing and reduce the potential for error. 


<p>&nbsp;</p>

## Terminology

### Identity Provider (IdP)
A service that enables a user to login using credentials to establish a user's identity and pass this information to downstream applications.

### Authentication 
Establishes "who you are" using information obtained by logging in through an Identity Provider (IdP).

### Authorization
Establishes "which data you have access to" with a given application

## Prerequisites
1. The files that specify the configuration parameters for the DAR service are stored in the GitHub repository `https://github.com/CBIIT/bento-frontend`. Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration parameters for RBAC elements can be specified in the file: `$(src)/bento-frontend/src/bento/siteWideConfig.js`.

<p>&nbsp;</p>

## Configuring Public Access

|Public Access|Metadata|File Download|Release
|:-------------|:--------|:-------------|:-------|
|Metadata Only |full access|no access| v.3.8.0|
|None|no access|no access|v.3.8.0|

Currently, public accessibility to data contained within a Bento-based system can be configured. The configuration applies to both unauthenticated users that have not logged in and unauthorized users that have logged in, but have not yet submitted any data access requests and therefore do not have access to any data.
1. Edit file: `$(src)/bento-frontend/src/bento/siteWideConfig.js`
2. Update field: public_access

### Public Access

    * Acceptable values are Metadata Only or None. The default is Metadata Only. 
    * If Public Access is set to "metadata only", public users can see all metadata in the database, but cannot open or download any files.

3. Example:
```javascript
export const PUBLIC_ACCESS = 'Metadata Only';
```
    * If public access is set to "none", public users cannot see any data and any attempts to access restricted pages will redirect unauthenticated users to the Login page and unauthorized users to the Data Access Request (DAR) page.

4. Example:
```javascript
export const PUBLIC_ACCESS = 'None';
```
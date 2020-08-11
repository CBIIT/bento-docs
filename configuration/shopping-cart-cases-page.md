---
layout: default
nav_order: 13
title: Shopping Cart Cases Page
---

# Shopping Cart Cases Page

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.


## How to Configure the Table Title for the "Cases Page in the "Shopping Cart/My Cases" workflow
To configure the table title on the page (right above the table)

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `myCasesPageData`, 
    1. set the field `myCasesMainTitle` to have the desired title for the page
    2. set the field `myCasesSubTitle` to have the desired subtitle 
3. For example, to have the page appear as 'My Subjects: Subjects' instead of 'My Cases: Cases' (with 'My Cases' being the title):

```javascript
export const myCasesPageData = {
  myCasesMainTitle: 'My Subjects :',
  myCasesSubTitle: 'Subjects',
```

## How to Configure the Table Content for "My Cases" Page in the "Shopping Cart/My Cases" workflow
To configure the table on the "My Cases" page

## Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `GET_MY_CASES_DATA_QUERY`, set graphql query ...

## How to Configure Table Icon
To configure the Table Icon for the "My Cases" page

### Add Icon file to repo
1. add icon file to appropriate file location: `$(src)/bento-frontend/src/assets/icons/`
2. add and commit file to repo; then push the commit to github

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under ` myCasesPageData`, 
    1. set the field `headerIconSrc` to point to the new desired image file
    2. Update the field `headerIconAlt` to an appropriate "alternate text" description for the icon
3. For example:

```javascript
export const myCasesPageData = {
  ...
  headerIconSrc: 'https://raw.githubusercontent.com/YOUR-USERNAME/bento-frontend/master/src/assets/icons/NewIcon.svg',
  headerIconAlt: 'NewIcon logo',
```

## How to Configure "Go To Files" Button* for the "Shopping Cart/My Cases" workflow
To configure the Configure "Go To Files" Button* for the "Shopping Cart/My Cases" workflow

## Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `myCasesPageData`, set the field `buttonText` to have the desired text value
3. For example, to have the link appear as 'Go To Files Page' instead of 'GO TO FILES':

```javascript
export const myCasesPageData = {
  ...
  buttonText: 'Go To Files Page',
```

## How to Configure the Workflow Icon for the "Shopping Cart/My Cases" workflow
To configure the Workflow Icon for the "Shopping Cart/My Cases" workflow

### Add Icon file to repo
1. add icon file to appropriate file location: `$(src)/bento-frontend/src/assets/icons/`
2. add and commit file to repo; then push the commit to github

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `myCasesPageData`, set the field `cartLabel` to have the desired text value
    1. Set the field `  wizardIconSrc` to point to the new desired image file
    2. Update the field `wizardIconAlt` to an appropriate "alternate text" description for the icon; 
3. For example, to have the icon to use the file `MyWizardIcon.svg` instead of file `MyCases-Wizard-Step2.svg`

```javascript
export const myCasesPageData = {
  ...  
  wizardIconSrc: 'https://raw.githubusercontent.com/YOUR-USERNAME/bento-frontend/master/src/assets/icons/MyWizardIcon.svg',
  wizardIconAlt: 'Go To Step 2',
};```

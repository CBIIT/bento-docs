---
sort: 11
title: Shopping Cart Files Page
---

# Shopping Cart Files Page

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.


## How to Configure the Table Title for the "Files Page in the "Shopping Cart/My Cases" workflow
To configure the table title on the page (right above the table)

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `myFilesPageData`, 
    1. set the field `myFilesMainTitle` to have the desired title for the page
    2. set the field `myFilesSubTitle` to have the desired subtitle 
3. For example, to have the page appear as 'My Subjects: Files' instead of 'My Files: Files':

```javascript
export const myFilesPageData = {
  myFilesMainTitle: 'My Subjects :',
  myFilesSubTitle: 'Files',
```

## How to Configure Table Icon
To configure the Table Icon for the "My Files" page

### Add Icon file to repo
1. add icon file to appropriate file location: `$(src)/bento-frontend/src/assets/icons/`
2. add and commit file to repo; then push the commit to github

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under ` myFilesPageData`, 
    1. set the field `headerIconSrc` to point to the new desired image file
    2. Update the field `headerIconAlt` to an appropriate "alternate text" description for the icon
3. For example:

```javascript
export const myFilesPageData = {
  ...
  headerIconSrc: 'https://raw.githubusercontent.com/YOUR_USERNAME/bento-frontend/master/src/assets/icons/NewIcon.svg',
  headerIconAlt: 'NewIcon logo',
```


## How to Configure the Workflow Icon for the Files Page in "Shopping Cart/My Cases" workflow
To configure the Workflow Icon for the Files Page in the "Shopping Cart/My Cases" workflow


### Add Icon file to repo
1. add icon file to appropriate file location: `$(src)/bento-frontend/src/assets/icons/`
2. add and commit file to repo; then push the commit to github

### Edit configuration file

1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `myFilesPageData`, set the field `cartLabel` to have the desired text value
    1. Set the field `  wizardIconSrc` to point to the new desired image file
    2. Update the field `wizardIconAlt` to an appropriate "alternate text" description for the icon; it is recommended to use underscores instead of spaces with this field
3. For example, to have the icon to use the file `MyWizardIcon.svg` instead of file `MyCases-Wizard-Step2.svg`

```javascript
export const myFilesPageData = {
  ...  
  wizardIconSrc: 'https://raw.githubusercontent.com/YOUR_USERNAME/bento-frontend/master/src/assets/icons/MyWizardIcon.svg',
  wizardIconAlt: 'Go To Step 2',
};
```


## How to Configure the File Manifest Name for "Shopping Cart/My Cases" workflow
To configure the File Manifest Name for "Shopping Cart/My Cases" workflow


### Edit configuration file

1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `myFilesPageData`, set the field `manifestFileName`: to have the desired file value
3. For example, to use the name "File Manifest" instead of `BENTO File Manifest`

```javascript
export const myFilesPageData = {
  ...  
  manifestFileName: 'File Manifest',
  ...
};
```


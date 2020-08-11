---
layout: default
nav_order: 15
title: Configuring the Shopping Cart Menu Bar
---

# Configuring the Shopping Cart Menu Bar

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.


## Configure the Menu Bar Text for the "Shopping Cart/My Cases" workflow
To configure the link that appears on the menu bar:

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `navarBarCartData`, set the field `cartLabel` to have the desired text value
3. For example, to have the link appear as 'MY SUBJECTS' instead of 'MY CASES':

```javascript
export const navBarCartData = {
  cartLabel: 'MY SUBJECTS',
```


## Configure the Menu Bar Icon for the "Shopping Cart/My Cases" workflow
To configure the icon that appears on the menu bar:

### Add Icon file to repo
1. Add icon file to appropriate file location: `$(src)/bento-frontend/src/assets/icons/`
2. Add and commit file to your repo; then push the commit to github

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `navarBarCartData`, 
    1. set the field `cartIcon` to point to the new desired image file
    2. Update the field `cartIconAlt` to an appropriate "alternate text" description for the icon
3. For example, to have the icon to use the file `MyIcon.svg` instead of file `Icon-MyCases.svg`

```javascript
export const navBarCartData = {
  ...
  cartIcon: 'https://raw.githubusercontent.com/YOUR-USERNAME/bento-frontend/master/src/assets/icons/MyIcon.svg',
  cartIconAlt: 'my_icon_logo',
};
```


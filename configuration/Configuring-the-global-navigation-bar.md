---
layout: default
nav_order: 4
title: Global Navigation Bar
---

# Global Navigation Bar
The Global navigation bar is the UX element that appears under the Global Header, and has links such 'Home', 'Programs', 'Cases', and 'About'.

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## Edit configuration file

1. Number of menu items: I would like to specify the number of menu items in the nav-bar (maximum = 4)
    * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
    * The UI will display 'Max value error message '

2. Menu item ordering: I would like to specify the left to the right ordering of the menu items.
    * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
    * The order of objects from topdown will display left to right in UI

3. Menu item type: I would like to specify the type of menu item. Menu Items can be one of two types: (a) link (b) drop-down.
   * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
   * set field `type` link or `dropdown` to get different types of navigation buttons

4. Menu item label: I would like to specify the label to be displayed for each menu item. Example labels: “Home”, “About”, “Programs”.
   * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
   * set field `label` of respective object to change the labels

5. Menu item link: I would like to specify a URL for each menu item of the type "link".
   * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
   * set field `link` of respective object to change the links for each button

6. Menu item drop-down: I would like to specify the list of sub-menu items for each menu item of the type "drop-down"
   * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
   * set field `type` to dropdown
   * create a field dropDonwLinks and add objects with these fields
     * labelText: 'purpose',
     * link: '/purpose'

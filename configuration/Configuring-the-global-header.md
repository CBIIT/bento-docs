---
layout: default
nav_order: 3
title: Configuring the Global Header
---

# Configuring the Global Header


## Prerequisites

1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)

2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## Edit configuration file

### Header Logo

To configure an image to be used as the  Header Logo: 

1. Edit `$(src)/bento-frontend/src/bento/headerData.js` with the editor of your choice

2. set field `globalHeaderLogo` with the stored image

### Header Logo Link
To configure the Header Logo link (the URL to be associated with the Header Logo):

1. Edit `$(src)/bento-frontend/src/bento/headerData.js` with the editor of your choice

2. set field `globalHeaderLogoLink` with the desired url

### Header Image

1. Edit `$(src)/bento-frontend/src/bento/headerData.js` with the editor of your choice

2. set field `globalHeaderLogoAltText` with the text need to display when image is not availble.

### Header Alt Tag

To specify an alt tag for the header image:

1. Edit `$(src)/bento-frontend/src/bento/headerData.js` with the editor of your choice
set field `globalHeaderImage` with a prestored image url

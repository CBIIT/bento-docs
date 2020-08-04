---
layout: default
nav_order: 9
title: Configuring Browser Tab Elements
---

# Configuring Browser Tab Elements

## Favicon
The favicon (short for favorite icon) or the icon that appears in the brower tab can be easily configured 

### Option A: Using a web-based location:

 1. Edit `$(src)/bento-frontend/public/index.html` with the editor of your choice
 2. Replace line  `<linkrel="shortcut icon" href="https://raw.githubusercontent.com/CBIIT/bento-frontend/master/public/favicon.ico"/>` with `<linkrel="shortcut icon"href="{url of the file}"/>`

### Option B: Using a local-based location (within the repo):
 1. The location is specified the the git repo is in the file:  `$(src)/bento-frontend/public/`
 2. Replace line  `<linkrel="shortcut icon" href="https://raw.githubusercontent.com/CBIIT/bento-frontend/master/public/favicon.ico"/>` with `<linkrel="shortcut icon"href="/{file_name}"/>`

## Title (Tab text)
The HTML Title element (`<title> `) defines the document's title that is shown in a browser's title bar or a page's tab.
The Title, or tab text, can be specified as follows:

 1. Edit `$(src)/bento-frontend/public/index.html` with the editor of your choice
 2. Replace line  `<title>Bento</title>` With `<title>{ title you want}</title>`

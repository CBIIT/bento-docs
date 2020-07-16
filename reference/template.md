---
layout: default
nav_order: 1
title: Template
---

# Template Title

This is the template for bento-tools documentation

## Introduction
Documentation will be saved in git, and presented using `github pages` using Jekyll. This requires that files be saved in markdown format. They will be automatically convered into html.  Furthermore, they can easily be converted into pdfs or other formats.

Currently, we are staging documentation in repo `https://github.com/CBIIT/bento-docs`.

Download this template here: [template.md](https://raw.githubusercontent.com/CBIIT/bento-docs/master/reference/template.md)

## Template Instructions Instructions

### Formatting
1. Format documentation using github-flavored markdown. For instructions on markdown syntax, please refer to
    * [Github Guides: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
    * [Markdown: Syntax](https://daringfireball.net/projects/markdown/syntax)
2. For images: put all images relative to `/assets` path, and we will put images in the `/assets/` folder
    * Example: the link to the image displayes `(assets/stormtroopocat.jpg)` via ```![Stormtrooper octocat](assets/stormtroopocat.jpg)``` ![Stormtrooper octocat](../assets/stormtroopocat.jpg)
3. File naming convention:
    * all configuration files should end in `.md`
    * use hyphens instead of spaces in file name (good: `my-file.md`, bad: `my file.md`)

### Documentation Structure
4. Only use 1 top level `#` header, keep it at the top of the documentation, under the "Front Matter"
5. Try to limit documentation to three heading levels. Do not use more than four levels of headers. (Do not use more than four octothorpe `####`)
6. Document structure: please include the following sections in your documentation
    * _Introduction_: please provide a summary of the documentation at the top of the page
    * _Pre-requisites_: describe anything that needs to be done for the documentation to work - whether it be other steps to have been done previously or have installed certain software, etc
    * _Installation or Configuration, etc_: the main body of the documentation
    * _Testing_: how do know that the installation or configuraiton was successful
7. "Front Matter": 
    * The "Front Matter" is the first five lines of this file
    * It describes how and where the page will be displayed on the docs website
    * Leave layout as default (i.e. `layout: default`)
    * Only change the "title" value (e.g. `title: My Title`)
    * `nav_order` describes the ordering of the page in the sidebar; this can be ajusted later
```
---
layout: default
nav_order: 1
title: Template
---
```

### Best Practices
8. Best practices:
    * include a troubleshooting section if appropriate
    * add any major terms to glossary.md
    * spell check the documentation


## An Example Section
An examples of markdown syntax is included [here](https://cbiit.github.io/bento-docs/reference/example)

### Code Blocks
Use code blocks with syntax highlighting, 
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```



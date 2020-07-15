---
layout: default
nav_order: 1
title: Installing Bento on Your Local Machine 
---

# Installing Bento on Your Local Machine


## Introduction
Documentation will be saved in git, and presented using `github pages` using Jekyll. This requires that files be saved in markdown format. They will be automatically convered into html.  Furthermore, they can easily be converted into pdfs or other formats.

Currently, we are staging documentation in repo `https://github.com/CBIIT/bento-docs`.

Download this template here: [template.md](https://github.com/CBIIT/bento-docs/blob/master/template.md)

## Template Instructions Instructions

1. Format documentation using github-flavored markdown. For instructions on markdown syntax, please refer to
    * [Github Guides: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
    * [Markdown: Syntax](https://daringfireball.net/projects/markdown/syntax)
2. Do not use more than four levels of headers. (Do not use more than four octothorpe `####`)
3. Only use 1 top level `#` header, keep it at the top of the markdown
4. `Front Matter`: 
    * The "Front Matter" is the first four lines of this file
    * It describes how and where the page will be displayed on the docs website
    * Leave layout as default (i.e. `layout: default`)
    * Only change the "title" value (e.g. `title: My Title`)
5. For images: put all images relative to `/assets` path, and we will put images in the `/assets/` folder
    * Example: the link to the image displayes `(assets/stormtroopocat.jpg)` via ```![Stormtrooper octocat](assets/stormtroopocat.jpg)``` ![Stormtrooper octocat](assets/stormtroopocat.jpg)
6. Please provide a summary of the documentation at the top of the page
7. File Format:
    * all configuration files should end in `.md`
    * use hyphens instead of spaces in file name (good: `my-file.md`, bad: `my file.md`)


## Markdown
Please use github-flavored markdown in this document.

### Example Sections
An examples of markdown syntax is included [here](/bento-docs/example)


#### Code Blocks
For code blocks with syntax highlighting, 
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

## Appendix
Note, after the markdown file is pushed to the repo, it can take 10 to 15 minutes for the changes to appear


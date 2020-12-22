# Template Page Title

This is a markdown template for bento-tools documentation

## Introduction
Documentation will be saved in git, and published using the Sphinx framework on github. This requires that files be saved in either  uses [RestructuredText](https://docutils.sourceforge.io/rst.html) or [Markdown](https://daringfireball.net/projects/markdown/syntax). Please use the extension `.rst` for [RestructuredText](https://docutils.sourceforge.io/rst.html) and `.md` for  [Markdown](https://daringfireball.net/projects/markdown/syntax). 

They will NOT automatically convered into html. (They have to be compiled using Sphinx, see [README.md](README.md)) . 

Once in either format, they can easily be converted into pdfs or other formats.

Currently, we are staging documentation in repo `https://github.com/CBIIT/bento-docs`.

Download this template here: [template-page.md](https://raw.githubusercontent.com/CBIIT/bento-docs/master/publishing/template.md)



## Template Instructions Instructions

### Formatting
1. Format documentation using github-flavored markdown or RestructuredText. For instructions on either syntax, please refer to
    * [Github Guides: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
    * [Markdown: Syntax](https://daringfireball.net/projects/markdown/syntax)
    * [reStructuredText](https://docutils.sourceforge.io/rst.html)
2. For images: put all images relative to `/assets` path, and we will put images in the `source/assets/` folder
3. File naming convention:
    * all markdown files should end in `.md`
    * all reStructredText should end in `.rst`
    * use hyphens instead of spaces in file name (good: `my-file.md`, bad: `my file.md`)

### Documentation Structure
4. Only use 1 top level `#` header, keep it at the top of the documentation, under the "Front Matter"
5. Try to limit documentation to three heading levels. Do not use more than four levels of headers. (Do not use more than four octothorpe `####`)
6. Document structure: please include the following sections in your documentation
    * _Introduction_: please provide a summary of the documentation at the top of the page
    * _Pre-requisites_: describe anything that needs to be done for the documentation to work - whether it be other steps to have been done previously or have installed certain software, etc
    * _Installation or Configuration, etc_: the main body of the documentation
    * _Testing_: how do know that the installation or configuraiton was successful
7. "Front Matter" is now deprecated. 


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

## Editor
Looking for a Markdown Editor? Try [Typora](https://typora.io/)! 

Most IDEs have markdown and restructuredText plugins.
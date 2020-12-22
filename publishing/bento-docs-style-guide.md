# Bento Docs Style Guide



## Format: Markdown vs ReStructuredText

Either markdown or restructured text can be used for writing. For instructions on either syntax, please refer to

* [Github Guides: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
* [Markdown: Syntax](https://daringfireball.net/projects/markdown/syntax)
* [reStructuredText](https://docutils.sourceforge.io/rst.html)

1. For images: put all images relative to `/assets` path, and we will put images in the `source/assets/` folder
2. File naming convention:
   * all markdown files should end in `.md`
   * all reStructredText should end in `.rst`
   * use hyphens instead of spaces in file name (good: `my-file.md`, bad: `my file.md`)



## Images

Please place images in the `source/assests/` folder. 

Please use relative paths; do not reference their location using the github base url (don't use: `https://github.com/CBIIT/bento-docs/blob/master/source/assets/Bento-Header-Logo.png`).



## Document Structure

1. Only use 1 top level `#` header, keep it at the top of the documentation, under the "Front Matter"
2. Try to limit documentation to three heading levels. Do not use more than four levels of headers. (Do not use more than four octothorpe `####`)
3. Document structure: please include the following sections in your documentation

* _Introduction_: please provide a summary of the documentation at the top of the page
* _Pre-requisites_: describe anything that needs to be done for the documentation to work - whether it be other steps to have been done previously or have installed certain software, etc
* _Installation or Configuration, etc_: the main body of the documentation
* _Testing_: how do know that the installation or configuraiton was successful

4. "Front Matter" is now deprecated. 



## Best Practices

* include a troubleshooting section if appropriate
* add any major terms to `bento-glossary.md`
* spell check the documentation



## Info and Warning Boxes
Use Warning and Notes to highlight important  points. Try using quotes and the following gist:



> :warning:   **WARNING**:   For every new facet section, the corresponding styling section should be updated with the same name (see #2 instructions to add styling for facet sections) 



> :point_right:   **NOTE**: the order of the entries in `tabIndex` should match the order in the `tabs` object. This is the order that the tabs will be displayed left to right on the UI.

or using tables (instead of quotes)


| :point_right: NOTE                                           |
| :----------------------------------------------------------- |
| For every new facet section, the corresponding styling section should be updated with the same name (see #2 instructions to add styling for facet sections) |



## Emoji support

Yup. It's in there!  Can be used as alternate symbols for things such as tips/hints/danger/bug boxes. Just don't go overboard.  😁 `:grin`:

💣	`:bomb:`
👉	`:point_right:`
🔧  `:wrench:`
🚫	`:no_entry_sign:`
‼️	`:bangbang:`
❓	`:question:`


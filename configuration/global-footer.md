---
layout: default
nav_order: 18
title: Global Footer
---

# Global Footer

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## Configuration

### Number of menu items: 
I would like to specify the number of menu items in the nav-bar (maximum = 4)
Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
The UI will display 'Max value error message '

**Organization logo:** I would like to specify the path to a file storing the organization's logo, as an image, that will be displayed on the left hand side of the footer. See example attached image: footer_text1.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice 
Change the `footerStaticText` to point internal or external Image url

**Static Footer text:** I would like to specify a short text content that will be placed in the bottom center of footer. See example attached image: footer_text_2.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change the `footerStaticText` to change Static Footer text

**The number of Footer Subsections**: A Footer subsection may be defined as a column of anchor links along with a column header. I would like to specify the number of footer subsections (maximum = 3). If this number is not specified, then no footer subsections will be displayed. See example attached image: footer_subsection.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change Add few more objects in `link_sections` you will see the error

**Footer Subsection Header:** I would like to specify the column header for each footer subsection. Examples: “About CTDC”, “More Information”.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change `title` in the `link_sections` you can edit the title subsection

**The number of Footer Subsection Links**: I would like to specify the number of links to be included for each footer subsection (maximum = 4).
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change Add few more objects in `items` in any of `link_sections` you will see the error

**Footer Subsection Link Text**: I would like to specify the text to be displayed for each footer subsection link.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change `text` in the object of `item` any of `link_sections` you will see the text is updates

**Footer Subsection Link Type:** There are three types of Footer Subsection Link types: (a) “anchor link”, (b) “email link” and (c) “social media link”. I would like to specify the link type for each footer subsection link.
Footer Subsection Link URL: For a footer subsection links of type “anchor link” or “social media link” I would like to specify the URL.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change `link` in the object of `item` any of `link_sections` you will see the link is updatedThe link can be internal, external or an email

**Footer Subsection Link Email:** For a footer subsection links of type “email link”, I would like to specify the email address to which the email should be sent.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change `link` in the object of `item` any of `link_sections` you will see the link is updated link can be internal, external or an email

**Footer Subsection Icon:** For footer subsection links of type “social media link” I would like to specify the path to a file, on the server, that stores an icon image for said social media platform.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice  Change /Add `icon` pointing to the image in the object of `item` any of `link_sections` you will see the icon displayed on the footer subsection.

**The number of Footer Anchor Links:** I would like to specify the number of footer anchor links to be displayed bottom center of the footer (maximum = 4). See example image: footer_links.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice
Change Add few more objects in `nci_links` you will see the error

**Footer Anchor Link Text:** I would like to specify the link text for each footer anchor link.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice
Change `text`  of any object `nci_links` you will the text changed

**Footer Anchor Link URL**: I would like to specify the URL for each footer anchor link.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice
Change `link`  of any object `nci_links` you will the link is updated.
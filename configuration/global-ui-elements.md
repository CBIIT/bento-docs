---
sort: 1
title: Global UI Elements
---

# Global UI Elements

Global UI elements are displayed on every page of a Bento application. These are the (a) Web Browser tab, (b) Global Footer, (c) Navigation Bar and (d) Global Footer. The "Stats" bar, that displays the high-level statistics is a semi-global element as it is displayed only in the Program Listing, Program Detail, Dashboard and Case Detail pages. See below for details.
![Global UI Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/global_elements.png?raw=true)
**Global User Interface Elements**. Displayed are the global elements that are displayed on all pages of a Bento-based data sharing platform. These are: the web browser tab, the global header, global footer, the navigation bar and the stats bar. The stats bar is semi-global in scope as it is displayed in only a subset of the application's pages.


### Prerequisites

1. The files that specify the configuration parameters of the Bento UI are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Here is a mapping of each Global UI element to it's configuration file:

Global UI Element    | Configuration File
---------------------|------------------------------------------------------
Web Browser Tab      |`$(src)/bento-frontend/public/index.html`
Global Header        |`$(src)/bento-frontend/src/bento/headerData.js`
Global Footer        |`$(src)/bento-frontend/src/bento/headerData.js`
Global Navigation Bar|`$(src)/bento-frontend/src/bento/navigationBarData.js`
Stats Bar            |`$(src)/bento-frontend/src/bento/stats.js`

3. All images and icons should be accessible via a public url. 

## Web Browser Tab
Web browser tabs allow you to have multiple web pages open at the same time. An application-specific icon and text will allow an end user to keep track of the tab running a Bento application.

### Configuring the Favicon
The favorite icon (or favicon) that appears in the web browser tab can be configured in two ways:

 Option A: Using a web-based location:

 1. Edit `$(src)/bento-frontend/public/index.html` with the editor of your choice
 2. Replace line  `<linkrel="shortcut icon" href="https://raw.githubusercontent.com/CBIIT/bento-frontend/master/public/favicon.ico"/>` with `<linkrel="shortcut icon"href="{URL of the file}"/>`

 Option B: Using a local-based location (within the repo):
 1. The location is specified the the git repo is in the file:  `$(src)/bento-frontend/public/`
 2. Replace line  `<linkrel="shortcut icon" href="https://raw.githubusercontent.com/CBIIT/bento-frontend/master/public/favicon.ico"/>` with `<linkrel="shortcut icon"href="/{file_name}"/>`

### Configuring the Tab Title
The HTML Title element `<title>` defines the document's title that is shown in a browser's title bar or a page's tab.
The Title, or tab text, can be specified as follows:
1. Edit `$(src)/bento-frontend/public/index.html` with the editor of your choice.
2. Replace line  `<title>Bento</title>` with `<title>{ title you want}</title>`

## Global Header
The Global header appears at the top of all Bento-based applications. It displays a platform-specific logo and image.

### Configuring the Global Header Logo
1. Edit `$(src)/bento-frontend/src/bento/headerData.js` with the editor of your choice
2. Set field `globalHeaderLogo` with stored image url.
3. An optional embedded link can be specified in the field `globalHeaderLogoLink`.
4. Example:
```javascript
export default {
  globalHeaderLogo: '<path to Global Header Logo file>',
  globalHeaderLogoLink: '<url to be embedded in Global Header Logo>',
  ...
 }
```

### Configuring the Global Header Image
1. Edit `$(src)/bento-frontend/src/bento/headerData.js` with the editor of your choice
2. Set field `globalHeaderImage` with a stored image URL.
3. Set field `globalHeaderLogoAltText` with the text need to display when image is not available.
4. Example:
```javascript
export default {
  ...
  globalHeaderLogoAltText: '<Alt text for your Global Header Image>',
  globalHeaderImage: '<path to Global Header Image file>',
};
```

## Global Footer
The Global Footer appears at the bottom of every page in a Bento-based application. The Global Footer may be used to display an organization logo and additional links, that may be helpful for the end user, such as documentation, support email and social media platforms.
![Global Footer Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/global_footer.png?raw=true)
**The Global Footer.** Displayed are the elements of the Global Footer. 

### Configuring the Organization Logo 
1. Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice 
2. Set field `footerLogoImage` with stored image URL.
3. Example:
```javascript
export default {
  footerLogoImage: '<URL for Global Footer Logo file>',
  ...
};
```

### Configuring Static Footer Text
I would like to specify a short text content that will be placed in the bottom center of footer.
1. Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice.
2. Set the field `footerStaticText` to the text of your choice.
3. Example:
```javascript
export default {
  ...
  footerStaticText: '<Your footer text>',
  ...
};
```

### Configuring the Footer Subsections
A Footer subsection may be defined as a column of anchor links along with a column header. These are optional components; if no footer subsections are specified, none will be displayed. Bento allows a maximum of *3* footer subsections to be displayed. If you specify more than 3 footer subsections, **Bento will display the first three without any error or warning messages**.
<br> Each Footer Subsection has several components: Header, Links, Link Text, Link Types, Link Icons. Given below are instructions on how to configure each of these components.

1. Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice.
2. Each Footer Subsection is configured by one element in the `links_section` list.
3. Set the field `title` to the Footer Subsection Title.
4. Footer subsection links provide an entry point to both internal and external pages. Bento allows a maximum of **4** links per Footer Subsection. Footer subsection links can be specified with the `items` dictionary of a `link_sections` list element.
If you specify more than 4 links, **Bento will display only the first 4 links without any warning or error message.**
  * Set the field `text` to the display text for your link.
  * Set the field `link` to the link of your choice. Valid links (a) an internal link to a Bento page (b) an external link (c) a valid email address.
  * A Footer Subsection Link can also be displayed as an icon. For example, you can embed the icon and link of a social media platform in your Footer Subsection.
5. Here is an example of a Footer Subsection with four types Footer Subsection links:
```javascript
export default {
  ...
  link_sections: [
    {
      title: '<Footer Subsection Header>',
      items: [
        {
          text: '<Link Text>',
          link: '<Internal Link>',
        },
        {
          text: 'Contact Us',
          link: '<Emai Link>',
        },
        {
          text: 'Documentation',
          link: '<External Link>',
        },
        {
          link: '<External Link>',
          icon: '<URL for displayed icon>',
        },
      ],
    },
    ...
    ]
  ...
};
```

### Configuring the number of Footer Anchor Links
I would like to specify the number of footer anchor links to be displayed bottom center of the footer (maximum = 4). 
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice
Add your anchor links `nci_links`.
Note: if you specify more than 4 links, the system will display the first four any warning or error message.

### Configuring the Footer Anchor Link Text
I would like to specify the link text for each footer anchor link.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice
Specify the text in the `text` field of a `nci_links` object.

### Configuring the Footer Anchor Link URL
I would like to specify the URL for each footer anchor link.
Edit `$(src)/bento-frontend/src/bento/footer.js` with the editor of your choice
Change `link`  of any object `nci_links` you will the link is updated.

## Global Navigation Bar
The Global Navigation bar (Nav bar) is serves as an entry point to other sites within the application. 

### Configuring the Global Navigation Bar

1. Specifiying the number of menu items: I would like to specify the number of menu items in the Nav bar (maximum = 4)
    * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
    * Note: Bento allows a maximum of **4** menu items. If you add more than 4 menu items, only the top 4 will be displayed without any warning or error message.

2. Menu item ordering: I would like to specify the left to the right ordering of the menu items.
    * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice
    * The top-down order of objects will display left to right in the UI.

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
   * Edit `$(src)/bento-frontend/src/bento/navigationBarData.js` with the editor of your choice.
   * set field `type` to dropdown
   * create a field dropDonwLinks and add objects with these fields
     * labelText: 'purpose',
     * link: '/purpose'

## "Stats" Bar
The Stats bar displays a set of summary statistics, for a Bento-based application, that gives the end user a high-level view of the volume and diversity of the curated data. 
### Configure the Stats Bar

1. Edit `$(src)/bento-frontend/src/bento/stats.js` with the editor of your choice

2. Under `stats`,

3. set the field `statTitle` to have the desired title for the stat.

4. set the field `datatable_field` to have the respective in the dashboard query (As the stat should be responsive).

5. set the field `type` to have one of the values [field, array, or object] how its returned in the dashboard query.

6. set the field `statAPI` to have its respective field to get initial value from stats query

7. Under `globalStatsQuery` add the respective GraphQL query field to get the initial value.

## Suggested Best Practice
- Suggested dimensions for the favicon: W X H pixels
- The Web Browser Tab title should have a maximum of X characters.
- Suggested dimensions for the Global Header Logo: 468x80 pixels
- Suggested dimensions for the Global Header Image: 1200x60 pixels
- Suggested dimensions for the Global Footer Logo: 310x80 pixels
- Suggested dimensions for the Footer Subsection Icon: W X H pixels
- All images should have a resolution >= 72 ppi and should be in the PNG format.
- All Alt tags should be short (maximum limit =125 characters). You may add multiple, comma-separated key words in the Alt tag.
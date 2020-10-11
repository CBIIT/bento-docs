---
sort: 1
title: Global UI Elements
---

# Global UI Elements

Global UI elements are displayed on every page of a Bento application. These are the (a) Web Browser tab, (b) Global Footer, (c) Navigation Bar and (d) Global Footer. The "Stats" bar, that displays the high-level statistics is a semi-global element as it is displayed only in the Program Listing, Program Detail, Dashboard and Case Detail pages. See below for details.
![Global UI Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/global_elements.png?raw=true)
**Global User Interface Elements**. Displayed are the global elements that are displayed on all pages of a Bento-based data sharing platform. These are: the web browser tab, the global header, global footer, the navigation bar and the stats bar. The Stats Bar is semi-global in scope as it is displayed in only a subset of the application's pages.


### Prerequisites

1. The files that specify the configuration parameters of the Bento UI are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. All images and icons that you use in your Bento instance should be accessible via a public URL. 

3. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query type(s) that return your data of interest.

4. Here is a mapping of each Global UI element to it's configuration file:

Global UI Element    | Configuration File
---------------------|------------------------------------------------------
Web Browser Tab      |`$(src)/bento-frontend/public/index.html`
Global Header        |`$(src)/bento-frontend/src/bento/globalHeaderData.js`
Global Footer        |`$(src)/bento-frontend/src/bento/globalFooterData.js`
Global Navigation Bar|`$(src)/bento-frontend/src/bento/navigationBarData.js`
Stats Bar            |`$(src)/bento-frontend/src/bento/globalStatsData.js`


## Web Browser Tab
Web browser tabs allow you to have multiple web pages open at the same time. An application-specific icon and text allows an end user to keep track of the tab running a Bento application.

### Configuring the Favicon
The favorite icon (or favicon) that appears in the web browser tab can be configured in two ways:

 Option A: Using a web-based location:

 1. Open `$(src)/bento-frontend/public/index.html`.
 2. Replace line  `<linkrel="shortcut icon" href="https://raw.githubusercontent.com/CBIIT/bento-frontend/master/public/favicon.ico"/>` with `<linkrel="shortcut icon"href="{URL of the file}"/>`

 Option B: Using a local file in your repo:
 1. The location is specified in the git repo and is in the file:  `$(src)/bento-frontend/public/`
 2. Replace line  `<linkrel="shortcut icon" href="https://raw.githubusercontent.com/CBIIT/bento-frontend/master/public/favicon.ico"/>` with `<linkrel="shortcut icon"href="/{file_name}"/>`

### Configuring the Tab Title
The HTML Title element `<title>` defines the document's title that is shown in a browser's title bar or a page's tab.
The Title, or tab text, can be specified as follows:
1. Open `$(src)/bento-frontend/public/index.html`.
2. Replace line  `<title>Bento</title>` with `<title>{ title you want}</title>`

## Global Header
The Global header appears at the top of all Bento-based applications. It displays a platform-specific logo and image.

### Configuring the Global Header Logo
1. Open `$(src)/bento-frontend/src/bento/globalHeaderData.js`.
2. Set field `globalHeaderLogo` with stored image URL.
3. An optional embedded link can be specified in the field `globalHeaderLogoLink`.
3. Set field `globalHeaderLogoAltText` to the ALT tags for the Global Header Logo.
4. Example:
```javascript
export default {
  globalHeaderLogo: '<path to Global Header Logo file>',
  globalHeaderLogoLink: '<URL to be embedded in Global Header Logo>',
  globalHeaderLogoAltText: '<ALT tags for Global Header Logo.>'
  ...
 }
```

### Configuring the Global Header Image
1. Open `$(src)/bento-frontend/src/bento/globalHeaderData.js`.
2. Set field `globalHeaderImage` with a stored image URL.
3. Example:
```javascript
export default {
  ...
  globalHeaderImage: '<path to Global Header Image file>',
};
```

## Global Footer
The Global Footer appears at the bottom of every page in a Bento-based application. The Global Footer may be used to display an organization logo and additional links, that may be helpful for the end user, such as documentation, support email and social media platforms.
![Global Footer Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/global_footer.png?raw=true)
**The Global Footer.** Displayed are the elements of the Global Footer. 

### Configuring the Organization Logo 
1. Open `$(src)/bento-frontend/src/bento/globalFooterData.js`. 
2. Set field `footerLogoImage` with stored image URL.
3. Example:
```javascript
export default {
  footerLogoImage: '<URL for Global Footer Logo file>',
  ...
};
```

### Configuring Static Footer Text
1. Open `$(src)/bento-frontend/src/bento/footer.js`.
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

1. Open `$(src)/bento-frontend/src/bento/footer.js`.
2. Each Footer Subsection is configured by one element in the `links_sections` list.
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
Footer Anchor Links allows you to optionally embed additional organizational URLs.
Bento allows you embed 4 footer anchor links. If you specify more than 4 links, **Bento will display the first four any warning or error message**. 
1. Open `$(src)/bento-frontend/src/bento/footer.js`.
2. Add your anchor links to `global_footer_links`.
  * Set the `text` field to the text to be displayed.
  * Set the `link` field to the desired URL.
3. Example: 
```javascript
export default {
...
  global_footer_links: [
    {
      text: '<Link Display Text>',
      link: '<Embedded URL>',
    },
    ...
  ],
};
```

## Global Navigation Bar
The Global Navigation bar (Nav bar) serves as an entry point to other sites within the application. Bento allows a maximum of **4** menu items. If you add more than 4 menu items, only the top 4 will be displayed without any warning or error message.

### Configuring the Global Navigation Bar

1. Open `$(src)/bento-frontend/src/bento/navigationBarData.js`. The top-down order of menu items will display left to right in the UI.
2. Specify a menu item as a object.
  * Set the field `labelText` to the text to be displayed.
  * Set the field `type` to 'link' (see below for configuring drop-down menu items). 
  * Set the field `link` to the desired external or internal link.
3. Example of adding a Menu Item of type 'Link':
```javascript
export default [
  {
    labelText: 'home',
    type: 'link',
    link: '/home',
  },
  ...
  ]
```
5. Bento allows the Nav Bar to display drop-down menu items. To specify drop-down menu items:
  * Set the field `labelText` to the text to be displayed.
  * Set the field `type` to 'dropdown'.
  * Each drop-down item can be specified in the dropDownLinks object. In the dropDownLinks object, for each drop-down item: (a) set the field `labelText` to the text to be displayed (b) set the field `link` to the desired external or internal link.
6. Example of adding a Menu Item of type 'Drop-down':
```javascript
export default [
  ...
  {
    labelText: '<Label for drop-down Menu>',
    type: 'dropdown',
    dropDownLinks: [
      {
        labelText: '<Label for first drop-down item>',
        link: '<link for first drop-down item>',
      },
      {
        labelText: '<Label for second drop-down item>',
        link: '<link for second drop-down item>',
      },
      {
        labelText: '<Label for third drop-down item>',
        link: '<link for third drop-down item>',
      },
    ],
  },
  ...
  ]
```

## "Stats" Bar
The Stats bar displays a set of summary statistics, for a Bento-based application, that gives the end user a high-level view of the volume and diversity of the curated data. A maximum of **6** statistics are allowed to be displayed. **If you add more than 6 statistics, only the top 6 will be displayed without any warning or error message**.

### Configure the Stats Bar
1. Open `$(src)/bento-frontend/src/bento/stats.js`.
2. For each object in `globalStatsData`:
  * Set the field `statTitle` to the display label for the statistic.
  * Set the field `datatable_field` to have the respective in the dashboard query.
  * Set the field `type` to have one of the values [field, array, or object] how its returned in the dashboard query.
  * Set the field `statAPI` to have its respective field to get initial value from stats query
  * Under `GET_GLOBAL_STATS_DATA_QUERY` add the respective GraphQL query field to get the initial value.
3. Example:
```javascript
export const globalStatsData = [
  // A maximum of 6 stats are allowed
  {
    statTitle: '<Stat Label>',
    datatable_field: '<Your Datatable field name',
    datatable_sub_field:: '<Your Datatable subfield name, if applicable>',
    type: '<field|array|object>',
    statAPI: '<Your GraphQL API query>',
  },
  ...
  ]
export const GET_GLOBAL_STATS_DATA_QUERY = gql`{
  '<Your GraphQL API query>'
  ...
  }
  `;
```

## Suggested Best Practice
- Dimensions of the favicon: 32 X 32 pixels
- The Web Browser Tab title should have a maximum of 33 characters
- Dimensions of the Global Header Logo: 468x80 pixels
- Dimensions of the Global Header Image: 1200x60 pixels
- Dimensions of the Global Footer Logo: 310x80 pixels
- Dimensions of the Footer Subsection Icon: 20 X 20 pixels
- All images should have a resolution >= 72 ppi and should be in the PNG format.
- All Alt tags should be short (maximum limit =125 characters). You may add multiple, comma-separated key words in the Alt tag.

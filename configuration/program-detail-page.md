---
sort: 4
title: Program Detail Page
---

# Program Detail Page
The Program Detail Page displays detailed, program-level information for each of the programs that has submitted data to your data sharing platform. A Bento Program Detail Page has several configurable components. See below for details. 
![Program Detail Page Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/program-detail-page.png?raw=true)
**Program Detail Page Elements.** Displayed are the configurable components of a Bento Program Detail Page: Program Detail Page Title, Program Detail Page Subtitle, Program Detail Page Icon, Breadcrumb, Data Labels, Data Fields, Table Title, Table Column Header, Table Column Content, Program Level Widget, Program Level Aggregate Count, Program Level File Count and Embedded External and Internal Links.

### Prerequisites

1. The files that specify the configuration parameters of the Bento Landing Page are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for all Program Listing Page elements can be specified in the file: `$(src)/bento-frontend/blob/master/src/bento/programData.js`.

3. All images and icons that you use in your Bento instance should be accessible via a public url. 

4. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query type(s) that return your data of interest.

## Page Title Configuration
The Page Title section has three components: (a) Page Title (b) Page Subtitle and (c) Breadcrumb.

### Configuring the Page Title, Page Subtitle and Breadcrumb

1. Open `bento-frontend/src/bento/programDetailData.js`
2. Under `pageTitle`:
	* Set the field `label` to the Page Title of your choice.
	* Set the field `field` to the GraphQl API query that returns the Page Title. 
3. Under pageSubTitle:
	* Set the field `field` to the GraphQL API query that will return the Page Subtitle.
4. Under `breadCrumb`:
	* Set the field `label` to the Breadcrumb text of your choice.
	* Set the field `link` to the internal link to be embedded in your Breadcrumb.
5. Add your GraphQL API queries to `PROGRAM_DETAIL_QUERY`.
6. Example:

```javascript
...
const pageTitle = {
  label: '<Your Page Title>',
  field: '<GraphQL API query that returns the Page Title>',
};

const pageSubTitle = {
  field: '<GraphQL API query that returns the Page Subtitle>',
};

const breadCrumb = {
  label: '<Your Breadcrumb display text>',
  link: '<Your Breadcrumb embedded link>',
};
...
```
 
## Configuring the Aggregate Count
The Program Level Aggregate Count field allows you to display a Program level count for an key data entity in your data sharing platform.
1. Open `bento-frontend/src/bento/programDetailData.js`.
2. Under `aggregateCount`:
	* Set the field `labelText` to the display text for your aggregate count of your choice.
	* Set the field `field` to the GraphQL API query that returns your aggregate count.
	* Set the field 'link'  to the embedded link for the aggregate count. This is usually a link to an internal page that displays additional detail on the aggregate count.
 	* Set the field `display` to 'true' if you want to display an aggregate  count, 'false' otherwise.
3. Add your GraphQL API queries to `PROGRAM_DETAIL_QUERY`.
4. Example:

```javascript
...
const aggregateCount = {
  labelText: '<Display label for your Aggregate Count>',
  field: '<GraphQL API query that returns your Aggregate Count>',
  link: '<embedded link for you Aggregate Count>',
  display: '<true|false>',
};
...
```
 

## Configuring the icons in the Program Detail Page
The Progam Detail Page supports a Program Detail Page Icon, displayed next to the Program Title, and an External Link Icon, that is displayed next to an external link in the page.

1. Open `bento-frontend/src/bento/programDetailData.js`.
2. Under `icon`:
	* Set the field 'src' to the URL for the Program Detail Page Icon of your choice.
	* Set the field 'alt' to the ALT tag for the Program Detail Page Icon.
3. Under `externalLinkIcon`:
	* Set the field 'src' to the URL for the External Link Icon of your choice.
	* Set the field 'alt' to the ALT tag for the External Link Icon.
4. Example:

```javascript
...
const icon = {
  src: '<URL to your Program Detail Page Icon>',
  alt: '<ALT tag for your Program Detail Page Icon>',
};

const externalLinkIcon = {
  src: '<URL to your External Link Icon>',
  alt: '<ALT tag for your External Link Icon>',
};
...
```

 

## Left panel configuration

### Configurable data elements (attributes)

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for label 'field' under 'leftPanelattributes'->'data'
3. Edit the value for label 'label' under 'leftPanelattributes'->'data'
4. Note limit set to a maximum of 6 attributes in this section.

### Configurable hyperlinks on data elements (Internal, External, external link to label, internal link to label)

Custodian shall have the ability to add hyperlinks to table contents.

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for label 'link' under 'leftPanelattributes'->'data'

#### Internal Links
1. links starting with '/' are considered as internal links
2. Internal links shall be opened in the same tab.
3. Dynamic links can be generated by passing a valid table filed to '{}'. For example, '/arm/{study_acronym}' shall link to 'arm/A'

#### External Links
1. External links shall start with 'http://' or'https://'
2. External links shall show-up with 'externalLinkIcon' (see #2 under 'icons configuration' on how to configure an external link icon)
3. External link shall be opened in a new tab.
4. Dynamic links can be generated by passing a valid table filed to '{}'. For example, 'https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}' shall link to 'https://pubmed.ncbi.nlm.nih.gov/29860917/'

#### Internal Links to label
1. Set 'internalLinkToLabel' as true under 'leftPanelattributes'->'data'.
2. Label is delivered as link with field value
3. Internal links to label shall be opened in same tab

### External Links to label
1. Set 'externalLinkToLabel' as true under 'leftPanelattributes'->'data'
2. Label is delivered as link with field value
3. External links shall show-up with 'externalLinkIcon' (see #2 under 'icons configuration' on how to configure an external link icon)
4. External links to label shall be opened in a new tab
 

## Right panel configuration

### Configure widget

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for key 'field' under 'rightpanel'->'widget'.
3. Edit the value for key 'label' under 'rightpanel'->'widget'.
4. Edit the value for key 'display' under 'rightpanel'->'widget'. (This can be either 'true' or 'false'. Setting this value to 'false' shall hide this widget section eniterly.)

### Configure Number of files

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for key 'field' under 'rightpanel'->'files'.
3. Edit the value for key 'label' under 'rightpanel'->'files'.
4. Edit the value for key 'fileIconSrc' under 'rightpanel'->'files' to display an icon.
5. Edit the value for key 'fileIconAlt' under 'rightpanel'->'files'.
6. Edit the value for key 'display' under 'rightpanel'->'files'. (This can be either 'true' or 'false'. Setting this value to 'false' shall hide this files section eniterly.)
 

## Table configuration

### Configure Table Title

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for key 'title' under 'table'.

### Configure Table Header (labels for each column)

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for label 'label' under 'table'->'columns'
3. Note: Limit set at maximum 10 table headers/columns

### Configure Table Contents

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for label 'field' under 'table'->'columns'
3. Note: Limit set at maximum 10 table headers/columns

### Configure default sort

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. To specify which table column should be sorted by default - Edit the value for label 'defaultSortField' under 'table'.
3. Note: This should be one of 'field' in table->'column'
4. To specify sort direction - Edit the value for label 'defaultSortDirection' under 'table'
5. Note: This should be either 'asc' for ascending or 'desc' for descending

### Configurable hyperlinks for table (Internal and External)

Custodian shall have the ability to add hyperlinks to table contents.

1. Open the configuration file located at bento-frontend/src/bento/programDetailData.js
2. Edit the value for label 'link' under 'table'->'columns'

#### Internal Links
1. links starting with '/' are considered as internal links
2. Internal links shall be opened in the same tab.
3. Dynamic links can be generated by passing a valid table filed to '{}'. For example, '/arm/{study_acronym}' shall link to 'arm/A'

#### External Links
1. External links shall start with 'http://' or'https://'
2. External links shall show-up with 'externalLinkIcon' (see #2 under 'icons configuration' on how to configure an external link icon)
3. External link shall be opened in a new tab.
4. Dynamic links can be generated by passing a valid table filed to '{}'. For example, 'https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}' shall link to 'https://pubmed.ncbi.nlm.nih.gov/29860917/'

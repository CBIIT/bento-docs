---
sort: 3
title: Program Listing Page
---

# Program Listing Page
The Program Listing Page lists the programs that store data in your data sharing platform. A Bento Program Listing Page has several configurable components. See below for details.
![Program Listing Page Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/program-listing-page.png?raw=true)
**Program Listing Page**. Displayed are the configurable elements of a Bento Program Listing Page. These are: Table Title, Table Icon, Table Column Headers, Table Content, embedded Internal and External URLs and External Link Icon.

### Prerequisites

1. The files that specify the configuration parameters of the Program Listing Page are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for all Program Listing Page elements can be specified in the file: `$(src)/bento-frontend/blob/master/src/bento/programData.js`.

3. All images and icons that you use in your Bento instance should be accessible via a public url. 

4. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query type(s) that return your data of interest.

## Icons in the Program Listing Page.
There are two configurable icons in the Program Listing Page: (a) the Table Icon, that is a visual represenation of the Program Listing Table and (b) the External Link Icon that is a visual representation of an external link.

### Configuring the Icons in the Program Listing Page.
1. Open `$(src)/bento-frontend/blob/master/src/bento/programData.js`.
2. Under `programListingIcon`:
	* Set the field `src` to the URL of your Table Icon image file.
	* Set the fild `alt` to the ALT tag for your Table Icon.
3. Under `externalLinkIcon`:
	* Set the field `src` to the URL of your External Link Icon image file.
	* Set the fild `alt` to the ALT tag for your External Link Icon.
4. Example: 

```javascript
const programListingIcon = {
  src: 'URL for your Table Icon',
  alt: 'ALT tag for your Table Icon',
};

const externalLinkIcon = {
  src: 'URL for your External Link Icon',
  alt: 'ALT tag for your External Link Icon',
};
```

## The Program Listing Table
The table in the Program Listing Page lists the programs that store data in your data sharing platform.

### Configuring the Program Listing Table.
1. Open `$(src)/bento-frontend/blob/master/src/bento/programData.js`.
2. In `table`:
	* The `display` field is set to true, by default. *Set this field to false if you do not wish to display a table in the Program Listing Page*.
	* Set the field `title` to the the title of your table.
	* Set the field `dataField` to the name of the GraphQL API query being used to return data for the Program Listing Page. *Note: This query should match the GraphQL API query in `GET_PROGRAMS_DATA_QUERY`*.
	* Set the field `defaultSortField` to the name of the query field that will be used to sort the Program Listing Table. Note: this query field should be displayed as one of the columns in the Program Listing Table.
	* Set the field `defaultSortDirection` to the sort order of your choice. Valid values are 'asc' (ascending) and 'desc' (descending).
	* Add your GraphQL API query to `GET_PROGRAMS_DATA_QUERY`.
3. Example:

```javascript
...
const table = {
  display: true,
  title: '<Table Title>',
  dataField: '<GraphQL API query returning data for this page.>',
  defaultSortField: '<GraphQL API query field used to sort the table.>',
  defaultSortDirection: '<sort order, asc|desc>',
 ...
const GET_PROGRAMS_DATA_QUERY = gql`{
  '<Your GraphQL query>'' {
  	'<Data fields returned by your GraphQL API query>'
	... 
 }
}
```

### Adding columns to the Program Listing Table.
You can add up to 10 columns in the Program Listing Table. If you add more than 10 columns, **Bento will display the first 10 columns without an error or warning message**. The top-down order of columns will be displayed left to right on the UI.
1. Open `$(src)/bento-frontend/blob/master/src/bento/programData.js`.
2. Under `table`, 
   * Add an object {dataField:, header: , link: } to `columns`:
	  * Set the field `dataField` to the GraphQL API query data field that returns the data for the column.
	  * Set the field `header` to the column header name.
	  * Set the field `link` to an internal or external link that is to be embedded into the the column value. See below for additional instructions on adding internal and external links. *Links are optional*.
	* Add your GraphQL API query data field to `GET_PROGRAMS_DATA_QUERY`.
3. Example:

```javascript
const table = {
  ...
  columns: [
    {
      dataField: '<GraphQL API query field returning data for this column>',
      header: '<Column Header>',
      link: '<link to be embedded in column value>',
    },
    {
      dataField: '<GraphQL API query field returning data for this column>',
      header: 'PubMed ID',
    },
    ...
  ],


};

const GET_PROGRAMS_DATA_QUERY = gql`{
  '<Your GraphQL query>'' {
  	'<Data fields returned by your GraphQL API query>'
	... 
 }
}
```


#### Internal Links in the Program Listing Table.
1. links starting with '/' are considered as internal links.
2. Internal links shall be opened in the same tab.
3. Dynamic links can be generated by passing a valid table field to '{}'. For example, '/program/{program_id}' shall link to 'program/NCT00310180'.

#### External Links in the Program Listing Table.
1. External links shall start with 'http://' or'https://'.
2. External links shall show-up with 'externalLinkIcon'.
3. External link shall be opened in a new tab.
4. Dynamic links can be generated by passing a valid table filed to '{}'. 
   For example, 'https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}' shall link to 'https://pubmed.ncbi.nlm.nih.gov/29860917/'.

## Suggested Best Practice
- Dimension of the Program Listing Icon= 100 X 100 pixels.
- Dimension of the External Link Icon = 16 X 16 pixels.
- All images should have a resolution >= 72 ppi and should be in the PNG format.
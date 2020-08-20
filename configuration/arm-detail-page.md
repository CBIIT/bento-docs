---
sort: 5
title: Arm Detail Page
---

# Arm  Detail Page
The Arm Detail Page provides a summary of a Study/Project/Arm of that belongs to a Program that participates in your data sharing platform.

![Arm Detail Page](../assets/arm-detail-page.png)

### Prerequisites
1. The files that specify the configuration parameters of the Arm Detail Page are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for all Arm Detail Page elements can be specified in the file: `$(src)/bento-frontend/blob/master/src/bento/armDetailData.js`.

3. All images and icons that you use in your Bento instance should be accessible via a public url. 

4. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query type(s) that return your data of interest.

<p>&nbsp;</p>

### Configuring the Arm Detail Page.
The Arm Detail Page allows you to add key arm attributes as label value pairs within a set of subsections(See 3. below). A maximum of **6** sections can be added to the Arm Detail Page. Within each subsection a maximum of **10** attributes can be displayed as label:value pairs. 
<br>If more than 6 subsections are configured, **only the first 6 subsections will be displayed in the UI, other subsections will be ignored**. 
<br>If more than 10 properties are configured, **only first 10 properties will be displayed in the UI, other properties will be ignored**.
<br> The Arm Detail Page also allows you to add an optional table to list Arm level entities.

1. Open the file `$(src)/src/bento/armDetailData.js`.
2. Under `header`:
	* Set the field `label` to the display label for your Arm Detail Page.
	* Set the field `dataField` to the GraphQL API query that returns the value, such as the Arm Name or Arm ID that you want to display.
3. Under `subsections`:
	* For each label:value pair that you wish to display, create a object {label: ,datafield: ,} in `properties`:
        * Set the field `label` to the display label for your attribute.
        * Set the field `dataField` to the GraphQL API query that returns the data to be displayed as value for the given label:value pair.
		* You can embed link to your label or your value, or both. Links can be internal or external. 
			* To add a link to your *value* specify an internal or external link by adding a `link` attribute to your object. 
			* To add a link to your *label* specify an internal or external link by adding a `labelLink` attribute to your object.
    * Add the GraphQL API query field to `GET_ARM_DETAIL_DATA_QUERY`. 




### Configuring the Program Detail Page Table.
1. Open `$(src)/bento-frontend/src/bento/programDetailData.js`.
2. In `table`:
  * The `display` field is set to true, by default. *Set this field to false if you do not wish to display a table in the Program Detail Page*.
  * Set the field `title` to the the title of your table.
  * Set the field `dataField` to the name of the GraphQL API query being used to return data for the Program Detail Page. *Note: This query should match the GraphQL API query in `PROGRAM_DETAIL_QUERY`*.
  * Set the field `defaultSortField` to the name of the query field that will be used to sort the Program Listing Table. Note: this query field should be displayed as one of the columns in the Program Listing Table.
  * Set the field `defaultSortDirection` to the sort order of your choice. Valid values are 'asc' (ascending) and 'desc' (descending).
  * Add your GraphQL API query to `GET_PROGRAM_DETAIL_DATA_QUERY`.
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
const GET_PROGRAM_DETAIL_DATA_QUERY = gql`{
  '<Your GraphQL query>'' {
    '<Data fields returned by your GraphQL API query>'
  ... 
 }
}
```

### Adding columns to the Program Detail Page Table.
You can add up to 10 columns in the Program Detail Page Table. If you add more than 10 columns, **Bento will display the first 10 columns without an error or warning message**. The top-down order of columns will be displayed left to right on the UI.

1. Open `$(src)/bento-frontend/src/bento/programDetailData.js`.
2. Under `table`, add an object `{dataField: , header: , link: ,}` to the `columns` list:
  * Set the field `dataField` to the GraphQL API query data field that returns the data for the column.
  * Set the field `header` to the column header name.
  * Set the field `link` to an internal or external link that is to be embedded into the the column value. See below for additional instructions on adding internal and external links. *Links are optional*.
  * Add your GraphQL API query data field to `GET_PROGRAM_DETAIL_QUERY`.
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

const GET_PROGRAM_DETAIL_QUERY = gql`{
  '<Your GraphQL query>'' {
    '<Data fields returned by your GraphQL API query>'
  ... 
 }
}
```


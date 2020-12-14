# Dashboard
The Dashboard provides the end user with several capabilities (a) filter data entities of in interested via faceted search (b) view graphical summaries of data entities and (c) select data entities for further exploration.

![Dashboard Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/dashboard.png?raw=true)
**Dashboard**. Displayed are the configurable elements of a Bento Dashboard. These are: Dashboard Sidebar Filters, Dashboard Widgets and Dashboard Table.

### Prerequisites

1. The files that specify the configuration parameters of the Dashboard are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for Dashboard elements can be specified in the file: `$(src)/bento-frontend/src/bento/dashboardData.js`.

3. All images and icons that you use in your Bento instance should be accessible via a public url. 

4. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query type(s) that return your data of interest.

## Dashboard Sidebar Filters
The Dashboard Sidebar Filters allow an end user to search for data of interest by applying multiple filters, based on faceted classification, of stored data entities.
<br>You can add a maximum of **12** filters. If you add more than 12 filters, **Bento will display only the first twelve filters, without any warning or error message**.

### Configuring the Dashboard Sidebar Filters

1. Open `$(src)/bento-frontend/src/bento/dashboardData.js`.
2. Under `facetSearchData` add an object {label: , field: , api: , datafield: , show: ,} to represent your filter. 
	* Set the field `label` to the display label for your filter.
	* Set the field `field` to the specific field in the GraphQL API query that is associated with your filter. 
	* Set the field `api` to the GraphQL API query that returns data for your filter.
	* Set the field `datafield` to cross-reference the API query that responds to your filter. For example, if your filter drives a widget that displays data from `responsive_api_query` and it drives a column in the Dashboard table that displays data from `responsive_api_query`, then set the `datafield` to `responsive_api_query`. 
	* Set the field `show` to 'true' to display the filter or to 'false', otherwise.
	* Update `GET_DASHBOARD_DATA_QUERY` with the all GraphQL API queries and fields that are associated with your filters.
3. Example:

```javascript
...
export const facetSearchData = [
  {
    label: '<Filter Label>', 
    field: '<API query field>', 
    api: '<GraphQL API query>', 
    datafield: '<responsive_api_query>', 
    show: <'true|false'>,
  },
  ...
  ]
...
export const GET_DASHBOARD_DATA_QUERY = gql`{
 GraphQL API query{
 	API query field
 }
}  
```

## Dashboard Widgets
Dashboard Widgets provide a graphical summary of the key data entities in your data sharing platform. In this version of Bento, you can add 3, 4 or 6 widgets. If you add more than **6** widgets, Bento will display the first widgets without any error or warning message.

### Configuring the Dashboard Widgets

1. Open `$(src)/bento-frontend/src/bento/dashboardData.js`.
2. Under `widgetsData` add an object {type: ,label: , dataName: , datatable_field: ,show:} to represent your widget.
	* Set the field `type` to the type of widget you want to display. Valid values are *'donut'* and *'sunburst'*.
	* Set the field `label` to the display label for your widget.
	* Set the field `dataName` to the name of the GraphQL API query that returns data for your widget.
	* *If your widget is of type 'donut'*, set the field `datatable_field` to the specific field in the GraphQL API query that returns data for your widget.
	* Sunburst widgets display two types of data within a single plot. *If your widget is of type 'sunburst'*, set the fields `datatable_level1_field` and `datatable_level2_field` to the specific fields in the GraphQL API query that returns data for your sunburst. The field `datatable_level1_field` drives the inner ring of of the sunburst. The field `datatable_level2_field` drives the outer ring of of the sunburst. 
	* Set the field `show` to 'true' to display the widget or to 'false', otherwise.
	* Enter all GraphQL API queries that drive the widgets in `GET_DASHBOARD_DATA_QUERY`.
3. Example:

```javascript
...
export const widgetsData = [
  {
    type: 'sunburst',
    label: '<Widget Label>',
    dataName: '<GraphQL API query that returns data for widget>',
    datatable_level1_field: '<GraphQl API query field that returns data for inner ring of sunburst>',
    datatable_level2_field: '<GraphQl API query field that returns data for outer ring of sunburst>',
    show: '<true|false>',
  },
  {
    type: 'donut',
    label: 'Diagnosis',
    dataName: '<GraphQL API query that returns data for widget>',
    datatable_field: '<GraphQl API query field that returns data for donut>',
    show: '<true|false>',
  },
  ...
  ]
...
export const GET_DASHBOARD_DATA_QUERY = gql`{
 GraphQL API query{
 	API query field
 }
}  
``` 

## Dashboard Table
The Dashboard Table can be configured to list key data entities in your data sharing platform along with a list of key data entity attributes. In the [Bento reference implementation](https://dev.bento-tools.org/#/cases) the Dashboard Table list the cases (or study subjects) in the program.
<br>You can add a maximum of **10** columns to the Dashboard Table. If you add more than 10 columns, **Bento will display only the first ten filters, without any warning or error message**. 

### Configuring External Icon Link
1. Open `$(src)/bento-frontend/src/bento/dashboardData.js`.
2. Under `externalLinkIcon`:
   * Set the field `src` to the URL for the External Icon image of your choice.
   * Set the field `alt` to the ALT tags you want to set for you External Icon.
3. Example: 

```javascript
...
export const externalLinkIcon = {
  src: '<URL for the External Icon of your choice.>',
  alt: '<ALT tags>',
};
...
```

### Configuring the Dashboard Table

1. Open `$(src)/bento-frontend/src/bento/dashboardData.js`.
2. Under `dashboardTable`:
   * Set the field `tableTitle` to a Table Title of your choice.
   * To add a column, add an object {dataField: ,header: ,sort: ,link: ,primary: ,display: ,} to `tableData`.
     * Set the field `dataField` to the GraphQL API query field that returns the data for your column.
     * Set the field `header` to the column header for your column.
     * Add a  `sort` field, if the Dashboard Table is to be sorted by the values of this column.Set the field `set` to 'asc' to sort table by ascending order on the column values, 'desc' to sort in the descending order. 
     * Set the field `link` to an internal or external link that needs to be embedded into the column value. See below for additional information on adding internal and external links. *Links are optional*.
     * Add a `primary` field and set it to 'true' if values in this column are to be used to add the listed data entities to the Cart. For example, if you wish to select cases, in a Dashboard Table displaying cases, by the Case ID column to add to the cart, then the column storing case ids should have a `primary` field and it should be set to 'true'.
     * Set the field `display` to 'true' if you wish to display the column and to 'false', otherwise.
    * Add your GraphQL API queries to `GET_DASHBOARD_TABLE_DATA_QUERY`.
3. Example: 

```javascript
...
export const dashboardTable = {
  tableTitle: 'Cases',
  tableData: [
    // A maximum of 10 columns (tableData) are allowed
    {
      dataField: 'subject_id',
      header: 'Case ID',
      sort: 'asc',
      link: '/case/{subject_id}',
      primary: true,
      display: true,
    },
    ...
    ]
  }
  ...
export const GET_DASHBOARD_TABLE_DATA_QUERY = gql`{

}
```

#### Internal Links in the Dashboard Table.
1. links starting with '/' are considered as internal links.
2. Internal links shall be opened in the same tab.
3. Dynamic links can be generated by passing a valid table field to '{}'. For example, '/program/{program_id}' shall link to 'program/NCT00310180'.

#### External Links in the Dashboard Table.
1. External links shall start with 'http://' or'https://'.
2. External links shall show-up with 'externalLinkIcon'.
3. External link shall be opened in a new tab.
4. Dynamic links can be generated by passing a valid table filed to '{}'. 
   For example, 'https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}' shall link to 'https://pubmed.ncbi.nlm.nih.gov/29860917/'.

## Suggested Best Practice
- Dimension of the External Link Icon = 16 X 16 pixels.
- All images should have a resolution >= 72 ppi and should be in the PNG format.

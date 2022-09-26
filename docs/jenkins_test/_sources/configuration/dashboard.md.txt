# Dashboard
The Dashboard provides the end user with several capabilities (a) filter data entities of in interested via faceted search (b) view graphical summaries of data entities and (c) select data entities for further exploration.

![Dashboard Elements](../assets/dashboard.png)

**Dashboard**. Displayed are the configurable elements of a Bento Dashboard. These are: Dashboard Sidebar Filters, Dashboard Widgets and Dashboard Table.

### Prerequisites

1. The files that specify the configuration parameters of the Dashboard are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for Dashboard elements can be specified in the file: `$(src)/bento-frontend/src/bento/dashboardData.js`.

3. All images and icons that you use in your Bento instance should be accessible via a public url. 

4. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query type(s) that return your data of interest.




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





## Dashboard Facet Search Filters on the Sidebar

The dashboard's facet filters allow an end user to search for data of interest by applying multiple filters, based on faceted classification, of stored data entities.

The facet filters and the sidebar are configured as described in [Dashboard: Facet Search Sidebar](dashboard-facet-search-sidebar.md)



## Dashboard Tabs and Tables

The Dashboard Table can be configured to list key data entities in your data sharing platform along with a list of key data entity attributes. In the [Bento reference implementation](https://dev.bento-tools.org/#/cases) the Dashboard Table list the cases (or study subjects) in the program.

Dashboard tabs and tables are configured as described in [Dashboard: Tabs and Tables](dashboard-tabs-and-tables.md)


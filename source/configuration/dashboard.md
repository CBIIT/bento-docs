# Dashboard
The Dashboard provides the end user with several capabilities (a) filter data entities of interest via faceted search (b) view graphical summaries of data entities and (c) select data entities for further exploration.

![Dashboard Elements](../assets/dashboard.png)

**Dashboard**. Displayed are the configurable elements of a Bento Dashboard: widgets, facet search filters, table, and tabs.

### Prerequisites

1. The files that specify the configuration parameters of the Dashboard are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for Dashboard elements can be specified in the file: `$(src)/bento-frontend/src/bento/dashboardData.js`.

3. All images and icons that you use in your Bento instance should be accessible via a public url. 

4. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query types that return your data of interest.

## Configuring the Dashboard Widgets
Dashboard Widgets provide a graphical summary of the key data entities in your data sharing platform. In this version of Bento, you can add 3, 4 or 6 widgets. If you add more than **6** widgets, Bento will display the first 6 widgets without any error or warning message.

1. Open `$(src)/bento-frontend/src/bento/dashboardData.js`.
2. Under `widgetsData` add an object {type,label, dataName, datatable_field, show} to represent your widget.
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

## Configuring Faceted Search

The dashboard's facet filters allow an end user to search for data of interest by applying multiple filters, based on faceted classification, of stored data entities.

The facet search on the dashboard's side bar can be organized into into sections (or categories), with a maximum count of 15 facets.

To configure the facets:

- Open the configuration file located at `bento-frontend/src/bento/dashboardData.js` (in the "CBIIT/bento-frontend" git repo)

- To represent your filter, edit or create a facet object under the `facetSearchData` object
  
- Each facet is defined as follows:
  
  - `label`:	the display label for your facet filter that appears in the sidebar
  
  - `api`:  the type in the GraphQL api query:  `GET_DASHBOARD_DATA_QUERY`  returns data for your filter.  (It is in the same file: `dashboardData.js`)
  
  - `field`:  the specific field in the GraphQL API query, as the  `api`
  
  - `section`:  the section (or category) that the facet should appear in the sidebar 
  
  - `datafield`: the variable used to cross-reference/pass data to widgets and dashboard data tables,  see: `bento-frontend/src/bento/dashboardTabData.js` (described in [Dashboard: Tabs and Tables](dashboard-tabs-and-tables.md))
  
  - `show`: controls if the facet is displayed or hidden (must be `true` or `false`)
  
  For Example: 
  
  ```javascript
    {
    	 label: 'Program', 
    	 field: 'group', 
    	 api: 'subjectCountByProgram', 
    	 datafield: 'programs',
    	 section: 'Filter By Cases',
     	 show: true,
    },
  ```
  
**NOTE**:  Update the GraphQL API Query in  `GET_DASHBOARD_DATA_QUERY` as needed; it should contain all queries and fields that are associated with your filters

### Faceted Search Styling

The style of each facet section of the side bar can be easily configured.

**Color**

- Open the configuration file located at `bento-frontend/src/bento/dashboardData.js` (in the "CBIIT/bento-frontend" git repo)
- Edit the value for corresponding 'section' under `facetSectionStyling` object
  
  For example:
  
    ```javascript
    'Filter By Cases': {
    	 color: '#10A075',
    	 height: '5px',
    },
    ```
  
**Height**

- Open the configuration file located at `bento-frontend/src/bento/dashboardData.js` (in the "CBIIT/bento-frontend" git repo)
- Edit the value for corresponding 'section' under `facetSectionStyling`
  
  For example: 
  
    ```javascript
    'Filter By Cases': {
       color: '#10A075',
       height: '5px',
    },
    ```
  
**Enabling Sort**
- Open the configuration file located at `bento-frontend/src/bento/dashboardData.js` (in the "CBIIT/bento-frontend" git repo)
- Edit the values in `sortLabels` to enable or disable
  For example:
    ```javascript
  export const sortLabels = {
  sortAlphabetically: 'Sort alphabetically',
  //sortByCount: 'Sort by counts',
  showMore: '...expand to see all selections',
};
    ```

## Configuring Tabs & Tables

The dashboard is structured to organize the data tables using tabs beneath the widgets. The Dashboard Table can be configured to list key data entities in your data sharing platform along with a list of key data entity attributes. In the [Bento reference implementation](https://dev.bento-tools.org/#/cases) the Dashboard Table lists the cases (or study subjects) in the program.


The tabs can be configured as follows:

1. Open `$(src)/bento-frontend/src/bento/dashboardTabData.js` 
2. To change Properties of tab go to `tabs` object:
- **`name`** : Text to show on tab
- **`dataField`**: specifies what data appears in the column, field must be from the GraphQL API query

**NOTE**: the order of the entries in `tabs` should match the order in the `tabsIndex` object. This is the order that the tabs will be displayed left to right on the UI.

To change the style of the tabs go to `tabIndex` object: 

-  **`title`** : Text to shown on tab
-  **`primaryColor`** : background color when tab is selected
-  **`selectedColor`** : font color when tab is selected

**NOTE**: the order of the entries in `tabIndex` should match the order in the `tabs` object. This is the order that the tabs will be displayed left to right on the UI.

The tables displayed in each tab can be configured as follows:

1. Open `$(src)/bento-frontend/src/bento/dashboardTabData.js` 
2. The `tabContainers` object is an array of tables, with each table object having the following fields:

- **`dataField`** : field name in "Data" object to get values for table. 

 **NOTE**: This field should be in the GraphQL API query specified in the `api` field.

- **`defaultSortField`**: Value must be one of the 'dataField' in columns.

- **`defaultSortDirection`**: Sort default column in Ascending or Descending order (value must be `asc` or `desc`)

- **`buttonText`**: Text to appear on Add to cart button

- **`saveButtonDefaultStyle`**: Style of on Add to cart button, with fields such as

          color: '#fff',
          backgroundColor: '#09A175',
          opacity: '1',
          border: '0px',
          cursor: 'pointer',

- **`ActiveSaveButtonDefaultStyle`**: Style of on Add to cart button when it is active mode

- **`DeactiveSaveButtonDefaultStyle`**: Style of on Add to cart button when it is disabled mode

- **`columns`**: a list of column objects. There is a maximum limit of 10 columns. If more than 10 columns are added, Bento will display the first 10 columns without an error or warning message. The top-down order of columns will be displayed left to right on the UI.  Each column object  is described by the following fields:

  * `dataField`: specifies what data appears in the column, field must be from the GraphQL API query

  * `header`: Heading Text for column

  * `sort`: sort order for column

    * must be `asc` or `desc`

  * `primary`: applies to primary field of table like "sample_ID" or "File_ID" based on which files will be added in to cart.

    * must be `true`  or `false`

  * `display`: Show  or Hide column 

    * must be `true`  or `false`

  * `dataFromRoot`: Get data from parent element.

    * must be `true`  or `false`

  * `link`: Hyperlink to internal or external page. The value can be injected in link dynamically using `{datafield}`, for example:

    ```javascript
    // Internal Link 
    link: '/arm/{dataField}',
    
    // External Link
    link: 'https://example.com/{dataField}',
    ```

     ### Internal Links in the Dashboard Table

    1. links starting with `/` are considered as internal links.
    2. Internal links will be opened in the same tab.
    3. Dynamic links can be generated by passing a valid table field to `{}`. For example, `/program/{program_id}` will link to `program/NCT00310180`.

    ### External Links in the Dashboard Table

    1. External links should start with `http://` or `https://`.
    2. External links should show-up with `externalLinkIcon`.
    3. External link will be opened in a new tab.
    4. Dynamic links can be generated by passing a valid table filed to `{}`.
       For example, `https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}` will link to `https://pubmed.ncbi.nlm.nih.gov/29860917/`

  >  :warning: **WARNING**: You can add a maximum of **10** columns to the dashboard tab table. If you add more than 10 columns, Bento will display only the first ten columns, without any warning or error message



### Tool Tips

To change Properties of tool tip for each tab, table go to `tooltipContent` object:

- **`icon`**: The help tip icon that appears next to the 'add button'
- **`alt`**: alt for the tooltip image
- **`0,1,2`**: tooltip content for first tab, second tab and third tab.



### GraphQL Queries

The GraphQL Query used in the Dashboard page is defined in `DASHBOARD_QUERY`. For example:

```javascript
// GraphQL query to retrieve detailed info for a case
export const DASHBOARD_QUERY = gql`{
  numberOfPrograms
  numberOfStudies
  numberOfSubjects
  numberOfSamples
  numberOfLabProcedures
  numberOfFiles
  subjectCountByProgram{
        group
        subjects
      }
...
    fileOverview {
        file_id
        file_name
        association
        file_description
        file_format
        file_size
        program
        arm
        subject_id
        sample_id
        diagnosis
    }
  }`;
```

### Suggested Best Practices

- Dimension of the External Link Icon = 16 X 16 pixels.
- All images should have a resolution >= 72 ppi and should be in the PNG format.



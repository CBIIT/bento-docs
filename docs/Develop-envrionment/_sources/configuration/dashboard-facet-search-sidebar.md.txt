# Dashboard: Facet Search Sidebar

The dashboard facet filters allow an end user to search for data of interest by applying multiple filters, based on faceted classification, of stored data entities.



## Facet Search Filters 

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
  
  

> :warning:   **WARNING**:  For every new facet section, the corresponding styling section should be updated with the same name (see #2 instructions to add styling for facet sections) 
>
> :point_right:   **NOTE**:  Update the GraphQL API Query in  `GET_DASHBOARD_DATA_QUERY` as needed; it should contain all queries and fields that are associated with your filters



## Sidebar Sections Styling

The style of each section of the side bar can be easily configured.

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
  
  

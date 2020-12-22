# Dashboard: Facet Search Sidebar



### **Facet Search Section**

The facet search on the dashboard's side bar can be organized into into sections (or categories), with a maximum count of 15 facets.

To configure the facets:

- Open the configuration file located at `bento-frontend/src/bento/dashboardData.js` (in the "CBIIT/bento-frontend" git repo)

- Edit or create a facets under the `facetSearchData` object
  
- Each facet is defined as follows:
  
  - `label`:	the text that appears for the facet in the sidebar
  
  - `api`:  the type in the GraphQL api query:  `GET_DASHBOARD_DATA_QUERY`  (in same file: `dashboardData.js`)
  
  - `field`:  the field in the above `api`
  
  - `section`:  the section (or category) that the facet should appear in the sidebar 
  
  - `datafield`: the variable name used to pass data in dashboard tab table, as defined in `bento-frontend/src/bento/dashboardTabData.js` (described in [Dashboard: Tabs](dashboard-tabs.md))
  
  - `show`: controls if the facet is displayed or hidden
  
    
  
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
  
  

> :warning:   **NOTE**:   For every new facet section, the corresponding styling section should be updated with the same name (see #2 instructions to add styling for facet sections) 



### **Sidebar Sections Styling**

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
  
  

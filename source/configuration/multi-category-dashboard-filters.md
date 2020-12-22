# Dashboard Facet Search Sidebar

### **Facet Search Section**

- Open the configuration file located at bento-frontend/src/bento/dashboardData.js
- Edit the value for label 'section' under facetSearchData
  
  - For Example - 
  
  
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
  
  Note - For every new facet section, the corresponding styling section should be updated with the same name (see #2 instructions to add styling for facet sections)
  



### **Sidebar Sections styling**

**Color**

- Open the configuration file located at bento-frontend/src/bento/dashboardData.js
- Edit the value for corresponding 'section' under facetSectionStyling
  
  - For Example:
  
  ```javascript
  'Filter By Cases': {
  	 color: '#10A075',
  	 height: '5px',
  },
  ```

**Height**

- Open the configuration file located at bento-frontend/src/bento/dashboardData.js
- Edit the value for corresponding 'section' under facetSectionStyling
  
  - For Example - 
  
  ```javascript
  'Filter By Cases': {
     color: '#10A075',
     height: '5px',
  },
  ```





### **Maximum Number of filters**

- A maximum number of 15 filters are allowed (previous limit is at 12)

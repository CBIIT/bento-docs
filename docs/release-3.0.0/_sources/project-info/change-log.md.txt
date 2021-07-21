# Change Log

## release-3.0.0

**Improvements**

* Enhanced dashboard filters
* Ability to filter within a single category
* Ability to clear all filter search criteria
* Ability to search using mulitple filters
* Table Download behavior is configurable
* System supports direct download of small, document-like files (and the configuration)
* Scroll Bar Global configuration
* New Facet Design
* New design for Dashboard Facet Filter
* Consistent NPM and Node version
* New Facet-Sorting Feature
* New Facet-bubble up Feature
* New Files Back End Microservice for serving Files using CloudFront
* Improved search query for consistent behavior
* Improved high performance filtering queries with GraphQL-Cypher translator
* Updated use of existing assets URL for with new datacommons-assets

**Fixed Issues**

 * Table record selection number would only display section for current page not the entire table
 * Add Associated Files button does not persist clickable state
 * Cart Comment Section writes to wrong cell in manifest file if comment contains a new line or comma
 * The files size in the api is not matching the UI screen
 * In the side bar after I click on sort by count , the refresh button disables
 * FE - Performace Issue - Remove unnecessary Network Calls
 * Clear icon to be moved to the left hand-side for consistency
 * FE- Dashboard table pagination - Incorrect Rows per Page
 * Reset option for single category behaves as global reset for sorting functionality.
 * Download button does not change the cursor
 * Borders to be removed from the left side image on the home page
 * Selected rows can be seen even facet dropdown is closed


## release-2.0.1

* Facet Filter - Updated the facet filter logic to represent updated filters while the user is actively filtering
* Facet Filter - Now the count in brackets of facet represents the respective facet tabs counts (Filter by samples represent samples count, Filter by files represent files count)


## release-2.0.0

* Added multiple tabs on Dashboard
* Added mutliple categories for facet filtering on Dashboard Sidebar
* Changed Cart Workflow to be file-centric
* Added Associated Samples table on Case Detail Page
* Added Associated Files table on Arm Detail Page
* Improved performance with very large datasets


## release-MVP (v1.0.0)
Initial release

# Change Log


## release-3.8.0

* Authentication service supports multiple Identity Providers (IdPs)
* Ability to configure IdPs

## release-3.7.0

**Features**

* Authentication service enabled
* Google supported as an Identity Provider
* Lock icons are displayed if unauthenticated user tries to download files
* Ability to enable or disable authentication
* Advanced facet filters for number ranges added to Explore Dashboard

## release-3.6.0

**Features**

* Elastic Search added to improve performance
    * Support for Global Search of site contents
    * Auto-complete of entered text for Global Search
    * Ability to filter Global Search results and counts
    * Consistent metadata displayed across Global Search categories
    * Magnifying glass for Global Search
    * Global Search results return hyperlinks that redirect to additional details
    * Return of paginated and ordered results from Global Search
* Support for Local Find for case IDs
    * Auto-complete of entered text for Local Find
    * Ability to enter a list to find a set of cases
    * Static query returned from Local Find parameters
    * Ability to view and modify previously loaded case sets
    * Display of both matched and unmatched entered case IDs in a pop-up window
    * Support for uploading a file to find a set of cases
* Dynamic query builds upon selection or removal of faceted filters and Local Find results
* Integration of JBrowse a next-generation genome browser
    * Visualization of bam and vcf files
    * Support for the human genome version hg19
* Increased compliance with the Individuals with Disabilities Education Act (IDEA)
* Mock dataset generator
    * Support for reading ID fields from a config file
    * Compatibility with Docker
* Bento Code Refactoring 

## release-3.2.0

**Features**

* Ability to sort and order additional facet values
* Widget text is configurable
* Text cutoff(...) for widgets on the Explore Dashboard
* Default styling for faceted sections
* Upgraded react-dev-utils from 7.0.5 to 11.0.4

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

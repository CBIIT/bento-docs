---
sort: 10
title: Configuring Faceted Search
---

# Configuring Faceted Search

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## Configuration

### Step A
The filtering categories (i.e. database properties) via which an end-user will be able to filter the data displayed within other elements of the system dashboard based upon the discrete values for each of the filterable properties, such that I can specify up to a total of 10 filtering categories.

   * Edit configuration file
   * Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
   * Under `dashboardTable`, set field `tableTitle` ...

### Step B
The label to be used for each filtering category, such that property names derived from the underlying database can be replaced by more user-friendly and/or intuitive labels.

   * Edit configuration file
   * Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
   * Under `dashboardTable`, under tableData set/add any of the fields field: string // Name of the field in dashboardquery
   * label: string // title to displayed on the table header
   * sort: [asc, dsc] // Defalut sort direction
   * primary: boolean //fetch the data in the remaining columns, and to fetch any downstream files required for the cart workflow
   * display: boolean // option to hide it in view

### Step C
The order in which said filtering categories are to be displayed from top to bottom

   * Edit configuration file
   * Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
   * Under `dashboardTable`, under tableData set/add any of the field `primary: true` to any object keep table sorted by that field ... (Note make sure this should be a case or subject ID's as this will be used for cart data pulling update the cart query if needed)

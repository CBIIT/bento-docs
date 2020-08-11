---
sort: 12
title: Configuring the System Dashboard
---

# Configuring the System Dashboard

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## Configuration

### Step A
Update cases table title

### Edit configuration file 
 1. Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
 2. Under `dashboardTable`, set field `tableTitle` ...

### Step B
The attributes for which data values are to be displayed as columns, such that I can specify columns to be displayed. (Tested by BENTO-369)

#### Edit configuration file
 1. Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
 2. Under `dashboardTable`, under tableData set/add any of the fields field: string // Name of the field in dashboardquery
 * label: string // title to displayed on the table header
 * sort: [asc, dsc] // Defalut sort direction
 * primary: boolean //fetch the data in the remaining columns, and to fetch any downstream files required for the cart workflow
 * display: boolean // option to hide it in view

### Step C
The column from which the data values will be used as the primary key required to fetch the data in the remaining columns, and to fetch any downstream files required for the cart workflow

#### Edit configuration file
 1. Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
 2. Under `dashboardTable`, under tableData set/add any of the field `primary: true` to any object keep table sorted by that field ... (Note make sure this should be a case or subject ID's as this will be used for cart data pulling update the cart query if needed)

### Step D
The order in which said columns are to be displayed from left to right                                                                                                                                                                             

#### Edit configuration file
 1. Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
 2. Under `dashboardTable`, under tableData move object up and down the top one is displayed in left and goes on ...


### Step E
The label to be used as a column header for each column to be displayed, such that property names derived from the underlying database can be replaced by more user-friendly and/or intuitive labels. 

#### Edit configuration file
 1. Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
 2. Under `dashboardTable`, under tableData edit `label` field of any data ...

### Step F
The column containing the data values upon which records shown in the table will be sorted by default, and the order of the sorting imposed by default

#### Edit configuration file
 1. Edit `$(src)/bento-frontend/src/bento/dashboardData.js` with the editor of your choice
 2. Under `dashboardTable`, under tableData set/add any of the field `sort: asc` to any object keep table sorted by that field ...

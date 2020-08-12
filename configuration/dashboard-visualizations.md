---
sort: 9
title: Configuring the Dashboard Visualizations
---

# Configuring the Dashboard Visualizations

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## STEP A
For the sunburst visualization, which will always be displayed by default, the pair of database properties for which counts of discrete values will be profiled.

### Edit configuration file
 * type: "sunburst" // This is the type of the sunburst widget
 * label: string // This is the title of the widget
 * dataName: string // This is the variable name used by the developer this can be any string value
 * datatable_level1_field: string // This is the value of the field from API query of dashboard which is displayed in level 1 of sunburst
 * datatable_level2_field: string // This is the value of the field from API query of the dashboard which is displayed in level 2 of sunburst
 * show: boolean // This is to show or hide the widget

## STEP B
For donut visualizations, the number such visualizations to be displayed in addition to the single sunburst visualization that will be displayed by default, such that I can specify either 2, 3 or 5 donut visualizations be displayed in addition to the sunburst visualization.

## STEP C
For each of the simple donut visualizations to be displayed, the single database property for which counts of discrete values will be profiled.

 * type : "donut" // This is the type of the sunburst widget
 * label: string // This is the title of the widget
 * dataName: string // This is varibale name used by developer this can be any string value
 * datatable_field: string // This is the value of the field from api query of dashboard which to be displayed in donut
 * show: boolean // This is to show or hide the widget

## STEP D
For each of the visualizations to be displayed, regardless of their type, the label to be used such that property names derived from the underlying database can be replaced by more user-friendly and/or intuitive labels

### Edit configuration file
 1. set field `label` to get update the name ...

## STEP E
For each of the visualizations to be displayed, regardless of their type, the order in which they are to be displayed from left to right when a total of 3 visualizations are to be displayed, and from upper left to bottom right when either 4 or 6 visualizations are to be displayed.

### Edit configuration file
 1. The order of the widgets is configured in this manner

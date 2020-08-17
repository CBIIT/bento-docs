---
sort: 5
title: Arm Detail Page
---

# Arm  Detail Page
The arm detail page lists the information for a given arm in a program in the Bento Commons

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

<p>&nbsp;</p>

## Instructions

All configurations can be specified in file: `$(src)/src/bento/armDetailData.js`

### Subsections
* Subsections can be configured in array "subsections", each object in the array represents a subsection.  Order of subsections displayed in the UI is same as the order of corresponding objects in the array. If more than 6 subsections are configured, only first 6 subsections will be displayed in the UI, other subsections will be ignored.
* Subsection Header can be set in property "sectionHeader"
* content order will be the same as order of corresponding objects in the array. If more than 10 properties are configured, only first 10 properties will be displayed in the UI, other properties will be ignored.
* <u>Label text</u> can be set in property "label"
* <u>Value</u> can be set in property "dataField"


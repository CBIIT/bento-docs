---
sort: 5
title: Arm Detail Page
---

# Arm  Detail Page

# Instructions to Configure the Arm Detail page

All configurations can be specified in file: src/bento/armDetailData.js

## Subsections
* Subsections can be configured in array "subsections", each object in the array represents a subsection.  Order of subsections displayed in the UI is same as the order of corresponding objects in the array. If more than 6 subsections are configured, only first 6 subsections will be displayed in the UI, other subsections will be ignored.
* Subsection Header can be set in property "sectionHeader"
* Subsection Text can be set in property "sectionDesc"
* Subsection Content can be set in array property "properties"
* content order will be the same as order of corresponding objects in the array. If more than 10 properties are configured, only first 10 properties will be displayed in the UI, other properties will be ignored.
* <u>Label text</u> can be set in property "label"
* <u>Value</u> can be set in property "dataField"
* <u>Link</u> on <u>Value</u> can be set in property "link"
* <u>Link</u> on <u>Label text</u> can be set in property "labelLink"
* Both internal and external links are supported. External links must start with a valid URL scheme, such as "https://", "ftp://" etc.

## Elements

* **Associated Files Table** can be configured in property "tableConfig"
* If "display" property is set to false, no file table will be displayed
* **Table Title** can be set in property "title"
* **Columns** can be configured in array "columns". If more than 10 columns are configured, only first 10 columns will be displayed, other columns will be ignored. Column order will be the same as the order of corresponding  objects in the array.
* **Column Header** can be set in property "header"
* **Column Content** can be set in property "dataField"
* **Default Sort column** can be set in property "defaultSortField"
* **Default Sort direction** can be set in property "defaultSortDirection" **

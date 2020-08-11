---
layout: default
nav_order: 4
title: Landing Page Stats Bar
---

# Landing Page Stats Bar

## Prerequisites
-Git repo `bento-frontend` is checked out in a directory, represented here as `$(src)`.


## Edit configuration file
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. Under `landingPageData` specify the display label for the statistic in the field `landingPageStatsBar[i]['statTitle']`.
3. Under `landingPageData` specify the GraphQL API query type, that returns the desired statistic, in the field `landingPageStatsBar[i]['statAPI']`.
4. Add the GraphQL API query type to `landingPageQuery`. 
5. For example:

```javascript
export const landingPageData = {
  ...
  landingPageStatsBar: [
  {
  statTitle: '<Display Label for statistic>'
  statAPI: '<GraphQL API query that returns statistic>'
  },
  ...
  ]
...
};

export const landingPageQuery = gql `{
	<GraphQL API query that returns statistic>
}
```

### Notes
1. A maximum of **five** high-level statistics can be displayed in the Landing Page Stats Bar.
2. The list of statistics is displayed from left to right.
3. Font properties cannot be edited in this version of Bento.

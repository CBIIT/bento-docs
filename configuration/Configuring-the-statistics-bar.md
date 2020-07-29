---
layout: default
nav_order: 2
title: How to Configure the Stats Bar for the "Dashboard " workflow
---

# How to Configure the Stats Bar for the "Dashboard " workflow

Instructions to configure the Stats Bar on the dashboard page (right above the widgets)

## Prerequisites

1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)

2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## Edit the configuration file

1. Edit `$(src)/bento-frontend/src/bento/stats.js` with the editor of your choice

2. Under `stats`,

3. set the field `statTitle` to have the desired title for the stat.

4. set the field `datatable_field` to have the respective in the dashboard query (As the stat should be responsive).

5. set the field `type` to have one of the values [field, array, or object] how its returned in the dashboard query.

6. set the field `statAPI` to have its respective field to get initial value from stats query

## Under `globalStatsQuery`
1. Add the respective graphql query field to get the initial value

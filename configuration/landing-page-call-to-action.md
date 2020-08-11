---
layout: default
nav_order: 3
title: Landing Page Call to Action
---

# Landing Page Call to Action 

## Prerequisites
Git repo `bento-frontend` is checked out in a directory, represented here as `$(src)`.

## Edit configuration file
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. Under `landingPageData` specify the “Call to Action” title  in the field `callToActionTitle`.
3. Under `landingPageData` specify the "Call to Action” description in the field `callToActionDescription`.
4. Under `landingPageData` specify the “Call to Action” button label in the field `callToActionButtonText`.
5. Under `landingPageData` specify the “Call to Action” button link in the field `callToActionButtonLink`.
6. For example:

```javascript
export const landingPageData = {
  callToActionTitle: '<Your Tagline Here>',
  callToActionDescription: '<Your Call To Action Description here.>',
  exploreCallToActionButtonText: '<Your Call To Action button label here.>',
  exploreCallToActionLink: '<Your Call To Action button link here.',
...
};
```

### Notes
1. Position of the “Call To Action” title and description on the page cannot be edited.
2. The size, position and color of the Call to Action button cannot be edited.
3. Font properties cannot be edited in this version of Bento.

### Suggested Best Practices
- The “Call To Action” title should be limited to a maximum of 60 characters.
- The “Call to Action” description should be limited to a maximum of 150 characters.

---
sort: 2
title: Landing Page Hero Image
---

# Landing Page Hero Image
The landing page for Bento will typically have a large image or graphic, that we refer to as a "Hero Image" (origin being that the image showed a physician being a hero helping a patient). This document describes how to configure the image used for the Hero Image on the landing page.

## Prerequisites
- Git repo `bento-frontend` is checked out in a directory, represented here as `$(src)`.
- The Landing Page Hero Image file is stored in an open-access repository like Github.

## Edit configuration file
 1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
 2. Under `landingPageData` specify the path to the Landing Page Hero Image in the field `landingPageHero.img`.
 3. Under `landingPageData` specify the ALT tag for the Landing Page Hero Image in the field `landingPageHero.alt`.
 4. For example:

```javascript
export const landingPageData = {
...
	landingPagehero: {
    alt: '<Your Alt Tag>',
    img: '<Path to Your specified Landing Page Hero Image File>',
  },
...
};
```

### Notes
In the current version of Bento, the position of the Hero Image cannot be specified in this version of Bento.

### Suggested Best Practices
- ALT tags should be short (maximum limit =125 characters).
- You may add multiple, comma-separated key words in the ALT tag.
- Suggested specifications for landingPageHero image:
  1. Dimensions: 1200x500 pixels
  2. Resolution: >= 72 ppi
  3. Image Format: PNG

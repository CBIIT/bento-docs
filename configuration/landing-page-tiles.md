---
sort: 5
title: Landing Page Tiles
---

# Landing Page Tiles 

## Prerequisites
-Git repo `bento-frontend` is checked out in a directory, represented here as `$(src)`.
-The tile image file(s) is stored in an open-access repository like Github.

## Edit configuration file
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. Under `landingPageData`, for a tile, `tile_i`:
    a. specify the tile title in the field `tile_i.titleText`.
    b. specify the tile description in the field `tile_i.descriptionText`.
    c. specify the tile image in the field `tile_i.img`.
    d. specify the ALT tag for the tile image in the field `tile_i.alt`.
    e. specify the tile's 'Call to Action' text in the field `tile_i.callToActionText`.
    f. specify the tile's 'Call to Action' link in the field `tile_i.callToActionLink`
3. For example, to edit properties of tile3:
```javascript
export const landingPageData = {
  ...
  tile3: {
    alt: '<ALT tag for tile>',
    img: '<Link to image>',
    titleText: '<Tile title>',
    descriptionText: '<Tile description>',
    callToActionText: '<Tile Link Label>',
    callToActionLink: '<Tile Link>',
  },
  ...
};
```

### Notes
1. Position of tiles on page cannot be edited.
2. Positions of tile components, within a tile, cannot be edited.
3. Font properties cannot be edited in this version of Bento.

### Suggested Best Practices
- The Tile title should be limited to a maximum of 60 characters.
- The Title description should be limited to a maximum of 150 characters.


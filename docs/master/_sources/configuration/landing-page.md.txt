# Landing Page
The Landing Page provides a visual and textual introduction to the overall mission of your data sharing platform, a concise summary of the volume and diversity of stored data and a bird's eye view of what an end user can accomplish at your data sharing platform. A Bento Landing Page has several configurable components. See below for details.
![Landing Page Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/landing-page-elements.png?raw=true)
**Landing Page Elements**. Displayed are the configurable components of a Bento Landing Page. These are: Landing Page Hero Image, Call To Action, Landing Page Tiles, Landing Page Stats Bar. The Call To Action feature consists of a title, a descriptive section and a text button. Each of the four Landing Page Tiles consist of an image, a title, a descriptive section and a text button. 

### Prerequisites

1. The files that specify the configuration parameters of the Bento Landing Page are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for all Landing Page elements can be specified in the file: `$(src)/bento-frontend/blob/master/src/bento/landingData.js` 

3. All images and icons that you use in your Bento instance should be accessible via a public url. 

4. Please review the list of [GraphQL queries](https://github.com/CBIIT/bento-backend/blob/master/src/main/resources/graphql/bento-extended-doc.graphql) to select query type(s) that return your data of interest.

## Landing Page Hero Image
The Landing Page Hero Image is a visual representation of the mission of your data sharing platform.

### Configuring the Landing Page Hero Image
 1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
 2. Under `landingPageData`
 	* Set the field `landingPageHero.img` with the URL to the Landing Page Hero image of your choice.
 	* Set the field `landingPageHero.alt` with the alt text to be associated with the Landing Page Hero image.
 3. Example:
 
 ``` javascript
export const landingPageData = {
  ...
  landingPageHero: {
    alt: '<Your Alt Tag>',
    img: '<URL for your Landing Page Hero Image>',
  },
  ...
  }
```

## Call To Action 
The Call To Action feature provides a concise summary of the all that an end user can accomplish at your data sharing platform.

## Configuring the Call To Action Feature
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. In `landingPageData`:
	* Set the field `callToActionTitle` to the Call To Action Title.
	* Set the field `callToActionDescription` to the Call to Action Descriptive Text.
	* Set the  field `callToActionButtonText` to the label for the Call To Action button.
	* Set the field `callToActionButtonLink` to the link to be embedded in the Call To Action button.
3. Example: 
``` javascript
export const landingPageData = {
  callToActionTitle: '<Your Call To Action Title>',
  callToActionDescription: '<Your Call To Action Descriptive Text>',
  callToActionButtonText: '<Your Call To Action Button Label>',
  callToActionLink: '<Your Call To Action Embedded Link>',
  ...
  }
```

## Landing Page Tiles
The four Landing Page Tiles provide additional visual and textual description of the mission and capabilities of your data sharing platform (see figure above for tile numbering). Note that in this version of Bento, the number, position and dimensions of these tiles cannot be configured. 

### Configuring the Landing Page Tiles
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. Under `landingPageData`, for a tile, `tile<i>`:
  * Set the field `tile_i.titleText` to the Tile Title.
  * Set the field `tile_i.descriptionText` to the Tile Description.
  * Set the field `tile_i.img` to the URL for the tile image.
  * Set the field `tile_i.alt` to the ALT tag for the tile image.
   * Set the field `tile_i.callToActionText` to the Call To Action text.
   * Set the field `tile_i.callToActionLink` to the Call To Action embedded link.
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

## Landing Page Stats Bar
The Landing Page Stats Bar provides the end user with a high level view of the volume and diversity of your stored data, by providing the counts of up to five major data entity types. Bento allows a maximum of **5** statistics. If you add more than 5 statistics, **only the top 5 will be displayed without any warning or error message**.

### Configuring the Landing Page Stats Bar
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. Under `landingPageData` you can add your statistic to landingPageStatsBar.
	* Set the field `statTitle` to the label to be displayed for your statistic.
	* Set the field `statAPI` to the GraphQL API query that returns your statistics of interest.
	* Add the GraphQL query to `GET_LANDING_PAGE_DATA_QUERY`.
3. Example:

``` javascript
export const landingPageData = {
...
  landingPageStatsBar: [
    {
      statTitle: '<Your Statistic Label',
      statAPI: '<Your GraphQL API query>',
    },
    ...
    ]
  }

export const GET_LANDING_PAGE_DATA_QUERY = gql`{
  '<Your GraphQL API query>'
  ...
  }
```


## Suggested Best Practice
- Dimensions of Landing Page Hero image: 1200x500 pixels
- Dimensions of  Tile 1, Tile 2 and Tile 3 images: 293x349 pixels
- Dimensions of Tile 4 image: 600x 436 pixels
- Image resolution >= 72 ppi and image format: PNG
- The “Call To Action” title should be limited to a maximum of 60 characters.
- The “Call to Action” description should be limited to a maximum of 150 characters.
- The Tile title should be limited to a maximum of 60 characters.
- The Title description should be limited to a maximum of 150 characters.
- Alt tags should be short (maximum limit =125 characters). You may add multiple, comma-separated key words in the Alt tag.

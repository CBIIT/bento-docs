---
sort: 2
title: Landing Page 
---

# Landing Page
The Landing Page provides a visual and textual introduction to the overall mission of your data sharing platform, a concise summary of the volume and diversity of stored data and a bird's eye view of what an end user can accomplish at your data sharing platform. A Bento Landing Page has several configurable components. See below for details.
![Landing Page Elements](https://github.com/CBIIT/bento-docs/blob/master/assets/landing_page_elements.png?raw=true)
**Landing Page Elements**. Displayed are the configurable components of a Bento Landing Page. These are: Landing Page Hero Image, Call To Action, Landing Page Tiles, Landing Page Stats Bar. The Call To Action feature consists of a title, a descriptive section and a text button. Each of the four Landing Page Tiles consist of an image, a title, a descriptive section and a text button. 

### Prerequisites

1. The files that specify the configuration parameters of the Bento Landing Page are stored in the GitHub `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`). Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration Parameters for all Landing Page elements can be specified in the file: `$(src)/bento-frontend/blob/master/src/bento/landingData.js` 

## Landing Page Hero Image
The Landing Page Hero Image is a visual representation of the mission of your data sharing platform.

### Configuring the Landing Page Hero Image
 1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
 2. Under `landingPageData` specify the path to the Landing Page Hero Image in the field `landingPageHero.img`.
 3. Under `landingPageData` specify the ALT tag for the Landing Page Hero Image in the field `landingPageHero.alt`.

## Call To Action 
The Call To Action feature provides a concise summary of the all that an end user can accomplish at your data sharing platform.

## Configuring the Call To Action Feature
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. Under `landingPageData` specify the “Call to Action” title  in the field `callToActionTitle`.
3. Under `landingPageData` specify the "Call to Action” description in the field `callToActionDescription`.
4. Under `landingPageData` specify the “Call to Action” button label in the field `callToActionButtonText`.
5. Under `landingPageData` specify the “Call to Action” button link in the field `callToActionButtonLink`.

## Landing Page Stats Bar
The Landing Page Stats Bar provides the end user with a high level view of the volume and diversity of your stored data, by providing the counts of up to five major data entity types.

### Configuring the Landing Page Stats Bar
1. Open the file `$(src)/bento-frontend/blob/master/src/bento/landingData.js`.
2. Under `landingPageData` specify the display label for the statistic in the field `landingPageStatsBar[i]['statTitle']`.
   * Note: Bento allows a maximum of **5** statistics. If you add more than 5 statistics, **only the top 5 will be displayed without any warning or error message**.
3. Under `landingPageData` specify the GraphQL API query type, that returns the desired statistic, in the field `landingPageStatsBar[i]['statAPI']`.
4. Add the GraphQL API query type to `landingPageQuery`. 

## Suggested Best Practice
- Alt tags should be short (maximum limit =125 characters). You may add multiple, comma-separated key words in the Alt tag.
- Suggested specifications for the Landing Page Hero image:
  1. Dimensions: 1200x500 pixels
  2. Resolution: >= 72 ppi
  3. Image Format: PNG
- The “Call To Action” title should be limited to a maximum of 60 characters.
- The “Call to Action” description should be limited to a maximum of 150 characters.

---
sort: 16
title: Shopping Cart Notifications
---

# Shopping Cart Notifications 

## Prerequisites
1. Fork the GitHub repo `https://github.com/CBIIT/bento-frontend` (representing your GitHub username as `YOUR-USERNAME`)
2. Create a local clone of your fork into a local directory, represented here as `$(src)`.

## How to Configure Notification text/message when adding cases to "Shopping Cart/My Cases”

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `cartSelectionMessages`, set the field `selectionsAddedMessage` to have the desired message
3. For example, 

```javascript
export const cartSelectionMessages = {
  selectionsAddedMessage: 'DONE: successfully added to the  list',
  ...
};
```

## How to Configure Notification text/message when adding cases to "Shopping Cart/My Cases”

### Edit configuration file
1. Edit `$(src)/bento-frontend/src/bento/cartWorkflowData.js` with the editor of your choice
2. Under `cartSelectionMessages`, set the field `selectionsRemovedMessage` to have the desired message
3. For example, 

```javascript
export const cartSelectionMessages = {
  ...
  selectionsRemovedMessage: 'DONE: successfully removed from the list',
};
```

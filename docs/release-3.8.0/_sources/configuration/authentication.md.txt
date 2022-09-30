# Authentication
*Service only available for cloud installations of the Bento Framework*
## Introduction
The Bento Framework provides an OIDC-compliant authentication (AuthN) service so that Bento-based platforms have the ability to authenticate users. Authentication can be enabled or disabled. Bento currently supports several identity providers (IdPs) and a single IdP or multiple IdPs can be configured for any given Bento platform. The configured IdPs will appear on the Bento login page and will allow users to select an account type before redirecting to the specific Login page of the selected IdP. The default behavior will redirect any unauthenticated users to the Bento Login page if attempting to access protected pages. Google is the current default IdP.

![Bento Login Page](../assets/login_page.png)

<p>&nbsp;</p>

## Prerequisites
1. The files that specify the configuration parameters for authentication are stored in the GitHub repositories `https://github.com/CBIIT/bento-frontend` and `https://github.com/CBIIT/bento-backend`. Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration parameters for RBAC elements can be specified in the file: `$(src)/bento-backend/src/main/resources/application.properties`

3. Configuration parameters for authentication UI elements can be specified in the file: `$(src)/bento-frontend/src/bento/siteWideConfig.js` and `$(src)/bento-frontend/src/bento/userLoginData.js`.

<p>&nbsp;</p>

### Configuring Authentication 
Authentication can be enabled or disabled for any Bento-based system.
  
  * Acceptable values for auth.enabled are "true" or "false". This value is important for determining Public Access. Refer to Authorization configuration for details.

1. Edit file: `$(src)/bento-backend/src/main/resources/application.properties`
2. Update field: auth.enabled

3. Example: Disable authentication
```javascript
auth.enabled=false
```

5. Edit file: `$(src)/bento-frontend/src/bento/siteWideConfig.js`
6. Set the field `enableAuthentication` to True or False
7. Set the field `authProviders` to google, nih, or loginGov
8. Example: 
```javascript
export default {
  // Suggested for replaceEmptyValueWith: 'N/A' or '-' or ''
  replaceEmptyValueWith: '',
  // Enable authenication
  enableAuthentication: true,
  // List for options for authentication empty array defaults to google
  authProviders: ['google', 'nih', 'loginGov'], // authEndPoint: []
};
```

### Configuring the Display of Identity Providers
The displayed icons and button text for IdPs is configurable.
1. Edit file `$(src)/bento-frontend/src/bento/userLoginData.js`
2. Set the path for the icon field.
3. Enter the text for the loginButtonText field.
4. Example:
```javascript
export const loginProvidersData = {
  google: {
    key: 'google',
    icon: 'https://raw.githubusercontent.com/CBIIT/datacommons-assets/main/bento/images/icons/png/google.png',
    loginButtonText: 'Sign in with Google',
  },
  loginGov: {
    key: 'loginGov',
    icon: 'https://raw.githubusercontent.com/CBIIT/datacommons-assets/main/bento/images/icons/png/login.gov.png',
    loginButtonText: 'Sign in Login.gov',
  },
  nih: {
    key: 'nih',
    icon: 'https://raw.githubusercontent.com/CBIIT/datacommons-assets/main/bento/images/icons/png/nih_itrust.png',
    loginButtonText: 'Sign in NIH iTrust',
  },
};
``` 





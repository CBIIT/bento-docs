# Authentication

*Service only available for cloud installations of the Bento Framework*

## Introduction

The Bento Framework provides an OIDC-compliant authentication (AuthN) service so that Bento-based platforms have the ability to authenticate users. Authentication can be enabled or disabled. Bento currently supports several identity providers (IdPs) and a single IdP or multiple IdPs can be configured for any given Bento platform. The configured IdPs will appear on the Bento login page and will allow users to select an account type before redirecting to the specific Login page of the selected IdP. The default behavior will redirect any unauthenticated users to the Bento Login page if attempting to access protected pages. Google is the current default IdP.

![Bento Login Page](../assets/login_page.png)

<p>&nbsp;</p>

## Prerequisites

1. The files that specify the configuration parameters for authentication are stored in the GitHub repositories `https://github.com/CBIIT/bento-frontend` and `https://github.com/CBIIT/bento-backend`. Create a local clone of your fork into a local directory, represented in these instructions as `$(src)`.

2. Configuration parameters for RBAC elements can be specified in the file: `$(src)/bento-backend/src/main/resources/application.properties`

3. Configuration parameters for authentication UI elements can be specified in the file(s): 
  * `$(src)/packages/bento-frontend/public/injectEnv.js`
  * `$(src)/packages/bento-frontend/src/bento/siteWideConfig.js`
  * `$(src)/packages/bento-frontend/src/bento/loginData.js`.
<p>&nbsp;</p>

### Configuring Authentication

	* Acceptable values for auth.enabled are "true" or "false". This value is important for determining Public Access. Refer to Authorization configuration for details.

	* If value is true, the service will require a user to login before API calls can be made

	* If value is false, the service allows API calls to metadata before login

#### Example

1. Edit file: `$(src)/bento-backend/src/main/resources/application.properties`

2. Update field: auth.enabled

```javascript
auth.enabled=false
```
3. Edit file: `$(src)/packages/bento-frontend/public/injectEnv.js`

4. Set the field `AUTH` to True or False

```javascript
// File: $(src)/packages/bento-frontend/public/injectEnv.js

// Set the field `AUTH` to True or False
window.injectedEnv = {
	AUTH: false,
}
```

5. Edit file: `$(src)/packages/bento-frontend/src/bento/siteWideConfig.js`

6. Set the field `enabledAuthProviders` to google, nih, or loginGov

```javascript
// File: $(src)/packages/bento-frontend/src/bento/siteWideConfig.js

// List of enabled identity providers. This is an array of enabled identity providers, where each element corresponds to a key from loginProvidersData from loginData.js.

export const enabledAuthProviders = ['google', 'nih', 'loginGov'];
```

### Configuring the Display of Identity Providers

The displayed icons and button text for IdPs are configurable

#### Example

1. Edit file `$(src)/packages/bento-frontend/src/bento/loginData.js`

2. Set the path for the icon field.

3. Enter the text for the loginButtonText field.

```javascript
export const loginProvidersData = {
  google: {
    key: 'google',
    icon: 'https://raw.githubusercontent.com/CBIIT/datacommons-assets/main/bento/images/icons/png/google.png',
    loginButtonText: 'Google',
  },
  loginGov: {
    key: 'loginGov',
    icon: 'https://raw.githubusercontent.com/CBIIT/datacommons-assets/main/bento/images/icons/png/login.gov.png',
    loginButtonText: 'Login.gov',
  },
  nih: {
    key: 'nih',
    icon: 'https://raw.githubusercontent.com/CBIIT/datacommons-assets/main/bento/images/icons/png/nih_itrust.png',
    loginButtonText: 'NIH iTrust',
  },
};
```
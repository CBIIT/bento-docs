# README

## Commands
To build the documentation, run the following command in the root directory of this repo:

```
>$ sphinx-multiversion source docs
```

WARNING: Do NOT run `sphinx-build source docs` in the top root directory.·

You do not need to run `make html` in the `source` directory, and do not manually copy `_build/html` to the `docs` directory.

It is recommended to run the `sphinx-multiversion` on the master branch, and then push the master branch to github.


## Publishing Lag
When changes are made and pushed to github, they are NOT going to show up right away at https://cbiit.github.io/bento-docs/ . It may take up to five minutes for changes to appear.

## Troubleshooting

### Test locally
Test any changes locally before pushing to github. Launch a local webserver, and review the changes. You can easily launch a python webserver in the `docs` folder with python one-liner:

```
>$ python -m http.server 8000
```

and then browse to localhost:8000 and review the documentation.

### Regenerating HTML
If there is any confusion about why changes are not appearing, you can delete the top level `docs` folder can be deleted and regenerated automatically when the documentation is built.

Note that if you do this, you will need to manually restore the special `index.html` file that redirects to the `index.html` of the master branch, and create the empty '.nojekyll' file.

## Markdown vs ReStructuredText
Either markdown or restructured text can be used for writing.

## Images
Please place images in the `source/assests/` folder. 

Please use relative paths; do not reference their location using the github base url (don't use: `https://github.com/CBIIT/bento-docs/blob/master/source/assets/Bento-Header-Logo.png`).

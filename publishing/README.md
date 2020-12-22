# README

## Introduction
The documentation uses the python-based sphinx framework. After adding a markdown-formatted file to the repo, it must be compiled (or built) into html for it to appear on the documentation site.



## Python Virtual Environment

Start by setting up a python virtual environment in the root directory (where you have checked out the `bento-docs` directory.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

This virtual environment (venv) is automatically excluded from the git repo (see the `.gitignore` file. 

Now that you have the python virtual environment setup, you can build/compile the html from markdown. 



## Building HTML

To build the documentation, run the following command in the root directory of this repo:

```
>$ sphinx-multiversion source docs
```

WARNING: Do NOT run `sphinx-build source docs` in the top root directory.·

You do not need to run `make html` in the `source` directory, and do not manually copy `_build/html` to the `docs` directory.

It is recommended to run the `sphinx-multiversion` on the master branch, and then push the master branch to github.

> :point_right: **NOTE:** Sphinx will only build/generate html for files that have been commited against a branch 



### Test locally

Test any changes locally before pushing to github. Launch a local webserver, and review the changes. You can easily launch a python webserver in the `docs` folder with python one-liner:

```
>$ python -m http.server 8000
```

and then browse to localhost:8000 and review the documentation.



## Sample Workflow

The overall process of adding content to `bento-docs` will be something like the following:
1. Clone the bento-docs repo (if you haven't already).
2. Fetch, pull the most recent master branch from github (origin) (assuming you are editing the latest documentation). See [Gitflow model](gitflow-model.md) for more info.
3. Edit the page (will be in the `source` directory)
4. If you are adding a new page, put properly formatted markdown file under the `source` directory.
   * Add the new page in `index.rst`, under the appropriate `toctree`. Note that the `index.rst` file uses [RestructuredText](https://docutils.sourceforge.io/rst.html) _not_ [Markdown](https://daringfireball.net/projects/markdown/syntax).
5. Please:
   * Put any images in the `assets` directory
   * Add links to other pages, pointing to the markdown formatted files. If it is in the same directory: `[Page Name](page-name.md)`, otherwise, use ` [Other Page Name](../path/to/page.md)`
   * Try to have a similar style; see [Bento Docs Style Guide](bento-docs-style-guide.md)
   * Use spell checker
6. Add changes to the branch, and commit with an informative message. (Preferring many, small commits over large changes). 
   * ideally, put the JIRA ticket number as the first line in the commit message (e.g. 'BENTO-123 Add instructions to take over world')
7. Build/activate the python virtual environment (see "python virtual environment" above)
8. Build the html changes, from the root directory of the repo (e.g. docroot) (see "Build HTML" above)
   * `>$ sphinx-multiversion source docs`
   * watch for any errors (see [Sphinx Notes](sphinx-notes.md) for examples of errors and successful build logs
9. Preview the generated html in the docs directory 
   * `>$ cd docs`
   * Start the python webserver to preview results (see "Test locally" below); 
   * `>$ python -m http.server 8000`
   * open browser and review changes
   * `http://localhost:8000/`
   * (assuming everything works, the browser will redirect to `http://localhost:8000/master/index.html`)
   * triple check the files you touched; only if the passed, should you continue to step 10
   * check that only the expected branches exist under `doc/` directory, along with the file `index.html`, and `.nojekyll`.  Nothing else should be in this directory.
10. Add the changes and commit to the master branch with a reasonable message
   * ideally, put the JIRA ticket number as the first line in the commit message (e.g. 'BENTO-123 Add instructions to take over world')
   * push the branch to github
   * wait 1 minute and make sure it appears as expected at `https://cbiit.github.io/bento-docs/`



## Also in `publishing/`

[Bento Docs Style Guide](bento-docs-style-guide.md) : A style guide for writing this documentation

 [Template-page](template-page.md) : a sample markdown template, (also see  [Markdown Example](markdown-exam))

[Gitflow model ](gitflow-model.md) :  describes the naming/use of branches to control versions and how to configure branch/versions with whitelists in `source/conf.py`  (see `sphinx-multiversion` and its documentation)

[Extensions](extensions.md) has more information on Sphinx extensions used.  

[Sphinx Notes](sphinx-notes.md) has some sample output/logs from running sphinx





## Troubleshooting



### Publishing Lag

When changes are made and pushed to github, they are NOT going to show up right away at https://cbiit.github.io/bento-docs/ . It may take up to five minutes for changes to appear (but around 1 minute is standard).



### Regenerating `docs/`
Make sure that the files with changes are actually commited to git.

If there is any confusion about why changes are not appearing, you can delete the top level `docs` folder can be deleted and regenerated automatically when the documentation is built.

Note that if you do this, you will need to manually restore the special `index.html` file that redirects to the `index.html` of the master branch, and create the empty `.nojekyll` file.








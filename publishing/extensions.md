# Extensions

## sphinx.ext.githubpages extension
The `sphinx.ext.githubpages` extension creates a `.nojekyll` file on generated HTML directory to publish the document on GitHub Pages.

The generated HTML directory is the top level `docs` directory in this repo.

The `.nojekyll` file is empty - its presence in the generated HTML directory tells GitHub to not use its internal Jekyll Framework to render the files. If the `.nojekyll` file is absent, the html will appear without the proper CSS. 

documentation: https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html


## sphinx-multiversion extension
The `sphinx-multiversion` extension acts as a wrapper around `sphinx-build` command.

This puts each documentation version in its own directory, whereas the `sphinx-build` command would put only the current branch documentation in the top level of `docs/` directory.

`sphinx-multiversion` is a new implementation of `sphinxcontrib-versioning` (see [comment by the author](https://github.com/sphinx-contrib/sphinxcontrib-versioning/pull/78#issuecomment-599193860)). 


### Generated HTML
Note that each `branch/tag` of code should appear under `docs`.  
The only other two things that should be in the branch are an empty file titled `.nojekyll` (which tells github to disable Jekyll framework for this repo)
and a special `index.html` file that redirects to the `index.html` of the master branch.

This is described in `sphinx-multiversion` documentation [github pages](https://github.com/Holzhaus/sphinx-multiversion/blob/master/docs/github_pages.rst)

    > You can easily redirect users that type https://username.github.io/reponame/ into their addressbar to the documentation for any version you like. Just add a :file:`index.html` file to the root directory of your gh-pages branch:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Redirecting to master branch</title>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=./master/index.html">
    <link rel="canonical" href="https://username.github.io/reponame/master/index.html">
  </head>
</html>
```

Also, and example `docs/` layout:
```
docs/
├── .nojekyll
├── index.html
├── master/
└── MVP/
```


## sphinx-rtd-theme extension
The `sphinx-rtd-theme` extension

install with 
```bash
>$ pip install sphinx_rtd_theme
```

and edit `conf.py` file:
```python
import sphinx_rtd_theme

extensions = [
    ...
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"
```

Source: https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html

https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

### Issue
There apparently is an incompatibility issue with sphinx_rtd_theme and sphinx-multiversion.

It can be addressed, as discussed here: https://holzhaus.github.io/sphinx-multiversion/master/templates.html#readthedocs-theme

As of version 0.4.3, the [Read the Docs theme](https://pypi.org/project/sphinx-rtd-theme/) does not support sidebar widgets. So instead of adding a custom template to html_sidebars, you need to create a template file named versions.html with the following content:

```
{%- if current_version %}
<div class="rst-versions" data-toggle="rst-versions" role="note" aria-label="versions">
  <span class="rst-current-version" data-toggle="rst-current-version">
    <span class="fa fa-book"> Other Versions</span>
    v: {{ current_version.name }}
    <span class="fa fa-caret-down"></span>
  </span>
  <div class="rst-other-versions">
    {%- if versions.tags %}
    <dl>
      <dt>Tags</dt>
      {%- for item in versions.tags %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </dl>
    {%- endif %}
    {%- if versions.branches %}
    <dl>
      <dt>Branches</dt>
      {%- for item in versions.branches %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </dl>
    {%- endif %}
  </div>
</div>
{%- endif %}
```

## markdown
Use `recommonmark` to use markdown in sphinx


## markdown tables
Use `sphinx-markdown-tables` to render markdown tables into html. Otherwise, you get a mess.


## markdown support for AutoStructify
This allows you to import parts of other markdown from another file 
(kinda like .
# AutoStructify - for advanced markdown to rst transformations
# Needs to be at the bottom of conf.py
# as described in https://recommonmark.readthedocs.io/en/latest/index.html
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

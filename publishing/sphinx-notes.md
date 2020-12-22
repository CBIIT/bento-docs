# Sphinx Notes

## Errors

Error caused by broken links
```
/var/folders/7x/d920c3ld56n6h2l894fbk9zcznn481/T/tmpf8mm17pn/dd932aebde54e5eab70e277f2d9b66fc060c79b3/source/configuration/dashboard.md:81: WARNING: None:any reference target not found: dashboard-tabs
/var/folders/7x/d920c3ld56n6h2l894fbk9zcznn481/T/tmpf8mm17pn/dd932aebde54e5eab70e277f2d9b66fc060c79b3/source/configuration/dashboard-facet-search-sidebar.md:26: WARNING: None:any reference target not found: dashboard-tabs
```

## build log

Typical successful build log looks like this
```
❯ sphinx-multiversion source docs
Running Sphinx v3.3.1
WARNING: The config value `smv_tag_whitelist' has type `NoneType', defaults to `str'.
loading pickled environment... failed
failed: source directory has changed
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 26 source files that are out of date
updating environment: [new config] 26 added, 0 changed, 0 removed
/Users/bensonml/0_SRC/bento-docs/venv/lib/python3.8/site-packages/recommonmark/parser.py:75: UserWarning: Container node skipped: type=document
  warn("Container node skipped: type={0}".format(mdnode.t))
reading sources... [100%] project-info/meet-the-team
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] project-info/meet-the-team
generating indices... genindex done
writing additional pages... search done
copying images... [100%] assets/Architecture/backend-neo4j-connection.jpg
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 1 warning.

The HTML pages are in ../../../../../../../../Users/bensonml/0_SRC/bento-docs/docs/MVP.
Running Sphinx v3.3.1
WARNING: The config value `smv_tag_whitelist' has type `NoneType', defaults to `str'.
loading pickled environment... failed
failed: source directory has changed
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 29 source files that are out of date
updating environment: [new config] 29 added, 0 changed, 0 removed
/Users/bensonml/0_SRC/bento-docs/venv/lib/python3.8/site-packages/recommonmark/parser.py:75: UserWarning: Container node skipped: type=document
  warn("Container node skipped: type={0}".format(mdnode.t))
reading sources... [100%] project-info/meet-the-team
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] project-info/meet-the-team
generating indices... genindex done
writing additional pages... search done
copying images... [100%] assets/Architecture/backend-neo4j-connection.jpg
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 1 warning.

The HTML pages are in ../../../../../../../../Users/bensonml/0_SRC/bento-docs/docs/master.
```

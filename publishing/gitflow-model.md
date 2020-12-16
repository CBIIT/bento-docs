# Versioning and Git Branching and Tagging

For now, the approach is to use the `master` branch for the current, latest release of Bento documentation, and then create a separate branch for each release (e.g. MVP, etc). This will allow easy maintenance/updating of different versions of documentation. This may change.

Internally, sphinx-multiversion uses the `conf.py` to configure which branches/tags will be used to generate html. 
For more information, please consult the official documentation for sphinx-multiversion: (see "Tags/Branch/Remote whitelists" at https://holzhaus.github.io/sphinx-multiversion/master/configuration.html).

## Suggestions
If you want to commit changes to multiple repos at once, try one of the following approaches

A. Create a new branch, then merge that branch into the other desired branches (e.g. master, MVP, etc).

B. Commit the changes to the master branch, then use `git cherry-pick` to apply those commits to the other desired branches.

Just don't forget to push the changes/commits to github afterward!

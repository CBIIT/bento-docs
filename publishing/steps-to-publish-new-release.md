# Steps to Publish New Release

1. Get the most recent copy of the code and documentation

   1. If not done already, clone the bento docs repository on your machine, and then pull all of the branches that have `release-` prefix.
      1. <u>Note</u>: when rebuilding the documentation, each github branch is treated as a release. If you have extra branches that you do not to be treated as a release, either remove the branch, or use sphinx-multiversion "Tag/Branch/Remote whitelists" (see [documentation here](https://holzhaus.github.io/sphinx-multiversion/master/configuration.html)).  For this reason, it is recommended to not have any extra git branches other than for release versions (branches such as `gitflow` where integrated and then deleted). Additionally, the sphinx-multiversion branches can be configured to use both/either remote and local branches!
   2. Make sure you have an updated master branch
      1. `git pull`

2. Add the new content

   1. Add release notes and other content to master branch.  For this exercise - this content will appear in both the master branch and the new release branch.

      1. Update the release notes in `project-info/change-log.md`.  Add any other additional pages and changes as desired.
      2. Commit these changes to master
      3. <u>Note</u>: if you add new pages, such as adding a page `gitflow.md` under `project-info` directory - then you will also need to update the main documentation file `index.rst` to explicitly list the page, otherwise it will not appear. 
      4. <u>Note</u>: it is recommended that new pages be written in markdown (or github-flavored markdown) and use the `.md` extension. It is not recommended to mix both restructured text (rst) and markdown. While many platforms can parse and handle mixed markup - it can cause issues. If there are issues such as improperly formatted markdown - it will hang/stop the documentation during the building step (having a new line in middle of hyperlink to an image path will stop the build).
      5. Note: it is assumed that reader knows that the `source` folder in the root directory holds the actual documentation to be edited, the `publishing/` folder holds these instructions for generating and publishing the documentation, the `docs/` folder holds the generated html output that will appear on the documentation site.

   2. Create new branch (from the master branch) with release name, and switch to that branch.

      1. Follow pattern of semantic versioning for branch naming : `release-major.minor.patch`.  For example: `release-3.0.0` 

      2. In new branch, update `conf.py` to specify desired version and release.

         1. master branch `conf.py` will have:

         ```
         # -- Project information -----------------------------------------------------
         
         project = 'Bento'
         copyright = '2021, CBIIT'
         author = 'CBIIT'
         version = "latest"
         ```

         1. the new release branch (e.g. `release-3.0.0`) then should have `conf.py` have something like:

         ```
         # -- Project information -----------------------------------------------------
         
         project = 'Bento'
         copyright = '2021, CBIIT'
         author = 'CBIIT'
         release = "release-3.0.0"
         version = "release-3.0.0"
         ```

      3. Commit the changes to branch

      4. Checkout master branch

3. Rebuild the documentation

   1. In the master branch, in the root directory, activate a virtual environment, e.g.  `venv`
      1. if there are any problems, simple remove and rebuild the virtual environment, i.e.:
         1. `python3 -m venv venv`
         2. `source venv/bin/activate`
         3. `pip install -r requirements.txt`
   2. rebuild docs (in root directory)
      1. `sphinx-multiversion source docs`
   3. test the new build
      1. `cd docs/; python3 -m http.server 8000`
      2. open browser, review http://localhost:8000 for correct changes
   4. if everything passes, then commit newly generated output (located in the docs folder) build to master branch.
      1. Make sure to look at all the pages where changes were made.
      2. As needed - repeat the above processes, and re

4. push both master and new release branches to github (origin)

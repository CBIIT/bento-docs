# Understand the Bento-docs folder structure:  
 
1. The `/source` folder in the root directory holds the actual documentation to be edited.
2. The `/publishing` folder holds these instructions for generating and publishing the documentation.
3. The `/docs` folder holds the generated html output that will appear on the documentation site.

# Update and Publish the New Release content
1. For each new bento release, create a develop branch from master. Follow pattern of semantic versioning for branch naming : `develop-major.minor.patch`.  For example: `develop-3.8.0`.

2. If not done already, clone the bento-docs repository on your machine.
    `git clone https://github.com/CBIIT/bento-docs.git bento-docs`

3. Make sure you have an updated master branch.
    `git pull`

4. Switch to the deveop branch.
    1. `git checkout develop-3.8.0`
    2. `git pull`

5. Add new pages and other content as desired in the develop branch. Add the new pages (.md) to their respective folder under the `source/` folder, ex/ configuration, data-and-modeling.

    <b><u>Note</u></b>: It is recommended that new pages be written in markdown (or github-flavored markdown) and use the `.md` extension. It is not recommended to mix both restructured text (rst) and markdown. While many platforms can parse and handle mixed markup - it can cause issues. If there are issues such as improperly formatted markdown - it will hang/stop the documentation during the building step (having a new line in middle of hyperlink to an image path will stop the build).

6. Add the new pages (.md) to the `source/project-info/index.rst` file whcih is the main documentation file to explicitly list the page, otherwise it will not appear.

7. Add the release notes in `source/project-info/change-log.md`.

8. In new branch, update `conf.py` to specify desired version and release.

    1. The master branch `conf.py` will have:

        ```
        # -- Project information -----------------------------------------------------
         
        project = 'Bento'
        copyright = '2021, CBIIT'
        author = 'CBIIT'
        version = "latest"
        ```

    2. The new release branch (e.g. `release-3.8.0`) then should have `conf.py` have something like:

        ```
        # -- Project information -----------------------------------------------------
        
        project = 'Bento'
        copyright = '2021, CBIIT'
        author = 'CBIIT'
        release = "release-3.8.0"
        version = "release-3.8.0"
        ```

9. Commit these changes to your develop-branch, ex/ `develop-3.8.0`.

10. Rename develop branch to release branch.
    1. Rename `develop-3.8.0` to `release-3.8.0`
    2. Push the new release branches to github (origin)
    3. Create a PR to merge `release-3.8.0` to master

        <b><u>Note</u></b>: For this exercise this content will appear in both the master branch and the new release branch.

11. Rebuild the documentation only when it's ready to publish the new release docs (right before the prod deploy).
    1. Checkout master branch and pull all of the branches that have `release-` prefix.
        1. `git checkout develop-3.8.0`
        2. `git pull`

            <b><u>Note</u></b>: When rebuilding the documentation, each github branch is treated as a release. Only the master branch and release branches (prefixed with "release-") will be built to create html output under the docs folder.
            
    *** For the Bento Reference Implementation the steps listed below are completed by an Jenkins job that is triggered by merging a PR to the master branch.

    2. In the master branch, in the root directory, activate a virtual environment, e.g.  `venv`
        1. If there are any problems, simple remove and rebuild the virtual environment, i.e.:
            1. `python3 -m venv venv`
            2. `source venv/bin/activate`
            3. `pip install -r requirements.txt`         
    3. Rebuild the docs (in root directory)
        1. `sphinx-multiversion source docs`
    4. Test the new build
        1. `cd docs/; python3 -m http.server 8000`
        2. Open browser, review http://localhost:8000 for correct changes.

12. If everything passes, then commit newly generated output (located in the docs folder) build to master branch.
    1. Make sure to look at all the pages where changes were made.
        2. As needed - repeat the above processes and rebuild.

*NOTE: For production releases these steps will be automated and built on the master branch of the bento-docs repository.
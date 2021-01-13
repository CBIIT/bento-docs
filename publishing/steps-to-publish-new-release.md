# Steps to Publish New Release



1. update master
   1. `git pull`
2. add release notes to master
   1. update `project-info/change-log.md`
   2. commit changes to master
3. create new branch with release name
   1. Follow pattern of semantic versioning for branch naming : `release-major.minor.patch`
   2. in new branch, update `conf.py` to desired version
   3. commit changes to branch
   4. checkout master branch
4. activate `venv` (in root directory)
   1. if there are any problems, simple remove and rebuild the virtual environment
      1. `python3 -m venv venv`
      2. `source venv/bin/activate`
      3. `pip install -r requirements.txt`
5. rebuild docs (in root directory)
   1. `sphinx-multiversion source docs`
6. test new build 
   1. `cd docs/; python3 -m http.server 8000`
   2. open browser, review 'localhost:8000' for correct changes
7. if everything passes
   1. commit new build to master branch
   2. push to github (origin)
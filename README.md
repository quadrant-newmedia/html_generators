# APP_NAME

This is a "seed" project for creating a reusable django app.
It aids with packaging the project for pypi, pushing to GitHub, and automating tests using tox.

For a more advanced setup, see https://www.b-list.org/weblog/2018/apr/02/testing-django/

For the python documentation on packagin, see https://packaging.python.org/tutorials/packaging-projects/

## How To Use:
- clone this repo, then delete the origin remote
- do a search and replace on this project, replacing APP_NAME with the actual name of your app
- rename the src/APP_NAME directory
- create venv, activate
- run: pip install -r requirements.txt
- run: tox (verify that the tests are working)
- verify setup.py

When you are ready to build and push to pypi/remote repo (after running tests):
- update version number
- update RELEASE_NOTES.md
- commit everything to git
- run build_and_push

## About django/dummy_project

This project contains a simple dummy django project, with complete settings. These files are not packed with distribution. They enable you run django's dev server, if needed, while developing.

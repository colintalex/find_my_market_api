# Find My Market

Welcome to Find My Market! This repo is the backend that our app uses to store it's users and their favorites.

### Running Locally

To run this api you need to have python installed on your local machine. [MacOS](https://docs.python-guide.org/starting/install3/osx/) [Windows](https://docs.python.org/3/using/windows.html)

Fork and clone.

CD into the local directory and run `source ./env/bin/activate` to start up a local python environment.

Run `pip install fastapi` and `pip install uvicorn` to install fastapi

Run `pip install -r requirements.txt` and `pip install -r dev-requirements.txt` to install the API dependencies.

This API uses a postgresql database so you'll need to create two: `market_api` and `market_api_test`

Next run `alembic upgrade head` to run all the migrations. **Note:** You may need to set your `PYTHONPATH` variable if you get the error `module app not found`. This can be done by running the command `export PYTHONPATH="$PYTHONPATH:/path/to/where/the/folder/is/located"` and then you can run `alembic upgrade head`

The API should be set up now and you can our test suite by using the command `bash test.sh`

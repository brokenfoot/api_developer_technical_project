# Requirements
- Built with python 3.6.6
- Python packages: falcon, pandas, and gunicorn

# Install
To install and run in a virtual environment:
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn app:app
```

# Querying the API
I made a few assumptions in the queries:
- If not *all* of the weights by name are passed, then no error is thrown. I'm assuming the client can query those weights that are important to *them*.
- This also means that if a parameter is skipped, then that parameter is not added to the city's overall score (in line with the assumption that it's not important to the client)
- I added an optional `limit` to the `rank` query, with a default value of `all`. The assumption is that the client may want data on all of the cities, but they can limit the results to just the top 5, 10, etc results.
- The `city/city_id` endpoint assumes that the id passed is an `integer`. If it isn't, then you get a `404 Not Found` response. However, if they query correctly with an id that does not match the database, then it throws an error.
- Added a `city/all` endpoint, that just returns the raw data for all the cities. This could be done through the `/rank` endpoint, but for the sake of simple user experience, I added this endpoint as well.
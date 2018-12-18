import falcon
import json
import pandas as pd


class City(object):
    def on_get(self, req, resp, city_id):
        data_file = open('data/cities.json')
        data = json.loads(data_file.read())
        resp.body = None
        for city in data:
            if city['id'] == city_id:
                resp.body = json.dumps(city)
                return

        if resp.body is None:
            raise falcon.HTTPError(
                "400 Bad Request",
                title = "City ID Error",
                description = "No city with id `{}` found".format(city_id)
            )


class AllCities(object):
    def on_get(self, req, resp):
        data_file = open('data/cities.json')
        resp.body = data_file.read()


class Ranking(object):
    def on_post(self, req, resp):
        json_body = json.loads(req.bounded_stream.read())
        try:
            weights = json_body['weights']
        except Exception as e:
            print(e)
            raise falcon.HTTPError(
                "400 Bad Request",
                title = "Weights Error",
                description = "Malformed request. Check out the documentation for how to make a request for this data.",
                href = "https://github.com/brokenfoot/api_developer_technical_project/blob/master/doc/endpoints.md"
            )

        limit = json_body['limit'] if 'limit' in json_body else "all"
        try:
            if limit != "all":
                limit = int(limit)
        except ValueError:
            raise falcon.HTTPError(
                "400 Bad Request",
                title = "Limit Error",
                description = "`limit` must be a number, not a string."
            )

        data_file = open('data/cities.json')
        data = json.loads(data_file.read())
        city_weightings = []
        for city in data:
            city['overall_score'] = 0
            for weight_name, weight_value in weights.items():
                try:
                    city['overall_score'] += city['scores'][weight_name] * float(weight_value)
                except KeyError:
                    raise falcon.HTTPError(
                        "400 Bad Request",
                        title = "Weights Error",
                        description = "Invalid weight parameter `{}` passed".format(weight_name)
                    )
                except ValueError:
                    raise falcon.HTTPError(
                        "400 Bad Request",
                        title = "Weights Error",
                        description = "`{}` value must be a number, not a string.".format(weight_name)
                    )

            city_weightings.append(city)

        df = pd.DataFrame(city_weightings)
        df.sort_values(by = 'overall_score', inplace = True, ascending = False)
        if limit != "all":
            df = df.head(limit)

        resp.body = json.dumps({
            "data": df.to_dict(orient = 'records'),
            "totalRows": len(df)
        })


app = falcon.API()

app.add_route('/city/{city_id:int}', City())
app.add_route('/city/all', AllCities())
app.add_route('/rank', Ranking())

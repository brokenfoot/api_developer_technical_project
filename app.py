import falcon
import json
import pandas as pd


class City(object):
    def on_get(self, req, resp, city_id):
        city_id = int(city_id)
        data_file = open('data/cities.json')
        data = json.loads(data_file.read())
        resp.body = None
        for city in data:
            if city['id'] == city_id:
                resp.body = json.dumps(city)

        if resp.body is None:
            raise falcon.HTTPError(
                "400 Bad Request",
                title = "City ID Error",
                description = "No city with id `{}` found".format(city_id)
            )


class Ranking(object):
    def on_post(self, req, resp):
        weights = req.get_param('weights')
        try:
            weights = json.loads(req.bounded_stream.read())['weights']
        except Exception as e:
            print(e)
            raise falcon.HTTPError(
                "400 Bad Request",
                title = "Weights Error",
                description = "Malformed request. Check out the documentation for how to make a request for this data.",
                href = "https://github.com/brokenfoot/api_developer_technical_project/blob/master/doc/endpoints.md"
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

        resp.body = json.dumps(df.to_dict(orient = 'records'))


app = falcon.API()

app.add_route('/city/{city_id}', City())
app.add_route('/rank', Ranking())

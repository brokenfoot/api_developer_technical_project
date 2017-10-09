# Endpoints

Errors are handled by returning an appropriate status code (e.g. 400) and with a JSON object like this one:

```
{
	"errors": [
		"No city with id '999'"
	]
}
```


## Get city `GET /city/:cityid`

Return all information about the requested city.  Example:

```
GET /city/1

{
	"name": "Chicago, IL",
	"id": 1,
	"scores": {
		"walkability": 1.7,
		"job_growth": 2.32,
		"green_space": 0.9,
		"taxes": 0.6
	}
}
```

Error cases should be thought through and handled as described at the beginning of this document.

## Get ranked list of cities using weighting `POST /rank`

Returns a ranked list of all cities, ordered descending by an overall score calculated using the client-supplied weighting.  This endpoint must take a JSON object as the body of the POST request, example:

```
POST /rank
{
	"weights": {
		"walkability": 1.0,
		"job_growth": 1.0
		"green_space": 2.5,
		"taxes": 0.5
	}
}

[
	{
		"name": "Seattle, WA",
		"id": 2,
		"scores": {
			"walkability": 1.3,
			"job_growth": 3.1,
			"green_space": 1.2,
			"taxes": 0.8
		},
		"overall_score": 7.8
	},
	{
		"name": "New York, NY",
		"id": 6,
		"scores": {
			"walkability": 1.5,
			"job_growth": 1.8,
			"green_space": 1.4,
			"taxes": 0.7
		},
		"overall_score": 7.15
	},
	{
		"name": "Chicago, IL",
		"id": 1,
		"scores": {
			"walkability": 1.7,
			"job_growth": 2.32,
			"green_space": 0.9,
			"taxes": 0.6
		},
		"overall_score": 6.57
	},
	
	...
]
```

Error cases should be thought through and handled as described at the beginning of this document.

# Emsi Developer Technical Project

## Introduction
This is the Emsi API Developer technical exercise.  Emsi's goal is to observe how you think about problems and write code.  Rather than limiting you to whiteboarding or writing code live, we want to simulate actual working conditions as closely as possible: you are welcome to use whatever technology stack you feel most comfortable with, to search Google and StackOverflow, and to generally approach the problem however you like.

Once you've finished your implementation (which we don't expect to take more than eight hours), be sure to push it to GitHub and send us a link to the repository.  The team at Emsi will review your code, then conduct a call with you to discuss it.  Please include a file in the project root called `INSTALL.md` which describes whatever steps we need to take to run your code and verify that it works.

## Project Story
In this hypothetical scenario, Emsi is working major corporation who are looking at relocating their headquarters to more favorable cities.  Each customer is different, but a data research team has identified a few key metrics and scored major U.S. metros by them.  These metrics include things like overall economic growth indicators such as job growth as well as quality of life indicators such as "walkability."  A frontend team is building out a web application which will be used directly by executives at client organizations to explore good options based on which metrics they value most highly.  Your job is to build out the API to support the frontend application.

There are two general "flows":
1) The customer wants to see how a particular city scores on all metrics.
2) The customer wants to weight each available metric and see a ranked list of cities.  For instance, they care very deeply about walkability and weight it as `4`, while job growth is left at a weight of `1`.  A city's overall score is determined by multiplying the metric value by the metric weight, then adding all metrics together.  So if Chicago has a walkability score of `1.7` and a jobs-growth score of `2.32`, in this scenario it's overall score would be `1.7 x 4 + 2.32 x 1 = 9.12`.

A description of these endpoints is in `doc/endpoints.md`.  Data is in `data/cities.json`; consider this a sample and design as if there are at least 300 cities in the full data set.  If you choose to put the data into a database of some sort, make sure you script it so that we can replicate it.

## Requirements
1) Write an API service that implements the endpoints described in `doc/endpoints.md`.
2) If some aspect of the spec is ambiguous, use your best judgement and document what decision you made and why.
3) Sample requests and responses are supplied in `doc/endpoints.md`.  You do _not_ need to match the pretty-printing style, field order, etc.
4) Anything you want to do to impress us, e.g. CI script, Dockerfile, Terraform plan for AWS, etc.
5) Write a file named `INSTALL.md` which describes the steps we need to take to run your code, preferably something that works on a recent Linux kernel.
6) Push everything up to a repository on GitHub, then send us a link.

## Review
__Remember to include a text file named `INSTALL.md`__ which clearly describes how we can go about running your code, preferably on a recent Linux kernel.

Here are the questions the team at Emsi will ask itself after reviewing your code:
* Does the code run and work as expected?
* Is the implementation well thought out?
* Is the code documented effectively?  Can we understand it within a few minutes?
* In what ways has your implementation exceeded our expectations?

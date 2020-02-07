# MdM Count

Counts the occurrences of query strings in a corpus of strings.

## Build

In the root directory of this repository, run: `docker build . -t mdm_test`

## Run

1. Run `docker run -p 5000:5000 mdm_test:latest`
2. A web server will starts and listen on port 5000.

To run and change the corpus:
`docker run -p 5000:5000 --env CORPUS=foo,lorem,ipsum mdm_test:latest`

## Use

1. In a web browser go to: `http://127.0.0.1:5000`
2. Click on `default`, `GET /occurrences` then `Try it out`. 
3. Add a value in `q` field then click `Execute`.
4. The response will be displayed.

Alternatively, in a browser go directly to: `http:127.0.0.1:5000/occurrences?q=foo,bar`

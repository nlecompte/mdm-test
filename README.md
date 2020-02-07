# countcli

Counts the occurrences of query strings in a corpus of strings.


## With Docker

### Build

In the root directory of this repository, run `docker build . -t mdm_test`

### Run

1. Run `docker run -t mdm_test ab,abc` where `ab,abc` is your query strings.
2. The result is displayed in the console, with the example: `{'ab': 2, 'abc': 0}`

To run and change the corpus:
`docker run --env CORPUS=foo,lorem,ipsum -t mdm_test foo,bar`

## Locally

Prerequisites:  Python 3.7

### Install

In the root directory of this repository, run `pip3 install .`

### Run

1. Set the environment variable `CORPUS` with the set of strings to look into. 
   For example in bash: `export CORPUS=ab,ab,abc`
2. Run the councli: `countcli ab,abc,bc` where `ab,abc,bc` are the query strings to count.
3. The result is displayed in the console, with the example: `{'ab': 2, 'abc': 1, 'bc': 0}`
 
### Uninstall
 
 Run `pip3 uninstall countcli`
 
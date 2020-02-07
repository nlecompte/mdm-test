# countcli

Counts the occurrences of query strings in corpus of strings.

## Prerequisites

- Python 3.7

## Install

In the root directory of this repository, run `pip3 install .`

## Usage

1. Set the environment variable `CORPUS` with the set of strings to look into. 
   For example in bash: `export CORPUS=ab,ab,abc`
2. Run the councli: `countcli ab,abc,bc` where `ab,abc,bc` are the query strings to count.
3. The result is displayed in the console, with the example: `{'ab': 2, 'abc': 1, 'bc': 0}`
 
 ## Uninstall
 
 Run `pip3 uninstall countcli`
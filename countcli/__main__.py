import argparse
import os

from .counter import Counter


def get_queries():
    parser = argparse.ArgumentParser()
    parser.add_argument("queries",
                        help="count occurrences of each query string in the list",
                        metavar="QUERY_1,QUERY_2")
    args = parser.parse_args()
    return args.queries.split(',')


def get_corpus():
    corpus_str = os.environ.get('CORPUS')
    if isinstance(corpus_str, str):
        return corpus_str.split(',')
    else:
        raise EnvironmentError("Environment variable CORPUS is required. Supported format is 'abc,ab'")


def display(content):
    print(content)


def main():
    queries = get_queries()
    corpus = get_corpus()

    counter = Counter(corpus)
    counts = counter.count(queries)

    display(counts)


if __name__ == "__main__":
    main()

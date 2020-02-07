import os

from flask import Flask
from flask import request
from flask_restx import Api, Resource

from counter import Counter

app = Flask(__name__)
api = Api(app,
          version='1.0.0',
          title='MdM Count API')


def get_queries(req):
    queries_str = req.args.get('q')
    if queries_str is None:
        api.abort(400, "Parameter 'q' is required")
    else:
        return queries_str.split(',')


def get_corpus():
    corpus_str = os.environ.get('CORPUS')
    if isinstance(corpus_str, str):
        return corpus_str.split(',')
    else:
        raise EnvironmentError("Environment variable CORPUS is required. Supported format is 'abc,ab'")


@api.route('/occurrences')
class Occurrences(Resource):
    @api.doc('Return occurrences of each query string.')
    @api.param('q', 'Comma-separated list of strings to count')
    def get(self):
        queries = get_queries(request)
        corpus = get_corpus()

        counter = Counter(corpus)
        return counter.count(queries)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

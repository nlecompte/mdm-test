class Counter:

    def __init__(self, corpus):
        self._corpus = corpus

    def count(self, queries):
        occurrences = dict.fromkeys(queries, 0)

        for string in self._corpus:
            counter = occurrences.get(string, None)
            if counter is not None:
                counter += 1
                occurrences[string] = counter

        return occurrences

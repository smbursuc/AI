from rdflib import Graph
graph = Graph()
graph.parse('food.rdf')


graph.serialize("output.nt", format="n3", encoding="utf-8")

import pprint
for stmt in graph:
    pprint.pprint(stmt)

# v = graph.serialize(format='xml')
# print(v)


from nltk.corpus import wordnet as wn
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
print(wn.synsets('dog'))
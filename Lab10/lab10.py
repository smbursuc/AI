from rdflib import Graph
graph = Graph()
graph.parse('food.rdf')


# graph.serialize("output.nt", format="n3", encoding="utf-8")

import pprint
for stmt in graph:
    pprint.pprint(stmt)

# v = graph.serialize(format='xml')
# print(v)


from nltk.corpus import wordnet as wn
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
# print(wn.synsets('dog'))

import random

triples = []

for s, p, o in graph:
    if len(s.split('#')) > 1 and len(o.split('#')) > 1 and len(p.split('#')) > 1:
        s = s.split('#')[1]
        o = o.split('#')[1]
        p = p.split('#')[1]
        if (p != 'type'):
            triples.append((s, p, o))

for triple in triples:
    print(triple)


def find_all_answers(attribute1,attribute2,answer_index):
    answers = []
    if attribute2 == None:
        for triple in triples:
            if attribute1 in triple:
                answers.append(triple[answer_index])
    else:
        for triple in triples:
            if attribute1 in triple and attribute2 in triple:
                answers.append(triple[answer_index])
    return answers


def play(use_synonym):
    stop = False
    while not stop:

        concept = random.choice(triples)
        question_index = random.choice([1, 2, 3])
        print(concept)

        questions = {1:{"q":0,"a":2}, 2:{"q":[0,2],"a":1}, 3:{"q":2,"a":0}}


        i = questions[question_index]["q"]

        synonyms = []
        answer_i = questions[question_index]["a"]
        if use_synonym:
            for syn in wn.synsets(concept[answer_i]):
                for l in syn.lemmas():
                    synonyms.append(l.name())
            print(synonyms)
        
        synonym = None
        if len(synonyms)>0:
            synonym = synonyms[0]
        
        use_synonym_in_question = random.choice([False,True])

        if question_index == 1:
            if use_synonym_in_question == False:
                print(f"Cine este in relatie cu {concept[i]}?")
            elif synonym is not None:
                print(f"Cine este in relatie cu {synonym}?")
        elif question_index == 2:
            print(f"Care este relatia dintre {concept[i[0]]} si {concept[i[1]]}?")
        else:
            if use_synonym_in_question == False:
                print(f"Cine este in relatie cu {concept[i]}?")
            elif synonym is not None:
                print(f"Cine este in relatie cu {synonym}?")

        


        if question_index == 2:
            answers = find_all_answers(concept[questions[question_index]["q"][0]],concept[questions[question_index]["q"][1]],questions[question_index]["a"])
        else:
            answers = find_all_answers(concept[questions[question_index]["q"]],None,questions[question_index]["a"])
        print(answers)
        
        synonyms = []
        answer_i = questions[question_index]["a"]
        if use_synonym:
            for syn in wn.synsets(concept[answer_i]):
                for l in syn.lemmas():
                    synonyms.append(l.name())
            print(synonyms)

        answer = input()

        if answer == 'exit':
            stop = True
            continue



        if not use_synonym:
            if answer in answers:
                print("corect")
            else:
                print("gresit")
        else:
            if answer in answers or answer in synonyms:
                print("corect")
            else:
                print("gresit")

play(False)

word = input("wordnet word: ")
print(wn.synsets(word))

play(True)


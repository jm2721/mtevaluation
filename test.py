from nltk.corpus import wordnet as wn


def getSynonyms(word):
    try:
        synonyms = []
        for s in wn.synsets(word):
            synonyms.append(s.name().split('.')[0])
        return set(synonyms)
    except UnicodeDecodeError:
        return set(word)

print getSynonyms('in')
if 'in' in getSynonyms('in'):
    print True

# Functions, methods, modules, packages

from pprint import pprint
# from countries_list import countries

# countries_with_land = []
# for country in countries:
#     if 'land' in country:
#         countries_with_land.append(country)

# print(countries_with_land)

# find_most_commost_english_words() find the most english word in any text and returns list dictionary with word key and its count

txt = 'I love Python. If you do not love Python what else can you love. Please show some love to Python.'

txt = """A list of 100 words that occur most frequently in written English is given below, based on an analysis of the Oxford English Corpus (a collection of texts in the English language, comprising over 2 billion words).[1] A part of speech is provided for most of the words, but part-of-speech categories vary between analyses, and not all possibilities are listed. For example, "I" may be a pronoun or a Roman numeral; "to" may be a preposition or an infinitive marker; "time" may be a noun or a verb. Also, a single spelling can represent more than one root word. For example, "singer" may be a form of either "sing" or "singe". Different corpora may treat such difference differently.

The number of distinct senses that are listed in Wiktionary is shown in the Polysemy column. For example, "out" can refer to an escape, a removal from play in baseball, or any of 36 other concepts. On average, each word in the list has 15.38 senses. The sense count does not include the use of terms in phrasal verbs such as "eat out" (chastise) and other multiword expressions such as the interjection "get out!", where the word "out" does not have an individual meaning.[6] As an example, "out" occurs in at least 560 phrasal verbs[7] and appears in nearly 1700 multiword expressions.[1]

The table also includes frequencies from other corpora, note that as well as usage differences, lemmatisation may differ from corpus to corpus - for example splitting the prepositional use of "to" from the use as a particle. Also the COCA list includes dispersion as well as frequency to calculate rank."""

def find_most_common_words(txt, n = 10):
    word_dct = {}
    words = txt.lower().split(' ')
    for word in words:
        if word.endswith('.') or word.endswith('?') or word.endswith('!'):
            word = word[0:-1]
        if word in word_dct:
            word_dct[word] = word_dct[word] + 1
        else:
            word_dct[word] = 1
    sorted_list = sorted(
        word_dct.items(), key=lambda x: x[1], reverse=True)[0:n]
    return sorted_list
    # return { k:v for k,v in sorted_list }
print(find_most_common_words(txt, 30))






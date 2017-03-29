# @Author: DivineEnder
# @Date:   2017-03-29 14:47:11
# @Email:  danuta@u.rochester.edu
# @Last modified by:   DivineEnder
# @Last modified time: 2017-03-29 15:13:55 

import Utils.settings as settings
settings.init()

import math
from nltk import word_tokenize
from wordcloud import STOPWORDS
import Utils.connection_utils as glc

def tokenize_article(article):
	stopwords = set(STOPWORDS).add("said")
	tokens = word_tokenize(article["content"])
	for stop_word in stopwords:
		tokens.remove(stop_word)

	return tokens

def build_class_dict(articles):
	total_words = 0

	class_dict = {}
	for article in articles:
		tokens = tokenize_article(article)
		for token in tokens:
			if token in class_dict.keys():
				class_dict[token] = class_dict[token] + 1
			else:
				class_dict[token] = 1
		total_words = total_words + len(tokens)

	for key, value in class_dict:
		class_dict[key] = -1 * math.log(float(class_dict[key]) / float(total_words))

	return class_dict

def classify_article(dictionaries, article):
	#comment below when testing with test_classify_article
	article_tokens = tokenize_article(article)
	#uncomment below when testing with test_classify_article
	#tokens = article.split(" ")
	sums = {}
	for d in dictionaries.keys():
		sums[d] = 0

	for each_token in tokens:
		for dictionary_name, dictionary_values in zip(dictionaries.keys(),dictionaries.values()):
			if dictionary_values.get(each_token) != None:
				sums[dictionary_name] = sums[dictionary_name] + dictionary_values[each_token]

	return min(sums, key=sums.get)
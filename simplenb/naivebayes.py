import numpy as np
import os

class NaiveBayes:
    def __init__(self):
        self.word_list = {}
        self.category_list = {}
        self.stop_word = []

    # adding word to the list
    def incr_word(self, word, category):

        # don't add word that is length less than two, lazy attemp to remove junk from classfication
        if len(word) < 2:
            return;

        # don't add word in the stop_word list that wouldn't of help in classfication
        if word in self.stop_word:
            return;

        #
        # this part
        # add total_word count, word appear in category count into word_list
        # and add total word add in each category
        #

        if word in self.word_list:
            self.word_list[word]["total_word"] += 1

            try:
                self.word_list[word]["category"][category] += 1
            except:
                self.word_list[word]["category"][category] = 1
        else:
            self.word_list[word] = {"total_word": 1, "category": {category: 1}}

        if category in self.category_list:
            self.category_list[category] += 1
        else:
            self.category_list[category] = 1

    def train(self, category, words):
        for word in words.split():
            self.incr_word(word, category)

    def get_wordcount_incat(self, word, category):
        try:
            return self.word_list[word]["category"][category]
        except:
            return 0.0

    def get_wordcount(self, word):
        try:
            return self.word_list[word]["total_word"]
        except:
            return 0.0

    def classify(self, text):
        best_prop = None
        markas = "undefine"
        total_trainingword = float(sum(self.category_list.values())) # total word count in word_list

        for cl in self.category_list:
            cat_total = float(self.category_list.get(cl)) # total number of word in this category
            cat_prop =  cat_total / float(total_trainingword) # probability of being in this category

            sumword_prop = 0.0 # summation of word probability
            for w in text.split():
                word_c = float(self.get_wordcount(w)) # total word count for particular word
                word_incat = self.get_wordcount_incat(w, cl) # total word count for word in particular category

                if word_incat > 0:
                    prob = np.log((word_incat / word_c) / cat_prop)
                    sumword_prop += prob

            result = np.log(cat_prop) + sumword_prop
            if result > best_prop:
                best_prop = result
                markas = cl

        return markas

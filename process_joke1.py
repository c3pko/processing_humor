import collections

import json
import nltk
from nltk.parse import ViterbiParser
from nltk.corpus import treebank
from itertools import islice
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
import collections
from nltk.tokenize import sent_tokenize, word_tokenize

 
#http://www.anc.org/data/masc/corpus/browse-masc-data/
#http://vknight.org/unpeudemath/code/2015/08/28/natural-language-processing-of-new-jokes-from-2015.html
#http://vknight.org/unpeudemath/code/2015/06/14/natural-language-and-predicting-funny.html
#http://drvinceknight.blogspot.co.uk/2013/08/a-very-brief-and-shallow-analysis-of.html

#use cky/chart parser to check for ambiguity of individual words and in transitions
#https://github.com/drvinceknight/EdinburghFringeJokes/blob/master/nlp-of-jokes-2015.ipynb


def main():


    #f = open('sample_joke1.txt')
    f = []
    f = "What do you want people to say about you at your funeral? Look! He’s moving!"
    count = 0
    word_and_token = {}
    f = f.split()
    word_and_token = {}
    for word in f:
        token = word_tokenize(word)
        #print(token)
       
        word_and_token[count] = [word,nltk.pos_tag(token)]
        count+=1
           # word_and_token[word].append(nltk.pos_tag(token))
    ##for line in f:
        #line = line.strip("\n")
        #line = line.strip('",.!?"')
        ##line = line.split("\n")
 
    print(word_and_token)     
    #print(line.split())
    #text = word_tokenize(f)
    #print(nltk.pos_tag(text))
    


main()

    


                
      









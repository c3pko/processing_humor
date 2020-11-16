import nltk
from nltk.corpus import wordnet

def main():
    #t = "Did you hear about the guy whose whole left side was cut off? He’s all right now"
    t = "Should I have a baby after 35? No, 35 children is enough."
    t = t.split()
    to_test = []
    score_test = {}
    #print(t)
    for i in t:
        #a = "'"
        #b = i
        #c = ".n.01'"
        #x = a+b+c
        #print(x)
        pos_possib = wordnet.synsets(i)
        print(pos_possib)
        if len(pos_possib)==0:
            continue
            print("na")
        if len(pos_possib)>0:

            pos = pos_possib[0]
            to_test.append(pos)
            #print(pos)
        else:
            pos = wordnet.synsets(i)
            to_test.append(pos)
            #print(pos)
    print(to_test)
    """
    count=0
    for i in to_test:
        element = i
        copy_list = to_test
        for j in copy_list:
            print(j)
            score = i.path_similarity(j)
            print(score)
            score_test[count] = [i,j, score]
            count=count+1
        #print(count)
        
    print(score_test)    
"""
    
main()
        

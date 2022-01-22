
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
from heapq import nlargest


#for opening the file making a function name read_article
def read_article(file_name):
    file = open(file_name,encoding="utf8")          #open the file
    filedata = file.readlines()          #read the data
    
    article = filedata[0].split(".")        #spliting the data into sentences with ". "
    sentences = [] 
                        #making array to store the sentences
    for sectence in article:                 #Loop for saving article ing array sentences
        sentences.append(sectence.replace("[^a-zA-Z]"," ").split(" "))          #creating a regex ( regular expression) and replacing them in place of sentence and then appending them in Sentence which store the sentenece in form of List
    sentences.pop() 
                        #Popup the sentence
    return sentences                        #returning the List


#Making a func which calculate the similarity between 2 sentence
# Here Stopword are the word like : - and ,The ,or 
def sentence_similarity(sent1,sent2,stopwords=None):
    if stopwords is None:                   # if stopword is empty
        stopwords=[]
                                # making an empty array taht contain stopwords
    sent1 = [w.lower() for w in sent1]        # converting all words into lower case in sentence1
    sent2 = [w.lower() for w in sent2]  
        # converting all words in lower case in sentene 2
    all_words = list(set(sent1+sent2))      #to get unique word we are using set which contain sent1+ sent2

    vector1 = [0] *len(all_words)             #Making two vector to calculate cosine function
    vector2 = [0] *len(all_words)
    for w in sent1:                         # loop for counting uniqe word except stop words
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1 
              #adding count in vector

    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1-cosine_distance(vector1,vector2)       # calculating cosine_distance between vectoe1 & vector2

#creating a function which can return similar 2Dmatrix which help us in genrating summary
def gen_sim_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences),len(sentences)))       #creating 2D matrix which initially contain zeros of size len(sentences)*len(sentences)
    
    for idx1 in range(len(sentences)):              #Loop for filling the value in matrix
        for idx2 in range(len(sentences)):
            if idx1 == idx2:            #if both are same then continue
                continue
            similarity_matrix[idx1][idx2]= sentence_similarity(sentences[idx1],sentences[idx2],stop_words) #filling the value using sentence_similarity func

    return similarity_matrix
    

# creating func which generate summary
def generate_summary(file_name ,top_n=5):
    stop_words = stopwords.words('english')
    summarize_text =[]
    sentences = read_article(file_name)
    sentence_similarity_matrix = gen_sim_matrix(sentences,stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)),reverse =True)

    select_length = int(len(ranked_sentences) * (int(30) / 100))

    # Using nlargest library to get the top x% weighted sentences.
    summary = nlargest(select_length, scores, key=scores.get)

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentences[i][1]))
    print("Summary \n",". ".join(summarize_text))


generate_summary("op2.txt", 2)

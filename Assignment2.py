#Problem 1 
import re
pattern = re.compile(r'\(d{3}\) \d{3}-\d{4} | \d{3}-\d{3}-\d{4}')
test_text = "Contact us at (123) 456-7890 or 987-654-3210. Also, try (555) 123-4567."
phone_number = re.findall(pattern,test_text)
print(phone_number)

#Problem 2 
import spacy 
nlp = spacy.load('en_core_web_sm')
text = "SpaCy is a powerful NLP library for tokenization status (is space)."
doc = nlp(text)
for token in doc :
     print(f"{token.text}---> {token.is_space}")
     
     
#Problem 3 
# There are two ways of doing it with a slight difference 
#1. With user data (Advantage is can use the doc object and its stored information elsewhere in your code, making it reusable.)

import spacy
from spacy.language import Language
nlp = spacy.load("en_core_web_sm")
@Language.component("token_counter")#Language is accessible 
def token_counter(doc):
    doc.user_data["token_count"] = len(doc)
    return doc

nlp.add_pipe("token_counter", last=True)
sentence = "Customizing a SpaCy pipeline can be very useful."
doc = nlp(sentence)
print(f"Token count: {doc.user_data['token_count']}")

 #2.without user data 

import spacy
nlp = spacy.load("en_core_web_sm")
def token_counter(doc):
    print(f"Token count: {len(doc)}")
    return 


nlp.add_pipe("token_counter", last=True)
sentence = "Customizing a SpaCy pipeline can be very useful."
doc = nlp(sentence)
token_counter(doc)

#Problem 4 
def pos_names(doc):
    for token in doc:
       print(token,"--->",token.pos_,"--->",spacy.explain(token.pos_))
    return 

sentence = "NLP is fascinating, and SpaCy makes it even more interesting."
doc = nlp(sentence)
pos_names(doc)

#Problem 5
def ner_names(doc):
    for ent in doc.ents:
        print(ent.text,"--->", ent.label_,"---->" , spacy.explain(ent.label_))
    return 
text = "Elon Musk, the CEO of Tesla, was born on June 28, 1971, in Pretoria, South Africa."
doc = nlp(text)
ner_names(doc)
from spacy import displacy
displacy.render(doc,style="ent")

#Problem 6
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np

corpus = ["Data science is amazing", "Machine learning is part of data science"]

ohe = OneHotEncoder(sparse_output=False)
words = [word for sentence in corpus for word in sentence.split()]
unique_words = np.array(list(set(words))).reshape(-1, 1)#set - removes duplicacy 

one_hot_encoded =ohe.fit_transform(unique_words)

print("One Hot Encoding:")
print(one_hot_encoded)
print("-"*50)

cv = CountVectorizer()
bow =cv.fit_transform(corpus).toarray()
print("Bag of Words:")
print(bow)
print("-"*50)

tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(corpus).toarray()
print("TF-IDF:")
print(tfidf)







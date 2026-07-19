import numpy as np
import pandas as pd 
import ast
import nltk
import sklearn
import pickle


movies=pd.read_csv("tmdb_5000_movies.csv")
credits=pd.read_csv("tmdb_5000_credits.csv")

movies=movies.merge(credits,on="title")
print(movies.head(3))


movies=movies[["movie_id","title","overview","genres","keywords","cast","crew"]]


# movies.head(3)

print(movies["genres"][0])

print(movies["keywords"][0])

print(movies.isnull().sum())

movies.dropna(inplace=True)

print(movies.isnull().sum())

print(movies.duplicated().sum())

def convert(obj):
    import ast
    lst=[]
    for i in ast.literal_eval(obj):
        lst.append(i["name"])
    return lst
movies["genres"]=movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)

print(movies["genres"][1:10])

print(movies["keywords"][1:10])

print(movies["keywords"][1])

def top_3_heros(obj):
    lst=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter != 3:
            lst.append(i["name"])
            counter+=1
        else:
            break
    return lst
movies["cast"]=movies["cast"].apply(top_3_heros)

print(movies["cast"][1:10])

def director_crew(obj):
    lst=[]
    for i in ast.literal_eval(obj):
        if i["job"]=="Director":
            lst.append(i["name"])
            break
    return lst
movies["crew"]=movies["crew"].apply(director_crew)

print(movies["cast"][1:10])

movies["overview"]=movies["overview"].apply(lambda x: x.split())

print(movies["overview"][0])

movies["tags"]= movies["cast"]  +  movies["crew"] + movies["genres"]  +  movies["keywords"] + movies["overview"]  

print(movies["tags"][1])



movies["tags"]=movies["tags"].apply(lambda x:[i.replace(" ","") for i in x])

print(movies["tags"][0])

movies["tags"]=movies["tags"].apply(lambda x: " ".join(x))

movies["tags"]=movies["tags"].apply(lambda x: x.lower())

print(movies["tags"][0])

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
def stem(obj):
    lst=[]
    for i in obj.split():
        
        lst.append(ps.stem(i))
    return " ".join(lst)


movies["tags"]=movies["tags"].apply(stem)

print(movies["tags"][0])



print(movies.head(2))

nw_movies = movies[["movie_id","title","tags"]]
print(nw_movies.head(2))

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words="english")
vectors=cv.fit_transform(nw_movies["tags"]).toarray()


print(vectors[0])

from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors)

print(similarity.shape)



import pickle
pickle.dump(nw_movies.to_dict(),open("movies.pkl","wb"))


top_similarity = {}

for index in range(len(similarity)):

    distances = similarity[index]

    top_movies = sorted(
        enumerate(distances),
        reverse=True,
        key=lambda x: x[1]
    )[1:201]   


    top_similarity[index] = top_movies


pickle.dump(
    top_similarity,
    open("top_similarity.pkl","wb")
)
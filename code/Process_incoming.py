import json 
import pandas as pd
import numpy as np 
import os 
import joblib
import requests
from sklearn.metrics.pairwise import cosine_similarity

def create_embedding(texts):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":texts
    })
    if r.status_code!=200:
        print("Api Error:")
    
    response=r.json()["embeddings"]
    return response


def inferances(prompt):
    r=requests.post("http://localhost:11434/api/generate",json={
        "model":"gemma3",
        "prompt":prompt,
        "stream":False
    })

    response=r.json()
    return response


df=joblib.load("embedding.joblib")

incoming_query=input("Ask The Question-->")
question_embedding=create_embedding([incoming_query])[0]


similarity=cosine_similarity(np.vstack(df["embedding"]),[question_embedding]).flatten()
# print(similarity)

top_result=3
max_index=np.argsort(similarity)[::-1][0:top_result]
# print(max_index)

new_df=df.loc[max_index]


prompt=f"""
=====================================================================
You are a helpful AI assistant trained only on Data Science notes.
=======================================================================
Answer the question using the context below.
=======================================================================
Context:
{new_df[["id","text"]].to_json(orient="records")}
=======================================================================
Question:                                                               
{incoming_query}
=======================================================================
Answer:
"""

with open("prompt.txt","w",encoding="utf-8") as f:
    f.write(prompt)
response=inferances(prompt)["response"]
print(response)

with open("response.txt","w",encoding="utf-8") as file:
    file.write(response)

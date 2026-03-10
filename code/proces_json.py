import json 
import os 
import pandas as pd
import numpy as np
import requests
import joblib

def create_embedding(texts):
    r=requests.post("http://localhost:11434/api/embed",
                    json={
                        "model":"bge-m3",
                        "input":texts
                    })
    
    if r.status_code!=200:
        print("Embedding Error")

    response=r.json()["embeddings"]
    return response

#print(create_embedding("Cat set on the mat"))

chunk_id=0
my_list=[]

load_json=os.listdir("new_json")
# print(load_json)

for file_json in load_json:
    with open(f"new_json/{file_json}","r",encoding="utf-8",errors="ignore") as f:
        content=json.load(f)
    

        if "chunks" not in content:
            print(f"Skip The->{content}")
            continue

        embeddings=create_embedding([c["text"] for c in content["chunks"]])

        for i,chunk in enumerate(content["chunks"]):
            chunk["chunk_id"]=chunk_id
            chunk["embedding"]=embeddings[i]
            chunk_id+=1
            my_list.append(chunk)
            

df=pd.DataFrame.from_records(my_list)
print(f"check The Data frame Len:{len(my_list)}")

embedding_joblib=joblib.dump(df,"embedding.joblib")
print(f"{embedding_joblib} successfully Run:")

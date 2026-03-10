import json 
import os 
import math

n=20

for filename in os.listdir("json"):
    if filename.endswith(".json"):
        file_path=os.path.join("json",filename)
    
        with open(file_path,"r",encoding="utf-8") as f:
            load_data=json.load(f)
            print(load_data)

        new_chunks=[]
        num_chunk=len(load_data)
        num_group=math.ceil(num_chunk / n)

        for i in range(num_group):
            start_index=i*n
            end_index=min((i+1)*n, num_chunk)
            chunk_group=load_data[start_index:end_index]
            new_chunks.append({
                "id":chunk_group[0]["id"],
                "text":"".join([c["text"] for c in chunk_group])
            })
        
        #Save The .json
        os.makedirs("new_json",exist_ok=True)
        with open(os.path.join("new_json","PDF.json"),"w",encoding="utf-8") as f:
            save_data=json.dump({"chunks":new_chunks},f,ensure_ascii=False,indent=4)
print(f"Successfully Run Your Code:{save_data}")

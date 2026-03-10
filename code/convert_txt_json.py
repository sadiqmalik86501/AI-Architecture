import json 
# Text File Read Kro 
with open("PDF.txt","r",encoding="utf-8") as f:
    text=f.readlines()
    print(text)

data=[]

for i,line in enumerate(text):
    if line.strip():
        data.append({
            "id":i+1,
            "text":line.strip()
        })

with open("PDF_1.json","w",encoding="utf-8") as f:
    save_data=json.dump(data,f,indent=4,ensure_ascii=False)

print(f"txt convert to structured json successfully;")

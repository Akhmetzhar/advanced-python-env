import json
with open("students.json","r") as f:
    data=json.load(f)

for s in data:
    s["average"]=sum(s["grades"])/len(s["grades"])

with open("students_updated.json","w") as f:
    json.dump(data,f)

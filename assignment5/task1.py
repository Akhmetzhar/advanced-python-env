import string

with open("text.txt","r",encoding="utf-8") as f:
    lines=f.readlines()

text=" ".join(lines).lower()
for c in string.punctuation:
    text=text.replace(c,"")

words=text.split()
freq={}

for w in words:
    freq[w]=freq.get(w,0)+1

with open("analysis.txt","w",encoding="utf-8") as f:
    f.write(str(len(lines))+"\n")
    f.write(str(len(words))+"\n")
    for k,v in freq.items():
        f.write(k+" "+str(v)+"\n")

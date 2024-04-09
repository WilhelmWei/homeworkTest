import spacy
nlp = spacy.load('zh_core_web_sm')
from spacy import displacy

def read_file(file_path):
    with open(file_path,'r',encoding = 'utf-8') as f:
        return f.read()

text = read_file('report.txt')
if text != 0:
    print("text loaded")
else:
    print("error")

#print(text)
doc = nlp(text)
print(doc)
displacy.render(doc,style='ent',jupyter = True)
# for token in doc:
#     print(token text,token)
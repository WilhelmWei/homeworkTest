# import spacy
# nlp = spacy.load('zh_core_web_sm')
# from spacy import displacy
#
#
# def read_file(file_path):
#     with open(file_path,'r',encoding = 'utf-8') as f:
#         return f.read()
#
# text = read_file('report.txt')
# if text != 0:
#     print("text loaded")
# else:
#     print("error")
#
# #print(text)
# doc = nlp(text)
# #print(doc)
# displacy.render(doc,style='ent',jupyter = True)
# # for token in doc:
# #     print(token text,token)
# import fasttext
# model = fasttext.train_supervised(input="cooking.train")
# model.predict("Which baking dish is best to bake a banana bread ?")
# model.predict("Why not put knives in the dishwasher?")
# model.test("cooking.valid")
# model = fasttext.train_supervised(input="cooking.train")
# model.test("cooking.valid")
# model = fasttext.train_supervised(input="cooking.train", epoch=25)
# model.test("cooking.valid")
# model = fasttext.train_supervised(input="cooking.train", lr=1.0, epoch=25)
# model.test("cooking.valid")
# model = fasttext.train_supervised(input="cooking.train", lr=1.0, epoch=25, wordNgrams=2)
# model.test("cooking.valid")
# model = fasttext.train_supervised(input="cooking.train", lr=1.0, epoch=25, wordNgrams=2, loss='hs')
# model.test("cooking.valid")
# model = fasttext.train_supervised(input='cooking.train', autotuneValidationFile='cooking.valid', autotuneDuration=600)
# model = fasttext.train_supervised(input="cooking.train", lr=0.2, epoch=25, wordNgrams=2, loss='ova')
# model.predict("Which baking dish is best to bake a banana bread ?", k=-1, threshold=0.5)
# model.save_model("./model_cooking.bin")
# model = fasttext.load_model("./model_cooking.bin")
# model.predict("Which baking dish is best to bake a banana bread ?", k=-1, threshold=0.5)
import fasttext

model = fasttext.train_supervised('cooking.train')
res = model.predict("which baking dish is best to bake a banana bread ?")
print(res)
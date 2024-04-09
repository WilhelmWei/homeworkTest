import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet

# 为了确保资源被正确下载，我们将下载代码放入try-except块中。
# 这样，如果资源已经被下载，就不会显示任何错误。
try:
    nltk.data.find('corpora/brown')
except LookupError:
    nltk.download('brown')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# 打印Brown语料库的类别
print("Categories in the Brown corpus:")
print(brown.categories())

# 获取Brown语料库中的所有词并统计词频
brown_words = [word.lower() for sent in brown.sents() for word in sent if word.isalpha()]
brown_freq = FreqDist(brown_words)

# 这里，我们对词进行了小写转换，并移除了非字母字符，使统计更准确。

# 打印最常出现的10个词
print("\nMost frequent 10 words in Brown corpus:")
for word, freq in brown_freq.most_common(10):
    print(f"{word}: {freq}")

# 处理句子
sentence = "Hello pal, how are you today? I hope everything is nice to see you."
tokens = word_tokenize(sentence)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words and word.isalpha()]

# 这里的改动是：对输入句子进行了小写转换，并移除了非字母字符。
# 同时也注意到，您原始的变量名'sents'可能会导致混淆，因为它实际上是一个句子，所以我们更改为'sentence'。

# 打印处理后的句子
print("\nFiltered tokens (excluding stopwords):")
print(filtered_tokens)

# 找到“great”的反义词
print("\nAntonyms of 'great':")
for syn in wordnet.synsets("great"):
    for lemma in syn.lemmas():
        antonyms = lemma.antonyms()
        if antonyms:
            for antonym in antonyms:
                print(f"{antonym.name()}")

            # 注意：在打印反义词时，我们没有添加任何特定的条件或筛选，
# 所以它可能会输出多个与'great'相关的反义词。
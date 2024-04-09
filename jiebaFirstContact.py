from collections import Counter

import jieba
import matplotlib.pyplot as plt
import numpy as np

#from wordcloud import WordCloud

# 读取报告文件内容
with open('report.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用jieba进行分词
seg_list = jieba.cut(content, cut_all=False)
words = list(seg_list)

# 读取停词文件，构建停词集合
with open('cn_stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(file.read().strip().split('\n'))

# 过滤停词
filtered_words = [word for word in words if word not in stopwords]

# 统计词频
word_counts = Counter(filtered_words)

# 获取频数最高的N个词
top_words = word_counts.most_common(100)

# 确定画布大小和词的布局
fig, ax = plt.subplots(figsize=(12, 12))
ax.axis('off')  # 关闭坐标轴

# 初始化字体大小和位置
font_size_min = 10
font_size_max = 100
num_words = len(top_words)
positions = np.random.rand(num_words, 2)
font_sizes = np.linspace(font_size_min, font_size_max, num_words)

# 计算缩放因子
scale = (font_sizes.max() - font_sizes.min()) / (font_size_max - font_size_min)
sizes = [int(size * scale + font_size_min) for size in font_sizes]

# 设置Matplotlib的字体配置
plt.rcParams['font.sans-serif'] = ['Microsoft yahei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 绘制词云
colors = [plt.cm.viridis(i) for i in np.linspace(0, 1, num_words)]  # 使用渐变色
for i, (word, count) in enumerate(top_words):
    ax.text(positions[i, 0], positions[i, 1],
            word,
            size=sizes[i],
            va='center',
            ha='center',
            backgroundcolor="white",
            color=colors[i],
            alpha=0.8,  # 设置透明度
            rotation=np.random.randint(-15, 15)  # 随机旋转角度
            )

# 设置背景色
ax.set_facecolor('#f0f0f0')  # 设置背景为浅灰色

# 添加标题
plt.title('词云图', fontsize=20, pad=20)
# #生成词云对象
# wordcloud = WordCloud(font_path='simhei.ttf',  # 指定支持中文的字体路径
#                       background_color='white',  # 设置背景颜色
#                       width=1000, height=800,  # 设置画布大小
#                       min_font_size=10,  # 设置最小字体大小
#                       max_font_size=200,  # 设置最大字体大小
#                       margin=2  # 设置词语间距
#                       ).generate_from_frequencies(word_counts)
#
# #显示词云图
# plt.figure(figsize=(12, 10))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')  # 关闭坐标轴
# 显示图像
plt.show()


# # 读取报告文件内容
# with open('report.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#
# # 使用jieba进行分词
# seg_list = jieba.cut(content, cut_all=False)
# words = list(seg_list)
#
# # 读取停词文件，构建停词集合
# with open('cn_stopwords.txt', 'r', encoding='utf-8') as file:
#     stopwords = set(file.read().strip().split('\n'))
#
# # 过滤停词
# filtered_words = [word for word in words if word not in stopwords]
#
# # 统计词频
# word_counts = Counter(filtered_words)
#
# # 生成词云对象
# wordcloud = WordCloud(font_path='simhei.ttf',  # 指定支持中文的字体路径
#                       background_color='white',  # 设置背景颜色
#                       width=1000, height=800,  # 设置画布大小
#                       min_font_size=10,  # 设置最小字体大小
#                       max_font_size=200,  # 设置最大字体大小
#                       margin=2  # 设置词语间距
#                       ).generate_from_frequencies(word_counts)
#
# # 显示词云图
# plt.figure(figsize=(12, 10))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')  # 关闭坐标轴
# plt.show()
#### in this solution, i have the problem that ValueError: anchor not supported for multiline text

# 绘制柱状图
words, counts = zip(*top_words)
plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Frequent Words')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

from collections import Counter
import jieba
import matplotlib.pyplot as plt

# 读取报告文件内容
with open('report.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用jieba进行分词
seg_list = jieba.cut(content, cut_all=False)
words = [word for word in seg_list if len(word) > 1]  # 只保留长度大于1的词

# 读取停用词文件，构建停用词集合
with open('cn_stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])

# 过滤停用词
filtered_words = [word for word in words if word not in stopwords]

# 统计词频
word_counts = Counter(filtered_words)

# 获取频数最高的N个词
top_words = word_counts.most_common(100)

# 设置画布大小和图的属性
plt.figure(figsize=(12, 12))

# 绘制散点图表示的词频可视化
for i, (word, count) in enumerate(top_words):
    plt.text(0.5, 0.5 - i * 0.05, word, ha='center', va='center', size=count * 0.01)

plt.title('词频散点图', fontsize=20, pad=20)
plt.axis('off')  # 关闭坐标轴
plt.show()

# 绘制柱状图显示最高频的词汇
plt.figure(figsize=(10, 8))
words, counts = zip(*top_words[:10])  # 只取前10个最高频词汇
plt.barh(words, counts, color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top 10 Most Frequent Words')
plt.show()

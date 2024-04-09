def CYK(words, grammar):
    n = len(words)
    table = [[set() for _ in range(n + 1)] for _ in range(n + 1)]

    # 将每个单词添加到二维矩阵的对角线上
    for i, word in enumerate(words):
        for rule in grammar:
            if len(rule[1]) == 1 and rule[1][0] == word:
                table[i + 1][i + 1].add(rule[0])

    for length in range(2, n + 1):
        for start in range(0, n - length + 1):
            end = start + length
            for split in range(1, length):
                for B in table[start + split][end - 1]:
                    for rule in grammar:
                        if len(rule[1]) == 2 and rule[1][1] == B:
                            A = rule[0]
                            C = rule[1][0]
                            if C in table[start + 1][start + split]:
                                table[start + 1][end].add(A)

                                # 检查起始符号是否在表格的第一个单元格到最后一个单元格的路径上
    return 'S' in table[1][n]


if __name__ == '__main__':
    # grammar = [
    #     ('S', ['NP', 'VP']),
    #     ('NP', ['Det', 'N']),
    #     ('VP', ['V', 'NP']),
    #     ('Det', ['a']),
    #     ('N', ['man']),
    #     ('V', ['saw'])
    # ]
    grammar = [
        ('S', ['NP', 'VP']),
        ('NP', ['Det', 'N']),
        ('VP', ['V', 'NP']),
        ('Det', ['a']),
        ('N', ['man']),
        ('V', ['saw'])
    ]

    # 需要添加的额外规则，以便句子可以正确解析
    grammar.extend([
        ('NP', ['a', 'N'])  # 添加这条规则来处理像 'a man' 这样的名词短语
    ])

    sentence = 'a man saw a man'.split()
    #sentence = 'a man saw'.split()
    res = CYK(sentence, grammar)
    print(res)  # 应该输出 True，表示句子是语法正确的
#
#     句法树构建过程（模拟）
#
#     S
#     └─ NP(我)
#     └─ VP
#     ├─ V(吃)
#     │   └─ NP(火锅)
#     └─ ADJ(喜欢)
#     └─ ADV(非常)
#
# （注意：上面的树结构并不完全符合之前给出的CFG规则和移进 - 归约过程，它只是为了展示如何用文本模拟树结构。下面是更准确的步骤模拟。）
#
# 步骤模拟（使用缩进表示层次）：
#
# 1.
# 移进
# "我"
# 堆栈: [我]
#
# 2.
# 移进
# "非常"
# 堆栈: [我, 非常]
#
# 3.
# 移进
# "喜欢"，归约
# NP → '非常'
# ADJ(这里有个问题，因为按照之前的CFG，应该是
# ADJ → '喜欢'，所以我们先归约这个)
# 堆栈: [我, NP(非常喜欢)]
#
# （注意：这里的归约并不符合之前给出的CFG，实际上在移进
# "喜欢"
# 之前应该先归约
# ADJ → '喜欢'。
# 但为了与之前的描述保持一致，我们在这里做了一个错误的归约，实际上应该分两步走。）
#
# 4.
# 移进
# "吃"，归约
# V → '吃'
# 堆栈: [我, NP(非常喜欢), V(吃)]
#
# 5.
# 移进
# "火锅"，归约
# NP → '火锅'
# 堆栈: [我, NP(非常喜欢), V(吃), NP(火锅)]
#
# 6.
# 归约
# VP → V
# NP
# 堆栈: [我, NP(非常喜欢), VP(吃火锅)]
#
# 7.
# 归约
# S → NP
# VP
# 堆栈: [S(我非常喜欢吃火锅)]
#
# （完成）
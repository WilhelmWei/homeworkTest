def CYK(words, grammar):
    n = len(words)
    table = [[set() for _ in range(n + 1)] for _ in range(n + 1)]

    # 将每个单词添加到二维矩阵的对角线上
    for i, word in enumerate(words):
        for rule in grammar:
            if rule[1] == [word]:
                table[i + 1][i + 1].add(rule[0])

    for length in range(2, n + 1):
        for start in range(0, n - length + 1):
            end = start + length
            for mid in range(start + 1, end):
                for rule in grammar:
                    if len(rule[1]) == 2:
                        B, C = rule[1]
                        if B in table[start + 1][mid] and C in table[mid][end]:
                            table[start + 1][end].add(rule[0])

    # 检查起始符号是否在表格的最后一个单元格中
    return 'S' in table[1][n + 1]

if __name__ == '__main__':
    grammar = [
        ('S', ['NP', 'VP']),
        ('NP', ['Det', 'N']),
        ('VP', ['V', 'NP']),
        ('Det', ['a']),
        ('N', ['man']),
        ('V', ['saw'])
    ]
    sentence = 'a man saw a man'.split()
    res = CYK(sentence, grammar)
    print(res)  # 应该输出 True，表示句子是语法正确的
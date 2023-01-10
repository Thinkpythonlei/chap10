import bisect


def make_word_list():
    """从文件中读取行并使用append构建列表。
       返回:字符串列表
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """使用二分搜索检查单词是否在列表中。
       前提条件:对列表中的单词进行排序
       Word_list:字符串列表词
       如果单词在列表中则返回:True;否则返回False
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):
    """使用二分搜索检查单词是否在列表中。
       前提条件:对列表中的单词进行排序
       Word_list:字符串列表词:字符串
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))
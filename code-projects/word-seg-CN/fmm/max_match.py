# -*- coding: UTF-8 -*-.
from trie_tree import TrieTree
import codecs


def build_trie_tree(dict_path):
    fin = codecs.open(dict_path, 'r', 'utf-8')
    file_info = fin.readline().strip().split('\t')
    max_count = int(file_info[1])
    tree = TrieTree()
    [tree.add(x.strip()) for x in fin]
    return tree, max_count


def forward_max_match(finPath, tree, maxCount):
    fin = codecs.open(finPath, 'r', 'utf-8')
    result = []
    for line in fin:
        head = 0
        tmp = []
        while head != (len(line) - 1):
            searchLen = maxCount
            while tree.search(line[head:head + searchLen]) == False and searchLen != 1:  # 从最大长度递减匹配
                searchLen -= 1
            subStr = line[head:head + searchLen]
            tmp.append(subStr)
            head += searchLen
        result.append(tmp)
    return result


def save_partition_result(result):
    ###保存分词结果###
    fout = codecs.open('../res/result1.txt', 'w', 'utf-8')
    for line in result:
        for word in line:
            fout.write(word + ' ')
        fout.write('\n')
    fout.close()


def save_PRF_result(myResultFilePath, rightResultFilePath):
    my_result = codecs.open(myResultFilePath, 'r', 'utf-8')
    right_result = codecs.open(rightResultFilePath, 'r', 'utf-8')
    f1 = my_result.readlines()
    f2 = right_result.readlines()
    right_count = 0

    for i in range(len(f1)):  # 读一行数据
        line1 = f1[i].strip().split(' ');head1 = 0
        line2 = f2[i].strip().split(' ');head2 = 0
        len_of_line = sum([len(x) for x in line1])  # 一行数据中汉字总数

        while head1 < len_of_line and head2 < len_of_line: # head1指针指向line1， head2指针指向line2
            j = 0;k = 0
            while j < len(line1) and k < len(line2):  # 读每一行中的词
                head1 += len(line1[j])
                head2 += len(line2[k])

                if head1 == head2:
                    right_count += 1

                while head1 < head2 or head1 > head2:  # 如果两个指针指的开头不同，修正指针
                    if head1 < head2:
                        j += 1
                        head1 += len(line1[j])
                    elif head1 > head2:
                        k += 1
                        head2 += len(line2[k])
                j += 1; k += 1

    my_result.seek(0);right_result.seek(0)  # 重置文件指针到开头，读取文本词数
    recognized_count = len(my_result.read().strip().split(' '))
    test_set_count = len(right_result.read().strip().split(' '))

    precision = right_count / float(recognized_count)
    recall = right_count / float(test_set_count)
    F = precision * recall * 2 / (precision + recall)

    result2_out = codecs.open('../res/result2.txt', 'w', 'utf-8')
    result2_out.write("统计正确词数 = %d 识别的词数 = %d 测试集的词数 = %d\n" % (right_count, recognized_count, test_set_count))
    result2_out.write("P = %f R = %f F = %f" % (precision, recall, F))

    my_result.close()
    right_result.close()
    result2_out.close()


if __name__ == '__main__':
    tree, maxCount = build_trie_tree('../res/CN.dict')  # 构建trie树
    result = forward_max_match('../res/textCN.txt', tree, maxCount)  # 前向最大匹配分文本
    save_partition_result(result)  # 保存分词结果
    save_PRF_result('../res/result1.txt', '../res/textCN.gold')  # 保存PRF结果

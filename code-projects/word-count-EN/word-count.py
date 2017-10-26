# -*- coding: UTF-8 -*-.
import re


def word_count(finPath):
    fin = open(finPath, 'r')
    all_words = re.split(r'[\s\.,:]', fin.read().strip())
    fin.close()
    result = {}
    for x in all_words:
        if x:
            result[x] = result.get(x, 0) + 1
    result = sorted(result.items(), key=lambda item:item[1], reverse=True)

    return result


if __name__ == '__main__':
    result = word_count('textEN.txt')
    fout = open('result.txt', 'w')
    for line in result:
        fout.write(line[0] + '\t' + str(line[1]) + '\n')
    fout.close()

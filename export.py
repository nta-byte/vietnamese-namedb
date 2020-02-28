import json
import collections
import os
from edit_name_db import edit_json_db




def export_name_freq_bigram(json_file_name, output, encoding='utf-8'):
    with open(json_file_name, encoding='utf-8') as f:
        data = json.load(f)
    text_out = ''
    names = []
    for dic in data:
        text_out += dic['full_name'] + '\n'
        names.append(dic['full_name'].lower())
    c = collections.Counter()
    for i in names:
        x = i.rstrip().split(" ")
        c.update(set(zip(x[:-1], x[1:])))
    bigram_txt = ''
    for i in c:
        if i != '' or i != ' ':
            bigram_txt += ' '.join(i) + ' ' + str(c[i] + 1000) + '\n'

    with open(output, "w", encoding=encoding) as f:
        f.write(bigram_txt)


def export_name_freq_dic(json_file_name, output, encoding='utf-8'):
    with open(json_file_name, encoding='utf-8') as f:
        data = json.load(f)
    words = []
    for dic in data:
        name_word = list(dic['full_name'].lower().split(' '))
        words.append(name_word)
    c = collections.Counter()
    words = list(words)
    for i in words:
        c.update(set(i))
    bigram_txt = ''
    for i in c:
        if i != '' or i != ' ':
            bigram_txt += i + ' ' + str(c[i] + 1000) + '\n'

    with open(output, "w", encoding=encoding) as f:
        f.write(bigram_txt)


if __name__ == "__main__":
    # json_file_name = 'uit_member_oringin.json'
    # edit_json_db(json_file_name)
    json_file_name = 'name_data.json'
    freq_name_bigram = '../symspellpy/freq_name_bigram.txt'
    export_name_freq_bigram(json_file_name, freq_name_bigram)
    freq_name_dic = '../symspellpy/freq_name_dic.txt'
    export_name_freq_dic(json_file_name, freq_name_dic)

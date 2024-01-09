from pprint import pprint
def sort_txt(txt1, txt2, txt3):
    with open('txt1.txt', encoding='utf-8') as f:
        text_1 = [line.strip() for line in f]
    with open('txt2.txt', encoding='utf-8') as f:
        text_2 = [line.strip() for line in f]
    with open('txt3.txt', encoding='utf-8') as f:
        text_3 = [line.strip() for line in f]
    all_texts = [text_1, text_2, text_3]
    all_texts[0] = ['txt1.txt', str(len(text_1))] + text_1
    all_texts[1] = ['txt2.txt', str(len(text_2))] + text_2
    all_texts[2] = ['txt3.txt', str(len(text_3))] + text_3
    all_texts = sorted(all_texts, key=len)
    return all_texts

#print(sort_txt('txt1.txt', 'txt2.txt', 'txt3.txt'))

with open('txt_all.txt', 'w', encoding='utf-8') as f:
    texts_all = sort_txt('txt1.txt', 'txt2.txt', 'txt3.txt')
    for text in texts_all:
        for line in text:
            f.write(line + '\n')
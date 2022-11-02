with open("1.txt", "r", encoding="utf8") as f_1:
    txt_1 = f_1.readlines()
    txt1 = ["1.txt\n", len(txt_1)]
    i = 0
    while i < len(txt_1):
        txt1.append(txt_1[i])
        i += 1
    txt_all = []
    txt_all.append(txt1)

with open("2.txt", "r", encoding="utf8") as f_2:
    txt_2 = f_2.readlines()
    txt2 = ["2.txt\n", len(txt_2)]
    i = 0
    while i < len(txt_2):
        txt2.append(txt_2[i])
        i += 1
    txt_all.append(txt2)
with open("3.txt", "r", encoding="utf8") as f_3:
    txt_3 = f_3.readlines()
    txt3 = ["3.txt\n", len(txt_3)]
    i = 0
    while i < len(txt_3):
        txt3.append(txt_3[i])
        i += 1
    txt_all.append(txt3)
    txt_all.sort(key=len)
    print(txt_all)
    i= 0
    text = []
    while i < len(txt_all) :
        text_num = " ".join(map(str,txt_all[i]))
        text.append(text_num)
        i += 1
print(text)
f = open("text.txt", 'w',encoding='utf8')
for element in text:
    f.writelines(element)
    f.write('\n')
f.close()
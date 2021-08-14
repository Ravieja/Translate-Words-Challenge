import csv
import os, psutil
process = psutil.Process(os.getpid())


fout2 = open("resources/t8.shakespeare.translated.txt","w")
dic = {}
freq = {}
with open("resources/french_dictionary.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dic[row[0]] = row[1]

parafile = open("resources/para.txt")
for line in parafile:
    pro_line = ""
    temp = ""
    for char in line:
        if char.isalpha():
            temp = temp + char
        else:
            if temp != "":
                if temp.lower() in dic:
                    if temp.lower() in freq:
                        freq[temp.lower()] += 1
                    else:
                        freq[temp.lower()] = 1

                    if temp.islower():
                        pro_line = pro_line + dic[temp.lower()].lower()
                    else:
                        if temp[1].islower():
                            pro_line = pro_line + dic[temp.lower()].capitalize()
                        else:
                            pro_line = pro_line + dic[temp.lower()].upper()
                else:
                    pro_line = pro_line + temp
            pro_line = pro_line + char
            temp = ""
    fout2.write(pro_line)

header = ['word', 'french translation', 'count']
with open('frequency.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    
    for word in sorted(freq.keys()):
        data = [word, dic[word], freq[word]]
        writer.writerow(data)

print(process.memory_info().rss) 
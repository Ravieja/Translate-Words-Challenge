import csv
import os, psutil
import time
# to calculate the memory usage
process = psutil.Process(os.getpid())

start=time.time() # for calculating run time


fout2 = open("resources/t8.shakespeare.translated.txt","w") # creating a text file to write translated text
dic = {}
freq = {}
with open("resources/french_dictionary.csv") as csv_file: # opening the french dictionary as a csv object
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dic[row[0]] = row[1]

parafile = open("resources/t8.shakespeare.txt") # Opening shakespeare text file

for line in parafile:                 #code to translate the words and to count the repetition
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

header = ['English Word', 'French Word', 'Frequency'] # creating header for csv file
with open('frequency.csv', 'w', encoding='UTF8') as f: # creating a scv file for the data
    writer = csv.writer(f)

    writer.writerow(header)
    
    for word in sorted(freq.keys()):
        data = [word, dic[word], freq[word]]
        writer.writerow(data)

end=time.time()
print(end-start)  # printing run time
print(process.memory_info().rss) # printing the memory usage

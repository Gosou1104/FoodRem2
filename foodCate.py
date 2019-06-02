# -*- coding:utf-8 -*-  
import json
import os
import sys
import subprocess
import unicodedata
import csv
import codecs


DIR = "/Users/gosou/Desktop/FoodRem/food_jsonFile/"
counterOfFile = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])#数有几个json

fr=open("/Users/gosou/Desktop/FoodRem/test4ge.csv",'r')

x=0

#for line in open('/Users/gosou/Desktop/FoodRem/test1.csv'):


temp_line_3=""
list=[]
listcsv_path = "/Users/gosou/Desktop/FoodRem/list.csv" # 在这改变输出csv的结果
if os.path.exists(listcsv_path): # 把那个list删了
    os.remove(listcsv_path)
for x in range(0,counterOfFile):# 所有的json里面


    line = fr.readline()
    with open(DIR+"rapide_"+str(x)+".json",'r') as load_f:#读取json按照顺序
        load_dict = json.load(load_f)
        new_load_dict =json.dumps(load_dict, ensure_ascii=False)
        #new_load_dict =new_load_dict.encode('unicode-escape')
        new_load_dict =json.loads(new_load_dict)# unicode_convert(json.loads(new_load_dict))
        #print(new_load_dict)

    w = open("/Users/gosou/Desktop/FoodRem/food_txtFile_final/final_result_"+str(x)+".txt","w")

    i=0
    for line1 in open("/Users/gosou/Desktop/FoodRem/food_txtFile/temp_output_9"+str(x)+".txt"):

        name_set =[]
        one_line = line1.strip().replace("\n", "")#.split(",")

        # print one_line#大根,だいこん/F
        temp_line_1 = one_line.split("/")[0]#大根,だいこん/F  豚,ぶた=ひき肉,ひきにく/F
        if '=' in temp_line_1:
            temp_line_1t = temp_line_1.split("=")
            for item_tt in temp_line_1t:
                name_set.append(item_tt.split(",")[0])
        else:

            name_set.append(temp_line_1.split(",")[0])#eg.大根 # 这个就是第一个

        for item_ttt in name_set:
            if (one_line in new_load_dict):


                csv_fifle = csv.reader(open("/Users/gosou/Desktop/FoodRem/food.csv","r"))


                for item in csv_fifle:  # item的第三项 # 打开了foodcsv
                    if(item[3]==item_ttt):
                        temp_line_3+=item[2]+" "
                        #w.write(one_line + ","+new_load_dict[one_line])
                        #w.write(temp_line_3)#new information #


                    else:
                        # print ("ERROR!!!")
                       pass

            #list.insert(x,temp_line_3)
            #
                #print(x)
    w.write(temp_line_3)
    #print(x)
    #print(temp_line_3)
    list.insert(x,temp_line_3+"\n")
    #if os.path.exists("/Users/gosou/Desktop/FoodRem/list.csv"):
    ff = open(listcsv_path, "a+", newline='')
    # else:
    #     ff = open("/Users/gosou/Desktop/FoodRem/list.csv", "w+", newline='')
    # csv_w = csv.writer(ff)
    # csv_w.writerows(list[x])
    ff.write(list[x])
    #print(list[x])
    temp_line_3 = ""


    #x+=1
    #fw.writerows(line+','+temp_line_3+"\n")
    #fw.close()
    #print "tempe_line_3"+temp_line_3
    #temp_line_3=""

#fr.close()
    w.close()
    ff.close()
# import StringIO
#
# s = StringIO.StringIO(text)
# with open('1.csv', 'w') as f:
# for line in list:
#    f.write(line)
#csvfile = open('/Users/gosou/Desktop/FoodRem/1.csv', 'w', newline = '')
#writer = csv.writer(csvfile)
#writer.writerows(list)
#csvfile.close()


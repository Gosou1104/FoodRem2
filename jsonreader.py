# -*- coding:utf-8 -*-  
import json
import os
import sys
import subprocess
import unicodedata
import csv
import codecs
import shutil
#import simplejson

def unicode_convert(input):#c处理乱码问题
    if isinstance(input, dict):
        return {unicode_convert(key): unicode_convert(value) for key, value in list(input.items())}
    elif isinstance(input, list):
        return [unicode_convert(element) for element in input]
    elif isinstance(input, str):
        return input.encode('utf-8')
    else:
        return input
DIR = "/Users/gosou/Desktop/FoodRem/action_jsonFile/"
counterOfFile = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])#数有几个json

for x in range(0,counterOfFile):

    print(x)

    with open(DIR+"rapide_"+str(x)+".json",'r') as load_f:#读取json按照顺序
        load_dict = json.load(load_f)
        new_load_dict =json.dumps(load_dict, ensure_ascii=False)
        #new_load_dict =new_load_dict.encode('unicode-escape')
        new_load_dict = json.loads(new_load_dict)#unicode_convert())
        print(new_load_dict)

    w = open("/Users/gosou/Desktop/FoodRem/action_txtFile_final/final_result_"+str(x)+".txt","w")#按照顺序读取txt
    counter = 0
    char_counter = 0 # count for the char dic
    dic_char = {} #to read the json to how many tags
    dic_counter_ttt =0
    with open("/Users/gosou/Desktop/FoodRem/tag_break/tag_break_"+str(x)+".json","r") as ff:#打开那个储存tag数量的json
            temp_char = json.load(ff)
            ff_load_dict = json.dumps(temp_char,ensure_ascii = False)
            dic_char = json.loads(ff_load_dict)#unicode_convert)
    dic_counter_ttt = dic_char[str(char_counter)]#初始值
    for line in open("/Users/gosou/Desktop/FoodRem/action_txtFile/temp_output_8"+str(x)+".txt"):
    
        
        #正常情况下
        if char_counter < 3 :
            if counter == dic_counter_ttt:# 相当于帮前面切
                print("-----------------nor--------------------")
                w.write("¥\n")
                char_counter+=1
                dic_counter_ttt +=dic_char[str(char_counter)] 
                
                if dic_char[str(char_counter)] == 0:#下一个为0
                    print("-----------------000--------------------")
                    w.write("¥\n")
                    char_counter+=1
                    dic_counter_ttt +=dic_char[str(char_counter)]

                if dic_char[str(char_counter)] == 0:#处理后面有两个0
                    print("-----------------000--------------------")
                    w.write("¥\n")
                    char_counter+=1
                    dic_counter_ttt +=dic_char[str(char_counter)]
        counter+=1




        print(("counter"+str(counter)))
        print(("char_counter"+str(char_counter)))
        # one_line = line.strip().replace("\n", "")#.split(",")
        # for line in open("/Users/gosou/Desktop/FoodRem/action_txtFile/temp_output_8"+str(x)+".txt"):
        one_line = line.strip().replace("\n", "")#.split(",")
        print(one_line)#eg.かけ,かける/Ac
        temp_line_1 = one_line.split("/")[0]#eg.かけ,かける
        temp_line_2 = temp_line_1.split(",")[1]#eg.かける
        #print (type(new_load_dict))
        if (one_line in new_load_dict):
            #w.write(one_line + ","+new_load_dict[one_line])
            csv_fifle = csv.reader(open("/Users/gosou/Desktop/FoodRem/make_food_action.csv","r"))
            for item in csv_fifle:
                #print(item[0].decode('utf-8'))
                #item_temp = item.split(",")
                #print(item[1].decode('utf-8'))
                #print(temp_line_2)
                #print("-------------")
                #print (item[1].decode('utf-8').encode('utf-8'))
                if(item[1]==temp_line_2):
                    w.write(one_line + ","+new_load_dict[one_line])
                    w.write(","+item[0]+"\n")
                    print("oo")

                else:
                    #print ("ERROR!!!")
                    pass
        w.write(str(counter)+"\n")# 看看哪些被省略了
    w.close()




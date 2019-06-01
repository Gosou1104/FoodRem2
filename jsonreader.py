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
        return {unicode_convert(key): unicode_convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [unicode_convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
<<<<<<< HEAD
DIR = "/Users/gosou/Desktop/FoodRem/action_jsonFile/"
=======
DIR = "/Users/gosou/Desktop/1/action_jsonFile/"
>>>>>>> bfee379a937bdd9bbce81ceb9bad4e9392154274
counterOfFile = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])#数有几个json

for x in xrange(0,counterOfFile):

<<<<<<< HEAD
    print(x)
=======

>>>>>>> bfee379a937bdd9bbce81ceb9bad4e9392154274
    with open(DIR+"rapide_"+str(x)+".json",'r') as load_f:#读取json按照顺序
        load_dict = json.load(load_f)
        new_load_dict =json.dumps(load_dict, ensure_ascii=False)
        #new_load_dict =new_load_dict.encode('unicode-escape')
        new_load_dict = unicode_convert(json.loads(new_load_dict))
        #print(new_load_dict)

<<<<<<< HEAD
    w = open("/Users/gosou/Desktop/FoodRem/action_txtFile_final/final_result_"+str(x)+".txt","w")#按照顺序读取txt
    counter = 0
    char_counter = 0 # count for the char dic
    dic_char = {} #to read the json to how many tags
    dic_counter_ttt =0
    with open("/Users/gosou/Desktop/FoodRem/tag_break/tag_break_"+str(x)+".json","r") as ff:#打开那个储存tag数量的json
            temp_char = json.load(ff)
            ff_load_dict = json.dumps(temp_char,ensure_ascii = False)
            dic_char = unicode_convert(json.loads(ff_load_dict))
    dic_counter_ttt = dic_char[str(char_counter)]#初始值
    for line in open("/Users/gosou/Desktop/FoodRem/action_txtFile/temp_output_8"+str(x)+".txt"):
    
        
        #正常情况下
        if char_counter < 3 :
            if counter == dic_counter_ttt:# 相当于帮前面切
                print("-----------------nor--------------------")
                w.write("-----------------nor--------------------\n")
                char_counter+=1
                dic_counter_ttt +=dic_char[str(char_counter)] 
                
                if dic_char[str(char_counter)] == 0:#下一个为0
                    print("-----------------000--------------------")
                    w.write("-----------------000--------------------\n")
                    char_counter+=1
                    dic_counter_ttt +=dic_char[str(char_counter)]

                if dic_char[str(char_counter)] == 0:#处理后面有两个0
                    print("-----------------000--------------------")
                    w.write("-----------------000--------------------\n")
                    char_counter+=1
                    dic_counter_ttt +=dic_char[str(char_counter)]
        counter+=1




        print("counter"+str(counter))
        print("char_counter"+str(char_counter))
        one_line = line.strip().replace("\n", "")#.split(",")
=======
    w = open("/Users/gosou/Desktop/1/action_txtFile_final/final_result_"+str(x)+".txt","w")#按照顺序读取txt
    for line in open("/Users/gosou/Desktop/1/action_txtFile/temp_output_8"+str(x)+".txt"):
        one_line = line.strip().replace("\n", "")#.split(",")
        print one_line#eg.かけ,かける/Ac
>>>>>>> bfee379a937bdd9bbce81ceb9bad4e9392154274
        temp_line_1 = one_line.split("/")[0]#eg.かけ,かける
        temp_line_2 = temp_line_1.split(",")[1]#eg.かける
        #print (type(new_load_dict))
        if (new_load_dict.has_key(one_line)):
            #w.write(one_line + ","+new_load_dict[one_line])
<<<<<<< HEAD
            csv_fifle = csv.reader(open("/Users/gosou/Desktop/FoodRem/make_food_action.csv","r"))
=======
            csv_fifle = csv.reader(open("/Users/gosou/Desktop/1/make_food_action.csv","r"))
>>>>>>> bfee379a937bdd9bbce81ceb9bad4e9392154274
            for item in csv_fifle:
                #print(item[0].decode('utf-8'))
                #item_temp = item.split(",")
                #print(item[1].decode('utf-8'))
                #print(temp_line_2)
                #print("-------------")
                #print (item[1].decode('utf-8').encode('utf-8'))
                if(item[1].decode('utf-8').encode('utf-8')==temp_line_2):
                    w.write(one_line + ","+new_load_dict[one_line])
                    w.write(","+item[0].decode('utf-8').encode('utf-8')+"\n")
<<<<<<< HEAD
=======
                    print "oo"
>>>>>>> bfee379a937bdd9bbce81ceb9bad4e9392154274

                else:
                    #print ("ERROR!!!")
                    pass
<<<<<<< HEAD
        w.write(str(counter)+"\n")# 看看哪些被省略了
      
=======
>>>>>>> bfee379a937bdd9bbce81ceb9bad4e9392154274
    w.close()




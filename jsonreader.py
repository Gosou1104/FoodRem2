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
import collections

def jsonreafer():
    DIR = "/Users/gosou/Desktop/FoodRem/action_jsonFile/"
    counterOfFile = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])  # 数有几个json

    for x in range(0, counterOfFile):

        print(x)

        with open(DIR + "rapide_" + str(x) + ".json", 'r') as load_f:  # 读取json按照顺序
            load_dict = json.load(load_f)
            new_load_dict = json.dumps(load_dict, ensure_ascii=False)
            # new_load_dict =new_load_dict.encode('unicode-escape')
            new_load_dict = json.loads(new_load_dict)  # unicode_convert())
            print(new_load_dict)

        w = open("/Users/gosou/Desktop/FoodRem/action_txtFile_final/final_result_" + str(x) + ".txt", "w")  # 按照顺序读取txt
        counter = 0
        char_counter = 0  # count for the char dic
        dic_char = {}  # to read the json to how many tags
        dic_counter_ttt = 0
        with open("/Users/gosou/Desktop/FoodRem/tag_break/tag_break_" + str(x) + ".json",
                  "r") as ff:  # 打开那个储存tag数量的json
            temp_char = json.load(ff)
            ff_load_dict = json.dumps(temp_char, ensure_ascii=False)
            dic_char = json.loads(ff_load_dict)  # unicode_convert)
        dic_counter_ttt = dic_char[str(char_counter)]  # 初始值
        for line in open("/Users/gosou/Desktop/FoodRem/action_txtFile/temp_output_8" + str(x) + ".txt"):

            # 正常情况下
            if char_counter < 3:
                if counter == dic_counter_ttt:  # 相当于帮前面切
                    print("-----------------nor--------------------")
                    w.write("¥\n")
                    char_counter += 1
                    dic_counter_ttt += dic_char[str(char_counter)]

                    if dic_char[str(char_counter)] == 0:  # 下一个为0
                        print("-----------------000--------------------")
                        w.write("¥\n")
                        char_counter += 1
                        dic_counter_ttt += dic_char[str(char_counter)]

                    if dic_char[str(char_counter)] == 0:  # 处理后面有两个0
                        print("-----------------000--------------------")
                        w.write("¥\n")
                        char_counter += 1
                        dic_counter_ttt += dic_char[str(char_counter)]
            counter += 1

            print(("counter" + str(counter)))
            print(("char_counter" + str(char_counter)))
            # one_line = line.strip().replace("\n", "")#.split(",")
            # for line in open("/Users/gosou/Desktop/FoodRem/action_txtFile/temp_output_8"+str(x)+".txt"):
            one_line = line.strip().replace("\n", "")  # .split(",")
            print(one_line)  # eg.かけ,かける/Ac
            temp_line_1 = one_line.split("/")[0]  # eg.かけ,かける
            temp_line_2 = temp_line_1.split(",")[1]  # eg.かける
            # print (type(new_load_dict))
            if (one_line in new_load_dict):
                # w.write(one_line + ","+new_load_dict[one_line])
                csv_fifle = csv.reader(open("/Users/gosou/Desktop/FoodRem/make_food_action.csv", "r"))
                for item in csv_fifle:
                    # print(item[0].decode('utf-8'))
                    # item_temp = item.split(",")
                    # print(item[1].decode('utf-8'))
                    # print(temp_line_2)
                    # print("-------------")
                    # print (item[1].decode('utf-8').encode('utf-8'))
                    if (item[1] == temp_line_2):
                        w.write(one_line + "," + new_load_dict[one_line])
                        w.write("," + item[0] + "\n")
                        print("oo")

                    else:
                        # print ("ERROR!!!")
                        pass
            w.write(str(counter) + "\n")  # 看看哪些被省略了
        w.close()

def is_japanese(string): # 检测是否包含日语
    for ch in string:
        name = unicodedata.name(ch)
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

def action_short():
    DIR = "/Users/gosou/Desktop/FoodRem/action_txtFile_final/"
    counterOfFile = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])  # 数有几个json
    for x in range(0,counterOfFile-1):
        wt = open("/Users/gosou/Desktop/FoodRem/action_txtFile_final/final_result_" + str(x) + ".txt", "r")# 按照顺序读取txt
        lastone = ""#作为最后的结果
        content_action = wt.read()  # 读取全部的文档
        title_action = []
        intru_action = []
        final_action = []
        content_temp = content_action.split("¥")  # 分成3个部分
        content_temp_tilte = content_temp[0].split("\n")# 首先对于题目的部分
        content_temp_intru = content_temp[1].split("\n")# 首先对于题目的部分
        content_temp_final = content_temp[2].split("\n")# 首先对于题目的部分
        for oneline in content_temp_tilte:
            if is_japanese(oneline):
                title_action.append(oneline.split(",")[3])#把料理方法记进去
        for oneline in content_temp_intru:
            if is_japanese(oneline):
                intru_action.append(oneline.split(",")[3])#把料理方法记进去
        for oneline in content_temp_final:
            if is_japanese(oneline):
                final_action.append(oneline.split(",")[3])#把料理方法记进去
        # 踢出他料理法
        while ("他の調理法" in title_action):
            for act in title_action:
                if act =="他の調理法":
                    title_action.remove(act)
        while ("他の調理法" in intru_action):
            for act in intru_action:
                if act =="他の調理法":
                    intru_action.remove(act)
        while ("他の調理法" in final_action):
            for act in final_action:
                    if act =="他の調理法":
                        final_action.remove(act)
        if len(final_action) != 0:  # 倒着来，如果title有值则会覆盖
            order_dt1 = shorter(final_action)
            lastone = findindic(order_dt1)
            #lastone = next(reversed(order_dt))# 按照从小到大排序输出最后一个key
        if len(intru_action) != 0:
            order_dt2 = shorter(intru_action)
            lastone = findindic(order_dt2)

            #lastone = next(reversed(order_dt))# 按照从小到大排序输出最后一个key
        if len(title_action) != 0:
            order_dt3 = shorter(title_action)
            lastone = findindic(order_dt3)

            #lastone = next(reversed(order_dt))# 按照从小到大排序输出最后一个key
        if is_japanese(lastone) == False:
            lastone ="他の調理法"
        print("last:"+lastone)
        wt.close()


def shorter(list1):
    dict1 = {}
    # 循环统计数字出现的个数并将其添加到字典集合中
    for i in list1:
        skey = dict1.get(i)  # 获取字典中的键的值
        if skey == None:  # 判断键的值是否为空
            dict1[i] = 1
        else:
            dict1[i] += 1
    return dict1# 返回一个有序的字典

def findindic(dic_t):
    max_t = 0
    max_n = ""
    # 第一次循环找到最大的
    for item in dic_t:
       if(dic_t[item]>max_t):
           max_t = dic_t[item]
           max_n = item
    # 第二次循环找到和最大的相同的元素
    same_list =[]
    if max_t !=0:
        for item in dic_t:
            if dic_t[item] == max_t:
                same_list.append(item)# 他的最大次数就是max_t
    #得到一个list，里面都是和他相同次数
    if len(same_list) > 1:
        return same_list[-1]
    else:
        return max_n



if __name__ == '__main__':
    jsonreafer()
    action_short()

#encoding:utf-8
import csv
import os
import unicodedata
from normalizer_sample import Normalizer
import preparation_for_ner_sample_ori
from finalizer_sample import Finalizer
import remove_sample
import replace_sample_action
import time
import shutil
import re
import json


char_path = "/Users/gosou/Desktop/FoodRem/jisx0208utf8.txt"
temp_input_path = "/Users/gosou/Desktop/FoodRem/temp_input.txt"
temp_output_path ="/Users/gosou/Desktop/FoodRem/temp_output.txt"
temp_output_path_2 ="/Users/gosou/Desktop/FoodRem/temp_output_2.txt"
temp_output_path_25 ="/Users/gosou/Desktop/FoodRem/temp_output_25.txt"
temp_output_path_3="/Users/gosou/Desktop/FoodRem/temp_output_3.txt"
temp_output_path_4="/Users/gosou/Desktop/FoodRem/temp_output_4.txt"
temp_output_path_5="/Users/gosou/Desktop/FoodRem/temp_output_5.txt"
temp_output_path_6="/Users/gosou/Desktop/FoodRem/temp_output_6.txt"
temp_output_path_7="/Users/gosou/Desktop/FoodRem/temp_output_7.txt"
temp_output_path_8="/Users/gosou/Desktop/FoodRem/temp_output_8.txt"
temp_output_path_9="/Users/gosou/Desktop/FoodRem/temp_output_9.txt"

def del_file(path):#删除文件
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

def add_tag(txt_path,tag_t):
    count_list=[]
    #打开全部的txt作为一个string的整体
    txt_f = open(txt_path)
    txt_content = str(txt_f.read())
    txt_content_temp = txt_content.split("\n")#通过换行进行分开
    count_list.append(len(txt_content_temp[0]))
    count_list.append(len(txt_content_temp[1]))
    count_list.append(len(txt_content_temp[2]))#统计每一段的字符数量
    #在数量范围内进行find
    char_dic={}
    pattern = re.compile(tag_t)#查找tag 
    result_0 = pattern.findall(txt_content_temp[0])
    result_1 = pattern.findall(txt_content_temp[1])
    result_2 = pattern.findall(txt_content_temp[2])
    print((txt_content_temp[2]))
    print(result_2)
    char_dic[0]=len(result_0)
    char_dic[1]=len(result_1)
    char_dic[2]=len(result_2)#统计find里面的tag的数量,也就是每一段的里面的tag数量
    #返回list
    return char_dic
if __name__ == '__main__':
    csv_file = csv.reader(open('/Users/gosou/Desktop/FoodRem/test.csv','r'))
    count=0
    counter =0
    string_list=[]
    DIR="/Users/gosou/Desktop/FoodRem/action_jsonFile/"
    shutil.rmtree(DIR)
    os.mkdir(DIR)
    del_file(DIR)
    for stu in csv_file:#每一行
        count+=1
        print(count)
        fp = open(temp_input_path,"w")
        fp.write(stu[2]+"\n"+stu[4]+"\n"+stu[6])

        fp.close()
        a = Normalizer(char_path)#1
        a.main(temp_input_path,temp_output_path)
        os.system("kytea -model /Users/gosou/Desktop/FoodRem/2014-10-23.kbm < "+temp_output_path +"> "+temp_output_path_2)#2
        
        os.chdir("/Users/gosou/Desktop/FoodRem/bccwjconv")#2.5
        #os.system("pwd")
        os.system("perl /Users/gosou/Desktop/FoodRem/addbase.perl <"+ temp_output_path_2+" > "+temp_output_path_25)
        os.chdir("/Users/gosou/Desktop/FoodRem/")

        #os.system("pwd")

        preparation_for_ner_sample_ori.main(temp_output_path_25,temp_output_path_3)#3
        os.system("kytea -model /Users/gosou/Desktop/FoodRem/recipe416.knm -out conf -nows -tagmax 0 -unktag /UNK "+temp_output_path_3 +"> temp.Ciob2 ")#4
        os.system("perl /Users/gosou/Desktop/FoodRem/bin/NESearch.pl temp.Ciob2 "+temp_output_path_4)#4
        b = Finalizer()
        b.main(temp_output_path_25,temp_output_path_4,temp_output_path_5)#5

        remove_sample.main(temp_output_path_5,temp_output_path_6)#6
        #os.system("python /Users/gosou/Desktop/FoodRem/remove_sample.py "+temp_output_path_5+" "+temp_output_path_6)

        os.system("python /Users/gosou/Desktop/FoodRem/remfood_real/replace_sample_action.py 0 "+temp_output_path_6+" "+temp_output_path_7)#7
        
        path_temp_8="/Users/gosou/Desktop/FoodRem/action_txtFile/temp_output_8"+str(counter)+".txt"# 这里的8是为了吧每一次的数据都存下来所以改变了path

        os.system("cat ./temp_output_7.txt | tr ' ' '\n' | grep '/Ac$'  > "+path_temp_8)#8

        tagdic = add_tag(temp_output_path_7,"/Ac")
        tag_breaker_path = "/Users/gosou/Desktop/FoodRem/tag_break/tag_break_"+str(counter)+".json"# 建好文件夹
        jsObj = json.dumps(tagdic,ensure_ascii=False)
        fileObj = open(tag_breaker_path,"w")
        fileObj.write(jsObj)
        fileObj.close()


        #os.system("cat ./temp_output_7.txt | tr ' ' '\n' | grep '/F$' | sort | uniq > "+path_temp_9)


        counter = counter+1
        
    #     os.system("./wcluster --text ./temp_output_7.txt --c `wc -l ./temp_output_8.txt` --threads 6 --restrict ./temp_output_8.txt")
    #     opf = open(temp_output_path_8,"r")
    #     # print opf
    #     # string_list.append(opf)
    # print string_list





    

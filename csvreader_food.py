#encoding:utf-8
import csv
import os
#import numpy as np
import unicodedata
from normalizer_sample import Normalizer
import preparation_for_ner_sample_ori
from finalizer_sample import Finalizer
import remove_sample
import replace_sample_food
import time
import shutil




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

if __name__ == '__main__':

    csv_file = csv.reader(open('/Users/gosou/Desktop/FoodRem/test4ge.csv','r'))
    count=0
    counter =0
    string_list=[]
    DIR="/Users/gosou/Desktop/FoodRem/food_jsonFile/"
    DIR2="/Users/gosou/Desktop/FoodRem/food_txtFile/"



    shutil.rmtree(DIR)
    os.mkdir(DIR)#清空json文件夹
    del_file(DIR)
    os.mkdir(DIR2) # 清空txt文件夹
    del_file(DIR2)

    for stu in csv_file:#每一行
        count+=1
        print (count)
        fp = open(temp_input_path,"w")
        #fp.write(stu[2]+" "+stu[4]+" "+stu[6])#action
        fp.write(stu[5])#food
        fp.close()
        a = Normalizer(char_path)#1
        a.main(temp_input_path,temp_output_path)
        os.system("kytea -model /Users/gosou/Desktop/FoodRem/2014-10-23.kbm < "+temp_output_path +"> "+temp_output_path_2)#2
        
        os.chdir("/Users/gosou/Desktop/FoodRem/bccwjconv")#2.5

        os.system("perl addbase.perl <"+ temp_output_path_2+" > "+temp_output_path_25)
        os.chdir("/Users/gosou/Desktop/FoodRem/")

        preparation_for_ner_sample_ori.main(temp_output_path_2,temp_output_path_3)#3
        os.system("kytea -model /Users/gosou/Desktop/FoodRem/recipe416.knm -out conf -nows -tagmax 0 -unktag /UNK "+temp_output_path_3 +"> temp.Ciob2 ")#4
        os.system("perl /Users/gosou/Desktop/FoodRem/bin/NESearch.pl temp.Ciob2 "+temp_output_path_4)#4

        b = Finalizer()
        b.main(temp_output_path_25,temp_output_path_4,temp_output_path_5)#5

        remove_sample.main(temp_output_path_5,temp_output_path_6)#6


        os.system("python /Users/gosou/Desktop/FoodRem/remfood_real/replace_sample_food.py 0 "+temp_output_path_6+" "+temp_output_path_7)#7
        
        path_temp_9="/Users/gosou/Desktop/FoodRem/food_txtFile/temp_output_9"+str(counter)+".txt"


        os.system("cat ./temp_output_7.txt | tr ' ' '\n' | grep '/F$' | sort | uniq > "+path_temp_9)#输出food文件夹


        counter = counter+1
        
    #     os.system("./wcluster --text ./temp_output_7.txt --c `wc -l ./temp_output_8.txt` --threads 6 --restrict ./temp_output_8.txt")
    #     opf = open(temp_output_path_8,"r")
    #     # print opf
    #     # string_list.append(opf)
    # print string_list


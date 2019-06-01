#coding:utf-8
import MeCab
m = MeCab.Tagger("-Owakati")
print("分かち書きしたい文章")
x = input()
print("入力文：",x)
print("結果：",m.parse(x))
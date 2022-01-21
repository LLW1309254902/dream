from django.shortcuts import render
import json
from django.http import HttpResponse

#调用模型
import string
import fasttext
import jieba
import json


# Create your views here.

#实例化模型
def modela():
    model_path = 'trained/mini.ftz'
    model = fasttext.load_model(model_path)
    return model

def run(texts):

    model = modela()
    y_label, Fy = model.predict(texts)
    if y_label=='__label__0':
        return True
    else:
        return False

def cut_sentence(texts):
    # 调用词典分词
    path = 'trained/keywords.txt'
    jieba.load_userdict(path)
    list_text = jieba.lcut(texts)
    #' '.join(jieba.lcut(texts)) '你 是 傻逼'
    return list_text

def getblack():
    text = []

    with open('trained/black.txt', 'r', encoding='utf-8') as c:
        important_words = c.readlines()
        for i in important_words:
            text.extend(i.strip().split())
    return text

def fencipanduan(list_text):
    new_text=''
    model = modela()
    for text_fenci in list_text:
        y_label, Fy = model.predict(text_fenci)
        if y_label[0] == '__label__0':
            black = getblack()

            # for i in black:
            #     if text_fenci == black:
            if text_fenci in black:
                new_text += '*'
            else :
                new_text += text_fenci
        else:
            new_text+='*'

    return new_text

def fenxi(texts):


    result = run(texts)
    if(not result):
        list_text = cut_sentence(texts)  #['你', '是', '傻逼']
        new_text=fencipanduan(list_text)
        result = new_text
    return result

def index(request):
    json_str = request.body

    req_data = json.loads(json_str)
    print(req_data['wenben'])

    result = fenxi(req_data['wenben'])
    print(result)

    # print(req_data['b'])
    return HttpResponse(result)




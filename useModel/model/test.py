import jieba
import fasttext

def cut_sentence(texts):
    # 调用词典分词
    path = 'trained/keywords.txt'
    # jieba.load_userdict(path)
    list_text = jieba.lcut(texts)

    return list_text

def modela():
    model_path = '../trained/mini.ftz'
    model = fasttext.load_model(model_path)
    return model
# result= cut_sentence('我是你爹')
# print(result)

model = modela()
y_label, Fy = model.predict('')
print(y_label, Fy)
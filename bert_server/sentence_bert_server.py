# coding=UTF-8
'''
@Author: xiaoyichao
LastEditors: xiaoyichao
@Date: 2020-06-11 08:42:52
LastEditTime: 2021-06-18 17:41:43
@Description:   获取SentenceBERT的向量
'''

import numpy as np
import torch
import os
import configparser
from sentence_transformers import SentenceTransformer

dir_name = os.path.abspath(os.path.dirname(__file__))

faq_config = configparser.ConfigParser()
faq_config.read(os.path.join(dir_name, "../config/befaq_conf.ini"))
Sentence_BERT_path = os.path.join(dir_name, "../", str(
    faq_config["AlgorithmConfiguration"]["Sentence_BERT_path"]))


class SentenceBERT(object):
    '''
    Author: xiaoyichao
    param {type}
    Description: SentenceBERT
    '''

    def __init__(self):
        self.model = SentenceTransformer(Sentence_BERT_path)
        if torch.cuda.is_available():
            self.model = self.model.to(torch.device("cuda"))
        print("Sentenence BERT使用的设备为：%s" % self.model.device)

    def normalize(self, vec):
        '''
        Author: xiaoyichao
        param {type}
        Description: 矢量在用于相似度计算之前被归一化为单位长度，使得余弦相似性和点积相当。参考文章https://www.thinbug.com/q/41387000
        '''
        norm = np.linalg.norm(vec)
        if norm == 0:
            return vec
        return vec/norm

    def get_bert(self, sentence_list):
        '''
        Author: xiaoyichao
        param {type}
        Description: 返回(512,)纬度的SentenceBERT向量
        '''
        sentences_vec = []
        sentences_vec = np.array(self.model.encode(sentence_list))
        sentences_vec_mean = np.mean(sentences_vec, axis=0).reshape(-1, 512)
        # sentences_vec_max = np.max(sentences_vec, axis=0).reshape(-1, 512)
        return np.array([self.normalize(sentences_vec_mean[0])])

    def get_object(self):
        '''
        Author: xiaoyichao
        param {type}
        Description: 返回SentenceBERT的对象
        '''
        return self.model


# # # 测试demo
if __name__ == '__main__':
    sentenceBERT = SentenceBERT()
    sentences_vec = sentenceBERT.get_bert(sentence_list=["hi", "你好"])
    print(sentences_vec.shape)
    print(sentences_vec)

# coding=UTF-8
'''
@Author: xiaoyichao
LastEditors: xiaoyichao
@Date: 2020-05-22 13:54:44
LastEditTime: 2021-06-06 21:42:47
@Description: 线性模型的重排序，给予不同的算法不同的权重
'''


class ReRank(object):
    def linear_model(self, consin_sim, jaccard_sim, bm25_sim, edit_distance_sim, consine_weight, jaccard_weight, BM25_weight, edit_distance_weight):
        if consin_sim != []:
            tmp_multiple_sims = [i * consine_weight + j*jaccard_weight + k*BM25_weight + l*edit_distance_weight
                                 for i, j, k, l in zip(consin_sim, jaccard_sim, bm25_sim, edit_distance_sim)]
            multiple_sims = []
            if consine_weight + jaccard_weight + BM25_weight + edit_distance_weight ==1:
                for multiple_sim in tmp_multiple_sims:
                    if multiple_sim > 1:
                        multiple_sim = 1
                    multiple_sims.append(multiple_sim)
            else:
                multiple_sims = tmp_multiple_sims
            return multiple_sims
        else:
            multiple_sims = jaccard_sim
            return multiple_sims


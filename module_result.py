import numpy as np

def __doc__():
    print("yはモデルの出力、ラベルの付与確率の予測")
    print("tは正解ラベル")

def get_n_label(t_list):
    """
    各文書に実際に付与されているFIの数のリスト
    get_n_lael_index
    """
    return [sum(t) for t in t_list]

def get_n_label_index(t_list, n):
    """
    n個ラベルが付与されている文書のインデックスを返す
    get_n_label_documents_top_m
    """
    index = []
    n_label = get_n_label(t_list)
    for i in range(len(t_list)):
        if n_label[i] == n:
            index.append(i)
    return index

def get_coverage_at_m(y, t, m):
    """
    coverage@30を返す
    １つの文書に関して
    """
    ind = np.argsort(y)[::-1]
    labels = t[ind]
    cov = np.sum(labels[:m]) / np.sum(labels)
    return cov

def get_n_label_documents_top_m(t_list, y_list, n, m):
    """
    n個ラベルが付与されている文書に関してcoverage@mを返す
    """

    n_label_index = get_n_label_index(t_list, n)
    for i in n_label_index:

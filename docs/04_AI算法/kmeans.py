import numpy as np

def kmeans(k, data, max_iter=100):
    """
    K-Means聚类
    :param k: 聚类簇数
    :param data: 训练数据，格式为[特征向量, ...]
    :param max_iter: 最大迭代次数
    :return: (预测结果列表, 簇中心)，预测结果为每个样本所属簇的下标
    """
    data = np.array(data, dtype=float)
    n_samples = len(data)

    # 随机选取k个样本作为初始簇中心
    centers = data[np.random.choice(n_samples, k, replace=False)]

    labels = np.zeros(n_samples, dtype=int)
    for _ in range(max_iter):
        # 将每个样本分配到距离最近的簇中心
        distances = np.linalg.norm(data[:, None] - centers[None, :], axis=2)
        new_labels = np.argmin(distances, axis=1)

        # 标签不再变化则收敛
        if np.array_equal(new_labels, labels):
            break
        labels = new_labels

        # 用簇内样本的均值更新簇中心
        for i in range(k):
            members = data[labels == i]
            # 簇为空时保留原中心，避免出现NaN
            if len(members) > 0:
                centers[i] = members.mean(axis=0)

    return labels.tolist(), centers

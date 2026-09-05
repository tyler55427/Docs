import numpy as np

def knn(k, train_data, test_data):
    """
    KNN算法
    :param k: K值
    :param train_data: 训练数据，格式为[(特征向量, 标签), ...]
    :param test_data: 测试数据，格式为[(特征向量, 标签), ...]
    :return: 预测结果列表
    """
    predictions = []
    for test_point, _ in test_data:
        # 计算测试点与训练数据中每个点的距离
        distances = []
        for train_point, label in train_data:
            distance = np.linalg.norm(np.array(test_point) - np.array(train_point))
            distances.append((distance, label))
        
        # 按距离排序并选择前K个最近的点
        distances.sort(key=lambda x: x[0])
        neighbors = distances[:k]
        
        # 统计K个邻居中出现最多的标签
        labels = [label for _, label in neighbors]
        predicted_label = max(set(labels), key=labels.count)
        predictions.append(predicted_label)
    
    return predictions
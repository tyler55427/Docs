from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass
class Node:
    feature: int = -1  # 划分特征的下标，-1 表示叶子
    cls: int = 0  # 叶子节点的类别
    left: Node | None = None  # 特征为 0 的分支
    right: Node | None = None  # 特征为 1 的分支


def entropy(indices, y):
    """样本集合的信息熵，空集返回 0"""
    if not indices:
        return 0.0
    ones = sum(y[i] for i in indices)
    p1 = ones / len(indices)
    p0 = 1 - p1
    # 任意一类为空时熵为 0，对应信息增益最大
    if p1 == 0 or p0 == 0:
        return 0.0
    return -p1 * math.log(p1) - p0 * math.log(p0)


def information_gain(indices, X, y, feature):
    """信息增益 = 原熵 - 条件熵，原熵固定，故只需比较条件熵"""
    used = [i for i in indices if X[i][feature] == 1]
    unused = [i for i in indices if X[i][feature] == 0]
    cond = len(used) / len(indices) * entropy(used, y)
    cond += len(unused) / len(indices) * entropy(unused, y)
    return entropy(indices, y) - cond


def build_tree(X, y, indices, used):
    """递归构建决策树，used 为已使用的特征下标集合"""
    labels = [y[i] for i in indices]

    # 全部样本同类：直接作为叶子
    if all(c == labels[0] for c in labels):
        return Node(cls=labels[0])

    # 在当前可用特征中选择信息增益最大的一个
    best_feature, best_gain = -1, 0.0
    for f in range(len(X[0])):
        if f in used:
            continue
        gain = information_gain(indices, X, y, f)
        if gain > best_gain:
            best_feature, best_gain = f, gain

    # 无可用特征，或所有特征增益都为 0：按多数类作为叶子
    if best_feature == -1:
        ones = sum(y[i] for i in indices)
        return Node(cls=1 if ones * 2 > len(indices) else 0)

    left = [i for i in indices if X[i][best_feature] == 0]
    right = [i for i in indices if X[i][best_feature] == 1]
    used.add(best_feature)
    node = Node(
        feature=best_feature,
        left=build_tree(X, y, left, used),
        right=build_tree(X, y, right, used),
    )
    # 回溯时释放该特征，兄弟分支仍可重新使用
    used.remove(best_feature)
    return node


def query(node, sample):
    """沿树下行到叶子，返回类别"""
    while node.feature != -1:
        node = node.right if sample[node.feature] == 1 else node.left
    return node.cls


def predict(root, samples):
    return [query(root, sample) for sample in samples]

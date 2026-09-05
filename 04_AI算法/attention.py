import torch

class Attention:    
    def __init__(self, hidden_size):
        self.hidden_size = hidden_size
        self.q_W = torch.nn.Linear(hidden_size, hidden_size)
        self.k_W = torch.nn.Linear(hidden_size, hidden_size)
        self.v_W = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, query, key, value):
        # 计算查询、键和值的线性变换
        Q = self.q_W(query)
        K = self.k_W(key)
        V = self.v_W(value)

        # 计算注意力权重
        attention_scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.hidden_size ** 0.5)
        attention_scores_exp = torch.exp(attention_scores)
        attention_weights = attention_scores_exp / torch.sum(attention_scores_exp, dim=-1, keepdim=True)

        # 计算加权值
        output = torch.matmul(attention_weights, V)
        return output
    
class MultiHeadAttention:
    def __init__(self, hidden_size, num_heads):
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.head_size = hidden_size // num_heads
        self.attention_heads = [Attention(self.head_size) for _ in range(num_heads)]
        self.output_linear = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, query, key, value):
        # 将输入分成多个头
        batch_size = query.size(0)
        query = query.view(batch_size, -1, self.num_heads, self.head_size).transpose(1, 2)
        key = key.view(batch_size, -1, self.num_heads, self.head_size).transpose(1, 2)
        value = value.view(batch_size, -1, self.num_heads, self.head_size).transpose(1, 2)

        # 对每个头进行注意力计算
        attention_outputs = []
        for i in range(self.num_heads):
            # 后面的:可以省略，因为已经指定了维度
            attention_output = self.attention_heads[i].forward(query[:, i], key[:, i], value[:, i])
            attention_outputs.append(attention_output)

        # 将多个头的输出拼接起来
        concatenated_attention = torch.cat(attention_outputs, dim=-1)
        
        # 通过线性层得到最终输出
        output = self.output_linear(concatenated_attention)
        return output
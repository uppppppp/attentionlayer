import torch
import torch.nn as nn
import torch.nn.functional as F
import math
class selfattention(nn.moudel):
    def __init__(self, embed_size):
        super(selfattention, self).__init__()
        self.embed_size = embed_size
        self.quiery = nn.Linear(embed_size, embed_size, bias=False)
        self.key = nn.Linear(embed_size, embed_size, bias=False)
        self.value = nn.Linear(embed_size, embed_size, bias=False)
        self.outputs = nn.Linear(embed_size, embed_size)
    def forward(self, quiery, key, value, mask=None):
        Q = self.quiery(quiery)
        K = self.key(key)
        V = self.value(value)
        attention_scores = torch.matmul(Q, K.transpose(-1,-2))/math.sqrt(self.embed_size)
        if mask:
            attention_scores = attention_scores.masked_fill(mask == 0 , -1e9)
        attention_weight = F.softmax(attention_scores,dim=-1)
        scores = torch.matmul(attention_weight,V)
        scores = self.outputs(scores)
        return scores
    
        

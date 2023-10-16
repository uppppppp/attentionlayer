import torch
import torch.nn as nn
import torch.nn.functional as F
import math
class Multiheadattention(nn.modules):
    def __init__(self, embed_size, h):
        self.embed_size = embed_size
        self.h = h
        

import torch
import torch.nn as nn 
import torch.nn.functional as F 
from torch.optim import Adam  
                             
from torch.utils.data import TensorDataset, DataLoader 

import lightning as L

class PositionEncoding(nn.Module):
    
    def __init__(self, d_model=2, max_len=6):
        
        super().__init__()
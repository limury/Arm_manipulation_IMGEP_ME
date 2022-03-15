'''import sys
import os
import numpy as np
from environment import ArmToolsToysEnvironment

import map_elites.cvt as cvt_map_elites

from experiment import Experiment


print(np.random.random(1))'''

import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv1d(1, 64, 2)
        self.conv2 = nn.Conv1d(64, 128, 2)
        print(torch.randn(30))
        print(torch.randn(30).view(-1, 1, 30))
        x = torch.randn(30).view(-1, 1, 30)
        self._to_linear = None
        self.convs(x)
    
    def convs(self, x):
        x = F.max_pool1d(F.relu(self.conv1(x)), 2)
        x = F.max_pool1d(F.relu(self.conv2(x)), 2)
        
        if self._to_linear is None:
            self._to_linear = x[0].shape[0] * x[0].shape[1]
            print ("x:", x, "_to_linear: ", self._to_linear)
        return x

x = Net().to(device)
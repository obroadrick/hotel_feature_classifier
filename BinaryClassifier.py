import torch.nn as nn
class BinaryClassification(nn.Module):
    def __init__(self):
        super(BinaryClassification, self).__init__()
        # Number of input features is 12.
        self.layer_1 = nn.Linear(128, 85) 
        self.layer_2 = nn.Linear(85, 160)


        self.layer_out = nn.Linear(160, 1) 
        
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)
        self.batchnorm_layer_1 = nn.BatchNorm1d(85)
        self.batchnorm_layer_2 = nn.BatchNorm1d(160)


        self.sigmoid = nn.Sigmoid()
    
        
    def forward(self, inputs):
        # complete layer 1
        x = self.relu(self.layer_1(inputs))
        x = self.batchnorm_layer_1(x)
        x = self.dropout(x)

        # complete layer 2
        x = self.relu(self.layer_2(x))
        x = self.batchnorm_layer_2(x)
        x = self.dropout(x)

        x = self.layer_out(x)
        return x
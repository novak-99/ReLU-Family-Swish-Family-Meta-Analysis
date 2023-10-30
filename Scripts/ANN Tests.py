import torch
import torch.nn as nn 
import torchvision
import torchvision.transforms as transforms

# device config
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#device = torch.device('cpu')

layers = 30
max_epoch = 15
batch_size = 128
learning_rate = 1e-5

class Serf(nn.Module):
        def __init__(self):
            super(Serf, self).__init__()
        def forward(self, X):
            return torch.erf(torch.nn.functional.softplus(X)) * X

def createAct(activation="relu"):  
    if activation == "silu":
      return nn.SiLU()
    elif activation == "relu":
      return nn.ReLU()
    elif activation == "mish":
      return torch.nn.Mish()
    elif activation == "serf":
      return Serf()

# MNIST
train_dataset = torchvision.datasets.MNIST(root='./data', train=True,
    transform=transforms.ToTensor(), download=True)

test_dataset = torchvision.datasets.MNIST(root='./data', train=False,
    transform=transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size,
                                          shuffle=False)


class ANN(nn.Module):
  def __init__(self, n_layers, n_input, n_hidden, n_class, activation):
    super(ANN, self).__init__()
    self.first = nn.Linear(n_input, n_hidden)
    self.firstbn = nn.BatchNorm1d(num_features=n_hidden) 
    self.firstdp = nn.Dropout(p=0.25)

    self.n_layers = n_layers
    self.n_class = n_class
    self.n_hidden = n_hidden
    self.activation = activation

    self.l = nn.ModuleList()  

    self.bn = nn.ModuleList()

    self.dp = nn.ModuleList()

    for i in range (self.n_layers):
      self.l.append(nn.Linear(self.n_hidden, n_hidden))
      self.bn.append(nn.BatchNorm1d(num_features=n_hidden))
      self.dp.append(nn.Dropout(p=0.25))
    self.final = nn.Linear(n_hidden, n_class) # 10 classes

  def forward(self, X):
    out = self.firstbn(self.firstdp(createAct(self.activation)(self.first(X))))
    for i in range (self.n_layers):      
      out = self.bn[i](self.dp[i](createAct(self.activation)(self.l[i](out))))
    return self.final(out)

network = ANN(layers, 784, 512, 10, act).to(device)

# Loss 
loss = nn.CrossEntropyLoss()
optimizer = torch.optim.RMSprop(network.parameters(), lr=learning_rate)

  

current_acc = 0.0
for epoch in range(max_epoch):
  # TRAIN
  network.train()
  for i, (images, labels) in enumerate(train_loader):
    images = images.reshape(-1, 28**2).to(device)
    labels = labels.to(device)

    l = loss(network(images), labels)
    l.backward() 
    optimizer.step()
    optimizer.zero_grad()

  # EVAL
  network.eval()
      
  n_c = 0
  n_s = 0

  for i, (examples, labels) in enumerate(test_loader):
    examples = examples.reshape(-1, 28**2).to(device)
    labels = labels.to(device)
    y_test_pred = network(examples)
    __, actual_pred = torch.max(y_test_pred, 1)
    n_c += torch.sum(actual_pred==labels).item()
    n_s += labels.shape[0]

  acc = (n_c/n_s) * 100
  if acc > current_acc:
    torch.save(network.state_dict(), 'best-model-parameters.pt')
  current_acc = acc

  print(current_acc)
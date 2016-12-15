import numpy as np

def inflate(rules, size):
            
    number = len(rules)
    rules = np.array(rules)
    inflated = rules[np.array(np.random.randint(low=0, high=number, size=size))]
    data, labels = zip(*inflated)
    data = np.array(data)
    labels = np.array(labels)
    return data, labels   

def onehot(val):
    
    # A simple one-hot encoding for single-digit integers
    onehot = [0,0,0,0,0,0,0,0,0,0]
    onehot[val] = 1
    return onehot

# Rules for training data

def place(a,b,c,l):
    if l == 1:
        return c
    elif l == 2:
        return b
    elif l == 3:
        return a
    else:
        return 0
    
def addition():
    
    # Generates addition rules for two single-digits (without carry-over)
    return [[(onehot(i),onehot(j)),(onehot((i+j)%10))] for i in range(10) for j in range(10)]   

def carry():
    
    # Generates addition carry-over rules for two single-digits 
    return [[(onehot(i),onehot(j)),(onehot((i+j)//10))] for i in range(10) for j in range(10)]   

def concatenation():
    
    rules = [[(onehot(i),onehot(j)),(onehot(i)+onehot(j))] for i in range(10) for j in range(10)]
    return rules

def successor():
    
    return [[[onehot(i)],(onehot((i+1)%10))] for i in range(10)]

def predecessor():
    
    return [[[onehot(i)],(onehot((i-1)%10))] for i in range(10)]

def extraction():
    
    return [[(onehot(i)+onehot(j)+onehot(k),onehot(0)+onehot(0)+onehot(l)),(onehot(place(i,j,k,l)))] for i in range(10) for j in range(10) for k in range(10) for l in range(1,4)]

def equality():
    
    return [[(onehot(i),onehot(j)),(onehot(int(i==j)))] for i in range(10) for j in range(10)]
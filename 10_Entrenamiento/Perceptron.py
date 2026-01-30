import numpy as np
import pandas as pd 

rg = np.random.default_rng()

def generate_data(n_features, n_values):
    features = rg.random((n_features,n_values))
    print(features)
    weights = rg.random((1,n_values))[0]
    print(weights)
    targets = np.random.choice([0,1],n_features)
    print(targets)

    data = pd.DataFrame(features, columns = ["x0","x1","x2"])
    data["targets"] = targets
    print(data)

    return data,weights

bias = 0.5 
l_rate = 0.1

def get_weighted_sum(feature,weights,bias):
    return np.dot(feature,weights)+bias

def sigmoid(w_sum):
    return 1/(1+np.exp(-w_sum))


def cross_entropy(target,prediction):
    return -(target*np.log10(prediction)+(1-target)*np.log10(1-prediction))

def update_weight(weights, l_rate, target, prediction,feature):
    new_weights = []
    for x,w in zip(feature, weights):
        new_w = w + l_rate*(target-prediction)*x
        new_weights.append(new_w)
    return new_weights

def update_bias(bias, l_rate, target, prediction):
    return bias+l_rate*(target-prediction)

data, weights = generate_data(4,3)

for i in range(len(data)):
    feature = data.loc[i][:-1]
    target = data.loc[i][-1]
    w_sum = get_weighted_sum(feature,weights,bias)
    print(w_sum)
    prediction = sigmoid(w_sum)
    print(prediction)
    loss = cross_entropy(target, prediction)
    print(loss)

    print("Old values")
    print(weights, bias)

    weights = update_weight(weights,l_rate,target,prediction,feature)

    bias = update_bias(bias,l_rate, target, prediction)

    print("New bias")
    print(weights,bias)


import numpy as np
import pandas as pd 

rg = np.random.default_rng()

def generate_data(n_features, n_values):
    features = rg.random((n_features,n_values))
    #print(features)
    weights = rg.random((1,n_values))[0]
    #print(weights)
    targets = np.random.choice([0,1],n_features)
    #print(targets)
    column_names = [f"x{i}" for i in range(n_values)]
    data = pd.DataFrame(features, columns = column_names)
    data["targets"] = targets
    #print(data)
    return data,weights

bias = 0.5 
l_rate = 0.1
epochs = 10
epochs_loss = []

def get_weighted_sum(feature,weights,bias):
    return np.dot(feature,weights)+bias

def sigmoid(w_sum):
    return 1/(1+np.exp(-w_sum))

def cross_entropy(target,prediction):
    epsilon = 1e-10
    prediction = np.clip(prediction,epsilon,1-epsilon)
    return -(target*np.log10(prediction)+(1-target)*np.log10(1-prediction))

def update_weight(weights, l_rate, target, prediction,feature):
    new_weights = []
    for x,w in zip(feature, weights):
        new_w = w + l_rate*(target-prediction)*x
        new_weights.append(new_w)
    return np.array(new_weights)

def update_bias(bias, l_rate, target, prediction):
    return bias+l_rate*(target-prediction)

def train_model(data,weights,bias,l_rate,epochs):
    for e in range(epochs):
        individual_loss = []
        for i in range(len(data)):
            row = data.iloc[i]
            feature = row[:-1].values
            target = row["targets"]
            w_sum = get_weighted_sum(feature,weights,bias)
            prediction = sigmoid(w_sum)
            loss = cross_entropy(target,prediction)
            individual_loss.append(loss)

            print("old values")
            print(weights, bias)

            weights = update_weight(weights,l_rate,target,prediction,feature)
            bias = update_bias(bias,l_rate, target, prediction)

            print("New values")
            print(weights,bias)

        average_loss = sum(individual_loss)/len(individual_loss)

        epochs_loss.append(average_loss)
        print("****")
        print("epochs",e)
        print(average_loss)

data, weights = generate_data(50,3)
train_model(data, weights, bias,l_rate,epochs)


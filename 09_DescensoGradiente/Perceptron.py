import numpy as np

def sigmoid(w_sum):
    return 1/(1+np.exp(-w_sum))

def get_prediction(features, weights, bias):
    return sigmoid(np.dot(features, weights)+bias)

def cross_entropy(target, pred):
    loss = -(target*np.log10(pred)+(1-target)*np.log10(1-pred))
    return loss

def gradient_descent(features, weights,target, prediction, I_rate, bias):
    bias += I_rate*(target-prediction)
    new_weights = weights+I_rate*np.dot((target-prediction),features)
    return new_weights,bias

features = np.array(([0.1,0.5,0.2],[0.2,0.3,0.1],[0.7,0.4,0.2],[0.1,0.4,0.3]))
targets =np.array([0,1,0,1])
weights = np.array([0.4,0.2,0.6])
bias = 0.5
I_rate = 0.1

prediction = get_prediction(features, weights, bias)
loss = cross_entropy(targets, prediction)
new_weights,bias =gradient_descent(features, weights, targets, prediction, I_rate,bias)
print("Update Weights: ", new_weights)
print("Update Bias: ", bias)
print("Loss: ", loss)

#Binary clasification with cross entropy loss
import numpy as np

np.random.seed(42)

NUM_SAMPLES = 10
NUM_FEATURES = 4

features = np.random.rand(NUM_SAMPLES,NUM_FEATURES)

true_labels = np.random.randint(0,2,size=NUM_SAMPLES)

def sigmoid(x):
    return 1

def mock_model(features):
    weights = np.random.rand(NUM_FEATURES)
    logits = np.dot(features, weights)
    return sigmoid(logits)

def binary_cross_entropy_loss(probs, labels):
    probs = np.clip(probs, 1e-10, 1- 1e-10)
    loss = -np.mean(labels*np.log(probs)+(1-labels)*np.log(1-probs))
    return loss

def classification_pipeline(features, true_labels):
    print("Features:\n", features)

    predicted_probs = mock_model(features)
    print("\nPredicted Probalities (for class 1):\n", predicted_probs)

    loss = binary_cross_entropy_loss(predicted_probs, true_labels)
    print("\nTrue Labels: ",true_labels)
    print(f"\nBinary Cross-Entropy Loss: {loss:.4f}")
    return loss

if __name__ == "__main__":
    loss = classification_pipeline(features, true_labels)
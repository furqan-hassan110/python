from sklearn.datasets import load_breast_cancer
data = load_breast_cancer

labels_names=data['target_names']
labels= data['labels']
features_names=data['features_names']
feature=data['data']

print(labels_names)
print(labels[0])
print(features_names)
print(feature[0])

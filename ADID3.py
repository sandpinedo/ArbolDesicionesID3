from collections import Counter
import math

# Datos del Clima y Temperatura
data = [
    ["soleado", "alta", "no"],
    ["soleado", "suave", "no"],
    ["nublado", "alta", "si"],
    ["lluvioso", "alta", "si"],
    ["lluvioso", "suave", "si"],
]   

# Funcion para calcular la Entropia
def entropy(labels):
    label_counts = Counter(labels)
    total_samples = len(labels)
    entropy =0
    for label, count in label_counts.items():
        probability = count / total_samples
        entropy -= probability * math.log2(probability)
    return entropy

# Funcion para calcular la Ganancia de Informacion
def ganancia_informac(data, labels, feature_idx):
    total_entropy = entropy(labels)
    unique_values = set([sample[feature_idx] for sample in data])
    weighted_entropy = 0
    for value in unique_values:
        subset_labels = [sample[-1] for sample in data if sample[feature_idx] == value]
        weighted_entropy += len(subset_labels) / len(labels) * entropy(subset_labels)
    return total_entropy - weighted_entropy   

# Funcion para selecionar el mejor atributo
def selec_mejor_atributo(data, labels):
    num_features = len(data[0]) - 1
    gains = [ganancia_informac(data, labels, i) for i in range(num_features)]
    best_feature_idx = gains.index(max(gains))
    return best_feature_idx

# Funcion para construir en arbol de Decision usando ID3
def id3(data, labels, features):
    if len(set(labels)) ==1:
        return labels[0]
    if len(features) == 0:
        majority_label = Counter(labels).most_common(1)[0][0]
        return majority_label
    
    best_feature_idx = selec_mejor_atributo(data, labels)
    best_feature = features[best_feature_idx]
    
    tree ={best_feature: []}
    unique_values = set([sample[best_feature_idx] for sample in data])
    for value in unique_values: 
        subset_data =[sample for sample in data if sample[best_feature_idx] == value]
        subset_labels = [sample[-1] for sample in subset_data]
        new_features = [f for i, f in enumerate(features) if i != best_feature_idx]
        tree[best_feature][value] = id3(subset_data, subset_labels, new_features)
     
    return tree   

# Ejemplo de uso 
feature =["clima", "temperatura"]
labels = [sample[-1] for sample in data]
tree = id3(data, labels, feature)
print (tree)

        
        
    
                       
                       
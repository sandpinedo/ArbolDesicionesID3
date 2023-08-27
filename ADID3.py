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

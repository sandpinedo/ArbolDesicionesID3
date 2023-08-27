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
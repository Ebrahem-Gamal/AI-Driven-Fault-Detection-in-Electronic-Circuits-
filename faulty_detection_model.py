import csv 
import itertools 
import random 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, LabelEncoder 
from sklearn.neural_network import MLPClassifier 
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score, confusion_matrix 
import numpy as np 

# ========== Part 1: DATASET GENERATION ========== 
SAMPLES_PER_CLASS = 10 

components = { 
    'C1': 1.0,    # nF 
    'C2': 1.0,    # nF 
    'R1': 1.0,    # kΩ 
    'R2': 10.0,   # kΩ 
    'R4': 10.0    # kΩ 
} 

fault_delta = {'up': 1.5, 'down': 0.5}
single_faults = [{'label': 'NF', **components}]

# Single faults 
for comp in components:
    for direction, factor in fault_delta.items():
        row = components.copy() 
        row[comp] = row[comp] * factor
        label = f'{comp}{"↑" if direction=="up" else "↓"}'
        row['label'] = label
        single_faults.append(row.copy())

# Double faults
double_faults = [] 
pairs = list(itertools.combinations(components.keys(), 2)) 

for c1, c2 in pairs: 
    for dir1, dir2 in [('up', 'up'), ('down', 'down'), ('up', 'down'), ('down', 'up')]: 
        row = components.copy() 
        row[c1] *= fault_delta[dir1] 
        row[c2] *= fault_delta[dir2] 
        label = f'{c1}{"↑" if dir1=="up" else "↓"}_{c2}{"↑" if dir2=="up" else "↓"}' 
        row['label'] = label 
        double_faults.append(row.copy()) 

all_cases = single_faults + double_faults 

def simulate_features(): 
    return [round(random.uniform(0.5, 1.5), 3) for _ in range(4)] 

header = list(components.keys()) + ['F1', 'F2', 'F3', 'F4', 'Label'] 
rows = [] 

for row in all_cases: 
    for _ in range(SAMPLES_PER_CLASS): 
        features = simulate_features() 
        csv_row = [row['C1'], row['C2'], row['R1'], row['R2'], row['R4']] + features + [row['label']] 
        rows.append(csv_row) 

# التصحيح هنا: إضافة encoding وظبط المسافات (Indentation)
with open('biquad_fault_dataset.csv', 'w', newline='', encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile) 
    writer.writerow(header) 
    writer.writerows(rows) 

print(f"CSV file 'biquad_fault_dataset.csv' generated with {len(rows)} rows.") 

# ========== Part 2: ANN AND SVM TRAINING ========== 
df = pd.read_csv('biquad_fault_dataset.csv') 
X = df.drop('Label', axis=1) 
y = df['Label'] 

label_encoder = LabelEncoder() 
y_encoded = label_encoder.fit_transform(y) 

scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 

X_train, X_test, y_train, y_test = train_test_split( 
    X_scaled, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded 
) 

# ANN Model 
ann = MLPClassifier(hidden_layer_sizes=(6,), activation='tanh', solver='adam', max_iter=1000, random_state=1) 
ann.fit(X_train, y_train) 
y_pred_ann = ann.predict(X_test)

# SVM Model 
svm = SVC(kernel='rbf', gamma='scale', C=1.0, random_state=42) 
svm.fit(X_train, y_train) 
y_pred_svm = svm.predict(X_test) 

print('\n[ANN] Accuracy:', accuracy_score(y_test, y_pred_ann)) 
print('[SVM] Accuracy:', accuracy_score(y_test, y_pred_svm))

# ========== Part 3: SAVE RESULTS ========== 
comparison_df = pd.DataFrame({ 
    'Model': ['ANN', 'SVM'], 
    'Test Accuracy': [accuracy_score(y_test, y_pred_ann), accuracy_score(y_test, y_pred_svm)]
}) 
comparison_df.to_csv('model_comparison.csv', index=False) 
print("Results saved successfully.")

# AI-Driven Fault Detection in Biquad Filter Circuits

## 🚀 Overview
This project uses **Artificial Neural Networks (ANN)** and **Support Vector Machines (SVM)** to detect and classify component faults in electronic circuits. Specifically, it targets a **Biquad Active Filter**.

## 🔌 Circuit Design
The circuit is based on the ADTL082 Op-Amp. We simulated a specific fault by changing the value of capacitor **C9** from **1pF** to **0.5nF**.

### Circuit Schematics
* **Normal State:**
![Normal Circuit](normal_circuit.png)
* **Faulty State (C9 Change):**
![Faulty Circuit](faulty_circuit.png)
## 📊 Results
The models were trained on a dataset of 510 samples, covering various fault scenarios:
- **ANN Accuracy:** 99.34%
- **SVM Accuracy:** 91.50%

## 🛠 Libraries Used
- Scikit-learn
- Pandas
- Numpy
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
- ## 🏁 Conclusion & Analysis

The experimental results demonstrate a significant capability of Machine Learning models in identifying hardware degradation and component failures within analog circuits.

### 🧠 Why did ANN outperform SVM?
1. **Non-Linear Complexity:** The Biquad filter's response to component changes (especially in Double Fault scenarios) is highly non-linear. The **Artificial Neural Network (ANN)**, with its hidden layers and **Tanh** activation functions, was better at mapping these complex relationships compared to the SVM's RBF kernel.
2. **Feature Interaction:** ANN inherently captures interactions between different features (F1-F4) more effectively, which is crucial when identifying simultaneous faults (e.g., $R_1$ and $C_1$ failing together).
3. **High Accuracy:** Achieving **99.34%** accuracy confirms that the selected features are highly representative of the circuit's health state.

### 🚀 Future Work
* Integrating real-time data acquisition from physical hardware instead of simulated datasets.
* Testing the model's robustness against thermal noise and component tolerances.

## 🛠 Libraries Used
- Scikit-learn
- Pandas
- Numpy

# 🛡️ AI-Driven Fault Detection in Biquad Filter Circuits ⚡

## 🎥 Results Visualization
![Model Performance & Output](output.png)
*Comparison between simulated circuit output and AI model predictions, showing high precision in fault classification.*

---

## 📝 Project Overview
This project leverages **Artificial Neural Networks (ANN)** and **Support Vector Machines (SVM)** to intelligently detect and classify component faults in electronic circuits. The study focuses on an active **Tow-Thomas Biquad Filter**, analyzing how variations in component values (like $C_9$) affect the circuit's behavioral signatures.

---

## 🔌 Circuit Design & Technical Description
The Biquad filter is a second-order active topology known for its stability. It employs three **ADTL082** Operational Amplifiers:

1.  **Integrator with Loss ($U_1$):** Acts as a summer and a lossy integrator using $R_{31}$ and $C_{10}$.
2.  **Pure Integrator ($U_2$):** Provides the second integration stage using $C_9$.
3.  **Inverting Amplifier ($U_3$):** Provides the necessary $180^\circ$ phase shift for the feedback loop.

### 📐 Mathematical Model
The transfer function $H(s)$ of this system is defined by:

$$H(s) = \frac{V_{out}(s)}{V_{in}(s)} = -\frac{\frac{1}{R_{33} C_{10}} s}{s^2 + \frac{1}{R_{31} C_{10}} s + \frac{1}{R_{32} R_{29} C_{10} C_9}}$$

---

## 🧠 Machine Learning Analysis
We compared the nominal state with specific faulty states to train our models on **510 samples** covering **51 different fault classes**.

### 📊 Performance Summary
| Model | Test Accuracy |
| :--- | :---: |
| **Artificial Neural Network (ANN)** | **99.34%** ✅ |
| **Support Vector Machine (SVM)** | **91.50%** |

### 🖼️ Simulation Comparison
| **Normal State (Healthy)** | **Faulty State ($C_9$ Deviation)** |
| :---: | :---: |
| ![Normal Circuit](normal_circuit.png) | ![Faulty Circuit](faulty_circuit.png) |

---

## 📂 Project Structure
* `faulty_detection_model.py`: Core Python script for dataset generation and ML training.
* `Biquad high-pass filter.asc`: **LTspice** schematic file for circuit simulation.
* `output.png`: Visual results of the filter's output and AI accuracy.
* `biquad_fault_dataset.csv`: The generated synthetic dataset used for training.
* `model_comparison.csv`: Exported accuracy results comparing ANN vs SVM.
* `normal_circuit.png` & `faulty_circuit.png`: Snapshots of the circuit states.
* `requirements.txt`: Python dependencies (`pandas`, `scikit-learn`, `numpy`).

---

## 🚀 How to Run
1.  **Simulation:** Open `Biquad high-pass filter.asc` in **LTspice** to view or modify the circuit.
2.  **AI Model:** * Install dependencies: `pip install -r requirements.txt`.
    * Run the training script: `python faulty_detection_model.py`.

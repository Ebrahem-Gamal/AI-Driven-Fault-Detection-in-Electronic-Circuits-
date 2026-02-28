# AI-Driven Fault Detection in Biquad Filter Circuits 🛡️⚡

## 🚀 Project Overview
This project leverages **Artificial Neural Networks (ANN)** and **Support Vector Machines (SVM)** to intelligently detect and classify component faults in electronic circuits. The study focuses on an active **Biquad Filter**, analyzing how small variations in component values affect the circuit's behavioral features.

---

## 🔌 Circuit Design & Technical Description
The circuit is a **Tow-Thomas Biquad Filter**, a second-order active filter topology known for its stability and low sensitivity to component tolerances. It employs three **ADTL082** Operational Amplifiers:

1.  **Integrator with Loss ($U_1$):** Acts as a summer and a lossy integrator using $R_{31}$ and $C_{10}$.
2.  **Pure Integrator ($U_2$):** Provides the second integration stage using $C_9$.
3.  **Inverting Amplifier ($U_3$):** Provides the necessary $180^\circ$ phase shift for the feedback loop.

### 📐 Mathematical Model
The transfer function $H(s)$ of this Biquad filter is defined by the following second-order equation:

$$H(s) = \frac{V_{out}(s)}{V_{in}(s)} = -\frac{\frac{1}{R_{33} C_{10}} s}{s^2 + \frac{1}{R_{31} C_{10}} s + \frac{1}{R_{32} R_{29} C_{10} C_9}}$$



### 🛠 Fault Simulation & Impact
We compared the nominal state with a specific faulty state to train the AI models:
* **Normal State (Healthy):** $C_9 = 1 \text{ pF}$ (Design target).
* **Faulty State:** $C_9 = 0.5 \text{ nF}$ (Causes a drastic shift in the time constant $\tau = R \cdot C$).

| **Normal State (Healthy)** | **Faulty State ($C_9$ Deviation)** |
| :---: | :---: |
| ![Normal Circuit](normal_circuit.png) | ![Faulty Circuit](faulty_circuit.png) |

---

## 📊 Machine Learning Performance
The models were trained on **510 samples**, covering **51 different fault classes**. The extracted features ($F_1, F_2, F_3, F_4$) represent the circuit's output response signatures (e.g., Amplitude, Phase, and Frequency response).

### Results Summary
| Model | Test Accuracy |
| :--- | :---: |
| **Artificial Neural Network (ANN)** | **99.34%** |
| **Support Vector Machine (SVM)** | **91.50%** |

---

## 🏁 Conclusion & Engineering Analysis
The high accuracy achieved confirms that Machine Learning can effectively automate hardware diagnostics.

### 🧠 Why did ANN outperform SVM?
1.  **Non-Linear Mapping:** The Biquad filter's response to component changes is highly non-linear. The ANN's hidden layers with **$\tanh$** activation functions are superior at capturing these complex patterns.
2.  **Feature Interaction:** ANN inherently learns the interactions between multiple failing components (Double Faults).
3.  **Pole Sensitivity:** Even a small change in $C_9$ alters the denominator of the transfer function, shifting the **complex poles** of the system, which the ANN detects with high precision.

## 🛠 Project Structure
* `faulty_detection_model.py`: Dataset generation and ML training.
* `biquad_fault_dataset.csv`: The generated synthetic dataset.
* `model_comparison.csv`: Exported accuracy results.
* `requirements.txt`: Required libraries (`pandas`, `scikit-learn`, `numpy`).

## 💻 How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Run the model: `python faulty_detection_model.py`.

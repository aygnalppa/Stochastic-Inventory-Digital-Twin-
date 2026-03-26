# 📦 StochasTrack: Digital Twin for Inventory Optimization

A discrete-event simulation and stochastic inventory modeling tool built with Python. 

Traditional inventory models often assume constant demand. However, in the real world, customer demand is highly volatile. This project simulates a supply chain environment by modeling demand as a stochastic process and dynamically calculating safety stocks to prevent stock-outs.

## ⚙️ How It Works

To manage the randomness of the system (Stochastic Demand), we utilize a core principle of Statistics and Probability: the **Additivity of Variance**. 

$$\sigma_L^2 = L \times \sigma_d^2$$

Taking the square root to find the total Standard Deviation ($\sigma_L$) over the lead time explains why the risk does not grow linearly:

$$\sigma_L = \sqrt{L} \times \sigma_d$$

Based on this mathematical reality and the targeted service level (Z-score), the **Safety Stock (SS)** and **Reorder Point (ROP)** are autonomously calculated as follows:

$$SS = Z \times \sigma_d \times \sqrt{L}$$

$$ROP = (d \times L) + SS$$

## 🚀 Features
* **Stochastic Demand Generation:** Uses Poisson distribution for realistic daily sales volume.
* **Dynamic Optimization:** Automatically adjusts inventory policies based on user-defined Service Levels.
* **Discrete-Event Simulation Loop:** A day-by-day "Digital Twin" that tracks inventory depletion and processes shipping delays.
* **Data Visualization:** Generates the classic Inventory Sawtooth Diagram alongside the demand volatility chart.

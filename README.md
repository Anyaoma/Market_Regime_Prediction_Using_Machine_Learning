# Market_Regime_Prediction_Using_Machine_Learning
*This project is influenced by the work of Lucas Inglese on market Regime prediction. This project however, differs interms of data size and the adoption and testing of several models and feature engineering techniques.
The objective of this project is to predict future market regime shifts (e.g., upward, downward using a Directional Change (DC) framework, where the target variable is defined as:

1. 1 (Buy): Predicted upward regime.
2. 0 (Sell): Predicted downward regime.

Key Adjustments for DC Framework; Event Definition:
1. DC Upward Event: Short-term price movement ≥ threshold (e.g., Δ% from trough to peak).
2. DC Downward Event: Short-term price movement ≤ threshold (e.g., Δ% from peak to trough).

![image](https://github.com/user-attachments/assets/b1202b26-4450-4efe-91e5-478e380f8752)

Feature Engineering was applied to the data. Below are the 
![image](https://github.com/user-attachments/assets/15d14179-2694-48f3-b951-dfb6d1ef17d9)

# Market_Regime_Prediction_Using_Machine_Learning
*This project is influenced by the work of Lucas Inglese on market Regime prediction. This project however, differs in terms of data size and the adoption & testing of several models and feature engineering techniques.

The objective of this project is to predict future market regime shifts (e.g., upward, downward using a Directional Change (DC) framework, where the target variable is defined as:

1. 1 (Buy): Predicted upward regime.
2. 0 (Sell): Predicted downward regime.

Key Adjustments for DC Framework; Event Definition:
1. DC Upward Event: Short-term price movement ≥ threshold (e.g., Δ% from trough to peak).
2. DC Downward Event: Short-term price movement ≤ threshold (e.g., Δ% from peak to trough).

The selection of data used in this analysis include; EUR_USD, GBP_USD, USD_JPY (2015 - 2023). The EUR_USD data was first analysed to get an insight into what the data was like. 

Feature Engineering: lagged log returns and lagged rolling autocorrelation values in the farthest past showed higher autocorelation with the response variable than the lagged variables in the recent past, hence there was a shift from [1,5,10...] to [20, 40, 60....] spaced lags to avoid multicollinearity. 

![image](https://github.com/user-attachments/assets/b1202b26-4450-4efe-91e5-478e380f8752)

The correlation matrix of the engineered features depicts multicollinearity among the volatility, and RSI variables.

![image](https://github.com/user-attachments/assets/15d14179-2694-48f3-b951-dfb6d1ef17d9)

Univariate analysis of the engineered features dipicted a mix of skewed and normal distribution
![image](https://github.com/user-attachments/assets/4a36cf92-af08-408b-988d-ffb596577446)

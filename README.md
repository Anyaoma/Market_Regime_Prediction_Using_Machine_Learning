# Market_Regime_Prediction_Using_Machine_Learning
*This project is influenced by the work of Lucas Inglese on market Regime prediction. This project however, differs in terms of data size and the adoption & testing of several models and feature engineering techniques.

The objective of this project is to predict future market regime shifts (e.g., upward, downward using a Directional Change (DC) framework, where the target variable is defined as:

1. 1 (Buy): Predicted upward regime.
2. 0 (Sell): Predicted downward regime.

Key Adjustments for DC Framework; Event Definition:
1. DC Upward Event: Short-term price movement ≥ threshold (e.g., Δ% from trough to peak).
2. DC Downward Event: Short-term price movement ≤ threshold (e.g., Δ% from peak to trough).

The selection of data used in this analysis include; EUR_USD, GBP_USD, USD_JPY (2015 - 2023). The EUR_USD data was first analysed to get an insight into what the data was like. 

![image](https://github.com/user-attachments/assets/b1202b26-4450-4efe-91e5-478e380f8752)

Feature Engineering: lagged log returns and lagged rolling autocorrelation values in the farthest past showed higher autocorelation with the response variable than the lagged variables in the recent past, hence there was a shift from [1,5,10...] to [20, 40, 60....] spaced lags to avoid multicollinearity. 
* Still the correlation matrix of the engineered features depicts multicollinearity among the volatility, and RSI features.

![image](https://github.com/user-attachments/assets/15d14179-2694-48f3-b951-dfb6d1ef17d9)


To reduce the issue of multicollinearity and retain more predictive individual variable, the PCA was applied to the volatility and RSI variable sets, thus resulting in singularised predictors:
![image](https://github.com/user-attachments/assets/8c91147d-bcb5-4f62-b0eb-44f241a3300f)

![image](https://github.com/user-attachments/assets/79916861-a33c-44f4-8fe1-bdb99a921f71)

The above activities reduced the predictor set and produced a defined predictor space:
![image](https://github.com/user-attachments/assets/40e7c67b-8e30-4bdf-a2c4-bed203739843)


To obtain a robust model, the three asset EUR_USD, GBP_USD and USD_JPY was combined to generate a larger data size. Below is the correlation matrix across the assets:
![image](https://github.com/user-attachments/assets/e5cb3778-9b78-456d-8dc0-8a71d83defaf)


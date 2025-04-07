import numpy as np


def dc_event(Pt, Pext, threshold):
    """
    Compute if we have a POTENTIAL DC event
    """
    var = (Pt - Pext) / Pext

    if threshold <= var:
        dc = 1
    elif var <= -threshold:
        dc = -1
    else:
        dc = 0

    return dc


def calculate_dc(df, threshold):
    """
    Compute the start and the end of a DC event
    """

    # Initialize lists to store DC and OS events
    dc_events_up = []
    dc_events_down = []
    dc_events = []
    os_events = []

    # Initialize the first DC event
    last_dc_price = df["close"][0]
    last_dc_direction = 0  # +1 for up, -1 for down

    # Initialize the current Min & Max for the OS events
    min_price = last_dc_price
    max_price = last_dc_price
    idx_min = 0
    idx_max = 0


    # Iterate over the price list
    for i, current_price in enumerate(df["close"]):

        # Update min & max prices
        try:
            max_price = df["high"].iloc[dc_events[-1][-1]:i].max()
            min_price = df["low"].iloc[dc_events[-1][-1]:i].min()
            idx_min = df["high"].iloc[dc_events[-1][-1]:i].idxmin()
            idx_max = df["low"].iloc[dc_events[-1][-1]:i].idxmax()
        except Exception as e:
            pass
            #print(e, dc_events, i)
            #print("We are computing the first DC")

        # Calculate the price change in percentage
        dc_price_min = dc_event(current_price, min_price, threshold)
        dc_price_max = dc_event(current_price, max_price, threshold)


        # Add the DC event with the right index IF we are in the opposite way
        # Because if we are in the same way, we just increase the OS event size
        if (last_dc_direction!=1) & (dc_price_min==1):
            dc_events_up.append([idx_min, i])
            dc_events.append([idx_min, i])
            last_dc_direction = 1

        elif (last_dc_direction!=-1) & (dc_price_max==-1):
            dc_events_down.append([idx_max, i])
            dc_events.append([idx_max, i])
            last_dc_direction = -1

    return dc_events_up, dc_events_down, dc_events


def calculate_future_trend(dc_events_down, dc_events_up, df):
    """
    Compute the DC + OS period (trend) using the DC event lists
    """

    #Initialize the variables
    trend_events_up = []
    trend_events_down = []

    # Verify which event occured first (upward or downward movement)

    # If the first event is a downward event
    if dc_events_down[0][0]==0:

        # Iterate on the index
        for i in range(len(dc_events_down)+1):

            try:

                # Calculate the start and end for each trend
                trend_events_up.append([dc_events_up[i][0], dc_events_down[i+1][0]])
                trend_events_down.append([dc_events_down[i][0], dc_events_up[i][0]])
            except Exception as e:
                pass

    # If the first event is a upward event
    elif dc_events_up[0][0]==0:

        # Iterate on the index
        for i in range(len(dc_events_up)+1):

            try:
                # Calculate the start and end for each trend
                trend_events_up.append([dc_events_up[i][0], dc_events_down[i][0]])
                trend_events_down.append([dc_events_down[i][0], dc_events_up[i+1][0]])
            except Exception as e:
                pass

    return trend_events_down, trend_events_up


def future_DC_market_regime(df, threshold):
    """
    Determines the market regime based on Directional Change (DC) and trend events.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        A DataFrame containing financial data. The DataFrame should contain a 'close' column 
        with the closing prices, and 'high' and 'low' columns for high and low prices.
    
    threshold : float
        The percentage threshold for DC events.
    
    Returns:
    --------
    df_copy : pandas.DataFrame
        A new DataFrame containing the original data and a new column "market_regime", 
        which indicates the market regime at each timestamp. A value of 1 indicates 
        an upward trend, and a value of 0 indicates a downward trend.
        
    """
    df_copy = df.copy()
    
    # Extract DC and Trend events
    dc_events_up, dc_events_down, dc_events = calculate_dc(df_copy, threshold=threshold)
    trend_events_down, trend_events_up = calculate_future_trend(dc_events_down, dc_events_up, df_copy)
    
    df_copy["future_market_regime"] = np.nan
    for event_up in trend_events_up:
        df_copy.loc[event_up[0], "future_market_regime"] = 0

    for event_down in trend_events_down:
        df_copy.loc[event_down[0], "future_market_regime"] = 1

    df_copy["future_market_regime"] = df_copy["future_market_regime"].fillna(method="ffill")
    
    return df_copy

def future_returns(df,N):
    df_copy = df.copy()
    df_copy["log_close"] = np.log(df_copy["close"])
    df_copy["fut_ret"] = (df_copy["log_close"].shift(-N) - df_copy["log_close"]) / df_copy["log_close"]
    return df_copy

def get_dc_price(dc_events, df):
    dc_events_prices = []
    for event in dc_events:
        prices = [df["close"].iloc[event[0]], df["close"].iloc[event[1]]]
        dc_events_prices.append(prices)
    return dc_events_prices
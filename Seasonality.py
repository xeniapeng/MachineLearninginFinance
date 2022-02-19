import pandas as pd
import pandas_datareader as pdr

spy = pdr.get_data_yahoo("SPY")

spy.plot()

spy["Adj Close"].plot()
spy.describe()

ret = spy.pct_change()
ret.describe()
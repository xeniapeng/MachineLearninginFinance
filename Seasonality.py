import pandas as pd
import yfinance as yf

spy = yf.download("QQQ")
print(spy)
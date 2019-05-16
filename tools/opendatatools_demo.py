"""https://github.com/PKUJohnson/OpenData"""
from opendatatools import stock
df, msg = stock.get_quote('600000.SH,000002.SZ')
print(df)
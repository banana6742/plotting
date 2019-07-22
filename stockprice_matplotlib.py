import numpy as np
import matplotlib.pyplot as plt
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

stock_price_url='https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(stock_price_url).read().decode()
stock_data = []
split_source = source_code.split('\n')

for line in split_source:
    split_line = line.split(',')
    if len(split_line) == 7:
        if 'Date' not in line:
            stock_data.append(line)

data,open,high,low,close,Adjusted_close,Volume = np.loadtxt(stock_data,delimiter=',',unpack=True,converters={0:bytespdate2num('%Y-%m-%d')})

plt.plot_date(date,close,'-',label='Price')
plt.legend()
plt.show()
import pandas_datareader.data as web
import datetime

now = datetime.datetime.now()
start = datetime.datetime(now.year-1, now.month, now.day)
end = datetime.datetime(now.year, now.month, now.day)

stocks = ['AMNF', 'WWAV', 'NYT']
g=web.DataReader(stocks, 'yahoo', start, end)

h = g['Close']

print("")
print("Statistics for WWAV")
print("Annual Average =", + sum(h.WWAV) / len(h.WWAV))
print ("Last close:", h.WWAV[-1])
print ("Year ago close:", h.WWAV[0])
print ("Change from previous close", (h.WWAV[-1]-h.WWAV[-2]))
print ("")
print("Statistics for AMNF")
print("Annual Average =", + sum(h.AMNF) / len(h.AMNF))
print ("Last close:", h.AMNF[-1])
print ("Year ago close:", h.AMNF[0])
print ("Change from previous close", (h.AMNF[-1]-h.AMNF[-2]))
print ("")

import csv
from datetime import datetime
path="c:\git\csvfile\TSLA.csv"
file=open(path, newline='')
reader = csv.reader(file)

header = next(reader)  #the file header

data = []
for row in reader:
    #row = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    #Date, Open, High, Low, Close, Adj
    #Close, Volume
    #08 / 11 / 2017, 356.970001, 361.26001, 353.619995, 357.869995, 357.869995, 4365800
    #day = datetime.strptime('{0}/{1}/{2}'.format(M, D, Y), '%m/%d/%Y').strftime('%A')
    date = datetime.strptime(row[0], '%m/%d/%Y')
    #open_price = float(row[1])
    #high = float(row[2])
    #low = float(row[3])
    #close = float(row[4])
    #adj_close = float (row[5])
    #volume = int(row[6])
print(data[0])





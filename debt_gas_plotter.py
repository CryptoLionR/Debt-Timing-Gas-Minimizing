'''
Purpose: Find the best time of day to take out new loans based on past data
'''

#imports
import urllib.request as rq
import json
import time
from matplotlib import pyplot as plt

#inits
timezone_offset = time.timezone/3600
gasprice = []
gasfees = []
times = []
url = 'https://api.flipsidecrypto.com/api/v2/queries/942dc3cf-a561-4d3d-a310-89dc0f225d6a/data/latest'

try:
    dataset = rq.urlopen(url)
    dataset = dataset.read()
    dataset = json.loads(dataset)
except Exception as e:
    print('Unable to get data from flipsidecrypto API. Check the URL below: \n{}'.format(url))

#simplify hour values *note HOURS in UTC
for i,item in enumerate(dataset):
    dataset[i]['HOUR'] = ':'.join(item['HOUR'].replace('T',',').rsplit(':')[0:2])

#sort ascending hours
dataset = sorted(dataset,key=lambda hour: hour['HOUR'])

#create series
for elem in dataset:
    gasfees.append(elem['AVERAGE_GASFEES'])
    gasprice.append(elem['AVERAGE_GASPRICE'])
    times.append(elem['HOUR'])

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.bar(times,gasfees)
ax1.set_ylabel('Average Gas Fees Paid (USD)')

ax2.plot(times,gasprice,color='r')
ax2.set_ylabel('Gas Price',color='r')

ax1.set_xlabel('7 Day Period')
ax1.set_xticks('')

plt.title('Average Gas Fees to Mint/Borrow alUSD by Hour Over 7 Days')
plt.tight_layout()
plt.show()
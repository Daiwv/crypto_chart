"""
A simple example of an animated plot
"""
import time
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from collections import deque

marketName = "BTC-ETH"

n = 450

r = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=" + marketName)

data = r.json()
res = data["result"]

x = [0] * n
y_bid = [res['Bid']] * n
y_ask = [res['Ask']] * n




fig, ax = plt.subplots()

def refreshData(i):
	r = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=" + marketName)

	data = r.json()
	res = data["result"]

	# print('Bid : {0}, Ask : {1}'.format(res['Bid'], res['Ask']))

	x.append(time.clock())
	x.pop(0)

	y_bid.append(res['Bid'])
	y_bid.pop(0)

	y_ask.append(res['Ask'])
	y_ask.pop(0)


	
	obj = ax

	obj.clear()
	# obj.plot(x0, y0, '--m', lw=2, label='$ Analytical 2 $')
	# obj.plot(x0, y0, '-k', lw=2, label='$ Analytical $')
	# obj.plot(x1, y1, '--', color='black', marker='o',
	#          lw=0.1, ms=8, mew=0, label='$ EMA $')
	# obj.plot(x2, y2, '-', color='red', marker='o',
	#          lw=2, ms=0, mew=0, label='$ EEA $')
	obj.plot(x, y_bid, '--', color='#0099FF', marker='o',
		   lw=1, ms=4, mew=0, label='$ Bid $')
	obj.plot(x, y_ask, '--', color='#FF5B00', marker='o',
		   lw=1, ms=4, mew=0, label='$ Ask $')
	# obj.plot([0, 0.0001],[2.3124e+06,2.3124e+06], '--', color='#FF5B00', marker='o',
	#          lw=2, ms=8, mew=0, label='$ Analytical $')
	# obj.plot(x4, y4, '--', color='#FF5B00', marker='o',
	#          lw=0.1, ms=6, mew=2, mfc='None', label='$ ROM $')
	# for l in obj.lines:
	#     l.set_alpha(.7)

	# obj.grid(which='major', linestyle="-", color='#444444',
	# 	   axis='both', zorder=0, linewidth=0.15)
	# obj.set_ylim([min(y_bid) - 0.01*min(y_bid), max(y_ask) + 0.01*max(y_ask)])
	obj.set_yticks(np.arange(min(y_bid), max(y_ask), abs(max(y_ask) - min(y_bid))/10))
	# obj.set_xlim([0, 0.05])
	obj.set_xlim([x[-1] - n/2, x[-1]])
	# obj.set_xticks(np.arange(0, 0.8, 0.1))

	# obj.set_ylabel("$\sigma_{11}, Pa$", fontsize=_fontsize, rotation=0, labelpad=0)
	# obj.yaxis.set_label_coords(-0.08, 0.5)
	# obj.set_xlabel("$r$, $cm$", fontsize=_fontsize)
	# obj.axhline(0, color='black', lw=1)

	obj.set_title(marketName)
	obj.legend()
	

	# ax = obj

	return obj
# Init only required for blitting to give a clean slate.

ani = animation.FuncAnimation(fig, refreshData, interval=2000)

plt.tight_layout()
plt.show()



# n = 5

# x = [0] * n
# y_bid = [0] * n
# y_ask = [0] * n

# # pop(0) and insert(0, v)

# while time.clock() < 5:
# 	r = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=BTC-WAVES")

# 	data = r.json()
# 	res = data["result"]

# 	print('Bid : {0}, Ask : {1}'.format(res['Bid'], res['Ask']))

# 	x.append(time.clock())
# 	x.pop(0)


# 	print(x)
# 	print(len(x))
# 	# print(y_bid)
# 	# print(y_ask)

# 	time.sleep(1)



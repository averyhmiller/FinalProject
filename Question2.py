import statistics
import matplotlib.pyplot as plt 
import numpy as np 
f = open("APPL.txt", "r")
listItems = f.read().splitlines()
prices=list(map(float,listItems))

x = np.arange(len(prices))
y = prices
  
plt.plot(x, y) 
plt.xlabel("Day") 
plt.ylabel("Trading price") 
plt.title("Apple Stock Price, Nov 2019 to Nov 2020") 
plt.show() 
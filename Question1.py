import statistics
f = open("APPL.txt", "r")
listItems = f.read().splitlines()
prices=list(map(float,listItems))
print(statistics.mean(prices))
print(statistics.stdev(prices))
x = [500, 1000, 1250, 175, 800, 120]
total = sum(x)
print("total espend :" , total)

x.sort()
print("greatest expense is:", x[-1]) 

x.sort()
print("cheapest spending is:", *x[:1]) 

avg = sum(x)/len(x)
print("The average is ", round(avg,2))
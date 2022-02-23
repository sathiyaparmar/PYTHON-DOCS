"""
Find the lowest distance between these
"""
series1 = [0,1,2,3,4]
series2 = [-1,2,0,0,0]

dist0 = abs(series1[0] - series2[0])
dist1 = abs(series1[1] - series2[1])
dist2 = abs(series1[2] - series2[2])
dist3 = abs(series1[3] - series2[3])

print(dist0,dist1,dist2,dist3)

lowest = min([dist0,dist1,dist2,dist3])
print(lowest)
sentiment=[2.3, 4.8, 9.5, 5.5, 1.4]
distance=[5, 7, 8, 10, 12]
optimumpath= []
def OptimizedPath(sentiment,distance):
  for i in range(5):
      for j in range(5):
          optimumpath.append=(sentiment[i]+distance[j])
  return optimumpath
for i in range(5):
 print(str(optimumpath[i]),end=" ")




import pdb

pdb.set_trace()

lista=[[1,2,3,4,5],[3,7,10,200],[20,10,1,0,2]]
maximos=[]

maximos = list(map(lambda x: max(x), lista))

print(maximos)
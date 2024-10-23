def simple_maths(x,y,z):
    return (x**y)/z
L1=[12,4,10]
L2=[12,4,9]
L3=[12,4,5]
mapfuncit_return= print(list(map(simple_maths,L1,L2,L3)))
Uselabda=print(list(map(lambda  x,y,z :(x**y)/z , L1,L2,L3)))
from collections import ChainMap

dic1 = {'a' : 1, 'b' : 2}
dic2 = {'c' : 1, 'b' : 4}

chain_map = ChainMap(dic1, dic2)
print(chain_map)
print(chain_map.maps)

print(chain_map['a'])
print(chain_map['b'])

chain_map['b'] = 6
print(chain_map.maps)

print(chain_map.keys())
print(chain_map.values())

print(list(chain_map.keys()))
print(list(chain_map.values()))

dict3 = {'e' : 8, 'f' : 10}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map.maps)


list1 = ["Hola bebe", 12312e+13, "lol",'no puede ser']
list2 = ('2',3,'4','2')
list3:int = (1,3)

list1.append('hola')
list1.extend(list3)
print(list2.index('2',1,4))

list1.remove('lol')
list1.pop()
list1.insert(3,'abc')
print(list2.count('2'))
print(list2,list1,list3)

list1.clear()


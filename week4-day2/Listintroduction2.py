ListA = ["Apple" , "Avocado" , "Blueberries" , "Durian" , "Lychee"]
ListB = ["Apple" ,"Avocado" , "Blueberries" , "Durian" , "Lychee"]
print(ListA[3])
ListB.remove("Durian")
print('Updated ListB : ', ListB)

ListA.append("Kiwifruit")
print(ListA)

if len(ListA) == len(ListB):
    print("the lenght of ListA and ListB are the same")
else: 
        print ("the lenght of ListA and ListB are not the same")


index = ListA.index('Avocado')
print('The index of Avocado:', index)


index = ListA.index('Durian')
print('The index of Durian:', index)

ListC = ["Passion Fruit" , "Pomelo"]
ListB = ListC + ListB
print(ListB)

print(ListA[2])

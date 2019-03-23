

nutrientList = ['orange', 'topango',' Topatoe']

nl1 = ['beach', 'strong', 'touchy']
nv1 = [11, 12, 13]

nl2 = ['beach', 'strong', 'touchy']
nv2 = [14, 15, 16]

nl3 = ['beach', 'strong', 'touchy']
nv3 = [17, 18, 19]


foodList = []
for item in nutrientList:
    name = item
    nutrients = dict([])
    for i in range(len(nl1)):
        nutrients[nl1[i]] = nv1[i]
    foodList.append([name, nutrients])


for item in foodList:
    print(item)

print(foodList[1][1]['strong'])
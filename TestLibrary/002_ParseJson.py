
from requests import get
import json

# Make our web call
url = 'https://api.nal.usda.gov/ndb/reports/?ndbno=11090&type=f&format=json&api_key=swc6iwKitEP0BtugYQn8Wo4nwWtn4uHrMDQWpxTc'
response = get(url)
response = response.text

#print(response)

# Encode it in json
raw_json = json.loads(str(response).encode("utf-8"))
#print(raw_json)



def looper(inputs):
    try:
        for item in inputs:
            print(str(item), str(inputs[item]))
            #print(inputs[item])
            looper(inputs[item])
    except:
        print("Found the bottom")


#looper(raw_json)
#['report']['food']['ru']
#print(raw_json['report']['food']['ru'])

report = raw_json['report']
food  = raw_json['report']['food']
nutrients = raw_json['report']['food']['nutrients']         #This is a list of nutrients, must traverese for informaiton
for item in nutrients:
    print(item['name'], item['value'], item['unit'])


#nutrientZero = nutrients[0]



#for item in nutrientZero:
#    print(str(item), str(nutrientZero[item]))

#for item in nutrientZero['measures']:
#    print(item)

#print (nutrientZero["value"])
#for item in nutrientZero['value']:
#    print(item)


#name
#nutrient_id
#value
#unit



#ofInterest = nutrients




#for item in ofInterest:
    #print(item['name'])
    #print(item, ofInterest[item])
    #print(food[item])
    #print (item)
    #for element in item:
    #    print (element)












#for line in raw_json:
#    print(raw_json[line])




'''

print("Raw Json : ", raw_json)
# Grab the inital keys and store them in a list

keys_1 = []
for line in raw_json:
    keys_1.append(line)
    # print(raw_json[line])
# print the first 4 keys
# print(keys_1)
# print(raw_json['count'])

# We only really want element 2 in this list [count, notfound, foods, api vrs]
foods = raw_json['foods']

for food in foods:
    print
    "yehaw"
    # food = food[1] #returned foods are stored in a list
    food = food["food"]  # food happens to be the key to food
    # print ("Food : ",food)

    ### Food Decode : [sr, sources, langual, nutrients, footnotes, type, desc]
    nutrients = food['nutrients']
    description = food['desc']

    We want nutrients, and 'desc'ription
    keys_2 = []
    for item in food:    #
        keys_2.append(item)
        #print item
    #nutrients = food[keys_2[3]]
    #description = food[keys_2[6]]

    ### Description Decode : [ru, manu, cn, ndbno, cf, nf, rd, r, pf, sn, ff, fg, sd, ds, name]
    f_refuse = description['r']  ### Amount of Refuse in a food
    f_name = description['name']  ### Name of the food
    f_id = description['ndbno']  ### Food Ndbno ID #
    print
    "Food Refuse% : ", f_refuse
    print
    "Food Name : ", f_name
    print
    "Food ID : ", f_id
    for line in description:
        print line

    food_list = []

    f_nutrient_list = getNutrients(nutrients)

food_list.append([f_name, id, f_refuse, f_nutrient_list])
'''




from requests import get
import json




targetFoods = [
    ['11090', "Broccoli, raw"],
    ['11286', "Onions, yellow, sauteed"],
    ['11267', "Mushrooms, shiitake, stir-fried"],
    ['11921', "Peppers, sweet, red, sautee"],
    ['11215', "Garlic, raw"],
    ['11439', "Sauerkraut, canned, solids and liquids"],
    ['04584', "Oil, sunflower, high oleic"],
    ['11097', "Broccoli raab, cooked"],
    ['11125', "Carrots, cooked, boiled, drained, without salt"],
    ['02010', "Spices, cinnamon, ground"],
    ['45136753', "SILK, ORGANIC SOYMILK, UNSWEETENED, UPC: 025293001060"],
    ['45310616', "GMILLS CHEERIOS CEREAL RTE, UNPREPARED, GTIN: 00016000275263"],
    ['45171403', "KROGER, NUTTY NUGGETS, CRUNCHY WHEAT & BARLEY CEREAL, UPC: 011110878243"]
]

# Make our web call
# IN : NDBO Number
# OUT : API Text callback for that food
def getWebcall(foodNDBO):
    url = 'https://api.nal.usda.gov/ndb/reports/?ndbno=' + foodNDBO + '&type=f&format=json&api_key=swc6iwKitEP0BtugYQn8Wo4nwWtn4uHrMDQWpxTc'
    response = get(url)
    response = response.text
    return response



# Grab Nutrients in a food
# IN : Raw Json of a food
# OUT : List of comma seperated nutrient values
def getNutrients(raw_json):
    nutrients = raw_json['report']['food']['nutrients']
    nutrientCSV = ''
    print("This food has : " + str(len(nutrients)) + " Nutrients")
    for nutrient in nutrients:
        # Really should just convert everything to Grams or L here...
        value = nutrient['value']
        name = nutrient['name']
        nutrientCSV += str(value) + ', '

    return nutrientCSV


# Grab Food in our list
masterFoodList = []
hackJson = ''

for item in targetFoods:
    response = getWebcall(item[0])      # This is because we are only using the NDBO number at the start of the target foods list. May need to modify this later
    raw_json = json.loads(str(response).encode("utf-8"))
    name = raw_json['report']['food']['name']
    nutrientBreakdown = getNutrients(raw_json)
    filename = str(str(item[0]) + '.txt')
    file = open(filename, 'w')
    file.write(response)
    file.close()
    hackJson = raw_json

    masterFoodList.append([item[0], name, nutrientBreakdown])

#Hack getting our Header String aka Nutrient Names
HeaderString = ''
nutrients = raw_json['report']['food']['nutrients']
for item in nutrients:
    name = str(item['name'])
    #value = str(item['value'])
    #col_width = len(name) + 2
    HeaderString += name + ', '
    #ValueString +=  ' '*(col_width - len(value)) + value + ', '

#Print it Out!
#print(HeaderString)
#for food in masterFoodList:
#    print(food)



#print(response)



''''# Encode it in json
raw_json = json.loads(str(response).encode("utf-8"))
#print(raw_json)

report = raw_json['report']
food  = raw_json['report']['food']
nutrients = raw_json['report']['food']['nutrients']         #This is a list of nutrients, must traverese for informaiton

HeaderString = ''
ValueString = ''

#col_width = max(len(word) for row in nutrients for word in row) + 2
for item in nutrients:
    name = str(item['name'])
    value = str(item['value'])
    col_width = len(name) + 2
    HeaderString +=   ' '*(col_width - len(name)) + name + ', '
    ValueString +=  ' '*(col_width - len(value)) + value + ', '

print(HeaderString)
print(ValueString)

'''








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



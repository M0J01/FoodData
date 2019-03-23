
from requests import get
import json

## Grab name for food
## Grab List of nutrients and values for each food
## Store name, and nutrient list, for each food in Dict


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
    nutrienList = []
    nutrientDict = dict([])
    for nutrient in nutrients:
        # Really should just convert everything to Grams or L here...
        value = nutrient['value']
        name = nutrient['name']
        nutrientDict[name] = value
        #nutrienList.append([name, value])
    #return nutrienList
    return nutrientDict


# Grab Food in our list
foodList = []
hackJson = ''

foodDict = dict([])

for item in targetFoods:
    response = getWebcall(item[0])      # This is because we are only using the NDBO number at the start of the target foods list. May need to modify this later
    raw_json = json.loads(str(response).encode("utf-8"))
    name = raw_json['report']['food']['name']
    nutrientBreakdown = getNutrients(raw_json)
    foodDict[name] = nutrientBreakdown

for item in foodDict:
    print(item)

    try:
        print(foodDict[item])
        print(foodDict[item]['Energy'])
        print(foodDict[item]['Vitamin B-6'])
    except:
        print ("that nutrient not in here")



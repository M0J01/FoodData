'''
Your API Key : oPreJHk0bkg7qxGyWAymXmeHIigGf2SXGTKRBnlV


example API call

https://api.data.gov/nrel/alt-fuel-stations/v1/nearest.json?api_key=oPreJHk0bkg7qxGyWAymXmeHIigGf2SXGTKRBnlV&location=Denver+CO


==Foods

Onions : Sauteed
Mushrooms : Shitake : Sauted
Yellow Pepper : Sauted
Red Pepper : Sauted
Garlic : Sauted
SaurKraut : Sauted
Sunflower Oil : For cooking
Broccoli : Steamed
Carrots : Steamed
Cinamon

Silk Unsweetened Soymilk - By hand if necissary
Gardein Chick'n - by hand if necissary
Cheerios - by hand if necissary
Nutty Nuggets - by hand if necissary

== Nutrient Requirments

Vitamins
Minerals
Daily Amount

11286, Onions, yellow, sauteed
11267, Mushrooms, shiitake, stir-fried
-Yellow Pepper
11921, Peppers, sweet, red, sauteed
11215, Garlic, raw
11439, Sauerkraut, canned, solids and liquids
04584, Oil, sunflower, high oleic
11097, Broccoli raab, cooked
11125, Carrots, cooked, boiled, drained, without salt
02010, Spices, cinnamon, ground

45136753, SILK, ORGANIC SOYMILK, UNSWEETENED, UPC: 025293001060
- Gardein Chick'n Strips
45310616, GMILLS CHEERIOS CEREAL RTE, UNPREPARED, GTIN: 00016000275263
45171403, KROGER, NUTTY NUGGETS, CRUNCHY WHEAT & BARLEY CEREAL, UPC: 011110878243


== Nutrient Calc

Food Item * serving
Sum Nutrient values
Report nutrient value totals compared to Daily amount (Body Weight Calculator, Activity Calculator)



Full report
'''

import mechanize
import cookielib
import re
import json
from time import sleep


# import mechanize
# import cookielib
def get_webpage(url):
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    try:
        r = br.open(url)
        htmltextz = r.read()

    except:
        print(url)
        htmltextz = '0'

    return (htmltextz)


### IN : Nutrient's list in Dictionary Form
### Out : Nutrient list in list form
def getNutrients(nutrients):
    nutrient_list = []
    for nutrient in nutrients:
        srccode = nutrient['sourcecode']  ###IDK
        derivation = nutrient['derivation']
        measures = nutrient['measures']  ### [eunit, g, eqv, qty, value, label, cup chopped]
        dp = nutrient['dp']  ###IDK
        se = nutrient['se']
        group = nutrient['group']
        name = nutrient['name']
        nut_id = nutrient['nutrient_id']
        value = nutrient['value']
        unit = nutrient['unit']
        # print "source code : ", srccode
        # print "derivation : ", derivation
        # print "measures : ", measures[0]['eunit']       ### 100 food grams
        # print "dp : ", dp           ###IDK
        # print "se : ", se           ###IDK
        # print "group : ", group        ### How is it measured?
        ###
        # print "name : ", name
        # print "nutrient id : ", nut_id
        # print "value : ", value  ### Value per 100g
        # print "unit : ", unit  ### Value
        current_nutrient = [name, nut_id, value, unit]
        nutrient_list.append(current_nutrient)
    return nutrient_list


# Itterate through the Food DB numbers


# Access DB for given food


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

# - Gardein Chick'n Strips
# Yellow Onions, Sauteed
# Navitas Cacao powder


for item in targetFoods:
    print
    item[0]

url_example = "https://api.nal.usda.gov/ndb/V2/reports?ndbno=01009&ndbno=45202763&ndbno=35193&type=f&format=json&api_key=DEMO_KEY"
url_start = "https://api.nal.usda.gov/ndb/V2/reports?ndbno="
url_next = "&ndbno="
url_end = "&type=f&format=json&api_key=oPreJHk0bkg7qxGyWAymXmeHIigGf2SXGTKRBnlV"

url_full = url_start + str(targetFoods[0][0])

###     Construct https link
for i in targetFoods[1:3]:
    url_full += url_next + str(i[0])
url_full += url_end
print
url_full

### Grab Web info and store in Json
web_json = get_webpage(url_full)
raw_json = json.loads(str(web_json).encode("utf-8"))
raw_json = raw_json
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
    '''
    We want nutrients, and 'desc'ription
    keys_2 = []
    for item in food:    #
        keys_2.append(item)
        #print item
    #nutrients = food[keys_2[3]]
    #description = food[keys_2[6]]
    '''

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
    '''
    for line in description:
        print line
    '''

    food_list = []

    f_nutrient_list = getNutrients(nutrients)

food_list.append([f_name, id, f_refuse, f_nutrient_list])

'''
### For nutrient in nutrient list
for nutrient in nutrients[0:1]:
    ### Nutrient Decode : [group, name, nutrient_id, measures, value, dp, sourcecode, se, unit, derivation]
    group = nutrient['group']
    name = nutrient['name']
    nut_id = nutrient['nutrient_id']
    measures = nutrient['measures']     ### [eunit, g, eqv, qty, value, label, cup chopped]
    value = nutrient['value']
    dp = nutrient['dp']                 ###IDK
    srccode = nutrient['sourcecode']    ###IDK
    se = nutrient['se']
    unit = nutrient['unit']
    derivation = nutrient['derivation']

    #print "source code : ", srccode
    #print "derivation : ", derivation
    #print "measures : ", measures[0]['eunit']       ### 100 food grams
    ###print "dp : ", dp           ###IDK
    ###print "se : ", se           ###IDK
    #print "group : ", group        ### How is it measured?

    print "name : ", name
    print "nutrient id : ", nut_id
    print "value : ", value     ### Value per 100g
    print "unit : ", unit       ### Value
    '''
import csv

with open('Food_Carbon_Emissions.csv', mode='r') as file1:
    reader=csv.reader(file1)
    food_carbon=list(reader)

food_carbon[1:]

def get_carbon(food_present):
    res={}
    results=[]
    for line in food_carbon[1:]:
        if line[0]==food_present:
            co2_per_serving=float(line[5])
            co2_per_gram=float(line[5])/float(line[2])
            results=results+[food_present.capitalize(),co2_per_serving,co2_per_gram]
            res['name'] = results[0]
            res['co2_per_serving'] = results[1]
            res['co2_per_gram'] = results[2]
    return res

def cfp_output(food):
    carbon_footprint = get_carbon(food.upper())
    return carbon_footprint

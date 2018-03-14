def city_country(city, country, population=""):
    if population:
        msg = city + ", " + country + " - population " + str(population)
    else: 
        msg = city + ", " + country
        
    return msg.title()
def make_car(manufacturer, model, **options):
    car_dict = {}
    car_dict['manufacturer'] = manufacturer.title()
    car_dict['modle'] = model.title()

    for key, value in options.items():
        car_dict[key] = value
    
    return car_dict

car = make_car('subaru', 'outback', color='bule', tow_package=True)
print("The car info: ")
print(car)

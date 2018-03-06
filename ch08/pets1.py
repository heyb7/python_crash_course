def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")

describe_pet(pet_name='willie')
describe_pet("willie")

describe_pet(pet_name="harry", animal_type='hamster')
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name="harry")
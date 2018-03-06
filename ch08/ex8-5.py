def describe_city(city, country="china"):
    """描述城市"""
    print("\n" + city + " is in " + country + ".")

describe_city("beijing")
describe_city("shanghai")

describe_city(city="reykjavik", country="iceland")
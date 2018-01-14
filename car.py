class Car:

    def __init__(self, price, advert_name, advert_description, milliage, year, engine_size, transmission, fuel_type,
                 thumbnail='', link_to_the_advert=''):
        self.price = price
        self.advert_name = advert_name
        self.advert_description = advert_description
        self.milliage = milliage
        self.year = year
        self.engine_size = engine_size
        self.transmission = transmission
        self.thumbnail = thumbnail
        self.link_to_the_advert = link_to_the_advert
        self.fuel_type = fuel_type

class Address:
    def __init__(self, street: str, city: str, zip_code: str, country: str = "USA"):
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country
        self.latitude = None
        self.longitude = None

    def get_full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.zip_code}, {self.country}"

    def set_coordinates(self, lat: float, lng: float):
        self.latitude = lat
        self.longitude = lng
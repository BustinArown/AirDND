class LocationSection:
    def __init__(self, listings, pagination):
        self.listings = listings
        self.pagination = pagination
        return
    def to_json(self):
        return {
            'listings':self.listings
            'pagination':self.pagination
        }

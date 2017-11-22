class Reservation:
    def __init__(self, listingId, dates):
        self.listingId = listingId
        self.dates = dates
        return
    def to_json(self):
        return {
            'listingId':self.listingId
            'dates':self.dates
        }

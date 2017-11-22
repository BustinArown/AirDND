class Listing:
    def __init__(self,details,pricing,availabilities):
        self.details=details
        self.pricing=pricing
        self.availabilities=availabilities
        return
    def to_json(self):
        return {
            'details':self.details
            'pricing':self.pricing
            'availabilities':self.availabilities
        }

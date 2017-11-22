class ListingDetail:
    def __init__(self,bathrooms,bedrooms,beds,location,uuid,instantBookable,
                 isNewListing,lat,lng,name,neighborhood,propertyType,reviewsCount,
                 roomType,starRating):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.beds = beds
        self.location = location
        self.uuid = uuid
        self.instantBookable = instantBookable
        self.isNewListing = isNewListing
        self.lat = lat
        self.lng = lng
        self.name = name
        self.neighborhood = neighborhood
        self.propertyType = propertyType
        self.reviewsCount = reviewsCount
        self.roomType = roomType
        self.starRating = starRating
        return
    def to_json(self):
        return {
            'bathrooms':self.bathrooms
            'bedrooms':self.bedrooms
            'beds':self.beds
            'locaiton'self.location
            'id':self.uuid
            'instantBookable':self.instantBookable
            'isNewListing':self.isNewListing
            'lat':self.lat
            'lng':self.lng
            'name':self.name
            'neighborhood':self.neighborhood
            'propertyType':self.propertyType
            'reviewsCount':self.reviewsCount
            'roomType':self.roomType
            'starRating':self.starRating
        }
    

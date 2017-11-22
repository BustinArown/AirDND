class Pagination:
    def __init__(self, hasNextSection, listingOffset, sectionOffset):
        self.hasNextSection = hasNextSection
        self.listingOffset = listingOffset
        self.sectionOffset = sectionOffset
    def to_json(self):
        return {
            'hasNextSection':self.hasNextSection
            'listingOffset':self.listingOffset
            'sectionOffset':self.sectionOffset
        }

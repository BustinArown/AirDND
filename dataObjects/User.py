class User:
    def __init__(self,acceptanceRate,createdAt,friendsCount,hardSuspended,uuid
                 listingsCount,publiclyVisibleWishlistsCount,recommendationCount,
                 responseRate,responseTime,revieweeCount,softSuspended,
                 suspended,totalListingsCount,wishlistsCount):
        self.acceptanceRate = acceptancRate
        self.createdAt = createdAt
        self.friendsCount = friendsCount
        self.hardSuspended = hardSuspended
        self.uuid = uuid
        self.listingsCount = listingsCount
        self.publiclyVisibleWishlistsCount = publiclyVisibleWishlistsCount
        self.recommendationCount = recommendationCount
        self.responseRate = responseRate
        self.responseTime = responseTime
        self.revieweeCount = revieweeCount
        self.softSuspended = softSuspended
        self.suspended = suspended
        self.totalListingsCount = totalListingsCount
        self.wishlistsCount = wishlistsCount
        return
    def to_json(self):
        return {
            'acceptanceRate':self.acceptanceRate
            'createdAt':self.createdAt
            'friendsCount':self.friendsCount
            'hardSuspended':self.hardSuspended
            'id':self.uuid
            'listingsCount':self.listingsCount
            'publiclyVisibleWishlistsCount':self.publiclyVisibleWishlistsCount
            'recommendationCount':self.recommendationCount
            'responseRate':self.responseRate
            'responseTime':self.responseTime
            'revieweeCount':self.revieweeCount
            'softSuspended':self.softSuspended
            'suspended':self.suspended
            'totalListingsCount':self.totalListingsCount
            'wishlistsCount':self.wishlistsCount
        }

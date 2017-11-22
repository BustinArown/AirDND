class Review:
    def __init__(self comments, createdAt, uuid):
        self.comments = comments
        self.createdAt = createdAt
        self.uuid = uuid
        return
    def to_json(self):
        return {
            'comments':self.comments
            'createdAt':self.createdAt
            'id':self.uuid
        }
    

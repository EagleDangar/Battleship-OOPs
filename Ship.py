class Ship:
    # be undefined even after the initialization method.
    def __init__(self, row, column,horizontal,length):
        shiptypes = ["S","D","C","B"]
        self.row = row
        self.column = column
        self.horizontal = horizontal
        self.length = length
        self.type = shiptypes[length-1]
        self.hits = set()

    def hit(self, row, column):
        self.hits.add((row,column))
        
    def is_sunk(self):
        sunk = False

        if len(self.hits) == self.length:
            sunk = True
        # print(sunk)
        return sunk

    def __repr__(self):
        return "{row:%s,column:%s,horizontal:%s,length:%s, type:%s, hits:%s}" % (self.row,self.column,self.horizontal,self.length,self.type, self.hits)
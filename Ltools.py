class Ltools:
    def __init__(self, data):
        self.data = data
    
    def median(self):
        '''returns the median for the container object contents
        The values are not arranged in ascending order, the median is of the
        keys'''
        length = len(self.data)
        if length%2==0:
            top = self.data[length//2+1]
            bottom = self.data[length//2]
            try:
                median = sum([top, bottom])/2
            except TypeError:
                median = (top, bottom)
        else:
            median = self.data[length//2+1]
        
        return median


    def mode(self):
        '''returns the mode for the container object contents'''
        counter = {}
        out = []

        for i in self.data:
            if self.data[i] in counter.keys():
                counter[self.data[i]] += 1
            else:
                counter[self.data[i]] = 1

        #if len(counter.keys()) == len(self.data.values()):
            #return None
            #couldn't get this working, but it should work something like this

        mode = max(counter.values())
        for k, v in counter.items():
            if v == mode:
                out.append((k, v))

        return out

#from math import *
from Ltools import Ltools


class Lict(Ltools):
    '''
    Stores contents like a dictionary, interfaced with like a list.
    Enumerated from 1, not zero.
    Create an object with the following:
        yourLList = LList(*arg1, *arg2...)
    It accepts an empty *arg
    '''
    def __init__(self, *args):
        self.__package_data__(*args)
        super().__init__(self.data)


#--- REGION: Private Methods
    def __package_data__(self, *args, inserting=False):
        '''
        IN: *args can be any type
        OUT: a dictionary object, ordered as items were presented in *args

        Creates a one-ordered dictionary of items from the *args presented
        Lict: the dictionary you interface with like a list.

        If inserting = True, this is being called from another method and
        already has a list of values. Otherwise, it will create it from the
        args presented.
        '''
        temp = inserting
        if not temp:
            temp = [i for i in args]

        key = 1
        self.data = {}
        for i in temp:
            self.data[key] = i
            key += 1


    def __str__(self):
        return str(self.data)


    def __iter__(self):
        for key in self.data.keys():
            yield self.data[key]


    def __len__(self):
        return len(self.data)


    def __getitem__(self, key=None):
        '''Used when indexing (LictObj[key]), key being a number > 0'''
        return self.data[key]


    def __setitem__(self, key, value):
        try:
            if type(key) is float:
                raise TypeError
            
            #if key in range(1, len(self.data)+1):
            if key in self.keys():
                self.data[int(key)] = value
            else:
                raise KeyError

        except (TypeError, ValueError):
            print(
             "TypeError: Lict keys must be integers or integer-convertible"
             )
        except KeyError:
            print("KeyError: Key not in Lict.keys()")


    def __delitem__(self, key=0):
        '''
        Deletes the specified item from the Lict based on the given key.
        If no key is specified, default behavior removes the final element.
        '''
        if key == 0:
           del self.data[len(self.data)]
        else: 
            del self.data[key]
        
        self.__package_data__(self, inserting=self.values())


    def __repr__(self):
        '''
        Called when entering just the instance name, ex test = Lict(1),
        then typing test will return '1'
        '''
        representation = []
        for key in self.data.keys():
            representation.append(self.data[key])
        #return ', '.join(str(x) for x in representation)
        return str(representation)


    def __insert__(self, new_item, pos):
       out = []

       for k, v in self.items():
           if k == pos:
               out.append(new_item)
           out.append(v)

       self.__package_data__(inserting=out)


    def __reversed__(self):
        '''Reverses the current order of the Lict items; saves data as such'''
        temp = Lict()
        for n in self.keys():
            temp.put(self.data[n], 1)

        self.data = temp.data


    def __contains__(self, item):
        if item in self.values():
            return True
        return False


    def __add__(self, other):
        '''appends items from other to the end of the Lict'''
        if type(other) == Lict or type(other) == list:
            for i in other:
                self.put(i)
        elif type(other) == dict:
            for i in other.values():
                self.put(i)


    def __sub__(self, other):
        '''Removes items from self which are found in both data structures'''
        if type(other) != list:
            try:
                temp = [x for x in other.values()]
            except AttributeError:
                temp = [other]
        else:
            temp = other

        for i in temp:
            self.remove(i, excepting=False)
        
        if type(self.data[1]) == Lict:
            #if data is now empty, it becomes an empty Lict
            self.__package_data__()


    def __mul__(self, x):
        '''
        Creates x-number of copies of self.data and appends their values to
        the end of self.data'''
        try:
            if type(x) == int:
                for n in range(x):
                    for i in self.values():
                        self.put(i)
            else:
                raise TypeError
        except TypeError:
            print(
                "TypeError: Invalid object type presented for multiplication"
            )


    def __truediv__(self, x):
        '''Returns x number of list objects based on the number passed
        with x'''

#--- ENDREGION

#--- REGION: Public Methods
    def put(self, value, pos=None):
        try:
            if pos is None:
                self.data[len(self.data)+1] = value
            elif type(pos) is int and pos > 0:
                if pos in self.keys():
                    self.__insert__(value, pos)
                else:
                    self.data[len(self.data)+1] = value
            else:
                raise TypeError
        except TypeError:
             print(
             "SyntaxError: incorrect value for kwarg 'pos': \n"
             "    Correct values are include indexes in the Lict and ints > 0"
             )


    def keys(self):
        '''returns a list of keys'''
        out = []
        for k in self.data.keys():
            out.append(k)
        return out


    def values(self):
        '''returns a list of the values'''
        out = []
        for v in self.data.values():
            out.append(v)
        return out


    def items(self):
        '''returns a list of tuples, one per key-value pair.'''
        out = []
        for k, v in self.data.items():
            out.append((k, v))
        return out


    def remove(self, item=None, excepting=True):
        '''
        Deletes the specified item from the Lict.
        If no item is specified, removes the final element.
        The excepting keyword is used when this method is called
            via the private method self.__sub__(), and allows the method to
            iterate through a list of items without raising an exception for
            missing items.
        If not used in that way, it will throw an error if the item is not
            found.
        '''
        try:
            if item is None:
               del self.data[len(self.data)]
               self.__package_data__(self, inserting=self.values())
            else:
                if item in self.values():
                    for k, v in self.items():
                        if item == v:
                            del self.data[k]
                    self.__package_data__(self, inserting=self.values())
                else:
                    if excepting:
                        raise NameError
        except NameError:
            print("NameError: No item {} found!".format(item))



#--- ENDREGION

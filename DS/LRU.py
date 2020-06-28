# LRU cache implementation.
#Tasks:
# 1. check if the dictionary has the key
# 2. if the dictionary has the key, find the value
# 3. if the dictinoary does not have the key, check if the capacity is full.
# 4. if the capacity is full, remove LRU
# 5. if the capacity is not full, just add the key

#input: We start with an empty dictionary.
    
# a note to myself: You were curious about whether it would work to work with a dictionary. Instead of thinking about
# the 'best' way to do it, you can simply try it. make small bits of the whole and combine

class LRU(object):
    def __init__(self, capacity, cache):
        self.capacity = 0
        self.cache = {}

    def remove_least(self):
# output: a dictionary with the least used key removed.
  
        minimum = min(self.cache.values())
# find the key with the corresponding min value.
        min_key = [key for key in self.cache if self.cache[key] == minimum]
        self.cache.pop(min_key[0])
        return self.cache
       
    def set_cache(self, key, value):
    # input: the current dictionary (LRU Cache), the key and value that are not already in the dictionary.
    # output: the dictionary after the key value pair is added.
        
        self.cache.update({key:value})
        self.capacity += 1
        return self.cache
    

    def get_cache(self, key):
    #if there is a value in the LRU cache, this function fetches it.
        if key in self.cache.keys():
            return self.cache[key]
        else:
            return -1

    def iscapacity(self):
        # checks the length of the dictionary if it is at capacity.
        if len(self.cache) == self.capacity:
            print("at capacity")
            return True
        elif len(self.cache) <= self.capacity:
            print("under capacity")
            return False
        else:
            print("Error: over capcity")
            return False
    '''    
    def driver(self, key, value):
        if key in self.cache.keys():
            self.get_cache(key)
        else:
            if self.capacity >= 5:
                self.remove_least()
                self.set_cache(key, value)
            else:
                self.set_cache(key, value)
        return self.cache
    '''         
    #current_dict = {'mem1': 1, 'mem2': 2}
    #another_dict = {'cat1': 1, 'cat2': 3, 'cat3': 1, 'cat4': 5}
    #empty_dict = {}
    
    #if input in current_dict.keys()
    

#print(remove_least(current_dict))
#print(remove_least(another_dict))

#print(set_cache(current_dict, 'mem3', 100))
#print(set_cache({}, 'number1', 2))

if __name__=="__main__":
    test_lru = LRU(5, {})
    print(test_lru.set_cache(23, 7))
    print(test_lru.set_cache(24, 8))
    print(test_lru.set_cache(25, 9))
    print(test_lru.set_cache(26, 10))
    print(test_lru.set_cache(27, 11))
    
    print(test_lru.get_cache(30))
    test_lru.iscapacity()
    print(test_lru.remove_least())
    print(test_lru.set_cache(30, 1000))


    
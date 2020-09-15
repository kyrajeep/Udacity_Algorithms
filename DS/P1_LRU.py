# Least Recently Used (LRU) cache implementation.
#Tasks:
# 1. check if the dictionary has the key
# 2. if the dictionary has the key, find the value
# 3. if the dictionary does not have the key, check if 
# the capacity is full.
# 4. if the capacity is full, remove LRU
# 5. if the capacity is not full, add the key

#input: We start with an empty dictionary.
    
# a note to self: You were curious about whether it would work to work with a dictionary. Instead of thinking about
# the 'best' way to do it, you can simply try it. make small bits of the whole and combine

class LRU(object):
    def __init__(self, capacity, cache):
        self.capacity = capacity
        self.cache = {}

    def remove_least(self):
# output: a dictionary with the least used key removed.
        if self.cache.values():
            minimum = min(self.cache.values())
# find the key with the corresponding min value.
            min_key = [key for key in self.cache if self.cache[key] == minimum]
            self.cache.pop(min_key[0])
            return self.cache
        else:
            print("Cache is empty")
            return
       
    def set_cache(self, key, value):
    # input: the current dictionary (LRU Cache), the key and value that are not already in the dictionary.
    # output: the dictionary after the key value pair is added.
        if self.iscapacity() == True:
            self.remove_least()
        self.cache.update({key:value})
        
        return self.cache
    
    def get_cache(self, key):
    #if there is a value in the LRU cache, this function fetches it.
    #if the value does not exist, the function returns -1.
        if key in self.cache.keys():
            return self.cache[key]
        else:
            
            return -1

    def iscapacity(self):
        # checks the length of the dictionary if it is at capacity.
        #print(len(self.cache))
        if len(self.cache) == self.capacity:
            return True
        elif len(self.cache) < self.capacity:
            return False
        else:
            return False
  
if __name__=="__main__":
    # Test Case 1
    test_lru = LRU(5, {})
    print(test_lru.set_cache(23, 7))
    print(test_lru.set_cache(24, 8))
    print(test_lru.set_cache(25, 9))
    print(test_lru.set_cache(26, 10))
    print(test_lru.set_cache(27, 11))
    # expected: -1 because 30 is not in the cache.
    print(test_lru.get_cache(30))
    # expected: True
    print(test_lru.iscapacity())
    # expected: with 23: 7 removed
    print(test_lru.remove_least())
    print(test_lru.set_cache(30, 1000))
    # expected : 30
    print(test_lru.get_cache(30))

    # Test Case 2: empty
    empty_cache = LRU(2, {})
    # expected : -1 because 30 is not in the cache.
    print(empty_cache.get_cache(30))

    # Test Case 3: when at capacity
    # expected to remove the least used element then add the new.
    print(test_lru.set_cache(45, 200))

    
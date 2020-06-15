#Tasks:
# 1. check if the dictionary has the key
# 2. if the dictionary has the key, find the value
# 3. if the dictinoary does not have the key, check if the capacity is full.
# 4. if the capacity is full, remove LRU
# 5. if the capacity is not full, just add the key

# we are creating a set of keys and values. we ar

#input: We start with an empty dictionary.
#def tests():
    
# You were curious about whether it would work to work with a dictionary. Instead of thinking about
# the 'best' way to do it, you can simply try it. make small bits of the whole and combine

def remove_least(current_dict):
# input: a dictionary
# output: a dictionary with the least used key removed.
  
    minimum = min(current_dict.values())
# find the key with the corresponding min value.
    min_key = [key for key in current_dict if current_dict[key] == minimum]
# remove that key. What if there are two? remove one, but the choice is random.

    
        
  


current_dict = {'mem1': 1, 'mem2': 2}
remove_least(current_dict)

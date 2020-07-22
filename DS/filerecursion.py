# Find paths of all files that end with '.c'
# do not need memoization...  

# Thought process :
# why would recursion be relevant? Is there a 
#repeated task in the problem?
# We need recursion in joining all the path 
#components in os since we are not using os.walk
 
# Tasks: 1. Going through all the folders requires 
#recursion or an iterative approach.
# 2.somehow save the directories and files we have been to. Do you think memoization would be necessary?
import os
result = []
def find_files(suffix, path):
    
    # input: the ending of a filename, path of the directory
    # output: list of paths

    # if the path is a .c file
    if path.endswith(suffix) == True:
        result.append(path)
    else:
    # if the path is a directory, go through its 
    #components
        if os.path.isdir(path):
            directory = os.listdir(path)
            #print(directory)
            dir_size = len(directory)
            for i in range(dir_size):
                cur_path = os.path.join(path, directory[i])
                find_files(suffix, cur_path)
                
                    
            return result
       
 # If you put a slash in front of the argument, it is considered an absolute path
path = "/Users/kyra/Documents/GitHub/Udacity_Algorithms/DS/testdir"    

print(find_files('.c', path))





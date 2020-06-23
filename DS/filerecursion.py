# Find paths of all files that end with '.c'
# Thought process :
# why would recursion be relevant? Is there a repeated task in the problem?
# We need recursion in joining all the path components in os since we are not using os.walk
 
# Tasks: 1. Going through all the folders requires recursion or an iterative approach.
# 2.somehow save the directories and files we have been to
import os

def lsdirectory(ending, path, result):
    # input: the ending of a filename, path of the directory
    # output: list of paths
    # if the path is just a file that ends with .c, add it to the list of the result.
    if str(path).endswith(".c") == True:
        
        result.append(path)
        path = os.chdir('..')
    # if the path is just a file, move on to the next directory in the same level if there is one.
    elif os.path.isfile(path) == True:

        # go up one directory and list all the directories in there
        path = os.chdir('..')        
    # If we hit a directory, list all the files/directories in the path
    
    elif os.path.isdir(path):
        
        directory = os.listdir(path)
        # if the directory is empty, go up to its super directory
        if directory == None:
            path = os.chdir('..')
        # find the first subdirectory if there is one as long as it is not 
        
        i = 0
        while directory and str(directory[i]).endswith(ending) == False:
            # visit this subdirectory
            
            curr_sub = os.path.join(path, directory[i])
            if os.path.isdir(curr_sub):
                print(curr_sub)
                lsdirectory(ending, curr_sub, result)
            elif (len(directory) -1) > i:
                i += 1
                print(i)
            elif (len(directory) -1) == i:
           # if we traversed through all files/directories on that level
                path1 = os.chdir('..')
                lsdirectory(ending, path1, result)
    
           
    lsdirectory(ending, path, result) 
    
    
    
    return result
    

path = "/Users/kyra/Documents/GitHub/Udacity_Algorithms/DS/testdir"

#print(join1) # If you put a slash in front of the argument, it is considered an absolute path

print(lsdirectory(".c", path, []))





path = "/Users/kyra/Documents/GitHub/Udacity_Algorithms/DS/testdir"    

    
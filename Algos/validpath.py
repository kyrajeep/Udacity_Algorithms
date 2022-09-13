class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        start = edges[source]
        q = list()
        q.append(start[1])
        while q:
            popped = q.pop()
            print(popped)
            if popped == destination:
                return True
            else:
                new = edges[popped][1]
                q.append(new)
        return False

# A path finding problem on Leetcode. See if there is a valid path from source to destination.                
# I am really enjoying this. I like their test cases because it makes debuggin easier.
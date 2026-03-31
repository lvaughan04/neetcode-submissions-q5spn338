class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapSet = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            mapSet[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if mapSet[course] == []:
                return True
            
            ## actual dfs through the prereqs
            visited.add(course)
            for prereq in mapSet[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            mapSet[course] = []
            return True
        
        ## have to run through every course to check
        for course in mapSet.keys():
            if not dfs(course):
                return False

        return True
            
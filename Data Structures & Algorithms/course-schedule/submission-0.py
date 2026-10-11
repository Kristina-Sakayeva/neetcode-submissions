class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = [[] for i in range(numCourses)]

        for pair in prerequisites:
            main, pre = pair[0], pair[1]

            adjacency_list[pre].append(main)

        indegrees = [0 for i in range(numCourses)]
        for i in range(len(adjacency_list)):
            for j in adjacency_list[i]:
                indegrees[j] += 1

        queue = [i for i in range(len(indegrees)) if indegrees[i] == 0]
        completed = []

        while queue:
            new_queue = []
            for course in queue:
                completed.append(course)
                for neigh in adjacency_list[course]:
                    indegrees[neigh] -= 1

                    if indegrees[neigh] == 0:
                        new_queue.append(neigh)
            queue = new_queue
        
        if len(completed) < numCourses:
            return False
        return True
        
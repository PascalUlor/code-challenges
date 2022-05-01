#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.56%)
# Likes:    8128
# Dislikes: 317
# Total Accepted:    764.4K
# Total Submissions: 1.7M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
from operator import le
import re


class Solution:
    def graph(self, num_vertices, edge_list):
        ajList = [[] for _ in range(num_vertices)]
           # c2 (course 2) is a prerequisite of c1 (course 1)
            # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edge_list:
            ajList[c2].append(c1)
        return ajList

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build Adjacency list from Edges list
        graph = self.graph(numCourses, prerequisites)
        visited = set()

        def hasCycle(vertex, stack):
            if vertex in visited:
                if vertex in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                # This vertex is processed so we pass
                return False

            # mark this vertex as visited
            visited.add(vertex)
            # add it to the current stack
            stack.append(vertex)

            for i in graph[vertex]:
                if hasCycle(i, stack):
                    return True
            # once vertex is processed, we pop it out of the stack
            stack.pop()
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if v not in visited:
                if hasCycle(v, []):
                    return False
        return True
        
# @lc code=end


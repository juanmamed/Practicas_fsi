# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

breadth = search.breadth_first_graph_search(ab)
depth = search.depth_first_graph_search(ab)
branch_and_bound = search.bbs_search(ab)

print(breadth[0].path(), breadth[1])
print(depth[0].path(), depth[1])
print(branch_and_bound[0].path(), branch_and_bound[1])

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

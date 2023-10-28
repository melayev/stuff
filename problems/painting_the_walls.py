"""
2742. Painting the Walls

You are given two 0-indexed integer arrays, cost and time, of size n 
representing the costs and the time taken to paint n different walls 
respectively. 

There are two painters available:

- A paid painter that paints the ith wall in time[i] units of time 
	and takes cost[i] units of money.
- A free painter that paints any wall in 1 unit of time at a cost of 0. But the 
	free painter can only be used if the paid painter is already occupied.
	
Return the minimum amount of money required to paint the n walls.
"""

from typing import List
import math

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        memo = {}

        def dfs(currentWall: int, paintedWalls: int) -> int:
            key = (currentWall, paintedWalls)

            # If the result is already in the memo, return it.
            if key in memo:
                return memo[key]

            # If we have already painted all the walls, return 0.
            if costListLength - currentWall <= paintedWalls:
                return 0

            # If we have reached the end of the cost list, return infinity.
            if currentWall >= costListLength:
                return math.inf

            # Return the minimum cost of painting the remaining walls,
            # either by painting the current wall or by not painting it.
            result = min(
                dfs(
                    currentWall + 1,
                    paintedWalls + time[currentWall]
                ) + cost[currentWall],

                dfs(currentWall + 1, paintedWalls - 1)
            )

            # Cache the result in the memo.
            memo[key] = result

            return result

        # Get the length of the cost list.
        costListLength = len(cost)

        # Call the recursive dfs function to calculate the minimum cost.
        return dfs(0, 0)



assert Solution().paintWalls(
          cost=[42, 8, 28, 35, 21, 13, 21, 35], 
          time=[2, 1, 1, 1, 2, 1, 1, 2]
        ) == 63

assert Solution().paintWalls(cost=[1,2,3,2], time=[1,2,3,2]) == 3
assert Solution().paintWalls(cost=[2,3,4,2], time=[1,1,1,1]) == 4

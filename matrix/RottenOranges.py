import collections
from typing import List


class RottenOranges:

    #https://neetcode.io/problems/rotting-fruit?list=neetcode150
    # this DFS algo.
    # Step 1: get a count of fresh fruits [1], and add the rotten to the queue [2].
    # Step 2: For each element in the q, check the left, up, right, down cells [boundary checked]
    # Step 3: make the boundary cells 2 and add to the q and decrease the fresh count.
    # Step 5: Increase the time count after processing each row.
    # Step 6: if the fresh count is 0 return the number of minutes else -1

    def  minTimeToRot(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = collections.deque()

        # Step 1: get a count of fresh fruits [1], and add the rotten to the queue [2].
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # check for fresh fruit
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    #add the row, col value for the rotten fruit
                    q.append((row,col))

        #Step 2: For each element in the q, check the left, up, right, down cells [boundary checked]
        boundaries = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        while fresh > 0 and len(q) > 0:
            len_of_q = len(q)
            for _ in range(len_of_q):
                r, c = q.popleft()
                for dr, dc in boundaries:
                    # Step 3: make the boundary cells 2 and add to the q and decrease the fresh count.
                    row, col = r + dr, c + dc
                    if (0 <= row < len(grid)
                            and 0 <= col < len(grid[0])
                            and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            # Step 5: Increase the time count after processing each row.
            time += 1
        # Step 6: if the fresh count is 0 return the number of minutes else -1
        return time if fresh == 0 else -1

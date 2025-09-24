import heapq
import math
import time

def heuristic(a, b, h_type):
    """
    Calculate heuristic distance between two points.
    
    Args:
        a: Starting point (x1, y1)
        b: Target point (x2, y2)
        h_type: Type of heuristic ('manhattan', 'euclidean', 'diagonal')
    
    Returns:
        float: Heuristic distance value
    """
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    if h_type == "manhattan": 
        return dx + dy
    elif h_type == "euclidean": 
        return math.sqrt(dx**2 + dy**2)
    elif h_type == "diagonal": 
        return max(dx, dy)
    return 0

def parse_grid(grid_str):
    """
    Parse grid string into 2D array and find start/goal positions.
    
    Args:
        grid_str: String representation of grid with '/' separators
    
    Returns:
        tuple: (grid, start_position, goal_position)
    """
    grid = [list(row) for row in grid_str.split("/")]
    start = goal = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S': 
                start = (i, j)
            elif grid[i][j] == 'G': 
                goal = (i, j)
    return grid, start, goal

def get_neighbors(pos, grid):
    """
    Get all valid neighboring cells (8-direction movement).
    
    Args:
        pos: Current position (x, y)
        grid: 2D grid array
    
    Returns:
        list: List of valid neighbor positions
    """
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    neighbors = []
    for dx, dy in directions:
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '1':
            neighbors.append((x, y))
    return neighbors

def cost(current, neighbor, grid):
    """
    Calculate movement cost between cells with ghost zone penalty.
    
    Args:
        current: Current cell coordinates
        neighbor: Neighbor cell coordinates
        grid: 2D grid array
    
    Returns:
        float: Movement cost
    """
    # Different cost for straight vs diagonal moves
    base_cost = 1 if current[0] == neighbor[0] or current[1] == neighbor[1] else math.sqrt(2)
    
    # Additional cost for ghost zones
    if grid[neighbor[0]][neighbor[1]] == '6': 
        return base_cost + 5
    return base_cost

def greedy_search(grid, start, goal, h_type):
    """
    Implement Greedy Best-First Search algorithm.
    
    Args:
        grid: 2D grid array
        start: Start position
        goal: Goal position
        h_type: Heuristic type
    
    Returns:
        tuple: (path, number_of_nodes_explored)
    """
    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal, h_type), start))
    came_from = {start: None}
    explored = set()
    
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal: 
            break
        explored.add(current)
        for neighbor in get_neighbors(current, grid):
            if neighbor not in came_from:
                heapq.heappush(frontier, (heuristic(neighbor, goal, h_type), neighbor))
                came_from[neighbor] = current
    
    # Reconstruct path
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path, len(explored)

def a_star_search(grid, start, goal, h_type):
    """
    Implement A* Search algorithm.
    
    Args:
        grid: 2D grid array
        start: Start position
        goal: Goal position
        h_type: Heuristic type
    
    Returns:
        tuple: (path, number_of_nodes_explored)
    """
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    explored = set()
    
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal: 
            break
        explored.add(current)
        for neighbor in get_neighbors(current, grid):
            new_cost = cost_so_far[current] + cost(current, neighbor, grid)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal, h_type)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    
    # Reconstruct path
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path, len(explored)

def visualize_path(grid, path):
    """
    Visualize the grid with the solution path marked.
    
    Args:
        grid: 2D grid array
        path: List of coordinates forming the path
    """
    visual = [row[:] for row in grid]
    for x, y in path:
        if visual[x][y] not in ('S', 'G'): 
            visual[x][y] = '*'
    for row in visual: 
        print(''.join(row))

def run_comparison(grid_str):
    """
    Run comparison between algorithms with different heuristics.
    
    Args:
        grid_str: String representation of the grid
    """
    grid, start, goal = parse_grid(grid_str)
    heuristics = ["manhattan", "euclidean", "diagonal"]
    
    print("PATHFINDING ALGORITHMS COMPARISON")
    print("=" * 40)
    print("Grid Configuration:")
    for row in grid:
        print(''.join(row))
    print(f"Start: {start}, Goal: {goal}")
    print()
    
    for h in heuristics:
        print(f"\n{'='*50}")
        print(f"HEURISTIC: {h.upper()}")
        print(f"{'='*50}")
        
        # Greedy Best-First Search
        print(f"\nGreedy Best-First Search:")
        start_time = time.time()
        path, explored = greedy_search(grid, start, goal, h)
        execution_time = time.time() - start_time
        print(f"Path length: {len(path)}")
        print(f"Nodes explored: {explored}")
        print(f"Execution time: {execution_time:.6f} seconds")
        visualize_path(grid, path)
        
        # A* Search
        print(f"\nA* Search:")
        start_time = time.time()
        path, explored = a_star_search(grid, start, goal, h)
        execution_time = time.time() - start_time
        print(f"Path length: {len(path)}")
        print(f"Nodes explored: {explored}")
        print(f"Execution time: {execution_time:.6f} seconds")
        visualize_path(grid, path)

# Main execution
if __name__ == "__main__":
    grid_input = "S0010/11016/00010/11011/0000G"
    run_comparison(grid_input)
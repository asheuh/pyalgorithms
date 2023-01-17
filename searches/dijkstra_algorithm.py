def dijkstra_algorithm():
    heap = []
    heappush(heap, (0, start)) # Initialize start with zero cost
    came_from = {}
    # For node n, g_score[n] is the cost of the cheapest path from start to n currently known.
    g_score = defaultdict(int)
    g_score[start] = 0
    result = None
    
    while heap:
        cost, current = heappop(heap)

        if current == goal:
            total_path = [current]
            while current in came_from:
                current = came_from[current]
                total_path = [*[current], *total_path]
            result = total_path
            break

        neighbours = neighbouring_vectors(current, h, w)
        
        for nr in neighbours:
            child = (nr.x, nr.y)
            if child not in g_score:
                g_score[child] = math.inf

            # d(current, child) is the weight of the edge from current to child
            t_score = g_score[current] + dist(current, child)
            if t_score < g_score[current]:
                came_from[child] = current
                g_score[child] = t_score

                if not contains(heap, child):
                    heappush(heap, (t_g_score, child))

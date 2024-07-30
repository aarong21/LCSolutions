class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)

        # Create adj list
        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # bfs to calculate the distances
        def bfs(adj_list, start_vert):
            n = len(adj_list)
            visited = [False for _ in range(n)]
            dist = [float('inf') for _ in range(n)]
            dist[0] = 0
            queue = deque([0])
            while queue:
                vert = queue.popleft()
                if visited[vert]:
                    continue
                visited[vert] = True
                # visit neighbors of current vertex
                for neighbor in adj_list[vert]:
                    neigh_dist = dist[vert]+1
                    if not visited[neighbor] and neigh_dist < dist[neighbor]:
                        dist[neighbor] = neigh_dist
                        queue.append(neighbor)
            return dist

        distances = bfs(adj_list, 0)
        # distances now contains all the shortest time values

        max_time = 0
        for i in range(1,n):
            return_time = 2*distances[i]
            msg_sent = (return_time - 1) // patience[i]
            last_sent = msg_sent * patience[i]
            max_time = max(max_time, return_time+last_sent)
        return max_time + 1



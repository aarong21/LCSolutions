class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        graph = {i: [] for i in range(1, n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
        
        # Initialize distance array
        distance = {node: float('inf') for node in range(1,n+1)}
        distance[k] = 0
        pq = [(0,k)]

        # Iterate over queue
        while pq:
            # Extract node with min dist
            time, node = heapq.heappop(pq)
            # Skip if shorter path to node
            if time > distance[node]:
                continue
            # Update values if better distance
            for neighbor, edge_time in graph[node]:
                # Calculate time
                total_time = time + edge_time

                if total_time < distance[neighbor]:
                    distance[neighbor] = total_time
                    heapq.heappush(pq, (total_time, neighbor))
        # Check if all nodes are reachable and return max time
        max_time = max(distance.values())
        return max_time if max_time < float('inf') else -1
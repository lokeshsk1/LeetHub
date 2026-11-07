class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        
        av_pq = [(e, i) for i,e in enumerate(servers)]
        heapify(av_pq)
        nav_pq = []

        res = []

        time = 0

        for i in range(len(tasks)):

            time = max(time, i)

            if not av_pq:
                time = max(time, nav_pq[0][0])

            # print(av_pq, nav_pq)

            while nav_pq and nav_pq[0][0] <= time:
                nav_time, ind = heappop(nav_pq)
                heappush(av_pq, (servers[ind], ind))
                
            server, ind = heappop(av_pq)

            # print(time, server, ind)
            res.append(ind)
            
            heappush(nav_pq, (time + tasks[i], ind))
        

        return res


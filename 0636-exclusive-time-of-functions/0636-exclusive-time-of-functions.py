class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0]*n

        st = []

        for l in logs:
            idn, status, time = l.split(":")
            idn, time = int(idn), int(time)
            
            if status == "start":
                st.append((idn, time))
            
            if status == "end":
                start_idn , start_time = st.pop()
                diff_time = time - start_time + 1
                res[idn] += diff_time

                if st:
                    start_idn1 , start_time1 = st[-1]
                    res[start_idn1] -= diff_time
        
        return res
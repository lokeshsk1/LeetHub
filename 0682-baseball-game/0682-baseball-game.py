class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        st = []

        for i in ops:
            # try:
            #     st.append(int(i))
            #     continue
            # except:
            #     pass

            if i.isnumeric() or i[0]=="-":
                st.append(int(i))
            elif i == '+':
                st.append(st[-1] + st[-2])
            elif i == 'D':
                st.append(st[-1] * 2)
            elif i == 'C':
                st.pop()
        
            print(st)

        return sum(st)
        
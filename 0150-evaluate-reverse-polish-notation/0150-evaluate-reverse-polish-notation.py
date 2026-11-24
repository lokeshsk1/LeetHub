class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        

        st = []

        for i in tokens:

            if i in '*/+-':

                
                one = st.pop()
                two = st.pop()

                if i == '+':
                    st.append(two + one)
                elif i == '-':
                    st.append(two - one)
                elif i == '*':
                    st.append(two * one)
                elif i == '/':
                    st.append(int(two / one))

                # print(st)
            
            else:
                st.append(int(i))
        
        return st.pop()
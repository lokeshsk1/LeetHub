class Solution:
    def simplifyPath(self, path: str) -> str:
        
        l = path.split('/')
        # l = list(filter(lambda x : (x!='' and x!='.') , l))
        
        st = [] 
        
        for i in l:
            if i != '' and i != '.':
                if st==[] and i=='..':
                    continue
                elif i == '..':
                    st.pop()
                else:
                    st.append(i)
        
        return ('/'+'/'.join(st))
        
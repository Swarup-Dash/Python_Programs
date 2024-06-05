class Solution:
    def simplifyPath(self, path):
        stack=[]
        components = path.split('/')
        for component in components:
            if component=="..":
                if stack:
                    stack.pop()
            elif component == "." or component == "":
                continue
            else:
                stack.append(component)
                
        simplified_path = "/" + "/".join(stack)
        return simplified_path
        
        
obj=Solution()
path = "/home//../hii/.../bay"
res=obj.simplifyPath(path)
print(res)
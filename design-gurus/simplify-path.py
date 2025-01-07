class Solution:
    def simplifyPath(self, path):
        splitted = path.split('/')
        stack = []
        print(splitted)

        for command in splitted:
            if command == '':
                continue
            if command == '.':
                continue
            if command == '..':
                if len(stack) > 0:
                  stack.pop()
                continue
            
            stack.append(command)
                
        return "/" + '/'.join(stack)


s = Solution()

print(s.simplifyPath("/a//b////c/d//././/.."))
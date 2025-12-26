class StringOperations:
    # https://neetcode.io/problems/minimum-remove-to-make-valid-parentheses
    @staticmethod
    def minParanRemoveToMakeValid(self, s:str) -> str:

        # the problem is to ensure we have equal number of open "(" and close ")" i.e. count = 0
        # 1st case if there are more closed ")" then remove the extra ")" i.e. count is -ve
        # 2nd case if there are more open "(" then to maintain the order, remove the extras from last

        res = []
        # extra parenthesis count
        count = 0
        for c in s:
            if c == "(":
                count += 1
                res.append(c)
            elif c == ")" and count > 0:
                count -= 1
                res.append(c)
            # count is 0, then ignore ")" but add non ")"
            elif c != ")":
                res.append(c)
        #now for 2nd case: the result string can contain extra "(" which is count > 0
        # reverse the string
        filtered = []
        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)
        # reverse the array and convert to single string
        return "".join(filtered[::-1])








        return res



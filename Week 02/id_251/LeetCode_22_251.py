# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为： 
#
# [
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
# ]
# 
# Related Topics 字符串 回溯算法

"""
1 暴力递归
2 回溯递归
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 1 暴力递归
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(a):
            if len(a) == 2 * n:
                if valid(a):
                    ans.append(''.join(a))
            else:
                a.append('(')
                generate(a)
                a.pop()
                a.append(')')
                generate(a)
                a.pop()

        def valid(a):
            count = 0
            for c in a:
                if c == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        ans = []
        generate([])
        return ans

    # 2 回溯
    def generateParenthesis2(self, n):
        res = []
        self._generate(0, 0, n, '', res)
        return res

    def _generate(self, left, right, n, s, res):
        # terminator
        if left == right == n:
            res.append(s)
            return

        # process current logic: left, right

        # drill down
        if left < n:
            self._generate(left + 1, right, n, s + '(', res)
        if right < left:
            self._generate(left, right + 1, n, s + ')', res)

        # reverse states


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.generateParenthesis2(n))

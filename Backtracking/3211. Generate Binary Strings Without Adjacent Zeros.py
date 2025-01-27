"""
You are given a positive integer n.

A binary string x is valid if all 
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

 

Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

"""

class Solution:
    def validStrings(self, n: int) -> list[str]:
        
        rel, sol = [], []

        def backtrack(i):
            if i == n:
                if ''.join(sol[:]).__contains__('00'):
                    return
                rel.append(''.join(sol[:]))
                return

        # Decided to pick 0

            sol.append('0')
            backtrack(i+1)
            sol.pop()

            # Decided to pick 1

            sol.append('1')
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return rel
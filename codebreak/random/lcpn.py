import sys
import re
from typing import List

class Solution:
    '''
    Using DFS
    Letter Combinations of phonenumbers
    '''
    def is_empty(self, stack):
        return len(stack) == 0
    
    def neighbours(self, value, characters):
        return [value + char for char in characters]
    
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 
                   5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        roots = mapping[int(digits[0])]
        stack = [item for item in roots]
        n = len(digits)
        explored = set()
        added = 0
        
        while not self.is_empty(stack):
            value = stack.pop()
            i = len(value)
            
            if i == n:
                return list(roots)
        
            if value not in explored:
                char = digits[i]
                characters = mapping[int(char)]
                neighbours = self.neighbours(value, characters)
                added = len(neighbours)

                for item in neighbours:
                    if item not in stack and item not in explored:
                        stack.append(item)
                i += 1

                if i >= n:
                    j = 0
                    
                    # backtrack
                    while j < (added):
                        if not self.is_empty(stack):
                            v = stack.pop()

                        if v not in explored:
                            explored.add(v)
                        j += 1
                
                    added = 0
                    
            explored.add(value)
            
        return [item for item in explored if len(item) == n]

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    s = str(input())

    assert re.match(r'^\d+$', s)
    assert 0 < len(s) <= 4

    solution = Solution()
    result = solution.letterCombinations(s)
    print(result)


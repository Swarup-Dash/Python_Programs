from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""       
        shortest = min(strs, key=len)
        
        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
        
        return shortest

# strs = ["Flow", "Flower", "Flight"]
# solution = Solution()
# result = solution.longestCommonPrefix(strs)
# print(result)

def main():
    input_strings = input("Enter strings separated by space: ").split()
    solution = Solution()
    result = solution.longestCommonPrefix(input_strings)
    print("Longest common prefix:", result)

if __name__ == "__main__":
    main()

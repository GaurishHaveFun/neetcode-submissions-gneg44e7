class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      arr = [0] * len(temperatures)
      stack = []

      for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
          stackVal, stackInd = stack.pop()
          arr[stackInd] = i - stackInd
        stack.append([t, i])
      return arr

        
        

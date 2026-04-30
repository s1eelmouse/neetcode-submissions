class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1
         
        while index1 < index2:
            summa =  numbers[index1] + numbers[index2]
            if summa < target:
                index1 += 1
            elif summa > target:
                index2 -= 1
            else:
                break
        return [index1 + 1, index2 + 1]
        
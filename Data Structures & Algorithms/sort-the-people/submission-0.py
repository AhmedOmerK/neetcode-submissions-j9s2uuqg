class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        hsh = {}
        for i in range(len(names)):
            hsh[heights[i]] = names[i]
        heights.sort(reverse=True)
        for i in range(len(names)):
            res.append(hsh[heights[i]])
        return res
        
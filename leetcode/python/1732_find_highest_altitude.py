class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitudes = [0]
        for i in range(0, len(gain)):
            altitudes.append(gain[i] + altitudes[i])
        return max(altitudes)

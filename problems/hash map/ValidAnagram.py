from collections import Counter

class MySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t) 
    
class BestSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
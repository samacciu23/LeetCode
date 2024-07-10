from collections import defaultdict

class MySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in anagrams:
                anagrams[s_sorted] = [s]
            else:
                anagrams[s_sorted].append(s)
        return list(anagrams.values())

class BestSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            res_dict["".join(sorted_s)].append(s)
        res_list = []
        for value in res_dict.values():
            res_list.append(value)
        return res_list
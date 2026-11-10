class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
    # array is always even length
    # 2 constraints = sum of skills must be even, return total chem = * 2 skills
    # probably hashmap + sorting
    # first part -> splitting into 2 teams
    # 1 2 3 4

        l,r = 0, len(skill) - 1
        skill.sort()
        chem = 0

        target = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            chem += skill[l] * skill[r]
            l += 1
            r -= 1
        return chem 


        


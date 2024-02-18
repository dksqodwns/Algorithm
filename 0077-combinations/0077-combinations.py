class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        num_list = list(range(1, n+1))
        
        def dfs(list, curr):
            if len(list) == k:
                result.append(list)
                return
            for num in num_list[curr:]:
                dfs(list + [num], num)
        
        dfs(list=[], curr=0)
        print(result)
        return result
        
        
    # 1 ~ n 범위의 정수로 이루어진 길이가 k인 배열의 조합
    # 단, 중복의 조합은 제외한다.
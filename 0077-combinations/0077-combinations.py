class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        num_list = list(range(1, n+1))
        
        def dfs(current, start):
            if len(current) == k:
                result.append(current)
                return
            
            for i in range(start, len(num_list)):
                dfs(current + [num_list[i]], i + 1)
        
        dfs([], 0)
        return result

        
        
    # 1 ~ n 범위의 정수로 이루어진 길이가 k인 배열의 조합
    # 단, 중복의 조합은 제외한다.
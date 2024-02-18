class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 결과 조합을 저장할 리스트
        result = []

        # 1부터 n까지의 숫자를 포함하는 리스트
        n_list = list(range(1, n+1))
        
        def dfs(list, start):
            # 현재 조합의 길이가 k와 같으면 result에 추가
            if len(list) == k:
                result.append(list)
                return
            
            # start 인덱스부터 num_list의 끝까지 순회
            for i in range(start, len(n_list)):
                dfs(list + [n_list[i]], i + 1)
        
        dfs([], 0)

        return result

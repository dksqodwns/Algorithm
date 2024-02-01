class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1  # 검색 범위의 시작과 끝을 설정합니다.

        while start <= end:  # 시작이 끝보다 작거나 같은 동안 반복합니다.
            mid = (start + end) // 2  # 중앙값의 위치를 찾습니다.

            # 타겟을 찾았을 경우, 그 위치의 인덱스를 반환합니다.
            if nums[mid] == target:
                return mid

            # 중앙값이 시작값보다 크거나 같은 경우, 앞부분이 정렬되어 있습니다.
            if nums[mid] >= nums[start]:
                # 타겟이 정렬된 앞부분에 위치하는지 확인합니다.
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1  # 타겟이 중앙값보다 작으면, 끝점을 중앙값 앞으로 이동시킵니다.
                else:
                    start = mid + 1  # 타겟이 중앙값보다 크면, 시작점을 중앙값 뒤로 이동시킵니다.
                    
            else: # 그렇지 않으면 뒷부분이 정렬되어 있습니다.
                # 타겟이 정렬된 뒷부분에 위치하는지 확인합니다.
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1  # 타겟이 중앙값보다 크면, 시작점을 중앙값 뒤로 이동시킵니다.
                else:
                    end = mid - 1  # 타겟이 중앙값보다 작으면, 끝점을 중앙값 앞으로 이동시킵니다.

        # 타겟을 찾지 못했다면, -1을 반환합니다.
        return -1
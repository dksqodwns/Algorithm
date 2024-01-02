"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # 들어온 노드가 null이면 null 리턴
            return
        
        clones = {} # 생성 된 노드를 저장해 둘 해시 테이블
        
        def dfs(node):
            if node in clones: # 해시 테이블의 키 존재 여부 확인 => 있으면 해당 값을 반환해주면 됨.
                return clones[node] # 해당 키 값 반환

            # 존재하지 않으면? 노드를 따로 복제해주어야 함.

            clone = Node(node.val) # 클래스를 이용해서 동일한 값으로 노드 복제
            clones[node] = clone # 원래 노드를 키, 복제된 노드를 값으로 

            # 다르 노드와 연결

            for i in node.neighbors: # neighbors 리스트 순회 -> 이웃하고 있는 노드들이 i가 됨
                clone.neighbors.append(dfs(i)) # 복제된 노드의 리스트에 복제된 이웃을 추가 (이웃이 두개라면 dfs 두번 호출)

            return clone
        
        return dfs(node)
    
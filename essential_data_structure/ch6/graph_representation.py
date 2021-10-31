class Graph:
    def __init__(self, vertex_num=None):
        # 인접 리스트
        self.adj_list = []
        self.vtx_num = 0

        # 정점이 있으면 True
        # 정점이 없으면 False
        self.vtx_arr = []

        # 정점 개수를 매개변수로 넘기면 초기화 진행
        if vertex_num:
            self.vtx_num = vertex_num
            self.vtx_arr = [True for _ in range(self.vtx_num)]
            # 배열 요소로 연결 리스트 대신 동적 배열 사용
            self.adj_list = [[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num == 0:
            return True
        return False

    def add_vertex(self):
        for i in range(len(self.vtx_arr)):
            # 중간에 삭제된 정점이 있을 경우
            # 이를 재사용
            # vtx_arr 값이 False면
            # 삭제된 정점이라는 의미
            if self.vtx_arr[i] == False:
                self.vtx_num += 1
                self.vtx_arr[i] = True
                return i

        # 삭제된 정점이 없다면 정점을 하나 추가
        self.adj_list.append([])
        self.vtx_num += 1
        self.vtx_arr.append(True)
        return self.vtx_num - 1

    def delete_vertex(self, v):
        if v >= self.vtx_num:
            raise Exception(f"There is no vertex of {v}")
        # 정점 v가 있으면
        if self.vtx_arr[v]:
            # 정점 v의 인접 정점 집합을 초기화
            self.adj_list[v] = []
            self.vtx_num -= 1
            self.vtx_arr[v] = False
            # 나머지 정점 중 v와 인접한 정점이 있다면
            # 그 정점의 리스트에서 v를 제거
            for adj in self.adj_list:
                for vertex in adj:
                    if vertex == v:
                        adj.remove(vertex)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def delete_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def adj(self, v):
        return self.adj_list[v]

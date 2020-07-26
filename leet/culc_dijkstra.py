import sys
import re
import heapq

# グラフの初期化
def initialize_graph():
  graph = {}
  edge_list = read_file()
  
  for edge_inf in edge_list:
    node1 = edge_inf.split(",")[0]
    node2 = edge_inf.split(",")[1]
    cost = int(edge_inf.split(",")[2])

    # ノードの設定と無向エッジのコスト設定
    graph = set_new_node(graph, node1, node2)
    graph[node1][node2] = cost
    graph[node1][node2] = cost
    return graph

def read_file():
  file_name = "edge_inf.csv"
  edge_list = []
  with open(file_name, "r") as fin:
    for line in fin.readlines():
      edge_list.append(re.sub(r"[\r\n]", "", line))
  return edge_list

def set_new_node(graph, node1, node2):
  if not node1 in graph.keys():
    graph[node1] = {}
  if not node2 in graph.keys():
    graph[node2] = {}
  return graph

def solve_by_dijkstra(graph):
  #ノード毎のSTARTからの最小コスト
  min_dist_dict = {}
  prev_node_dict = {}
  q = []
  headpq.heappush(q, (0, "START"))

  prev_node = ""

  while True:
    dist, node = heapq.headppop(q)
    min_dist_dict[node] = dist
    prev_node_dict[node] = prev_node

    if node == "GOAL":
      return min_dist_dict, prev_node_dict
    prev_node = node
    # 確定したノードから
    culc_min_dist_and_put(graph, q, node, min_dist_dict, prev_node_dict)

def culc_min_dist_and_put(graph, q, departure_node, min_dist_dict, prev_node_dict):
  for arrival_node in graph[departure_node].keys():
    tmp_d = min_dist_dict[departure_node] + graph[departure_node][arrival_node]
    # 遷移可能なノードについて直前に確定したノードから遷移した場合のコストを計算
    if arrival_node in min_dist_dict.keys():
      if tmp_d < min_dist_dict[arrival_node]:
        min_dist_dict[arrival_node] = tmp_d
        heapq.heappush(q, (min_dist_dict[arrival_node], arrival_node))
    else:
      min_dist_dict[arrival_node] = tmp_d
      heapq.heappush(q, (min_dist_dict[arrival_node], arrival_node))


if __name__ == "__main__":
  main()
  sys.exit(0)

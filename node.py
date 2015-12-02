class Node:
  def __init__(self, path_metric, historical_path, lookup_table):
    self.path_metric = path_metric
    self.historical_path = historical_path # newest to oldest
    self.lookup_table = lookup_table

  def create_next_nodes(self, transition_bits):
    key = self.historical_path[:len(transition_bits)]

    next_nodes = []
    for transition_info in self.lookup_table[key]:
      # unpack a possible transition from this state
      transition_bit = transition_info[0]
      parity_bits = transition_info[1]
      branch_metric = hamming_distance(parity_bits, transition_bits)

      # create the node which is the target of the transition
      next_path_metric = branch_metric + self.path_metric
      next_historical_path = transition_bit + self.historical_path
      next_node = Node(next_path_metric, next_historical_path, self.lookup_table)

      next_nodes.append(next_node)

    return next_nodes


def hamming_distance(str1, str2):
  hamming_dist = 0

  for i, char1 in enumerate(str1):
    char2 = str2[i]
    if char1 != char2:
      hamming_dist += 1

  return hamming_dist

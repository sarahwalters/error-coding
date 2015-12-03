from node import Node
import string_utils

class Trellis:
  def __init__(self, gen_polys, rcv_bits):
    self.gen_polys = gen_polys # generator polynomials, e.g. ['111', '110']
    self.k = len(gen_polys[0]) # window size, e.g. 3
    self.rcv_bits = rcv_bits
    self.lookup_table = self.gen_lookup() # maps from state ID to possible next state IDs
    self.col = [Node(0, "0"*(self.k-1), self.lookup_table, self.k)] # list of nodes for a column in the trellis. Initialized by
    # convention with a node whose prevoius path is 0's for the lenght of the window

  def gen_lookup(self):
    """
    Pre-computes the trellis transition information
    """
    lookup_table = {}
    for i in range(2**(self.k-1)): # for each node in the column
      key = string_utils.int_to_bin_string(i, self.k)
      transition_info = []
      for i in ["0", "1"]: #for both possible message bits (1 or 0)
        next_key = i + key[:-1]
        parity_arr = [string_utils.str_dot(poly, i+key) for poly in self.gen_polys]
        parity_bits = "".join(parity_arr)
        transition_info.append((i, parity_bits, next_key)) #determine the parity bits and next node
      lookup_table[key] = transition_info
    return lookup_table


  def create_next_col(self, parity_bits):
    """
    Creates a new trellis column given a group of parity bits
    """
    node_candidates = []
    new_column = []
    for node in self.col:
      single_list = node.create_next_nodes(parity_bits) #nodes a single prev node could go to
      node_candidates.append(single_list[0])
      node_candidates.append(single_list[1])

    for key in self.lookup_table:
      # then, groups all of the next_nodes by state id (eg '00') and keeps the one with the
      filtered_candidate_nodes = [n for n in node_candidates if n.historical_path[:self.k-1] == key]
      if len(filtered_candidate_nodes) >= 1:
        sorted_list = sorted(filtered_candidate_nodes, key=lambda x: x.path_metric, reverse=False)
        new_column.append(sorted_list[0])

    self.col = new_column


  def decode_message(self):
    """
    Decodes message using received bits and generator polynomials
    """
    start = 0
    while start < (len(self.rcv_bits)-1):
      end = start+len(self.gen_polys)
      self.create_next_col(self.rcv_bits[start:end]) #slide window with
      start += len(self.gen_polys)
    sorted_col = sorted(self.col, key=lambda x: x.path_metric, reverse=False) #sort by path metric
    backwards_message = sorted_col[0].historical_path[:-self.k+1] # returns the path with the lowest path_metric
    return backwards_message[::-1]


if __name__ == '__main__':
  t = Trellis(["111", "110"], "111011000110")
  print t.decode_message()

class Trellis:
  def __init__(self, gen_polys, rcv_bits):
    self.gen_polys = gen_polys # generator polynomials, e.g. ['111', '110']
    self.k = len(gen_polys[0]) # window size, e.g. 3
    self.rcv_bits = rcv_bits
    self.lookup_table = {} # maps from state ID to possible next state IDs
    self.col = None # will be a list of nodes

    def create_next_col(self):
      # calls create_next_nodes(node, transition_bits) for all of the nodes in self.col
      # then, groups all of the next_nodes by state id (eg '00') and keeps the one with the
      #     smallest path metric from each group
      pass

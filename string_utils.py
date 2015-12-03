def str_dot(s1,s2):
  """
  Calculates a dot product between bitstrings.
  """
  if len(s1)!=len(s2):
    raise Exception("Input bitstrings are not same length!")
  tmp_sum = 0
  for i in range(len(s1)):
    tmp_sum ^= (int(s1[i]) & int(s2[i])) #performs sum(a[i]*b[i]) on bins
  return str(tmp_sum)

def int_to_bin_string(integer, length):
  """
  Converts an integer to a binary string.
  """
  bin_string = bin(integer)[2:] #slice off the 0b
  if len(bin_string) < length-1: #left pad to correct length
    pad = "0" * (length -1 - len(bin_string))
    bin_string = pad + bin_string
  return bin_string

def hamming_distance(str1, str2):
  """
  Computes the hamming distance between two strings of the same length.
  """
  hamming_dist = 0

  for i, char1 in enumerate(str1):
    char2 = str2[i]
    if char1 != char2:
      hamming_dist += 1

  return hamming_dist

from trellis import Trellis
from encoder import Encoder
from string_utils import hamming_distance

def test(polys, ber, message=None, print_flag=False):
  if message == None:
    f = open('message.txt', 'rb') # holds a 1000-bit binary string
    message = f.read().strip()

  e = Encoder(polys, message, ber, print_flag=print_flag)
  encoded = e.encoded
  sent = e.send()

  t = Trellis(polys, sent)
  decoded = t.decode_message()

  if print_flag:
    print 'Message: %s' % message
    print 'Decoded: %s' % decoded

  return hamming_distance(message, decoded)

if __name__ == '__main__':
  polys =  ('1011', '1111', '0101')
  test(polys, 0.1, message='110110', print_flag=True)

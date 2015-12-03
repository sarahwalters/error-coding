from trellis import Trellis
from encoder import Encoder

if __name__ == '__main__':
  polys =  ('1011', '1111', '0101')
  message = '10111'

  a = Encoder(polys, message, 0.05)
  encoded = a.encoded
  sent = a.send()

  t = Trellis(polys, sent)
  decoded = t.decode_message()

  print 'Message: %s' % message
  print 'Decoded: %s' % decoded

import random
import string_utils

class Encoder:
  def __init__(self, gen_polys, mesg, err_rate):
    """
    gen_polynomials is a list a length k generator polynomials
    mesg is a string containing the bit message to transmit
    err_rate is a fraction that determines
    """
    self.gen_polys = gen_polys
    self.err_rate = err_rate
    self.k = len(gen_polys[0]) #The window size
    self.r = len(gen_polys) #The number of parity bits made
    self.mesg = '0'*(self.k-1)+mesg
    self.encoded = self.__encode()


  def __encode(self):
    """
    Encodes the raw message with the supplied generators.
    """
    tmp_msg = ""
    for i in range(len(self.mesg)-self.k+1):
      for g in self.gen_polys:
        last = string_utils.str_dot(self.mesg[i:i+self.k], g[::-1]) # reverse g
        tmp_msg+=last
    return tmp_msg


  def send(self):
    """
    Takes the encoded message and causes errors
    I repent for ugly string manipulation! >_<
    """
    count = 0
    noisy_msg = [int(x) for x in self.encoded]
    for i in range(len(noisy_msg)):
      if random.random()<=self.err_rate:
        noisy_msg[i]=noisy_msg[i]^1
        count+=1
    print count, 'error(s) generated at', self.err_rate,'error rate.'
    return ''.join([str(x) for x in noisy_msg])

if __name__ == '__main__':
  #This particular test case from http://wits.ice.nsysu.edu.tw/course/pdfdownload/93_2/%E9%8C%AF%E8%AA%A4%E6%9B%B4%E6%AD%A3%E7%A2%BC/CC-ConvolutionalCode.pdf  
  polys =  ('1011','1111')
  a = Encoder(polys,'10111',0.1)
  print "Input Message with 0 padding is", a.mesg
  print "Message encodes as", a.encoded
  print a.send(), "is noisy message"

from test_bench import test
import matplotlib.pyplot as plt
import time

def accuracy_vs_rate():
  # run simulations
  ber = 0.1
  num_iterations = 100
  polys = ('1011', '1111', '0101', '1101', '1010', '1001', '0110')
  rate_reciprocals = range(2, len(polys)+1)
  polys_list =  [polys[:recip] for recip in rate_reciprocals]
  accuracies = [accuracy(p, ber, num_iterations) for p in polys_list]
  rates = [1/float(recip) for recip in rate_reciprocals]

  # plot and format
  fig = plt.figure()
  plt.plot(rates, accuracies, 'ro', markersize=10)
  plt.title('Accuracy vs. Rate for k=%s, BER=%s' % (len(polys[0]), ber))
  plt.xlabel('Rate, 1/r')
  plt.ylabel('Hamming distance over 1000 bits')
  plt.show()
  fig = plt.gcf()
  fig.savefig('imgs/accuracy_vs_rate.png')
  return rates, accuracies


def accuracy(polys, ber, num_iterations):
  sum_error = 0

  for _ in range(num_iterations):
    sum_error += test(polys, ber)

  return sum_error/float(num_iterations)

def accuracy_vs_windowsz(max_window = 10):
  # Larger window sizes obtained by repeating polys.
  ber = 0.1
  polys = ['11','10','01']
  num_iterations = 10
  accuracies = []
  sizes = range(2,max_window+2)
  for i in range(max_window):
    print "Testing with window size ",i+2
    now=time.time()
    accuracies.append(accuracy(polys,ber,num_iterations))
    print "Accuracy was ",accuracies[-1]
    print "Test took ",time.time()-now,"seconds."
    if len(polys[0]) < max_window:
      for p_i in range(len(polys)):
        polys[p_i]+=str(1-int(polys[p_i][-1]))

  plt.plot(sizes,accuracies)
  plt.title('Accuracy vs. Window Size, BER=%s' % ber)
  plt.xlabel('Window Size, k')
  plt.ylabel('Hamming distance over 1000 bits')
  plt.show()
  fig = plt.gcf()
  fig.savefig('imgs/accuracy_vs_window_size.png')
  return (sizes, accuracies)


if __name__ == '__main__':
  #print accuracy_vs_rate()
  accuracy_vs_windowsz()

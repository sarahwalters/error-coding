from test_bench import test
import matplotlib.pyplot as plt


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

if __name__ == '__main__':
  print accuracy_vs_rate()

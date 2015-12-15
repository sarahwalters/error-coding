###A Python implementation of a convolutional error correcting code.
######Kyle Flores, Lindsey Vanderlyn, Sarah Walters
######Olin College Discrete Math Fall 2015

Directory structure:
* `encoder.py` contains a convolutional encoder class
* `trellis.py` contains a Viterbi decoder class
  * `node.py` defines a class which represents a state in the decoder trellis
* `string_utils.py` contains peripheral utility functions
* `test_bench.py` instantiates an encoder and a decoder and simulates the sending of a message
* `graphs.py` produces the graphs found in the [imgs directory](/imgs)

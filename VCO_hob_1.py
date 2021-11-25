import math
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """genera una senoidad cuyos parametros pueden ser manipulados por las senales entrantes asi: la primera senal manipula la amplitud; la segunda la frecuencia; la tercera la fase"""
    def __init__(self, ):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='VCO_hob_fc',   # will show up in GRC
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        self.n_m=0 # guarda el ultimo valor de n
        #self.f=f
        #self.samp_rate=samp_rate

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m, self.n_m+N-1,N)
        self.n_m += N
        #y[:]=A*np.cos(2*math.pi*self.f*n/self.samp_rate+P)
        y[:]=A*np.exp(1j*Q)
        return len(y)

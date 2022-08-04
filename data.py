class Distributor(object):
    def __init__(self, a1, b1, a2, b2):
        self.a1, self.b1, self.a2, self.b2 = a1, b1, a2, b2

    def split(self, str_in):
        a1i = self.a1
        b1i = a1i+self.b1
        a2i = b1i+self.a2
        b2i = a2i+self.b2
        a1 = str_in[0: a1i]
        b1 = str_in[a1i: b1i]
        a2 = str_in[b1i: a2i]
        b2 = str_in[a2i: b2i]
        N = 2 ** self.a2

        a1, b1, a2, b2 = [int(i, 2) for i in [a1, b1, a2, b2]]
        return a1, b1, a2, b2

    def __call__(self, seq):
        a1_seq, b1_seq, a2_seq, b2_seq = [list() for _ in range(4)]
        for state in seq:
            a1, b1, a2, b2 = self.split(state)
            a1_seq.append(a1)
            b1_seq.append(b1)
            a2_seq.append(a2)
            b2_seq.append(b2)
        return a1_seq, b1_seq, a2_seq, b2_seq


def find(value, seq, indices=None):
    indices = indices if indices is not None else list(range(len(seq)))
    indices_filtered = list()
    for i in indices:
        if value == seq[i]:
            indices_filtered.append(i)
    return indices_filtered


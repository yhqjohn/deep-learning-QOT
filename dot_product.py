import torch
import random


def sub_multinoulli(x):
    factor = random.random() < x.sum()
    c = torch.multinomial(x, 1)
    return factor * torch.nn.functional.one_hot(c, len(x))[0]


def xor_sum(x):
    ans = False
    for i in x:
        ans = i ^ ans
    return ans


class OTFailError(Exception):
    pass


def ot(ot0, ot1, s, memory):
    random.shuffle(memory)
    pass0 = filter(lambda x: int(x[0])==ot0, memory)
    pass1 = filter(lambda x: int(x[1])==ot1, pass0)
    pass2 = filter(lambda x: int(x[2])==s, pass1)
    return int(next(pass2)[3])


def ot_mul(a, b, memory):
    a_bin = sub_multinoulli(a).type(torch.bool)
    b_bin = sub_multinoulli(b).type(torch.bool)
    k_bin = torch.randint(0, 2, a.shape)
    ot0s = torch.logical_xor(a_bin, k_bin)
    ot1s= torch.logical_xor(torch.zeros(a.shape), k_bin)
    cs = [ot(ot0, ot1, s, memory) for ot0, ot1, s in zip(ot0s, ot1s, b_bin)]
    c = xor_sum(cs)
    k = xor_sum(k_bin)
    return k ^ c


def ot_mul_stats(a, b, memory, shots=1000):
    lst = [ot_mul(a,b,memory) for _ in range(shots)]
    return sum(lst)/len(lst)


def lambda_factor(err, n):
    return 0.5 - 0.5 * ((1 - 2*err)**n)


def corrected_l(p, l=0.):
    return (p-l)/(1 - 2*l)

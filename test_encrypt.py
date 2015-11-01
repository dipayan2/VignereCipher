from vignere import Vignere
p = raw_input()
k = raw_input()

p = Vignere.encrypt(p, k, len(k))
print p
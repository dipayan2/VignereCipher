from vignere import Vignere
c = raw_input()
k = raw_input()

p = Vignere.decrypt(c, k, len(k))
print p
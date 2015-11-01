#!/usr/bin/python

import gflags
import re
import os

eng_prob_vals = {
  0: .082, 13: .067,
  1: .015, 14: .075,
  2: .028, 15: .019,
  3: .043, 16: .001,
  4: .127, 17: .060,
  5: .022, 18: .063,
  6: .020, 19: .091,
  7: .061, 20: .028,
  8: .070, 21: .010,
  9: .002, 22: .023,
  10: .008, 23: .001,
  11: .040, 24: .020,
  12: .024, 25: .001
}

def most_frequent_trigram(inp):
  tri_map = {}

  for i in range(0, len(inp)-2):
    if inp[i:i+3] not in tri_map:
      tri_map[inp[i:i+3]] = 0
    
    tri_map[inp[i:i+3]] = tri_map[inp[i:i+3]] + 1

  max_freq = -1
  max_tri = ''

  for trigram in tri_map:
    if max_freq < tri_map[trigram]:
      max_freq = tri_map[trigram]
      max_tri = trigram

  return max_tri

def GCD(a, b):
  if b == 0:
    return a
  else:
    return GCD(b, a % b)

def key_len(inp, mf_trigram):
  dist_list = [m.start() for m in re.finditer(mf_trigram, inp)]
  for i in range(1,len(dist_list)):
    dist_list[i] = dist_list[i] - dist_list[0]

  gcd = reduce(lambda x,y:GCD(x,y),dist_list[1:])

  return gcd

def Ic(inp):
  char_freq = {}
  for c in range(0, 26):
    char_freq[chr(c + ord('A'))] = 0

  for c in inp:
    char_freq[c] = char_freq[c] + 1

  num_sum = 0

  for c in char_freq:
    num_sum = num_sum + char_freq[c]*(char_freq[c]-1)

  ic_value = float(num_sum)/float(len(inp)*(len(inp)-1))

  return ic_value

def ic_list(yi_strings):
  ic_vals = []

  for s in yi_strings:
    ic_vals.append(Ic(s))

  return ic_vals

def yi_strings(inp, m):
  yi_list = ['' for i in range(m)]

  for i in range(0, len(inp)):
    yi_list[i%m] = yi_list[i%m] + inp[i]

  return yi_list

def check_validity(ic_vals):
  length = len(ic_vals)
  count = 0
  for ic_val in ic_vals:
    if(abs(ic_val - 0.065) < 0.01):
      count = count +1
  
  if(float(count) > 0.5 * float(length)):
    return True
  return False

def verify_m(inp, m):
  for l in xrange(m, 0, -1):
    yi_list = yi_strings(inp, l)
    ic_vals = ic_list(yi_list)
    if(check_validity(ic_vals)):
      return yi_list

def iThKeyChar(yi):
  char_freq = {}

  for i in range(0,26):
    char_freq[i] = 0

  for c in yi:
    j = ord(c)-ord('A')
    char_freq[j] = char_freq[j] + 1

  mg_list = []

  for g in range(0, 26):
    num_sum = 0.0
    for i in range(0, 26):
      num_sum = num_sum + eng_prob_vals[i]*char_freq[(i+g)%26]

    mg_list.append(float(num_sum)/float(len(yi)))

  diff = 100.0

  for i in range(0, 26):
    if(abs(mg_list[i]-0.065) < diff):
      diff = abs(mg_list[i]-0.065)
      key_var = i

  return chr(ord('A') + key_var)

def get_key(yi_list):
  key = ''

  for yi in yi_list:
    key = key + iThKeyChar(yi)

  return key

def cryptanalysis(inp):
  mf_trigram = most_frequent_trigram(inp)
  m = key_len(inp, mf_trigram)
  yi_list = verify_m(inp, m)
  return get_key(yi_list)

def main():
  inp = str(raw_input())
  print cryptanalysis(inp)

if __name__ == '__main__':
  main()
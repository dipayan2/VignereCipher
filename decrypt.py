def decrypt(cipher, key, m):
	plain = ''
	x = []
	for i in range(len(cipher)):
		x.append((ord(cipher[i])-ord(key[i%m])+26)%26)
		plain += chr((ord(cipher[i])-ord(key[i%m])+26)%26+97)

	print plain

if __name__ == '__main__':
	c=raw_input()
	k=raw_input()
	m=len(k)
	decrypt(c, k, m)
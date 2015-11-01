def encrypt(plaintext, key, m):
	""" encrypts plain text
		input: 
			   string: plaintext(lower case)
			   string: key(upper case)
			   int: m
	    output: 
	    		string: ciphertext 
	"""

	ciphertext = ""
	for i,x in enumerate(plaintext):
		y = (ord(x) - ord('a') + ord(key[i%m]) - ord('A')) % 26
		y = y + ord('A')
		y = chr(y)
		ciphertext+=y

	return ciphertext

ciphertext = encrypt("manav", "BCD", 3)
print ciphertext

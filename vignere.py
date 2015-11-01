class Vignere:
	'''
	This class describes encryption and decryption functions of Vignere Cipher
	'''
	@staticmethod
	def encrypt(
				plaintext, 
				key, 
				m
				):
		'''
		encrypts plain text

		parameters
		------------------------------------
	   	string: plaintext(lower case)
	   	string: key(upper case)
	   	int: m

	   	returns
	   	------------------------------------
	    string: ciphertext
	    '''

		ciphertext = ""
		for i,x in enumerate(plaintext):
			y = (ord(x) - ord('a') + ord(key[i%m]) - ord('A')) % 26
			y = y + ord('A')
			y = chr(y)
			ciphertext+=y

		return ciphertext

	@staticmethod
	def decrypt(
				ciphertext,
				key,
				m
				):
		'''
		decrypts cipher text
		parameters
		-----------------------------------
		string: ciphertext
		string: key
		int: m

		returns
		-----------------------------------
		string: plaintext
		'''
		plaintext = ''
		for i in range(len(ciphertext)):
			plaintext += chr((ord(ciphertext[i])-ord(key[i%m])+26)%26+97)

		return plaintext
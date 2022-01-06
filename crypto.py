from hashlib import sha512

def crypto_pass(password):
	for i in range(15000):
		password = sha512(password.encode('utf-8')).hexdigest()
	return password
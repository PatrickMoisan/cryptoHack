from Crypto.PublicKey import RSA


rsa_key = RSA.import_key(open('/Users/patrickmoisan/Desktop/py\ code\ /cryptoHack-2/Gerneral/DataFormats/2048b-rsa-example-cert.der', 'rb').read())

print(rsa_key.n)
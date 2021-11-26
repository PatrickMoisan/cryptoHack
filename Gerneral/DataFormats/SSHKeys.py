from Crypto.PublicKey import RSA


rsa_key = RSA.import_key(open('/Users/patrickmoisan/Desktop/py\ code\ /cryptoHack-2/Gerneral/DataFormats/bruce_rsa.pub ', 'rb').read())

print(rsa_key.n)
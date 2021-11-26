from Crypto.PublicKey import RSA

rsa_key = RSA.import_key(open('/Users/patrickmoisan/Desktop/py code /cryptoHack-2/Gerneral/DataFormats/privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'rb').read())

print(rsa_key.n)


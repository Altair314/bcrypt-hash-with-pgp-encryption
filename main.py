import bcrypt
import gnupg
import os
import sys

gpg = gnupg.GPG(gnupghome=os.path.dirname(os.path.abspath(sys.argv[0])))
gpg.encoding = 'utf-8'


pubkey = gpg.import_keys_file('pub-key.asc')
user_pass = input("Please input password: ")

password_hash = bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt(prefix=b"2a"))
#print(password_hash)

print(repr(str(gpg.encrypt(password_hash, pubkey.fingerprints[0], always_trust=True))))

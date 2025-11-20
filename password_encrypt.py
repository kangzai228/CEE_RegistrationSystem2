# 使用基于C库的 gmssl-python 库
from gmssl import *

# 1. 生成SM2密钥对
# key_pair = Sm2KeyPair.generate_key_pair()
# public_key = key_pair.public_key
public_key ="04d5982dcb21ad8bd5df69bc63984c2ae6550fcb2aae5cb1941afc76146a0570ea532fe1695e6103b888b2af4f7ad15b1c07a33a8ba8ad02205dc24b20ebb287f7"
# private_key = key_pair.private_key

# 2. 初始化加密上下文（使用公钥）
encryptor = Sm2Encryption(public_key)

pwd="#ydzxgk2026#_2025-11-20 10:29:49"
# 3. 待加密的数据
data = pwd.encode('utf-8')

# 4. 使用公钥进行加密
ciphertext = encryptor.encrypt(data)
print(f"加密后的数据 (Hex): {ciphertext.hex()}")

# 5. 初始化解密上下文（使用私钥）
# decryptor = Sm2Decryption(private_key)

# 6. 使用私钥进行解密
# plaintext = decryptor.decrypt(ciphertext)
# print(f"解密后的数据: {plaintext.decode('utf-8')}")
from gmssl import *
import base64

def sm2_encrypt(public_key, plaintext):
    """
    使用SM2公钥加密数据
    Args:
        public_key: SM2公钥
        plaintext (bytes/str): 待加密的明文数据，如果是字符串会被编码为bytes
    Returns:
        bytes: 加密后的密文数据
    """
    # 确保明文是bytes类型
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # 初始化SM2加密上下文 [citation:1]
    encryptor = Sm2Encryption(public_key)
    
    # 执行加密 [citation:2]
    ciphertext = encryptor.encrypt(plaintext)
    
    return ciphertext


# 示例使用
if __name__ == "__main__":
    # 1. 生成密钥对
    public_key="04d5982dcb21ad8bd5df69bc63984c2ae6550fcb2aae5cb1941afc76146a0570ea532fe1695e6103b888b2af4f7ad15b1c07a33a8ba8ad02205dc24b20ebb287f7"
    print("密钥对生成成功！")
    
    # 2. 准备待加密的数据
    original_data = "这是一条需要加密的敏感信息。"
    print(f"原始数据: {original_data}")
    
    # 3. 加密数据
    encrypted_data = sm2_encrypt(public_key, original_data)
    # 将加密后的bytes转换为Base64字符串以便于传输或存储 [citation:4]
    encrypted_b64 = base64.b64encode(encrypted_data).decode('utf-8')
    print(f"加密后的数据 (Base64): {encrypted_b64}")
    

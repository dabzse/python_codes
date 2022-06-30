from cryptography.fernet import Fernet
 
message = "this will be encrypted, and decrypted"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
 
print(f"original string: {message}")
print(f"encrypted string: {encMessage}")
 
decMessage = fernet.decrypt(encMessage).decode()
 
print(f"decrypted string: {decMessage}")

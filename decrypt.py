import pyAesCrypt, os
os.chdir("C:\\Users\\brobi\\Desktop")
password=""
pyAesCrypt.decryptFile('main.aes','main.py', password)
pyAesCrypt.decryptFile('data_storage.aes','data_storage.py',password)
pyAesCrypt.decryptFile('data_storage_back.aes','data_storage_back.py',password)
pyAesCrypt.decryptFile('junk_save.aes','junk_save.py',password)
pyAesCrypt.decryptFile('custom_func.aes','custom_func.txt',password)
"""
Project Name: Kms_Vault
Project Description: Write a python program that gets a message and encrypts/decrypts
it using “aes256-gcm96”
Programmer: Michaela Pierce
Date: 11/17/2022
UNCW, CSC 592 - Introduction to Cryptography
"""

"""
The steps to use Vault are:
1. start vault 
    vault server -dev
2. set vault address 
    set VAULT_ADDR = http://127.0.0.1:8200
3. set VAULT_TOKEN
    set VAULT_TOKEN = (token returned from previous step)
4. type in vault address into browser / sign in using token 
5. enable transit engine 
    vault secret enable transit
6. create a key 
    vault write transit/keys/keyname type=aes256-gcm96
7. encrypt data 
    vault write transit/encrypt/k1 plaintext=$(base64 <<< "message")
8. decrypt data
    vault write transit/decrypt/k1 ciphertext [cipher text]
"""

# You MUST have Vault Server running before launching this program

import os
import base64

#os.system("vault kv get secret/hello")
#os.system("set VAULT_ADDR= http://127.0.0.1:8200")
# to manipulate vault server use these functions
# os.system("<vault command to execute>")
# os.environ["<target environment variable>"]="<value>"

def configserver(token):
    # input is the root token of vault server (in main())
    # assigns variables for the server
    token = os.environ.get('VAULT_TOKEN')
    os.system("vault secrets enable transit")
    os.system("vault write transit/keys/mytestkey type=aes256-gcm96")


def base64EncodeToString(message):
    # input is the message to encode (in main())
    # output is the message converted to a string 'message'that is in base64
    base64_message = base64.b64encode(bytes('message', 'utf-8'))
    return base64_message

def base64DecodeToString(message):
    #input is base64 message to decode
    #output is the message converted to a string in ASCII
    convert_message = message.encode(encoding='ascii')
    return convert_message


def encryptInServer (message):
    #input is plaintext message to be encrypted
    
    #does not return an output
    #runs the vault server commands to encrypt the message found in
    #original vault lab


def decryptInServer(ciphertext):
    #input is the encrypted base64 message
    #returns the decrypted string in ASCII
    plaintext_bytes= base64.b64decode(plaintext_bytes)
    plaintext = plaintext_bytes.decode(decoding='ascii')

# Driver Code
if __name__ == "__main__":
    #header 
    print("VAULT SERVER")
    print(" ")
    print("It is important that you have Vault Server running already for the\nprogram to work correctly!")
    
   
    #function configserver
    # input is the root token of vault server (in main())
    token = input("Please enter the Vault token: ")
    # assigns variables for the server
    configserver(token)    
    
    #function base64EncodeToString
    # ask user for message
    # input is the message to encode (in main())
    message = input("Please enter the message you would like encrypted: ")
    # output is the message converted to a string 'message'that is in base64 encode message
    message_string= str(base64EncodeToString(message), 'utf-8')
    
    #function base64DecodeToString
    #input is base64 message to decode
    message = base64DecodeToString(message_string)
    #output is the message converted to a string in ASCII
    print("This is the message converted to a string in ASCII", message)

    #function encryptInServer
    #does not return an output
    #runs the vault server commands to encrypt the message found in
    #original vault lab
    ciphertext = encryptInServer(message)


    #function decryptInServer
    #input is the encrypted base64 message
    #returns the decrypted string in ASCII
    plaintext = decryptInServer(ciphertext)
    print("This is the plaintext : ", plaintext)
    

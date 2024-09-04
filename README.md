# Kms_Vault
The Kms_Vault project is a Python program designed to interact with a Vault server for encrypting and decrypting messages using the AES256-GCM96 algorithm. The program utilizes the Vault server's transit secrets engine to securely handle encryption and decryption tasks. The goal is to demonstrate how to use Vault's capabilities for cryptographic operations in a practical scenario.


## Features
- **Vault Server Integration:** Configures and interacts with a Vault server for encryption and decryption operations.
- **AES256-GCM96 Encryption:** Utilizes AES256-GCM96 algorithm for secure message encryption.
- **Base64 Encoding/Decoding:** Converts messages to and from base64 encoding for secure transmission.
- **User Interaction:** Prompts users for input and displays results of encryption and decryption.

## Requirements
- **Vault Server:** Ensure Vault server is installed and running.
- **Python 3.x:** Ensure Python 3.x is installed.
- **Vault CLI:** Requires Vault command-line interface for interacting with the server.

## Installation & Usage

1. **Start Vault Server**:
   ```bash
   vault server -dev
   ```

2. **Set Vault Address**:
   ```bash
   set VAULT_ADDR=http://127.0.0.1:8200
   ```

3. **Set VAULT_TOKEN**:
   ```bash
   set VAULT_TOKEN=(token returned from previous step)
   ```

4. **Access Vault Server**:
    - Type the Vault address into your browser and sign in using the token.

5. **Enable Transit Engine**:
   ```bash
   vault secrets enable transit
   ```

6. **Create a Key**:
   ```bash
   vault write transit/keys/mytestkey type=aes256-gcm96
   ```

7. **Encrypt Data**:
   ```bash
   vault write transit/encrypt/mytestkey plaintext=$(base64 <<< "message")
   ```

8. **Decrypt Data**:
   ```bash
   vault write transit/decrypt/mytestkey ciphertext=<ciphertext>
   ```

## Example Usage

1. **Run the Program**:
   ```bash
   python kms_vault.py
   ```

2. **Follow the Prompts**:
    - Enter the Vault token when prompted.
    - Enter the message you want to encrypt.

3. **Output Information**:
    - The program will display the base64 encoded message, its ASCII representation, and the decrypted plaintext.

### Example Output

```plaintext
VAULT SERVER

It is important that you have Vault Server running already for the program to work correctly!

Please enter the Vault token: [token]

Please enter the message you would like encrypted: [message]

This is the message converted to a string in ASCII: [base64_encoded_message]

This is the plaintext: [decrypted_message]
```


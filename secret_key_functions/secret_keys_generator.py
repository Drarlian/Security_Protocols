# UTILIZANDO SECRETS PARA GERAR CHAVES SEGURAS: (UTILIZADA PARA CRIAR E VALIDAR TOKENS)
import secrets

# Gerar uma chave secreta de 256 bits (32 bytes)
secret_key = secrets.token_hex(32)  # Representação hexadecimal de 32 bytes (256 bits)

print(f'Chave Secreta: {secret_key}')

# Chave Secreta: 90a7fd04393bd527abe773f93a486277e8ed830058e812499ae197147679f022
# Chave Secreta: c56a16fe243f2a9743991725ba78d9374a63cc5193934307c1e7a8b228988b64

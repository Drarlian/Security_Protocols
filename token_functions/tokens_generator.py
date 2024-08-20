# CRIANDO TOKENS
import jwt
import datetime

# Chave secreta para assinatura dos tokens
SECRET_KEY = 'sua_chave_secreta'


def generate_tokens(user_id):
    # Definição do tempo de expiração
    access_token_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=15)  # 15 minutos
    refresh_token_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=7)  # 7 dias

    print(f'Token Padrão Data: {access_token_exp}')
    print(f'Refresh Token Data: {refresh_token_exp}')

    # Payload do token de acesso
    access_payload = {
        'user_id': user_id,
        'exp': access_token_exp
    }

    # Payload do refresh token
    refresh_payload = {
        'user_id': user_id,
        'exp': refresh_token_exp
    }

    # Geração dos tokens
    access_token = jwt.encode(access_payload, SECRET_KEY, algorithm='HS256')
    refresh_token = jwt.encode(refresh_payload, SECRET_KEY, algorithm='HS256')

    return access_token, refresh_token


def verify_token(token):
    try:
        # Decodificar e verificar o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Token expirado'
    except jwt.InvalidTokenError:
        return 'Token inválido'


def refresh_access_token(refresh_token):
    try:
        # Decodificar e verificar o refresh token
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=['HS256'])

        # Gerar novo token de acesso
        user_id = payload['user_id']
        new_access_token, _ = generate_tokens(user_id)

        return new_access_token
    except jwt.ExpiredSignatureError:
        return 'Refresh token expirado'
    except jwt.InvalidTokenError:
        return 'Refresh token inválido'


# Exemplo de uso: (generate_tokens)
user_id_out = 123
access_token_out, refresh_token_out = generate_tokens(user_id_out)
print(f'Access Token: {access_token_out}')
print(f'Refresh Token: {refresh_token_out}')


# Exemplo de uso: (verify_token)
decoded_payload_out = verify_token(access_token_out)
print(decoded_payload_out)


# Exemplo de uso: (refresh_access_token)
new_access_token_out = refresh_access_token(refresh_token_out)
print(f'Novo Access Token: {new_access_token_out}')

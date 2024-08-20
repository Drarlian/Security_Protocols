# UTILIZAÇÃO DO BCRYPT:
import bcrypt

senha = b'teste'
print(senha)

# salt = bcrypt.gensalt()
# print(bcrypt.gensalt())

# hashed_password = bcrypt.hashpw(senha, b'$2b$12$nfBMC2AjzoYYTcpjKltOn.')
hashed_password = bcrypt.hashpw(senha, bcrypt.gensalt())

print(hashed_password)

# b'$2b$12$nfBMC2AjzoYYTcpjKltOn../DOIdvybUoB7XuEasUjwzRZhh1tCWW'  # -> Com gensalt() fixo.
# b'$2b$12$nfBMC2AjzoYYTcpjKltOn../DOIdvybUoB7XuEasUjwzRZhh1tCWW'  # -> Com gensalt() fixo.

# b'$2b$12$0Ju/LfPdLvZ9ZaLpU4Kwlu98gUmxiS15YnGGXJRzNqIacTsB060GS'  # -> Com gensalt() aleátorio.
# b'$2b$12$X1blBf.VcaoJOcgHCPq6z.ufdg1tPBudP34l9qc.FwiF7dQmNhEfK'  # -> Com gensalt() aleátorio.

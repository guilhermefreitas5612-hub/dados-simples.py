print("=" * 50)
print("  Olá campeão, bem-vindo ao Sistema de Dados!")
print("=" * 50)
print("Este sistema coleta suas informações e as exibe de forma organizada.")
print()

nome = input("Digite o seu nome: ").strip()
if nome == "":
    print("Erro: o nome não pode ficar em branco!")
    exit()

idade = input("Digite sua idade: ").strip()
if not idade.isdigit():
    print("Erro: a idade deve ser um número válido!")
    exit()

time_favorito = input("Digite seu time do coração: ").strip()
if time_favorito == "":
    print("Erro: o time não pode ficar em branco!")
    exit()

print()
print("=" * 50)
print("        ✅ Dados cadastrados com sucesso!")
print("=" * 50)
print(f"  Nome:  {nome}")
print(f"  Idade: {idade} anos")
print(f"  Time:  {time_favorito}")
print("=" * 50)
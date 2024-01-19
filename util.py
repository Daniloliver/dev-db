from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Julio', idade=22)
    print(pessoa)
    pessoa.save()
    
# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    
    for p in pessoa:
        print(p.nome)

# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Julio').first()
    pessoa.idade = 26
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Julio').first
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    consulta_pessoas()
    # altera_pessoas()
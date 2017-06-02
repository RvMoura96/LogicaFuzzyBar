#coding=utf-8
"""
Listagem das variaveis 
"""
op = ''
refri = 0
ml = 0
rum = 0
mgelo = 0
contAux = ''
rFraco = 0
rSuave = 0
rForte = 0
rGelo = 0
Suave = 0
Fraco = 0
Forte = 0
Paladar = 0

"""
Sistema desenvolvido para determinar o teor e precificação do drink Cuba Livre, por meio de
utilização de logica Fuzzy para disciplina de IA.
Autor: Renan Moura
"""

def printSuave(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri):
    """
    Função responsável pela exibição dos resultados obtidos através da execução do software e o
    teor do drink for Suave.
    """
    if refri == 1:
        print('Drink com Teor Suave seu valor será de R$ 20,00\n')
        print('Expressão para o Paladar Fraco\nMax(Min(CocaFraca(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaFraca(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumFraco(', rum, '), Gelo(', mgelo, ')) = ', Fraco, '\n')

        print('Expressão para o Paladar Suave\nMax(Min(CocaForte(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaFraca(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Suave, '\n')

        print('Expressão para o Paladar Forte\nMax(Min(CocaForte(', ml, '), RumSuave(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaForte(', ml, '), RumForte(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Forte, '\n')

        print('Expressão para o Teor do Drink é Max(Suave(', Suave,
              '), Forte(', Forte, '), Fraco(', Fraco, '))\n')
    else:
        print('Drink com Teor Suave seu valor será de R$ 20,00\n')
        print('Expressão para o Paladar Fraco\nMax(Min(PepsiFraca(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiFraca(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumFraco(', rum, '), Gelo(', mgelo, ')) = ', Fraco, '\n')

        print('Expressão para o Paladar Suave\nMax(Min(PepsiForte(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiFraca(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Suave, '\n')

        print('Expressão para o Paladar Forte\nMax(Min(PepsiForte(', ml, '), RumSuave(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiForte(', ml, '), RumForte(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Forte, '\n')


        print('Expressão para o Teor do Drink é Max(Suave(', Suave,
              '), Forte(', Forte, '), Fraco(', Fraco, '))\n')


def printFraco(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri):
    """
    Função responsável pela exibição dos resultados obtidos através da execução do software e
    o teor do drink for Fraco.
    """
    if refri == 1:
        print('Drink com Teor Fraco seu valor será de R$ 15,00\n')
        print('Expressão para o Paladar Fraco\nMax(Min(CocaFraca(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaFraca(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumFraco(', rum, '), Gelo(', mgelo, ')) = ', Fraco, '\n')

        print('Expressão para o Paladar Suave\nMax(Min(CocaForte(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaFraca(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Suave, '\n')

        print('Expressão para o Paladar Forte\nMax(Min(CocaForte(', ml, '), RumSuave(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaForte(', ml, '), RumForte(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Forte, '\n')

        print('Expressão para o Teor do Drink é Max(Suave(', Suave,
              '), Forte(', Forte, '), Fraco(', Fraco, '))\n')

    else:
        print('Drink com Teor Fraco seu valor será de R$ 15,00\n')
        print('Expressão para o Paladar Fraco\nMax(Min(PepsiFraca(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiFraca(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumFraco(', rum, '), Gelo(', mgelo, ')) = ', Fraco, '\n')

        print('Expressão para o Paladar Suave\nMax(Min(PepsiForte(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiFraca(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Suave, '\n')

        print('Expressão para o Paladar Forte\nMax(Min(PepsiForte(', ml, '), RumSuave(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiForte(', ml, '), RumForte(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Forte, '\n')


        print('Expressão para o Teor do Drink é Max(Suave(', Suave,
              '), Forte(', Forte, '), Fraco(', Fraco, '))\n')


def printForte(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri):
    """
    Função responsável pela exibição dos resultados obtidos através da execução do software e
    o teor do drink for Forte.
    """
    if refri == 1:
        print("Drik com Teor Forte seu valor será de R$ 25,00\n")
        print('Expressão para o Paladar Fraco\nMax(Min(CocaFraca(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaFraca(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumFraco(', rum, '), Gelo(', mgelo, ')) = ', Fraco, '\n')

        print('Expressão para o Paladar Suave\nMax(Min(CocaForte(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaFraca(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Suave, '\n')

        print('Expressão para o Paladar Forte\nMax(Min(CocaForte(', ml, '), RumSuave(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(CocaForte(', ml, '), RumForte(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(CocaSuave(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Forte, '\n')

        print('Expressão para o Teor do Drink é Max(Suave(', Suave,
              '), Forte(', Forte, '), Fraco(', Fraco, '))\n')
    else:
        print("Drik com Teor Forte seu valor será de R$ 25,00\n")
        print('Expressão para o Paladar Fraco\nMax(Min(PepsiFraca(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiFraca(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumFraco(', rum, '), Gelo(', mgelo, ')) = ', Fraco, '\n')

        print('Expressão para o Paladar Suave\nMax(Min(PepsiForte(', ml, '), RumFraco(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumSuave(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiFraca(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Suave, '\n')

        print('Expressão para o Paladar Forte\nMax(Min(PepsiForte(', ml, '), RumSuave(', rum,
              '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiForte(', ml, '), RumForte(', rum, '), Gelo(', mgelo, '),\n' +
              '(Min(PepsiSuave(', ml, '), RumForte(', rum, '), Gelo(', mgelo, ')) = ', Forte, '\n')

def verificaCuba(ml, rum, mgelo, refri):
    """
    Função responsável pela verificação se os igredientes do drink e se o mesmo será Cuba
    seguindo as seguintes regras
    1 - Caso for Coca-Cola deverá seguir a seguinte receita quantidade de refrigerante deverá ser
        >= 50 e <= 60;
    2 - Caso for Pepsi-Cola deverá seguir a seguinte receita quantidade de refrigerante deverá ser
        >= 60 e <=70;
    3 - A quantidade de Rum deverá ser >=10 e <=30;
    4 - A quantidade de gelo deverá ser == 20.
    """
    controle = True
    if refri == 1:
        if ml < 50 or ml > 60:
            controle = False
            print('Os valores aceitáveis de coca são no mínimo 50ml e no máximo 60ml\n')
        elif rum < 10 or rum > 30:
            controle = False
            print('Os valores aceitáveis de rum são mínimo 10ml e no máximo 30ml')
        elif mgelo < 20 or mgelo > 20:
            controle = False
            print('O único valor aceitável de gelo é 20ml')
    else:
        if ml < 60 or ml > 70:
            controle = False
            print('Os valores aceitáveis de pepsi são no mínimo 60ml e no máximo 70ml\n')
        elif rum < 10 or rum > 30:
            controle = False
            print('Os valores aceitáveis de rum são mínimo 10ml e no máximo 30ml')
        elif mgelo < 20 or mgelo > 20:
            controle = False
            print('O único valor aceitável de gelo é 20ml')
    return controle



def pertForte(ml, vForte, refri):
    """
    Função responsável em verificar a pertinencia de refrigerante em forte.
    """
    x = ml
    if refri == 1:
        if x < 50:
            vForte = 0
        elif x <= 50 or x < 52:
            vForte = 1
        elif x <= 52 or x <= 54:
            vForte = (54-x)/(54-52)
        elif x > 54:
            vForte = 0
    else:
        if x < 60:
            vForte = 0
        elif x <= 60 or x < 62:
            vForte = 1
        elif x <= 62 or x <= 64:
            vForte = (64-x)/(64-62)
        elif x > 64:
            vForte = 0
    return vForte

def pertSuave(ml, vSuave, refri):
    """
    Função responsável em verificar a pertinencia de refrigerante em suave.
    """
    x = ml
    if refri == 1:
        if x < 52:
            vSuave = 0
        elif x <= 52 or x < 54:
            vSuave = (x-52)/(54-52)
        elif x <= 54 or x < 56:
            vSuave = 1
        elif x <= 56 or x <= 58:
            vSuave = (58-x)/(58-56)
        elif x > 58:
            vSuave = 0
    else:
        if x < 62:
            vSuave = 0
        elif x <= 62 or x < 64:
            vSuave = (x-62)/(64-62)
        elif x <= 64 or x < 66:
            vSuave = 1
        elif x <= 66 or x <= 68:
            vSuave = (68-x)/(68-66)
        elif x > 68:
            vSuave = 0
    return vSuave

def pertFraca(ml, vFraca, refri):
    """
    Função responsável em verificar a pertinencia de refrigerante em fraco.
    """
    x = ml
    if refri == 1:
        if x < 56:
            vFraca = 0
        elif x <= 56 or x < 58:
            vFraca = (x-56)/(58-56)
        elif x <= 58 or x <= 60:
            vFraca = 1
        elif x > 60:
            vFraca = 0
    else:
        if x < 66:
            vFraca = 0
        elif x <= 66 or x < 68:
            vFraca = (x-66)/(68-66)
        elif x <= 68 or x <= 70:
            vFraca = 1
        elif x > 70:
            vFraca = 0
    return vFraca

def rumForte(rum, rForte):
    """
    Função responsável em verificar a pertinencia de Rum em forte.
    """
    x = rum
    if x < 23:
        rForte = 0
    elif x <= 23 or x < 28:
        rForte = (ml-23)/(28-23)
    elif x <= 28 or x <= 30:
        rForte = 1
    elif x > 30:
        rForte = 0
    return rForte

def rumSuave(rum, rSuave):
    """
    Função responsável em verificar a pertinencia de rum em suave.
    """
    x = rum
    if x < 15:
        rSuave = 0
    elif x <= 15 or x < 20:
        rSuave = (x-15)/(20-15)
    elif x <= 20 or x < 25:
        rSuave = 1
    elif x <= 25 or x <= 27:
        rSuave = (27-x)/(27-25)
    elif x > 27:
        rSuave = 0
    return rSuave

def rumFraco(rum, rFraco):
    """
    Função responsável em verificar a pertinencia de rum em fraco.
    """
    x = rum
    if x < 10:
        rFraco = 0
    elif x <= 10 or x < 15:
        rFraco = 1
    elif x <= 15 or x <= 20:
        rFraco = (20-x)/(20-15)
    elif x > 20:
        rFraco = 0
    return rFraco

def gelo(mgelo, rGelo):
    """
    Função responsável em verificar a pertinencia de gelo.
    """
    x = mgelo
    if x < 20:
        rGelo = 0
    elif x == 20:
        rGelo = 1
    elif x > 20:
        rGelo = 0
    return rGelo

def suave(vForte, rFraco, rGelo, vSuave, rSuave, vFraca, rForte, Suave):
    """
    Função responsável em verificar a pertinencia do drink em suave.
    """
    minimo1 = 0
    minimo2 = 0
    minimo3 = 0

    minimo1 = min(vForte, rFraco, rGelo)
    minimo2 = min(vSuave, rSuave, rGelo)
    minimo3 = min(vFraca, rForte, rGelo)
    Suave = max(minimo1, minimo2, minimo3)

    return Suave

def fraco(vFraca, rFraco, rGelo, rSuave, vSuave, Fraco):
    """
    Função responsável em verificar a pertinencia do drink em fraco.
    """
    fraco1 = 0
    fraco2 = 0
    fraco3 = 0
    Fraco = 0

    fraco1 = min(vFraca, rFraco, rGelo)
    fraco2 = min(vFraca, rSuave, rGelo)
    fraco3 = min(vSuave, rFraco, rGelo)
    Fraco  = max(fraco1, fraco2, fraco3)
    
    return Fraco

def forte(vForte, rSuave, rGelo, rForte, vSuave, Forte):
    """
    Função responsável em verificar a pertinencia do drink em forte.
    """
    forte1 = 0
    forte2 = 0
    forte3 = 0

    forte1 = min(vForte, rSuave, rGelo)
    forte2 = min(vForte, rForte, rGelo)
    forte3 = min(vSuave, rSuave, rGelo)
    Forte = max(forte1, forte2, forte3)

    return Forte

def paladar(Fraco, Suave, Forte, Paladar):
    """
    Função responsável em verificar o paladar do Drink.
    """
    Paladar = max(Fraco, Suave, Forte)
    return Paladar

def coleta(refri):
    """
    Função responsável pela coleta dos valores dos igredientes no drink.
    """
    contAux = ''
    vForte = 0
    vSuave = 0
    vFraca = 0
    rFraco = 0
    rSuave = 0
    rForte = 0
    rGelo = 0
    Suave = 0
    Fraco = 0
    Forte = 0
    Paladar = 0
    while True:
        try:
            ml = float(input('Digite a quantidade de Refrigerante: '))
            break
        except ValueError:
            print('Digite apenas números!')
    while True:
        try:
            rum = float(input('Digite a quantidade de Rum: '))
            break
        except ValueError:
            print('Digite apenas números!')
    while True:
        try:
            mgelo = float(input('Digite a quantidade de Gelo: '))
            break
        except ValueError:
            print('Digite apenas números!')

    contAux = verificaCuba(ml, rum, mgelo, refri)

    if contAux == True:
        vForte = pertForte(ml, vForte, refri)
        vSuave = pertSuave(ml, vSuave, refri)
        vFraca = pertFraca(ml, vFraca, refri)
        rFraco = rumFraco(rum, rFraco)
        rSuave = rumSuave(rum, rSuave)
        rForte = rumForte(rum, rForte)
        rGelo = gelo(mgelo, rGelo)
        Suave = suave(vForte, rFraco, rGelo, vSuave, rSuave, vFraca, rForte, Suave)
        Fraco = fraco(vFraca, rFraco, rGelo, rSuave, vSuave, Fraco)
        Forte = forte(vForte, rSuave, rGelo, rForte, vSuave, Forte)
        Paladar = paladar(ml, rum, mgelo, Fraco, Suave, Forte, Paladar)

        if Paladar == Fraco:
            if Paladar == Suave and Paladar == Forte:
                print('\nO Drink possui o paladar Forte.')
                print('Normas do estabelecimento, em casos de "empates", será cobrado pelo valor'
                      'do teor mais caro.')
                printForte(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri)
            elif Paladar == Suave:
                print('\nO Drink possui o paladar Suave.')
                print('Como questões para desembate de teores e normas do estabelecimento,'
                      ' em casos de "empates", será cobrado pelo valor mais caro')
                printSuave(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri)
            else:
                printFraco(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri)

        elif Paladar == Suave:
            if Paladar == Forte and Fraco != 0:
                print("\nO Drink possui o paladar Forte.")
                print('Como questões para desembate de teores e normas do estabelecimento,'
                      'em casos de "empates", será cobrado pelo valor mais caro')
                printForte(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri)
            elif Paladar == Forte:
                print('\nO Drink possui o paladar Forte.')
                print('Como questões para desembate de teores e normas do estabelecimento,'
                      'em casos de "empates", será cobrado pelo valor mais caro')
                printForte(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri)
            else:
                print('\nO Drink possui o paladar Suave.')
                printSuave(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri)

        elif Paladar == Forte:
            print('\nO Drink possui o paladar Forte.')
            printForte(ml, rum, mgelo, Fraco, Suave, Forte, Paladar, refri)
    else:
        print('Não é cuba Libre')

while op != 'q':
    print('a - Realizar uma consulta')
    print('q - Sair')
    op = input('Selecione sua opção: ')
    op2 = op.lower()
    op = op2

    if op == 'a':
        print('============================\n')
        print('== Escolha o Refrigerante ==\n')
        print('==    1 - Coca-Cola       ==\n')
        print('==    2 - Pepsi-Cola      ==\n')
        print('============================\n')

        while True:
            try:
                refri = int(input('Selecione sua opção: '))
                if refri in range(1, 3):
                    break
            except:
                pass
            print('Opção inválida, digite novamente.')

        coleta(refri)
        
    elif op == 'q':
        print('Obrigado pela preferência')
        exit()

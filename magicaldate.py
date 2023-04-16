
'''
Aluno: Mateus Henrique Machado 
'''

def bissexto(ano):
    if ano%400 == 0: 
        return True

    elif ano%100 == 0:
        return False

    elif ano%4 == 0:
        return True

    else: 
        return False


def quantos_dias(mes, ano):

    trinta_dias = [4, 6, 9, 11]
    trinta_e_um_dias = [1, 3, 5, 6, 7, 8, 12]
    
    verificar = bissexto(ano)
    
    if verificar == True:
        if mes == 2:
            return 29
        elif mes in trinta_dias:
            return 30
        else:
            return 31
    
    else:
        if mes == 2:
            return 28
        elif mes in trinta_dias:
            return 30
        else:
            return 31


def datas_magicas(dia, mes, ano):
    aux = int(str(ano)[2:4])

    if (dia * mes) == aux:
        return True
    else:
        return False

datas = []

for a in range(1901, 2000):
    for m in range(1,12):
        aux = quantos_dias(m,a)
        for d in range(1, aux):
            if datas_magicas(d, m, a) == True:
                datas.append(f"{d:>2} / {m:>2} / {a:>3}")

print("Datas Mágicas do Século XX\n--------------------------------------")           
for k in range(len(datas)):
    print(datas[k])
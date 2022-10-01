from pathlib import Path
from re import compile as cp
import pandas as pd
from calendar import monthrange as mt


busca = cp('\d\d\d\d/\d\d/\d\d')
busca1 = cp('\d\d\d\d')
busca2 = cp('\d\d')
pasta = Path('dados\kp')
busca_d = cp('\d\d\d\d-\d\d-\d\d')

kp_in = ['0+', '1-', '1+', '2-', '2+', '3-', '3+','4-', '4+', '5-', '5+', '6-', '6+', '7-', '7+', '8-', '8+', '9-']
kp_deci = [0.33, 0.67, 1.33, 1.67, 2.33, 2.67, 3.33, 3.67, 4.33, 4.67, 5.33, 5.67, 6.33, 6.67, 7.33, 7.67, 8.33, 8.67]



from calendar import monthrange as mr

def p_indice(filename):
    df = pd.read_csv(filename, sep='\s+')
    indicet = df['data']
    indicet = [i.replace('/', "-") for i in indicet]
    indice = [''.join(busca1.findall(str(i))) for i in indicet]
    indice_d = [i.replace('/', "-") for i in indicet]
    return indice, indice_d

caminho_tempestade = Path('dados/tempestades_kp.txt')

indicet = p_indice(filename=caminho_tempestade)
indicep = indicet[1]
indice = indicet[0]

def dias(ano):

    """
    Recebe um valor de ano, e retorna os valores dos dias, dos respectivos meses
    ano = 2005
    print(dias(ano))
    Retorna = [..., [...], [335, 336, 337, ...]] equivale aos dias 1, 2 e 3 de dezembro
    """
    
    dia_m = [mr(year=ano, month=i)[1] for i in range(1, 13)]
    dia_a = list(range(1, sum(dia_m)+1))

    e = 0
    sep_dia_mes = []
    for i in dia_m:
        di = dia_a[e:i+e]
        sep_dia_mes.append(di)
        e += i
    return sep_dia_mes


def sem_tempestade(caminho='dados/vento_ano_intenso'):
    pasta = Path(caminho)

    if pasta.exists() is True:

        busca_ano = cp('\d\d\d\d')
        anos_tempestade = set([int(''.join(busca_ano.findall(str(i)))) for i in pasta.glob('*')])
        anos_sem_temp = []
        for ano in range(2001, 2020):
            if not ano in anos_tempestade:
                anos_sem_temp.append(ano)
        return anos_sem_temp

#Ajuste de datas gregorianas parajuliana


from calendar import monthrange as mg
from datetime import datetime as date


def data_juliana(stddate):
    fmt='%Y-%m-%d'
    sdtdate = date.strptime(stddate, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    print(sdtdate.tm_yday)
    return jdate


def dju_dgr(juliano: int, ano: int)->date.date:
    num_dias = sum([[dia for dia in mg(ano, dias)][1] for dias in range(1, 13)])
    juliano = int(juliano)
    if num_dias == 365:
        i=0
    else:
        i=1

    if juliano <=31:
        dias= range(1, 32)
        mes = 1
    elif (juliano >31 and juliano <=59+i):
        dias= range(32, 60+i)
        mes = 2
    elif (juliano >59+i and juliano <=90+i):
        dias= range(60+i, 91+i)
        mes = 3
    elif (juliano >90+i and juliano <=120+i):
        dias= range(91+i, 121+i)
        mes = 4
    elif (juliano >120+i and juliano <=151+i):
        dias= range(121+i, 152+i)
        mes = 5
    elif (juliano >151+i and juliano <=181+i):
        dias= range(152+i, 182+i)
        mes = 6
    elif (juliano >181+i and juliano <=212+i):
        dias= range(182+i, 213+i)
        mes = 7
    elif (juliano >212+i and juliano <=243+i):
        dias= range(213+i, 244+i)
        mes = 8
    elif (juliano >243+i and juliano <=273+i):
        dias= range(243+i, 274+i)
        mes = 9
    elif (juliano >273+i and juliano <=304+i):
        dias= range(274+i, 305+i)
        mes = 10
    elif (juliano >304+i and juliano <=334+i):
        dias= range(305+i, 335+i)
        mes = 11
    else:
        dias= range(335+i, 366+i)
        mes = 12
    data = date(ano, mes, list(dias).index(juliano)+1)
    
    return data.date()

if __name__=='__main__':
    s = dias(2008)
    #print(indicep)
    #print(busca1.findall('dados/ventos/Cachoeira/wind.199903-199912.brazil.mer')[0])
    #print(sem_tempestade())
    #print(data_juliana('2000-01-01'))
    print(dju_dgr(60, 4000))
    print(dias(3002))




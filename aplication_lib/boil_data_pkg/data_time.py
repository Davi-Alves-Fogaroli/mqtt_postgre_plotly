import datetime as dt

###############################################################
############## CONSULTA E ESPECIFICAÇÃO DE DATAS ##############
###############################################################
data_atual = dt.datetime.now()
print(f"\nData_atual: {data_atual}")

data_especifica = dt.datetime(2024, 8, 22, 8, 16, 0)
print(f"\nData_especifica: {data_especifica}")

ano = data_especifica.year
print(f"\nAno: {ano}")


#################################################
############## OPERAÇÕES COM DATAS ##############
#################################################
data_1 = dt.datetime(2024, 8, 22)
data_2 = dt.datetime(2024, 4, 11)
data_3 = data_2 + dt.timedelta(seconds=20)
print(f"\nOperação data_3: {data_3}")
resultado_operacao_data = data_1 + dt.timedelta(days=7)
print(f"\nResultado operação data: {resultado_operacao_data}")


##############################################
############## FORMATANDO DATAS ############## 
##############################################
data = dt.datetime(2024, 8, 22)
data_formatada = data.strftime("%d/%m/%y")
print(f"\nData formatada: {data_formatada}")


########################################
############## FUSORARIOS ############## 
########################################
import pytz

fuso_horario = pytz.timezone("America/Sao_Paulo")
data = dt.datetime.now(fuso_horario)
data2=data.time()
# print(f"\nData com fusorario de são paulo: {data.time()}")
data3 = str(data2)
print(f"Data: {data.time()}, type: {type(data.time())}")
print(f"Data2: {data2}, type: {type(data2)}")
print(f"Data2: {data3}, type: {type(data3)}")

################################################
############## INTERVALO DE TEMPO ############## 
################################################
# intervalo = dt.timedelta(hours=2)
# print(f"\nIntervalo de tempo {intervalo}")

# data = dt.datetime.now()
# intervalo = dt.timedelta(days=3)
# previsao = data + intervalo # ou # previsao = data + dt.timedelta(days=3)
# print(f"\nPrevisao de horario da que 3 dias: {previsao}")

data = dt.datetime.now()
print(20*"=","\n", data.time())
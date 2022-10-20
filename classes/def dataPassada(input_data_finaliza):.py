from datetime import datetime, timedelta
import datetime
input_data_finaliza = "01/10/2022"
dia_mes_ano = input_data_finaliza.split('/')
# apenas para demonstração atribui um valor 'hard-coded' para data_modificao
data_modificacao = datetime.now()
hora = int(data_modificacao.hour)
if hora >= 12:
    data_modificacao = data_modificacao + datetime.timedelta(days=1)

if (
data_modificacao.day <= dia_mes_ano[0]) and \
(data_modificacao.mouth <= dia_mes_ano[1]) and \
(data_modificacao.year <= dia_mes_ano[2]):
    
else:
    print('data_modificacao está fora do período selecionado')
data_modificacao = datetime.now()
print(int(data_modificacao.hour))

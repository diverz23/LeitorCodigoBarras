import lcd
import time

def DadosOT(msg):
    if str(msg[0]) !='Estado':
        maquina = str(msg[0])
        intervencao = str(msg[1])
        lcd.lcd16x2('Maquina',maquina)
        lcd.linha('Int.' + intervencao)
        time.sleep(4.0)
        lcd.lcd16x2('Estado Int.' + intervencao,'Clear')
    elif str(msg[0]) == 'Estado':
        lcd.lcd16x2('Estado',str(msg[1]))
        mensagem_enviar ={'DadosOT','EstadoActual'}
    
    

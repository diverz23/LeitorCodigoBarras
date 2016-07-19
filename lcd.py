#!/usr/bin/python
import Adafruit_CharLCD as LCD

#Inicializar LCD com base nos pinos utilizados
lcd_rs        = 7  
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18

    # Definit tipo  de LCD 16x2
lcd_columns = 16
lcd_rows    = 2


    # Inicializar LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows)


def lcd16x2 (msg, codigo):
    
    lcd.clear()
    lcd.message(msg + '\n')
    if codigo == 'Clear':
        lcd.clear()
        lcd.message(msg +'\n')
    else:
        lcd.message(codigo)

def linha (msg):
    lcd.set_cursor(7,1)
    lcd.message(msg)







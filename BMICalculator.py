import math
import sys
import time

print('BODY MASS INDEX (BMI) CALCULATOR')
name = input('Your name please// ')
bmi_calc = 0


def bmi_cal():
    try:
        print(' ')
        global bmi_calc
        weight = float(input('Your weight please// '))
        weight_type = input('(L)bs or (K)g// ').upper()
        height = float(input("Your Height please// "))
        height_type = input('(m)eters or (I)nches// ').upper()
        if weight_type == "L" and height_type == 'I':
            bmi_calc = 703 * weight / (height ** 2)
        elif weight_type == "K" and height_type == 'M':
            bmi_calc = weight / (height ** 2)
        else:
            print('Combine (k) and (m) OR (l) and (i)')
            time.sleep(2)
            bmi_cal()
        if bmi_calc >= 25.0:
            print(bmi_calc)
            bmi_result = 'overweight'
            print(' ')
            print(f"{name} you are {bmi_result}")
        elif 18.5 <= bmi_calc <= 24.9:
            print(bmi_calc)
            bmi_result = 'healthy'
            print(' ')
            print(f"{name} you are {bmi_result}")
        elif bmi_calc < 18.4:
            print(bmi_calc)
            bmi_result = 'underweight'
            print(' ')
            print(f"{name} you are {bmi_result}")
        time.sleep(2.0)
        new = input('''Would you like to continue
        [y/n] ''').lower()
        if new == 'y':
            time.sleep(3)
            bmi_cal()
        if new == 'n':
            print('quited')
            sys.exit()
    except ValueError:
        print('Please enter a number ')
        bmi_cal()
    except ZeroDivisionError:
        print('weight or height cannot be zero')
        bmi_cal()


bmi_cal()

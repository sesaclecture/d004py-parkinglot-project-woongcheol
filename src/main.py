import numpy as np
import datetime
from parkmodule import *


# 입차기능

while True:
    print("\n==== 주차장 관리 ====")
    print("1. 입차")
    print("2. 출차")
    print("q. 종료")
    
    choice = input("선택해주세요: ")

    ## q. 종료
    if choice.lower() == 'q':
        print("프로그램 종료")
        break


    ## 1. 입차
    elif choice == '1':
        while True:
            car_number = input("[입차] 차량번호를 입력해주세요: ")
            if car_number in carlog :
                print("중복된 차량입니다. 다시 입력해주세요")

            elif car_number not in carlog :
                incar(car_number)
                break

    ## 2. 출차                    
    elif choice == '2':
        while True:
            out_number = input("[출차] 차량번호를 입력해주세요: ")
            if out_number not in carlog:
                print("없는 차량 입니다. 다시 입력해주세요")
            elif out_number in carlog:
                outcar(out_number)
                break
    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")

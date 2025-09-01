import numpy as np
import datetime

carlog = {}
regis={"1234":1} #정기차량목록 카넘버 : count



### 입차기능

def incar(car_number):

    while True:

        intime = datetime.datetime.now()
        if car_number == 'q':
            break
        ## 주차장 출력
        parkprint()

        if car_number not in regis:
            regis[car_number] = 1 # 정기차량 목록에 방문회수 카운팅

        else:
            regis[car_number] += 1
        
        

        ## 층수 입력받기



        floor = int(input('원하는 층수를 말해주세요(1~3)')) - 1
        position = ord(input('원하는 자리를 말해주세요 (A~J)')) -65 


        f,p = floor,position

        carlog[car_number] = [intime,f,p] # 인타임, 층, 포지션

        carlog  

        ## 그 층수에 자리가 있을경우 다시 입력받기

        if parking[f][p] == '[X]':
            print('자리가 차있습니다. 다시 입력해주세요')

        elif parking[f][p] == '[ ]':
            YN = input('빈자리 입니다. 여기로 확정하시겠습니까? (Y/N)')
            if YN == 'Y':
                parking[f][p] = '[X]'
                print('자리가 확정됐습니다')

                #### 주차장 출력 #####
                parkprint()
                break

            elif YN == 'N':
                continue
        
        # O = input("입차기능을 종료하고싶으면 'q' 를 입력해주세요")
        # if O == 'q':
        #     break



# 주차장 만들기
wn = np.zeros((3,10))

wn[0][1] = 1
wn[0][4] = 1
wn[1][5] = 1
wn[2][4] = 1

parking = np.where(wn == 0 , '[ ]', '[X]')




## 주차장 출력


def parkprint():

    a = 0
    print("칸: A  B  C  D  E  F  G  H  I  J")
    for i in reversed(parking):
        print(f'{len(parking)-a}층', end='')
        for o in i:
            print(o, end='')
        print()
        a+=1





## 출차기능

def outcar(out_number):

    while True:
        if out_number == 'q':
            break
        fee = 0
        outtime = datetime.datetime.now()
    # 기본요금 10분당 300원으로 계산
        fee = (outtime-carlog[out_number][0]).seconds//60*30 # 1분당 30원

        totalfee = fee

        # 정기차량 여부확인 -> 10% 할인
        if regis[out_number] > 1 :
            totalfee *= 0.9
            print("2회 이상 방문한 차량입니다 10% 할인 ~")
            print(f"방문횟수 : {regis[out_number]}")
            print(f"현재요금 : {totalfee}")

        else :
            print(f"방문횟수 : {regis[out_number]}")
        # 물품구매시 -> 30% 할인
        item = input('구입한 물품이 있으신가요? (Y/N)')
        if item == 'Y' :
            totalfee *= 0.7

        # 최종요금 출력
        print(f"최종요금은 {totalfee} 입니다")

        # 결제 물어봄 (y/n)
        rufwp = input("결제하시겠습니까? (Y/N)")
        if rufwp == 'Y':
        # 결제 완료 메시지를 출력하고 주차장 빈자리 업데이트
            print("결제 됐습니다")
            nf,np = carlog[out_number][1],carlog[out_number][2]
            parking[nf][np] = '[ ]'# parking[f][p]
            parkprint()
            del carlog[out_number]
            break

        # n 입력시 결제가 취소되었습니다, 그대로 유지
        elif rufwp == 'N':
            print("결제가 취소되었습니다.")
            break

        # # O = input("출차기능을 종료하고싶으면 'q' 를 입력해주세요")
        # if O == 'q':
        #     break

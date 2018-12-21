#인코딩
def Data_to_code():
    data = input("Dataword : ")
    div = input("Divisor : ")
    #기본 데이터 저장
    original_data = data

    #계산용 데이터 생성
    for i in range(len(div)-1):
        data = data + "0"

    rem = data
    while(len(rem)>=len(div)):
        temp_div=""

        #div 설정
        if(rem[0] == "0"):
            for i in range(len(div)):
                temp_div = temp_div + "0"
        else:
            temp_div = div

        for i in range(len(rem) - len(div)):
            temp_div = temp_div + "0"

        # XOR연산
        temp_rem = ""
        for i in range(len(rem)):
            if(i == 0):
                continue
            if(rem[i]==temp_div[i]):
                temp_rem = temp_rem + "0"
            else:
                temp_rem = temp_rem + "1"
        rem = temp_rem

    fcs = rem
    rem = rem.lstrip('0')
    code = data + fcs
    print("Remainder : " + rem)
    print("FCS : " + fcs)
    print()
    print("Codeword : " + original_data + fcs)

#디코딩
def Code_to_data():
    code = input("Codeword : ")
    div = input("Divisor : ")

    rem = code
    while(len(rem)>=len(div)):
        temp_div=""

        #div 설정
        if(rem[0] == "0"):
            for i in range(len(div)):
                temp_div = temp_div + "0"
        else:
            temp_div = div

        for i in range(len(rem) - len(div)):
            temp_div = temp_div + "0"

        # XOR연산
        temp_rem = ""
        for i in range(len(rem)):
            if(i == 0):
                continue
            if(rem[i]==temp_div[i]):
                temp_rem = temp_rem + "0"
            else:
                temp_rem = temp_rem + "1"
        rem = temp_rem

    fcs = rem
    rem = rem.lstrip('0')
    print("Remainder : " + rem)
    print("FCS : " + fcs)
    print()
    #판별
    if "1" in fcs:
        print("무효함!")
    else:
        print("유효함!")
#메인 함수
while(True):
    print("1 : Dataword to codeword")
    print("2 : Codeword to dataword")
    print("3 : Exit")
    opt = int(input())
    if opt == 1:
        Data_to_code()
    elif opt == 2:
        Code_to_data()
    elif opt == 3:
        break
    else :
        print("input correct integer")
    print("---------------------------------------------------")


list_16 = []
list_2 = []
c_list = []
c2_list = []

str = input("수신 메세지(16진수) 입력 : ")
print("<2진수 변환>")

for i in range(0, len(str), 4):
    list_16.append(str[i:i+4])

for i in list_16:
    temp = bin(int(i,16))
    temp = temp[2:]
    # 0으로 패딩
    while(len(temp) < 16):
        temp= "0" + temp

    list_2.append(temp)

sum = 0
for i in list_2:
    print(i)
    sum = sum + int(i,2)

sum = bin(sum)
sum = sum[2:]
#올림 수 발생 시 처리
if(len(sum)>16):
    up = sum[:-16]
    sum = sum[-16:]
    sum = int(sum,2) + int(up,2)
    sum = bin(sum)
    sum = sum[2:]
    #올림 수 한 번 더 발생 시
    if(len(sum)>16):
        up = sum[:-16]
        sum = sum[-16:]
        sum = int(sum,2) + int(up,2)
        sum = bin(sum)
        sum = sum[2:]

# 0으로 패딩
while(len(sum) < 16):
    sum= "0" + sum
print("Sum : ",sum)

#체크썸 계산
for i in range(0, len(sum), 4):
    c_list.append(sum[i:i+4])
#보수 처리
for i in c_list:
    temp = ""
    for j in i:
        if j == "0":
            temp = temp + "1"
        else:
            temp = temp + "0"
    c2_list.append(temp)

hex_check_sum = ""
for i in c2_list:
    temp = hex(int(i,2))
    temp = temp[2:]
    hex_check_sum = hex_check_sum + temp.upper() + " "
print("Calculated Checksum: " + hex_check_sum)

#판별
if (hex_check_sum == "0 0 0 0 "):
    print("오류 없음")

else:
    print("오류 있음")

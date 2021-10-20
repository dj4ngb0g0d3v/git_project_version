# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print(q1["가을"])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print("사과" in q2.values())

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
num = 100
if 80 < num <= 100:
    print('A학점')
elif 61 < num <= 80:
    print('B학점')
elif 41 < num <= 60:
    print('C학점')
elif 21 < num <= 40:
    print('D학점')
else:
    print('E학점')
#61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 12
b = 6
c = 18

if a>b>=c:
    print(a)
elif b>a>=c:
    print(b)
else:
    print(c)

print()

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
id = '890105-2234567'
index = list(enumerate(id))

if index[7] == (7, '1'):   
    print('남자') 
elif index[7] == (7, '3'):
    print('남성') 
else:
    print('여성')
    



# 6 ~ 10 반복문 사용(while 또는 for)
# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for i in q3:
    if i == "정":
        continue
    print(i)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
cnt = 0
while cnt < 100:
    cnt += 1
    if cnt%2 != 0:
        print(cnt, end='')

print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for ans in q4:
    if len(ans) >= 5:
        print(ans)

print()
print()
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for chr in q5:
    if chr.upper() != chr:
        print(chr)
        
print()
print()
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for illo in q6:
    if illo.upper() == illo:
        print(illo.lower())
    else:
        print(illo.upper())
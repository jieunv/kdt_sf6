# list, set을 사용 - 중복이름 찾기
name = ["흥부", "콩쥐", "놀부", "콩쥐"]

duplicated_name = set() # 빈 셋을 생성
# duplicated_name = [] - 리스트를 이용해서도 입력 가능 이렇게 하면 append()도 이용가능하다

n = len(name)
for i in range(0, n-1): # n=4이기때문에 따지면 3까지 출력됨
    for j in range(i+1, n):
        if name[i] == name[j]:
            duplicated_name.add(name[i]) #set()이기 때문에 append를 쓰지 않고 add를 사용한다.
        '''
        i = 0, j = 1, name[0] == name[1] '흥부' == '콩쥐'
               j = 2, name[0] == name[2] '흥부' == '놀부'
               j = 3, name[0] == name[3] '흥부' == '콩쥐'      
        i = 1, j = 2, name[1] == name[2] '콩쥐' == '놀부'
               j = 3, name[1] == name[3] '콩쥐' == '콩쥐' 중복!!
        i = 2, i = 3, name[2] == name[3] '놀부' == '콩쥐'     


        '''

print(f'중복 이름: {duplicated_name}')

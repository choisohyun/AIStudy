import sys

'''
Assignment: 성적 관리 프로그램
이름: 최소현
날짜: 20190816-20190819

구성 함수
avg_grade
order
base_prt
show
search
changescore
add
searchgrade
remove
quit
'''



######################################################################
# avg_grade: 학생의 중간, 기말 점수의 평균, 학점 계산
######################################################################
def avg_grade(line1, line2):

    avg = ( int(line1)+int(line2) ) / 2 # 평균

    # 평균과 학점 return
    if avg >= 90:
        return avg,'A'
    elif avg >= 80:
        return avg,'B'
    elif avg >= 70:
        return avg,'C'
    elif avg >= 60:
        return avg,'D'
    else:
        return avg,'F'

######################################################################
# 파일 읽기
######################################################################

if len(sys.argv) == 1:              # 파일명 입력하지 않을 경우
    fr = open("students.txt", "r")
else:                               # 파일명을 입력할 경우
    fr = open(sys.argv[1], "r")

stu_list = []

for line in fr:
    a, b, c, d = line.strip().split('\t')

    a = [a, b, c, d, avg_grade(c, d)[0], avg_grade(c, d)[1]]
    stu_list.append(a)

fr.close()


######################################################################
# order: 명령어 입력받고 판단해 함수 실행
######################################################################
def order():

    order = ''
    # 유효한 명령어를 리스트로 생성
    or_li = ['show','search','changescore','add','searchgrade','remove','quit']

    while order not in or_li: # 유효한 명령어를 입력할 때까지 반복
        order = input("#")
        order = order.lower()

    if order == "show":
        show()
    elif order == "search":
        search()
    elif order == "changescore":
        changescore()
    elif order == "add":
        add()
    elif order == "searchgrade":
        searchgrade()
    elif order == "remove":
        remove()
    elif order == "quit":
        quit()

######################################################################
# base_prt : 학생 내역 출력 시 기본 포멧
######################################################################
def base_prt():
    print("Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade")
    print("------------------------------------------------------------------")

######################################################################
# show: 전체 학생 정보 출력
######################################################################
def show():
    base_prt()
    stu_list.sort(key=lambda e: e[4], reverse=True)

    for stu in stu_list:
        for i in stu:
            print(i,'\t',end='')
        print()
    print()
    order()

######################################################################
# search: 학번으로 학생 검색
######################################################################
def search():
    stu_id = input("Student ID: ")
    sea = [i[0] for i in stu_list]

    if stu_id in sea:
        base_prt()
        for i in stu_list[sea.index(stu_id)]:
            print(i, '\t', end='')
        print()

    else:
        print("NO SUCH PERSON.")

    print()
    order()

######################################################################
# changescore: 학번으로 중간이나 기말 점수 수정
######################################################################
def changescore():
    stu_id = input("Student ID: ")
    # stu_list = file_list()
    sea = [i[0] for i in stu_list]

    if stu_id in sea:
        mid_final = input("Mid/Final? ")
        mid_final = mid_final.lower()

        stu_idx = stu_list[sea.index(stu_id)]

        if mid_final == 'mid' or mid_final == 'final':
            score = int(input("Input new {} Score: ".format(mid_final)))

            if 0 <= score <= 100:

                base_prt()
                for i in stu_idx:
                    print(i, '\t', end='')
                print()

                print("Score changed")

                if mid_final == 'mid':
                    stu_idx[2] = score
                    stu_idx[4] = avg_grade(stu_idx[2], stu_idx[3])[0]
                    stu_idx[5] = avg_grade(stu_idx[2], stu_idx[3])[1]
                else:
                    stu_idx[3] = score
                    stu_idx[4] = avg_grade(stu_idx[2], stu_idx[3])[0]
                    stu_idx[5] = avg_grade(stu_idx[2], stu_idx[3])[1]

                for i in stu_idx:
                    print(i, '\t', end='')
                print()

    else:
        print("NO SUCH PERSON.")

    print()
    order()
    return stu_list

######################################################################
# add: 학생 추가
######################################################################
def add():
    stu_id = input("Student ID: ")
    sea = [i[0] for i in stu_list]

    if stu_id in sea:
        print("ALREADY EXISTS.")

    else:
        name = input("Name: ")
        m_score = int(input("Midterm Score: "))
        f_score = int(input("Final Score: "))

        new_stu = [stu_id, name, str(m_score), str(f_score),
                   avg_grade(m_score,f_score)[0],
                   avg_grade(m_score,f_score)[1]]

        stu_list.append(new_stu)

        print("Student added.")

    print()
    order()
    return stu_list

######################################################################
# searchgrade: 등급을 입력받아 해당 등급의 학생(들) 출력
######################################################################
def searchgrade():
    stu_gr = input("Grade to search: ")

    stu_idx = [];new_list = []
    gr = ['A','B','C','D','F']

    if stu_gr in gr:

        i = 0;k = 0
        for stu in stu_list:
            if stu_gr == stu[5]:
                stu_idx.append(i)
                k += 1
            i += 1

        if k != 0:  # 입력한 등급과 일치하는 학생이 리스트 안에 있으면
            for k in stu_idx:
                new_list.append(stu_list[k])  # 새로운 학생 리스트 생성

            base_prt()

            for stu in new_list: # 추가된 학생이 있는 리스트 출력
                for i in stu:
                    print(i, '\t', end='')
                print()
            print()

        else: # 입력한 등급과 일치하는 학생이 리스트 안에 없으면
            print("NO RESULTS.")

    order()

######################################################################
# remove: 학번으로 학생 삭제
######################################################################
def remove():

    stu_id = input("Student ID: ")
    sea = [i[0] for i in stu_list] # 학번 저장

    if not stu_list:
        print("List is empty.")

    else:
        if stu_id in sea: # 입력 학번이 리스트에 있으면

            del stu_list[sea.index(stu_id)] # 삭제
            print("Student removed.")

        else:
            print("NO SUCH PERSON.")

    print()
    order()

######################################################################
# quit: 편집한 내용 저장 및 프로그램 종료
######################################################################
def quit():
    yes_no = input("Save data? [yes/no] ")
    if yes_no == "yes": # 저장 O --> 파일 저장 --> 프로그램 종료
        file_name = input("File name: ")

        fw = open(file_name,"w")
        data = ''

        stu_list.sort(key=lambda e: e[4], reverse=True)
        store_li = [i[0:4] for i in stu_list] # 평균, 학점은 저장하지 않음
        for stu in store_li:

            for i in stu: # 한 줄씩 입력
                data += "%s\t" %i
            fw.write(data + '\n')
            data = ''

        fw.close()
    # 저장 X--> 프로그램 종료
    sys.exit()

######################################################################
# main: 프로그램 시작
######################################################################
def main():
    order()

if __name__ == '__main__':
    main()

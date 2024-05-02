mark = int(input('Enter makrs: '))
if mark<40 and mark>=0:
    print('you are failed')
elif mark>=40 and mark<50:
    print('C')
elif mark>=50 and mark<70:
    print('B')
elif mark>=70 and mark<90:
    print('A')
elif mark>=90 and mark<=100:
    print('A+')
else:
    print('wrong makrs entered')


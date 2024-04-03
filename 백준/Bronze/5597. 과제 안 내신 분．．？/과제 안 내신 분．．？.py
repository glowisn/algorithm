STUDENT_NUMBER = 30
ASSIGNMENT = 28

students = [i for i in range(1,STUDENT_NUMBER+1)]

for _ in range(ASSIGNMENT):
  students.remove(int(input()))


print(*students,sep='\n')
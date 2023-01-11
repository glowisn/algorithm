# Python 기본 문법 연습
# Novemver 1, 2022

# 1. List
print("1. List")
a = [1, 2, 3, 4, 5]
print("a:" + str(a))

print("")

# List Indexing
print("1. List Indexing")
print("a[0]:" + str(a[0]))
print("a[4]:" + str(a[4]))
print("a[-1]:" + str(a[-1]))
print("a[-5]:" + str(a[-5]))

print("")

# List Slicing
print("2. List Slicing")
print("a[0:2]:" + str(a[0:2]))
print("a[2:4]:" + str(a[2:4]))
print("a[2:]:" + str(a[2:]))
print("a[:2]:" + str(a[:2]))
print("a[:-1]:" + str(a[:-1]))
print("a[:-3]:" + str(a[:-3]))

print("")

# List Operation
print("3. List Operation")
print("a + a:" + str(a + a))
print("a * 3:" + str(a * 3))

print("")

# List Method
print("4. List Method")
print("append(x) : x를 리스트 a의 맨 마지막에 추가")
a.append(6)
print("a.append(6):" + str(a))
print("sort() : 리스트 a를 오름차순으로 정렬")
a.sort()
print("a.sort():" + str(a))
print("reverse() : 리스트 a를 역순으로 정렬")
a.reverse()
print("a.reverse():" + str(a))
print("index(x) : 리스트 a에서 x의 위치를 반환")
print("a.index(3):" + str(a.index(3)))
print("insert(i, x) : 리스트 a의 i번째 위치에 x를 삽입")
a.insert(0, 7)
print("a.insert(0, 7):" + str(a))
print("remove(x) : 리스트 a에서 첫 번째로 나오는 x를 삭제")
a.remove(6)
print("a.remove(6):" + str(a))
print("pop() : 리스트 a의 맨 마지막 요소를 돌려주고 그 요소는 삭제")
a.pop()
print("a.pop():" + str(a))
print("count(x) : 리스트 a에서 x가 몇 개 있는지 조사하여 그 개수를 돌려줌")
print("a.count(4):" + str(a.count(4)))
print("extend(x) : 리스트 a에 x 리스트를 더하게 됨")
a.extend([8, 9])
print("a.extend([8, 9]):" + str(a))
print("len(a) : 리스트 a의 길이를 돌려줌")
print("len(a):" + str(len(a)))
print("clear() : 리스트 a의 모든 요소를 삭제")
a.clear()
print("a.clear():" + str(a))

print("")

# 2. Tuple
print("2. Tuple")
t = (1, 2, 3, 4, 5)
print("강민이가 Tuple 안쓴다고 함 공부 안함!")

print("")


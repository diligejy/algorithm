py_list = [1, 2, 3, 4, 5]
py_list.append(6)
print(py_list)

py_list_1 = [1, 2, 3]
py_list_2 = [4, 5, 6]
py_list_1.append(py_list_2)
print(py_list_1)

py_list_1 = [1, 2, 3]
py_list_2 = [4, 5, 6]
py_list_1.extend(py_list_2)
print(py_list_1)

py_list = [1, 2, 3]
py_list.insert(4, 4)
print(py_list)

# list에 중복된 값이 있을 수 있고, 여러 값들 중에 가장 앞선 인덱스의 요소 삭제
py_list = [1, 2, 3, 2, 4]
py_list.remove(2)
print(py_list)

py_list = [1, 2, 3]
py_list.clear()
print(py_list)

py_list = [1, 2, 3]
del py_list[1]
print(py_list)

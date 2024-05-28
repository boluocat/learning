# src/main.py
import sys

sys.path[0] = 'e:\\git\\learning\\python\\materials\\modularization\\project_modulariztion'
# print(sys.path)


from proto.mat import Matrix
from utils_define.mat_mul import mat_mul


a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

print(mat_mul(a, b).data)


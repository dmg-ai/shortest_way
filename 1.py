n = int(input())
 
# Считываем заданный граф
gr = [0] * n
for i in range(n):
    gr[i] = list(map(int, input().split()))
 
# Флоид-уоршел позволяет преобразовать таблицу и получить минимальное расстояние между каждой парой вершин
for k in range(n):
    for i in range(n):
        for j in range(n):
            if not gr[i][k]:
                continue
            if not gr[k][j]:
                continue
            if not gr[i][j] or (gr[i][j] > gr[i][k] + gr[k][j]):
                gr[i][j] = gr[i][k] + gr[k][j]
 
# Делаем рекурсивный перебор всех комбинаций 2-n
bw = [False] * n
cr = []
 
if n == 1:
    print (0)
    exit(0)
 
if n == 2:
    print (gr[0][1] * 2)
    exit(0)
    
bst = -1
 
def dfs():
    global bst
    if (len(cr) == n - 1):
        # Для каждой комбинации считаем пройденный путь и обновляем ответ.
        lcl = gr[0][cr[0]] + gr[cr[n-2]][0]
        for i in range(1, n-1):
            lcl += gr[cr[i-1]][cr[i]]        
        
        if bst < 0 or bst > lcl:
            bst = lcl
    
    for i in range(1, n):
        if not bw[i]:
            bw[i] = True
            cr.append(i)
            dfs()
            cr.pop()
            bw[i] = False
 
dfs()
 
print(bst)

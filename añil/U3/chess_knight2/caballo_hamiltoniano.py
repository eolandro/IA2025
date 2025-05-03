import json
import time

result_path = [[0 for _ in range(8)] for _ in range(8)]


with open("hamiltonian_loop.json") as f:
    path = json.load(f)

position = input("\nPosicion inicial  (formato x,y;  ej: 0,1)>" ) 
# position = "0,1"

#inicio de procesamiento
start=time.time()

x,y = map(int, position.split(","))

for i in range (1,64+1):
    result_path[x][y] = i 
    if position not in path:
        print(i)
        break
    position = path[position]
    x,y = position.split(",")
    x,y = int(x),int(y)

#fin 
end = time.time()

print()
print(end-start)

for row in result_path:
    print(row)


# hamiltoniano_cerrado = [
#     [[34],[51],[32],[15],[38],[53],[18],[3]],
#     [[31],[14],[35],[52],[17],[2],[39],[54]],
#     [[50],[33],[16],[29],[56],[37],[4],[19]],
#     [[13],[30],[49],[36],[1],[20],[55],[40]],
#     [[48],[63],[28],[9],[44],[57],[22],[5]],
#     [[27],[12],[45],[64],[21],[8],[41],[58]],
#     [[62],[47],[10],[25],[60],[43],[6],[23]],
#     [[11],[26],[61],[46],[7],[24],[59],[42]]
# ]





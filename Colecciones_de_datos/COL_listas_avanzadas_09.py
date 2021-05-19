from collections import deque

cola_del_cine = deque(['fan1', 'fan2', 'YO', 'fan3', 'fan4'])

print('La cola al principio:')
print(cola_del_cine)

print('Llega otro fan más, la cola queda:')
cola_del_cine.append('fan5')
print(cola_del_cine)

print('Le dan la entrada y pasa el primero, la cola queda:')
cola_del_cine.popleft()
print(cola_del_cine)

cola = []

for i, proceso in enumerate(['p1', 'p2', 'p3', 'p4', 'p5']):
	cola.append((proceso, i))
	print(f'{proceso} agregado a cola')

for _ in range(len(cola)):
	p_terminado = cola.pop(0)
	print(f'{p_terminado} terminado')
	print(f'estado cola: {cola}')

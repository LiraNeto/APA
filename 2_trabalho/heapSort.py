def max_heapify(v, n, i):
  iMax = i
  left = 2 * i + 1
  right = 2 * i + 2

  if (left >= n):
    return

  if (left < n) and (v[i] < v[left]):
    iMax = left

  if (right < n) and (v[iMax] < v[right]):
    iMax = right

  if (iMax != i):
    v[i], v[iMax] = v[iMax], v[i]
    max_heapify(v,n, iMax)

  return

def heapSort(v):
  n = len(v)

  for i in xrange (n/2 - 1, -1, -1):
    max_heapify (v, n, i)

  for i in xrange (n-1, 0, -1):
    v[i], v[0] = v[0], v[i]
    max_heapify (v, i, 0)


  return



input_file = raw_input('\n\n\nDigite o nome do arquivo: ')

text_file = open(input_file, "r")
entrada = map (int, text_file.read().split())
text_file.close()

cpy_heap = entrada[:]

#cpy_heap = [64, 31, 87, 1, 35, 7, 5, 98, 0, 55, 35]


print '\n\nEntrada para o HeapSort: ', cpy_heap, '\n'

heapSort (cpy_heap)

print 'Saida do HeapSort: ', cpy_heap, '\n\n'

raw_input('Aperte qualquer letra para sair.')

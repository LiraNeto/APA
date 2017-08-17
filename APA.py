def insertionSort(v):
  i = 1
  j = 0
  n = len(v)
  
  atual = 0
  
  while i < n:
    atual = v[i]
    j = i - 1
    
    while (j >= 0) & (atual < v[j]):
      v[j+1] = v[j]
      j = j -1
    
    v[j+1] = atual
    
    i = i + 1

def selectionSort (v):
  i = 0
  j = 0
  n = len(v)
  
  iMin = 0
  
  for j in xrange (0, n - 1):
    iMin = j
    
    for i in xrange (j + 1, n):
      
      if (v[i] < v[iMin]):
        iMin = i
    
    if (iMin != j):
      v[j], v[iMin] = v[iMin], v[j]

input_file = raw_input('\n\n\nDigite o nome do arquivo: ')

text_file = open(input_file, "r")
entrada = map (int, text_file.read().split())
text_file.close()

cpy_insert = entrada[:]

print '\n\nEntrada para o Insertion Sort: ', cpy_insert, '\n'

insertionSort (cpy_insert)

print 'Saida do Insertion Sort: ', cpy_insert, '\n\n'

cpy_selection = entrada[:]

print 'Entrada para o Selection Sort: ', cpy_selection, '\n'

insertionSort (cpy_selection)

print 'Saida do Selection Sort: ', cpy_selection, '\n\n\n'

raw_input('Aperte qualquer letra para sair.')
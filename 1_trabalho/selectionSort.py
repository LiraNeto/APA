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

print 'Entrada para o Selection Sort: ', cpy_selection, '\n'

insertionSort (cpy_selection)

print 'Saida do Selection Sort: ', cpy_selection, '\n\n\n'

raw_input('Aperte qualquer letra para sair.')
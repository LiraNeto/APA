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

input_file = raw_input('\n\n\nDigite o nome do arquivo: ')

text_file = open(input_file, "r")
entrada = map (int, text_file.read().split())
text_file.close()

cpy_insert = entrada[:]

print '\n\nEntrada para o Insertion Sort: ', cpy_insert, '\n'

insertionSort (cpy_insert)

print 'Saida do Insertion Sort: ', cpy_insert, '\n\n'

raw_input('Aperte qualquer letra para sair.')
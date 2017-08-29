def partition(v, left, right):
  pivo = v[right]

  i = left - 1

  for j in xrange (left, right):
    if (v[j] <= pivo):
      i += 1
      v[i], v[j] = v[j], v[i]

  v[i+1], v[right] = v[right], v[i+1]

  return i + 1

def quickSort(v, left, right):
  iPivo = 0
  
  if (left < right):
    
    iPivo = partition (v, left, right)

    quickSort (v, left, iPivo -1)
    quickSort (v, iPivo + 1, right)

  return



input_file = raw_input('\n\n\nDigite o nome do arquivo: ')

text_file = open(input_file, "r")
entrada = map (int, text_file.read().split())
text_file.close()

cpy_quick = entrada[:]

print '\n\nEntrada para o QuickSort: ', cpy_quick, '\n'

quickSort (cpy_quick, 0, len(cpy_quick) - 1)

print 'Saida do QuickSort: ', cpy_quick, '\n\n'

raw_input('Aperte qualquer letra para sair.')
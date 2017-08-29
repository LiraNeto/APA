def merge (v, left, right):
  m = (left+right)/2
  n_left = m - left + 1
  n_rigth = right - m

  #aux_l = [0] * n_left
  #aux_r = [0] * n_rigth

  aux_L = v[left:left + n_left]
  aux_R = v[left + n_left: right + 1]

  i = 0
  j = 0
  k = left

  while i<n_left and j < n_rigth:
    if aux_L[i] < aux_R[j]:
      v [k] = aux_L[i]
      i += 1

    else:
      v [k] = aux_R[j]
      j += 1

    k += 1

  while i < n_left:
    v[k] = aux_L[i]
    i += 1
    k += 1

  while j < n_rigth:
    v[k] = aux_R[j]
    j += 1
    k += 1

  return 

def mergeSort(v, left, right):
  if left < right:
    
    m = (left+right)/2

    mergeSort (v, left, m)
    mergeSort (v, m+1, right)
    merge (v, left, right)

  return

input_file = raw_input('\n\n\nDigite o nome do arquivo: ')

text_file = open(input_file, "r")
entrada = map (int, text_file.read().split())
text_file.close()

cpy_merge = entrada[:]

print '\n\nEntrada para o Merge Sort: ', cpy_merge, '\n'

mergeSort (cpy_merge, 0, len(cpy_merge)-1)

print 'Saida do Merge Sort: ', cpy_merge, '\n\n'

raw_input('Aperte qualquer letra para sair.')
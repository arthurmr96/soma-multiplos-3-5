#declara variavel que recebe total
total = 0

# para cada numero da range de 0 a 1001
for num in range(1001):
  # if (or -> ||)
  if num % 5 == 0 or num % 3 == 0:
    total += num

#printa total
print(total)

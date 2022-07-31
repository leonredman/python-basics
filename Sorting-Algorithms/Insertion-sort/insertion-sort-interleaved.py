from tempfile import tempdir


def insertion_sort_interleaved(numbers, start_index, gap):
  for i in range(start_index + gap, len(numbers), gap):
    j = 1
    while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
      temp = numbers[j]
      numbers[j] = numbers[j - gap]
      numbers[j - gap] = temp
      j = j - gap
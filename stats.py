def get_word_count(text):
  word_count = len(text.split())
  return word_count

def char_count(text):
  lowercase = text.lower()
  counts = {}
  for char in lowercase:
    if char not in counts:
      counts[char] = 1
    else:
      counts[char] += 1
  return counts
def get_word_count(text):
  word_count = len(text.split())
  return word_count

def char_count(text):
  lowercase = text.lower()
  counts = {}
  for char in lowercase:
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1
  return counts

def sort_dict(dict_char):
  sorted_dict = [{k: v} for k, v in dict_char.items()]
  sorted_dict = alphanum_only(sorted_dict)
  sorted_dict.sort(key=lambda item: list(item.values())[0], reverse=True)
  return sorted_dict

def alphanum_only(dict_list):
  alphanum = []
  for item in dict_list:
    for key in item:
      if key.isalpha():
        alphanum.append(item)
  return alphanum
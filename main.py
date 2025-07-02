from stats import (
  get_word_count,
  char_count,
  sort_dict,
)

def get_book_text(file_path):
  with open(file_path) as f:
    book_text = f.read()
    return book_text
  
def print_report(words, chars, book_path):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {words} total words")
  print("--------- Character Count -------")
  for item in chars:
    for key in item:
      print(f"{key}: {item[key]}")
  print("============= END ===============")

def main():
  book_path = "./books/frankenstein.txt"
  text = get_book_text(book_path)
  words = get_word_count(text)
  chars = sort_dict(char_count(text))
  print_report(words, chars, book_path)
  return

main()
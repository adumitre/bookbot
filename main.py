from stats import get_word_count, char_count

def get_book_text(file_path):
  with open(file_path) as f:
    book_text = f.read()
    return book_text

def main():
  book_path = "./books/frankenstein.txt"
  text = get_book_text(book_path)
  words = get_word_count(text)
  chars = char_count(text)
  print(f"{words} words found in the document")
  print(chars)
  return

main()
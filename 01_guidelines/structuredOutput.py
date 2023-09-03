import sys
sys.path.append("./00_lib/")
import studylib


prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = studylib.get_completion(prompt)
print(response)
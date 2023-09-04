import time
import sys
sys.path.append("./00_lib/")
from studylib import get_completion

prompt = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = get_completion(prompt)
print(response)
import time
import sys
sys.path.append("./00_lib/")
from studylibwithTemp import get_completion_from_messages

messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Hi, my name is Isa'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)

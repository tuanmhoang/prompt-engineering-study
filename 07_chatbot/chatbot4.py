import time
import sys
sys.path.append("./00_lib/")
from studylibwithTemp import get_completion_from_messages

messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},
{'role':'user', 'content':'Hi, my name is Isa'},
{'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
Is there anything I can help you with today?"},
{'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]

response = get_completion_from_messages(messages, temperature=1)
print(response)
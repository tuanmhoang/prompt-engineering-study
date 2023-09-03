import sys
sys.path.append("./00_lib/")
import studylib


prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response = studylib.get_completion(prompt)
print(response)
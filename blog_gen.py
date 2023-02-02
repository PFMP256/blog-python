import os
import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)
        

openai.api_key = open_file('openaiapikey.txt')       

#GPT-3 Function        
def gpt_3 (prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    return text

input = open_file("input.txt")    
write = open_file("prompt1.txt").replace("<<INPUT>>", input) 
write2 = gpt_3(write)
print(write2)
save_file("blogpost.txt", write2)
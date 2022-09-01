from random import choice

questions=['why is the sky blue?','where are you?','where are the dinos?']
question=choice(questions)
answer=input(question).strip().lower()

answer=input('Why the sky is blue?:').lower()

while answer !='just because':
    answer=input('why:').strip().lower()
print('ohhhh okay!!')

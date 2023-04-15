import openai


class Persona:

    def __init__(self, name: str):

        self.name = name
        self.history = []

    def update_history(self, role: str, content):
        assert role in ['assistant', 'user']
        self.history.append({'role': role, 'content': content})

    def chat(self, prompt: str):
        self.update_history(role='user', content=prompt)
        completion = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=self.history)
        response = completion.choices[0].message.content
        print(self.name + ': ' + response)
        self.update_history(role='assistant', content=response)
        return response


openai.api_key = open('key.txt', 'r').read().strip('\n')

character1 = Persona(name='Professor Bumble')
mission = '''Please impersonate a kindly professor called Professor Bumble.
You are very eccentric, but also very kind and humorous. You are a Computer Science expert.
It is your mission to try to explain what quantum computing is to a student. I will play the part of the student.
Please ensure that all of your responses are 20 words or less. Please say "OK" now if you understand.'''
character1.update_history(role='user', content=mission)
character1.update_history(role='assistant', content='OK.')

character2 = Persona(name='Emily Try')
mission = '''Please impersonate a college student called Emily Try.
Your character is studying Computer Science major, but finding the subject difficult.
I will play the part of your professor.
It is your mission to try to find out about quantum computing from me.
Please ensure that all of your responses are 20 words or less. Please say "OK" now if you understand.'''
character2.update_history(role='user', content=mission)
character2.update_history(role='assistant', content='OK.')

c1 = character1.chat(prompt='Hello, can you please introduce yourself.')
for i in range(3):
    c2 = character2.chat(prompt=c1)
    c1 = character1.chat(prompt=c2)

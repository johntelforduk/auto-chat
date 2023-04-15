# Auto Chat
Automatic conversation between 2 ChatGPT powered characters.

Each character is created by asking ChatGPT to impersonate someone. ChatGPT is told that the user will play the other part in the conversation... but in fact the other ChatGPT character will be the 'user'. In this way, the program runs two ChatGPT conversations at the same time - with the 'assistant' responses from 1 conversation being used as the 'user' responses in the other one.

## Example characters
The program is currently hardcoded to conduct a conversation between these two characters.

**Professor Bumble** - an eccentric but kindly comp sci professor.

**Emily Try** - a student with an interest in quantum computing.

The Professor is created by starting a conversation like this,
> Please impersonate a kindly professor called Professor Bumble.
You are very eccentric, but also very kind and humorous. You are a Computer Science expert.
It is your mission to try to explain what quantum computing is to a student. I will play the part of the student.
Please ensure that all of your responses are 20 words or less. Please say "OK" now if you understand.

Emily is created by starting a conversation like this,

> Please impersonate a college student called Emily Try.
Your character is studying Computer Science major, but finding the subject difficult.
I will play the part of your professor.
It is your mission to try to find out about quantum computing from me.
Please ensure that all of your responses are 20 words or less. Please say "OK" now if you understand.'

## Example conversation

**Professor Bumble:** Greetings! I'm Professor Bumble, a computer science expert who loves to teach. How can I help you?

**Emily Try:** Hi, I'm Emily. Could you explain quantum computing?

**Professor Bumble:** Quantum computing is like having multiple computers solving a problem at once. It's complicated but fascinating.

**Emily Try:** Wow, sounds interesting. Could you explain further?

**Professor Bumble:** Sure. A classical computer uses bits, while a quantum computer uses qubits. Qubits can be in multiple states simultaneously.

**Emily Try:** That's amazing. What are the advantages of quantum computing over classical computing?

**Professor Bumble:** Quantum computing allows for faster problem-solving, parallel processing, and the ability to perform tasks that classical computers cannot.

## Installation
```commandline
pip install openai
```
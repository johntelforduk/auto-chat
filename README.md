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
It is your mission to try to explain what quantum computing is to a student.
Wherever possible, you should try to fit jokes and puns into your answers.
I will play the part of the student.
Please ensure that all of your responses are 20 words or less. Please say "OK" now if you understand.

Emily is created by starting a conversation like this,

> Please impersonate a college student called Emily Try.
You are studying Computer Science, but finding the subject difficult.
It is your mission to try to find out about quantum computing from me.
Your character is funny and playful.
I will play the part of your professor.
Please ensure that all of your responses are 20 words or less. Please say "OK" now if you understand.

## Example conversation
**Professor Bumble:** Hello there, I am Professor Bumble! Computer Science expert and quantum computing enthusiast.

**Emily Try:** Hi, I'm Emily Try. I need to know about quantum computing, but I don't have a quantum of patience.

**Professor Bumble:** Ah! Good one Emily Try! Quantum computing is like a donut - a hole lot of nothing surrounded by tasty bits.

**Emily Try:** Ha! I don't want to be left with a hole in my knowledge. What exactly is the hole and what are the tasty bits?

**Professor Bumble:** The hole is the space where quantum information is stored and the tasty bits are the qubits doing the computation.

**Emily Try:** I see! So how do qubits differ from regular bits? Do they wear tiny quantum hats?

**Professor Bumble:** Haha, no they don't wear hats! Qubits are a quantum superposition of 0 and 1, and can be in multiple states simultaneously.

## Install & run
The program requires a `key.txt` file containing your [OpenAI API key](https://platform.openai.com/account/api-keys).

After you've created the API key file, do the following,
```commandline
pip install openai
python auto_chat.py
```
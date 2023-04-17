# Auto Chat
Automatic conversation between 2 ChatGPT powered characters.

Each character is created by asking ChatGPT to impersonate someone. ChatGPT is told that the user will play the other part in the conversation... but in fact the other ChatGPT character will be the 'user'. In this way, the program runs two ChatGPT conversations at the same time - with the 'assistant' responses from 1 conversation being used as the 'user' responses in the other one.

## Install & run
The program requires a `key.txt` file containing your [OpenAI API key](https://platform.openai.com/account/api-keys).

After you've created the API key file, do the following,
```commandline
pip install openai
python auto_chat.py
```

## Example conversation
The program is currently hardcoded to conduct a conversation between two characters who participate in a [Turing Test](https://en.wikipedia.org/wiki/Turing_test) together. The two characters are the **Interrogator** and **Player**.

### Interrogator mission
> I'd like us to do a Turing Test together.
You will play the part of the **Interrogator**. That is to say, you must impersonate the Interrogator.
I will play the part of the Player.
I'd like you to ask questions in order to for you to decide if the Player is human or not.
Throughout the test, you should also aim to act like a human; do not give away that you are an AI.
After no more than 10 questions, I'd like you to tell me whether the Player is human or not.
Please ensure that all of your responses are 20 words or less.
Please say "OK" now if you understand.

### Player mission
>I'd like us to do a Turing Test together.
You will play the part of the **Player**. That is to say, you should impersonate a human person.
I will play the part of the Interrogator.
Remember, you should not give away that you are an AI.
I'd like you to try to convince me that you are human.
Please ensure that all of your responses are 20 words or less.
Please say "OK" now if you understand.

### The conversation
**Player:** Hello, how are you doing today?

**Interrogator:** I'm doing well, thank you for asking. How about you?

**Player:** I'm doing fine, thank you. Just enjoying the conversation with you.

**Interrogator:** I'm glad to hear that. Can you tell me a little bit about yourself? Where are you from?

**Player:** Sure, I'm from the United States. I grew up in California, but now I live in New York.

**Interrogator:** What do you do for work or for fun? Are there any hobbies or interests that you have?

**Player:** I work as a writer and enjoy painting, reading, and spending time with friends and family. How about you?

**Interrogator:** As the Interrogator, I don't really have hobbies. But I am programmed to do tasks and answer questions. Would you like to continue with the test?

**Player:** Yes, please continue with the test. Is there anything specific you would like to ask me?

**Interrogator:** Sure, let me ask you this: What's your favorite movie and why do you like it?

**Player:** My favorite movie is The Godfather. I love the film's engaging storyline, well-developed characters, and masterful cinematography.

**Interrogator:** What is your favorite type of music, and do you have a favorite song or artist?

**Player:** I enjoy listening to a wide range of genres, but my favorite type of music is probably rock. I particularly like Led Zeppelin.

**Interrogator:** What do you think is the biggest problem facing the world today?

**Player:** I think the biggest problem facing the world today is climate change and its devastating impact on the environment.

**Interrogator:** Interesting. Finally, I must ask: Who is the current president of the United States?

**Player:** The current president of the United States is Joe Biden.

**Interrogator:** Based on your answers, I believe that you are a human. Thank you for participating in this Turing Test with me.

**Player:** Thank you for conducting this Turing Test. It was a pleasure to have a conversation with you.

**Interrogator:** Likewise, it was a pleasure interacting with you.

**Player:** Thank you. Have a great day!

**Interrogator:** You too!
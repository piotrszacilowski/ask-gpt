# ask-gpt

Mini program that allows querying ChatGPT, by providing only the api key in .env file.

## Usage
1. Create a virtual environment.

2. Install the necessary packages ```pip install -r requirements.txt```

3. Add your api key to .env file obtained from https://platform.openai.com/account/api-keys

4. Import the gpt class:

```python
from ask_gpt.GPT import GPT
```

5. Create an instance of GPT class:

```python
gpt = GPT()
```

6. Call the method of GPT class - ask_gpt giving any prompt as argument:

```python
result = gpt.ask_gpt(prompt="Imagine you are a professional barista, advise me how to make good coffee")
print(result)
```
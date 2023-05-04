from GPT import GPT


def main():
    gpt = GPT()
    print(gpt.ask_gpt(prompt="Imagine you are a professional barista, advise me how to make good coffee"))


if __name__ == "__main__":
    main()

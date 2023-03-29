import sys


def say_hello(num, lang):
    if lang == "english":
        hello = "hello"
    elif lang == "chinese":
        hello = "nihao"
    elif lang == "russian":
        hello = "privet"
    else:
        print("Unsupported language!")
        return

    for i in range(num):
        print(hello)


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: python hello.py <number> <language>")
        sys.exit(1)

    num = int(sys.argv[1])
    lang = sys.argv[2]

    say_hello(num, lang)

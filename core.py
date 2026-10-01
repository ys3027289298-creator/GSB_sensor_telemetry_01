import json


def new_game():
    return {"next_id": 1}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["next_id"] += 1
    return state


def tokenize(text):
    return text.split(",")


def parse(text):
    return tokenize(text)


def normalize(record):
    return record


def validate(record):
    return True


def count_fields(record):
    return len(record)


def find_error(record):
    return -1


def transform(record):
    return record


def main():
    print("命令: tokenize/parse/normalize/validate/count/find/transform/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()

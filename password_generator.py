import os
import random
import string
from datetime import datetime

WORDS_FILE = "top_english_nouns_lower_100000.txt" 


def timestamp_string():
    return datetime.now().strftime("%a %b %d, %Y %I:%M:%S %p")


def ensure_dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def append_log(folder, password):
    ensure_dir(folder)
    path = os.path.join(folder, "Generated_Passwords.txt")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp_string()} | {password}\n")


def load_words(filename):
    if not os.path.exists(filename):
        return [
            "river", "paper", "cloud", "orange", "planet", "pencil", "coffee",
            "window", "garden", "camera", "rocket", "forest", "music", "storm"
        ]
    words = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w:
                words.append(w)
    return words


def apply_case(word, case_option):
    case_option = case_option.strip().lower()
    if case_option == "random":
        case_option = random.choice(["lower", "upper", "title"])
    if case_option == "lower":
        return word.lower()
    if case_option == "upper":
        return word.upper()
    if case_option == "title":
        return word.title()
    return word.lower()


def generate_memorable(words_list, num_words=3, case_option="lower"):
    chosen = random.choices(words_list, k=num_words)
    parts = []
    for w in chosen:
        w2 = apply_case(w, case_option)
        digit = str(random.randint(0, 9))
        parts.append(w2 + digit)
    password = "-".join(parts)
    append_log("Memorable", password)
    return password


def generate_random(length=12, include_punctuation=True, disallowed=""):
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if include_punctuation:
        pool += string.punctuation

    disallowed_set = set(disallowed)
    filtered_pool = "".join(ch for ch in pool if ch not in disallowed_set)

    if filtered_pool == "":
        raise ValueError("Character pool is empty after removing disallowed characters.")

    password = "".join(random.choice(filtered_pool) for _ in range(length))
    append_log("Random", password)
    return password


def prompt_int(msg, default_val):
    raw = input(f"{msg} (default {default_val}): ").strip()
    if raw == "":
        return default_val
    try:
        return int(raw)
    except ValueError:
        print("Invalid number. Using default.")
        return default_val


def prompt_yes_no(msg, default_val):
    default_letter = "y" if default_val else "n"
    raw = input(f"{msg} (y/n, default {default_letter}): ").strip().lower()
    if raw == "":
        return default_val
    return raw.startswith("y")


def interactive(words_list):
    print("\nChoose password type: memorable or random")
    ptype = input("Type: ").strip().lower()

    if ptype == "memorable":
        n = prompt_int("How many words?", 3)
        case_option = input("Case (lower/upper/title/random) (default lower): ").strip().lower()
        if case_option == "":
            case_option = "lower"
        pw = generate_memorable(words_list, num_words=n, case_option=case_option)
        print("\nMemorable password:", pw)
        print("Saved to Memorable/Generated_Passwords.txt")

    elif ptype == "random":
        length = prompt_int("Password length?", 12)
        include_punct = prompt_yes_no("Include punctuation?", True)
        disallowed = input("Disallowed characters (blank for none): ")
        pw = generate_random(length=length, include_punctuation=include_punct, disallowed=disallowed)
        print("\nRandom password:", pw)
        print("Saved to Random/Generated_Passwords.txt")

    else:
        print("Invalid choice. Type 'memorable' or 'random'.")


def generate_1000(words_list):
    for _ in range(1000):
        if random.choice(["memorable", "random"]) == "memorable":
            generate_memorable(words_list, num_words=3, case_option="random")
        else:
            generate_random(length=12, include_punctuation=True, disallowed="")
    print("Generated 1000 passwords. Check Memorable/ and Random/ folders.")


def main():
    words_list = load_words(WORDS_FILE)

    print("1) Generate one password (interactive)")
    print("2) Generate 1000 passwords (random types)")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "2":
        generate_1000(words_list)
    else:
        interactive(words_list)


if __name__ == "__main__":
    main()
 
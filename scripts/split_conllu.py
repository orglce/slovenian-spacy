import typer
import pyconll
import random


def main():
    conll = pyconll.load_from_file("./assets/Janes-Tag/Janes-Tag-with-NER.conllu")

    random.seed(230)
    random.shuffle(conll)  # shuffles the ordering of filenames (deterministic given the chosen seed)

    split_1 = int(0.8 * len(conll))
    split_2 = int(0.9 * len(conll))
    train = conll[:split_1]
    dev = conll[split_1:split_2]
    test = conll[split_2:]

    # write to file
    with open("./assets/Janes-Tag/sl_janes-train.conllu", "a") as f:
        for sent in train:
            f.write(sent.conll())
            f.write("\n\n")
    #
    with open("./assets/Janes-Tag/sl_janes-dev.conllu", "a") as f:
        for sent in dev:
            f.write(sent.conll())
            f.write("\n\n")

    with open("./assets/Janes-Tag/sl_janes-test.conllu", "a") as f:
        for sent in test:
            f.write(sent.conll())
            f.write("\n\n")


if __name__ == "__main__":
    typer.run(main)

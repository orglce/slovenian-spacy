import pathlib
import re
import typer


def main(
        ud_path: str
):
    print("\nConverting SSJ NER tags to Spacy compatible NER tags...")
    files = list(pathlib.Path(ud_path).glob('*.conllu'))

    if len(files) == 0:
        print("No Conll-U files found in the assets folder...\nMaybe you forgot to run \"spacy project assets\"?")
        return

    file_prefix = "sl_ssj-ud-"
    file_suffix = "-ner-converted"
    for file in files:
        file_type_match = re.search("(?<=" + file_prefix + ").*?(?=[.-])", file.as_posix())
        if file_type_match and file_suffix not in file.as_posix():
            file_type = file_type_match.group(0)

            print("Converting " + file_type + " file...")

            with open(ud_path + "/" + file_prefix + file_type + ".conllu", "r") as r:
                with open(ud_path + "/" + file_prefix + file_type + file_suffix + ".conllu", "w") as w:
                    for line in r:
                        w.write(line.replace("NER=", "name=")
                                .replace("B-per", "B-PER")
                                .replace("I-per", "I-PER")
                                .replace("B-loc", "B-LOC")
                                .replace("I-loc", "I-LOC")
                                .replace("B-org", "B-ORG")
                                .replace("I-org", "I-ORG")
                                .replace("B-misc", "B-MISC")
                                .replace("I-misc", "I-MISC")
                                .replace("B-deriv-per", "B-DERIV_PER")
                                .replace("I-deriv-per", "I-DERIV_PER"))
    print("")


if __name__ == "__main__":
    typer.run(main)

from xml.dom import minidom
import pyconll
import shutil
import typer


def main():
    shutil.unpack_archive("./assets/Janes-Tag/Janes-Tag.conllu.zip", "./assets/Janes-Tag/")
    shutil.unpack_archive("./assets/Janes-Tag/Janes-Tag.TEI.zip", "./assets/Janes-Tag/")

    file_tei = minidom.parse('./assets/Janes-Tag/Janes-Tag.TEI/janes.tag.body.xml')
    file_conllu = pyconll.load_from_file("./assets/Janes-Tag/Janes-Tag.conllu/Janes-Tag.conllu")
    sents = file_tei.getElementsByTagName('s')

    ner_janes = open('./assets/Janes-Tag/Janes-Tag-with-NER.conllu', 'w')

    for i in range(len(sents)):
        names = sents[i].getElementsByTagName('name')
        tags = []

        for name in names:
            j = 0
            name_tpye = name.getAttribute('type')

            for sub in name.childNodes:
                if sub.nodeType == 1:
                    tag = sub.tagName
                    final_tag = ""

                    if j == 0:
                        final_tag += "B-"
                    else:
                        final_tag += "I-"
                    j += 1

                    final_tag += name_tpye.upper()

                    if (tag == "w"):
                        tags.append({'tag': final_tag, 'word': sub.firstChild.nodeValue})
                        final_tag += " - " + str(sub.firstChild.nodeValue)
                    elif (tag == "choice"):
                        tags.append({'tag': final_tag,
                                     'word': sub.getElementsByTagName('orig')[0].getElementsByTagName('w')[
                                         0].firstChild.nodeValue})
                        final_tag += " - " + str(
                            sub.getElementsByTagName('orig')[0].getElementsByTagName('w')[0].firstChild.nodeValue)

        for tok in file_conllu[i]:
            item = [item["tag"] for item in tags if item["word"] == tok.form]
            tok.misc['name'] = set()
            tag_to_add = "O"
            if len(item) == 1:
                tag_to_add = item[0]
            tok.misc['name'].add(tag_to_add)
            tok.head = "_"

        ner_janes.write(file_conllu[i].conll() + "\n\n")


if __name__ == "__main__":
    typer.run(main)

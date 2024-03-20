<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# Slovenian SpaCy Pipeline

Train models for standard and non-standard Slovenian on the ssj500k and Janes corpuses. The project gives you the option to train standard Spacy pipelines and pipelines with the transformer. The Slovenian transfrormer model is [SloBERTa](https://huggingface.co/EMBEDDIA/sloberta), available at HuggingFace.

The of training of the models is described in this [Slovenian paper](https://repozitorij.uni-lj.si/Dokument.php?id=160420&lang=slv).

*UPDATE* - Jul 7, 2023: SpaCy now offers [official models for Slovenian](https://spacy.io/models/sl)

### Requirements

`pyconll` is needed for the conversion of the datasets.

### Download 

Prebuilt models are available at the [following link](https://mega.nz/folder/nZ5w3L5K#t9aeusn82ivhLMJrpDFU2w). The metrics of the models are available at the `metrics` folder in this repository.

## project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Command | Description |
| --- | --- |
| `convert-all` | Convert all datasets .spacy format |
| `init-vectors-all` | Initalize all word vectors for further training |
| `train-standard-no-vectors` | Train and evaluate a standard model without vectors |
| `train-standard-sloberta` | Train and evaluate a standard model with SloBERTa embeddings |
| `train-nonstandard-no-vectors` | Train and evaluate a nonstandard model without vectors |
| `train-nonstandard-sloberta` | Train and evaluate a nonstandard model with SloBERTa embeddings |

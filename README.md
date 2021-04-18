# Puppu-generaattori

Generate random text in Finnish.

## Setup

```
# Create Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

pip install wheel
pip install -r requirements.txt

# Install voikko
sudo apt install libvoikko1 voikko-fi

# Download and preprate Finnish words dataset
mkdir -p data/finnish_vocab
wget --directory-prefix data/finnish_vocab http://bionlp-www.utu.fi/.jmnybl/finnish_vocab.txt.gz
python tools/divide_by_word_class.py
```

## Run

```
python -m src.puppu
```

## Unit tests

```
python -m pytest tests
```

## License

MIT

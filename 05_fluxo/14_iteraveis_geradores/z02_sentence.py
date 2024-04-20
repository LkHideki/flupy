import re, reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text.strip()
        self.words = RE_WORD.findall(self.text)
    
    def __getitem__(self, index: int) -> str:
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

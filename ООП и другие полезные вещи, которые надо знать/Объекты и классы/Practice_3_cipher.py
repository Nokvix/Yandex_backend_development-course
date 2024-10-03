from typing import Dict


class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self) -> None:
        self.letter_pos_dict: Dict[str, int] = {}
        self.pos_letter_dict: Dict[int, str] = {}
        self._create_dictionaries()

    def _create_dictionaries(self) -> None:
        if self.letter_pos_dict:
            return

        for i, symbol in enumerate(self.alphabet):
            self.letter_pos_dict[symbol] = i
            self.pos_letter_dict[i] = symbol

    def cipher(self, original_text: str, shift: int) -> str:
        new_text: str = ''
        for symbol in original_text:
            if not symbol.isalpha():
                new_text += symbol
                continue

            new_pos: int = ((self.letter_pos_dict[symbol.lower()] + shift)
                            % len(self.alphabet))

            new_text += self.pos_letter_dict[new_pos]
        return new_text

    def decipher(self, cipher_text: str, shift: int) -> str:
        new_text: str = ''
        for symbol in cipher_text:
            if not symbol.isalpha():
                new_text += symbol
                continue

            new_pos: int = ((self.letter_pos_dict[symbol.lower()] - shift)
                            % len(self.alphabet))

            new_text += self.pos_letter_dict[new_pos]
        return new_text


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text=('Однажды ревьюер принял проект с первого раза, '
                   'с тех пор я его боюсь'),
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))

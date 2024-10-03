class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text: str, shift: int, is_encrypt: bool) -> str:
        new_text: str = ''
        shift = shift if is_encrypt else -shift

        for symbol in text:
            if not symbol.isalpha():
                new_text += symbol
                continue

            new_pos: int = (self.alphabet.index(symbol.lower()) + shift) % 33
            new_text += self.alphabet[new_pos]

        return new_text


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))

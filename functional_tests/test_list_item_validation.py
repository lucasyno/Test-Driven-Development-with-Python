from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        # Edyta przeszła na stronę główną i przypadkowo spróbowała utworzyć
        # pusty element na liście. Nacisneła klawisz Enter w pustym polu tekstowym

        # Po odświeżeniu strony głównej zobaczyła komunikat błędu
        # informujący o niemożliwości utworzenia pustego elementu na liscie.

        # Spróbowała ponownie, wpisując dowolny teskt i wszystko zadziałało

        # Przekornie spróbwała po raz drugi utworzyć pusty element na liście

        # Na stronie otrzymała ostrzeżenie podobne do wcześniejszego

        # Element mogła poprawić, wpisując w nim dowolny tekst
        self.fail('Napisz test')


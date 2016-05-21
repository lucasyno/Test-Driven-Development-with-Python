from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        # Edyta przeszła na stronę główną i przypadkowo spróbowała utworzyć
        # pusty element na liście. Nacisneła klawisz Enter w pustym polu tekstowym
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # Po odświeżeniu strony głównej zobaczyła komunikat błędu
        # informujący o niemożliwości utworzenia pustego elementu na liscie.
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'Element nie może być pusty')

        # Spróbowała ponownie, wpisując dowolny teskt i wszystko zadziałało
        self.get_item_input_box().send_keys('Kupić mleko\n')
        self.check_for_row_in_list_table('1: Kupić mleko')

        # Przekornie spróbwała po raz drugi utworzyć pusty element na liście
        self.get_item_input_box().send_keys('\n')

        # Na stronie otrzymała ostrzeżenie podobne do wcześniejszego
        self.check_for_row_in_list_table('1: Kupić mleko')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'Element nie może być pusty')

        # Element mogła poprawić, wpisując w nim dowolny tekst
        self.get_item_input_box().send_keys('Zrobić herbatę\n')
        self.check_for_row_in_list_table('1: Kupić mleko')
        self.check_for_row_in_list_table('2: Zrobić herbatę')

    def test_cannot_add_duplicate_item(self):
        # Edyta przeszła na stronę główną i zaczeła tworzyć nową listę
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Kupić kalosze\n')
        self.check_for_row_in_list_table('1: Kupić kalosze')

        # Przypadkowo spróbowała wpisać element który już znajdował się na liście
        self.get_item_input_box().send_keys('Kupić kalosze\n')

        # Otrzymała czytelny komunikat błędu
        self.check_for_row_in_list_table('1: Kupić kalosze')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'Podany element już istnieje na liście')



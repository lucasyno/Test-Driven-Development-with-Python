import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziała się o nowej, wspaniałej aplikacji w postaci listy rzeczy do zrobienia
        # Postanowiła więc przejść na stronę główną tej aplikacji
        self.browser.get('localhost:8000')

        # Zwróciła uwagę, że tytuł strony i nagłówek zawierają słowo Listy
        self.assertIn('Listy', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Twoja', header_text)

        # Od razu zostaje zachęcona, aby wpisać rzeczy do zrobienia
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Wpisz rzecz do zrobienia'
        )

        # W polu teskstowym wpisała 'Kupić pawie pióra'(hobby Edyty
        # polega na tworzeniu ozdobnych przynęt)
        inputbox.send_keys('Kupić pawie pióra')

        # Po naciśnięciu klawisza Enter strona została uaktualniona i wyświetla
        # '1: Kupić pawie pióra' jako element listy rzeczy do zrobienia
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Kupić pawie pióra')

        # Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego zadania.
        # Edyta wpisałą 'Użyć pawich piór do zrobienia przynęty' (Edyta jest nezwykle skrupulatna)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Użyć pawich piór do zrobienia przynęty')
        inputbox.send_keys(Keys.ENTER)

        # Strona została ponownie uaktualniona i teraz wyświetla dwa elementy na liście rzeczy do zrobienia
        self.check_for_row_in_list_table('1: Kupić pawie pióra')
        self.check_for_row_in_list_table('2: Użyć pawich piór do zrobienia przynęty')

        # Edyta była ciekawa czy strona zapamięta jej listę. Zwróciła uwagę na wygenerowany dla niej
        # unikatowy adres URL, obok którego znajduję się pewien tekst z wyjaśnieniem
        self.fail('Zakończenie testu!')

        # Przechodzi pod podany adres URL i widzi wyświetloną swoją listę rzeczy do zrobienia

        # Usatysfakcjonowana kładzie się spać

if __name__ == '__main__':
    unittest.main(warnings='ignore')

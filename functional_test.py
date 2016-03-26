import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziała się o nowej, wspaniałej aplikacji w postaci listy rzeczy do zrobienia
        # Postanowiła więc przejść na stronę główną tej aplikacji
        self.browser.get('localhost:8000')

        # Zwróciła uwagę, że tytuł strony i nagłówek zawierają słowo Listy
        self.assertIn('Listy', self.browser.title)
        self.fail('Zakończenie testu!')

        # Od razu zostaje zachęcona, aby wpisać rzeczy do zrobienia

        # W polu teskstowym wpisała 'Kupić pawie pióra'(hobby Edyty
        # polega na tworzeniu ozdobnych przynęt)

        # Po naciśnięciu klawisza Enter strona została uaktualniona i wyświetla
        # '1: Kupić pawie pióra' jako element listy rzeczy do zrobienia

        # Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego zadania.
        # Edyta wpisałą 'Użyć pawich piór do zrobienia przynęty' (Edyta jest nezwykle skrupulatna)

        # Strona została ponownie uaktualniona i teraz wyświetla dwa elementy na liście rzeczy do zrobienia

        # Edyta była ciekawa czy strona zapamięta jej listę. Zwróciła uwagę na wygenerowany dla niej
        # unikatowy adres URL, obok którego znajduję się pewien tekst z wyjaśnieniem

        # Przechodzi pod podany adres URL i widzi wyświetloną swoją listę rzeczy do zrobienia

        # Usatysfakcjonowana kładzie się spać

if __name__ == '__main__':
    unittest.main(warnings='ignore')

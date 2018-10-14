from datetime import date

from django.test import TestCase

from pessoas.exceptions import BirthDateException
from pessoas.services import PessoaRn


class TestPessoaRn(TestCase):

    def setUp(self):
        self.date_today = date.today()
        self.mock_one_year = date(
            self.date_today.year - 1,
            self.date_today.month,
            self.date_today.day)
        self.mock_future_year = date(
            self.date_today.year + 1,
            self.date_today.month,
            self.date_today.day)

        self.pessoa_rn = PessoaRn()
        self.pessoa_rn.birth_date = self.mock_one_year

        self.pessoa_wrong_rn = PessoaRn()
        self.pessoa_wrong_rn.birth_date = self.mock_future_year

    def test_calculate_years_old(self):
        """Test if function will calculate the years old correctly"""
        years_old = self.pessoa_rn.calculate_years_old()

        self.assertEquals(1, years_old)

    def test_exception_calculate_years_old(self):
        """Test if the function will raise exceptions with future date"""
        with self.assertRaisesMessage(
                BirthDateException,
                "It's not possible be born in the future"):
            self.pessoa_wrong_rn.calculate_years_old()

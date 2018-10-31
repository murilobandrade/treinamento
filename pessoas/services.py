from datetime import date

from pessoas.exceptions import BirthDateException
from pessoas.models import Pessoa


class PessoaRn(Pessoa):
    """Pessoa with Business Role"""

    def calculate_years_old(self) -> int:
        """Return the age of a Pessoa"""

        if self.birth_date is None:
            raise BirthDateException("This person don't have 'birth date'")

        today_date = date.today()
        if self.birth_date > today_date:
            raise BirthDateException("It's not possible be born in the future")
        return today_date.year - self.birth_date.year - (
            (today_date.month, today_date.day) <
            (self.birth_date.month, self.birth_date.day)
        )
    
    class Meta:
        proxy = True

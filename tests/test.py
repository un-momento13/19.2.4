import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_division_success(self):
        assert self.calc.division(self, 100, 2) == 50

    def test_adding_success(self):
        assert self.calc.adding(self, -5, 5) == 0

    def test_substraction_success(self):
        assert self.calc.substraction(self, -10, 0) == -10

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)


    def teardown(self):
        print('Выполнение метода Teardown')

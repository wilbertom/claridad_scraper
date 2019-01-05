from unittest import TestCase

from claridad.helpers import translate_spanish_month_to_number


class TestHelpers(TestCase):
    def test_translating_enero_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('enero'),
            1
        )

    def test_translating_febrero_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('febrero'),
            2
        )

    def test_translating_marzo_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('marzo'),
            3
        )

    def test_translating_abril_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('abril'),
            4
        )

    def test_translating_mayo_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('mayo'),
            5
        )

    def test_translating_junio_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('junio'),
            6
        )

    def test_translating_julio_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('julio'),
            7
        )

    def test_translating_agosto_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('agosto'),
            8
        )

    def test_translating_septiembre_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('septiembre'),
            9
        )

    def test_translating_octubre_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('octubre'),
            10
        )

    def test_translating_noviembre_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('noviembre'),
            11
        )

    def test_translating_diciembre_to_month_number(self):
        self.assertEquals(
            translate_spanish_month_to_number('diciembre'),
            12
        )

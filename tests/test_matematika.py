import pytest
from src.matematika import tambah, kali

def test_tambah():
    assert tambah(2, 3) == 5
    assert tambah(-1, 1) == 0

def test_kali():
    assert kali(3, 4) == 12
    assert kali(0, 10) == 0
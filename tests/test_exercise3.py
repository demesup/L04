import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def test_r1_average_returns_0_for_empty_list():  
    assert average([]) == 0


# bug report 2
def test_r2_first_word_returns_empty_string_for_empty_or_whitespace_text():  
    assert first_word("   ") == ""  
    assert first_word("") == ""


# bug report 3
def test_r3_percent_returns_0_when_total_is_0():
    assert percent(5, 0) == 0

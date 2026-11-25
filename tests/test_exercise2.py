import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_returns_true_for_grade_5():  
    assert is_passing(5) == True


# bug report 2
def test_r2_is_valid_password_fails_for_8_chars_no_digit():  
    assert is_valid_password("abcdefgh") == False


# bug report 3
def test_r3_clamp_returns_correct_value_when_x_is_between_low_and_high():  
    assert clamp(10, 5, 15) == 10

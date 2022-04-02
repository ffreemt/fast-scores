"""Test word_tr.

See also from tinybee.mdx_e2c import mdx_e2c
    tinybee-aligner\tests\test_mdx_e2c.py
"""
from fast_scores.word_tr import word_tr


def test_word_tr0():
    """Test word_tr normal."""
    assert word_tr("test")


def test_word_tr1():
    """Test word_tr capital."""
    assert word_tr("Test")


def test_word_tr2():
    """Test word_tr stripping ., ."""
    assert word_tr("Test.,")


def test_word_tr3():
    """Test word_tr strip = False ., ."""
    assert word_tr("Test.,", strip=False)

    # return orginal phrase if not found in mdx_dict (msbing_c_e.msgpk)
    assert word_tr("Test.,", strip=False) in ["test.,"]
    assert word_tr("测测试.,", strip=True) in ["测测试"]

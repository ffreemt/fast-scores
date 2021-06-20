"""Test process_zh."""
from fast_scores.process_zh import process_zh


def test_process_zh():
    """Test process_zh."""
    (_,) = process_zh("萨达test")
    # assert len(_) == 3
    assert len(_) == 6


def test_process_zh_remove():
    """Test process_zh remove."""
    (_,) = process_zh("萨达test", remove_nonchinese=True)
    assert len(_) == 2


def test_process_zh_remove1_dedup():
    """Test process_zh remove."""
    (_,) = process_zh("萨达萨萨达test", remove_nonchinese=True, dedup=True)
    assert len(_) == 2


def test_process_zh_dedup():
    """Test process_zh remove."""
    (_,) = process_zh("萨达萨萨达test", dedup=True)

    # assert len(_) == 3
    assert len(_) == 5


def test_process_zh_list():
    """Test process_zh remove."""
    _ = process_zh(["萨达萨萨达test"] * 2)

    # assert [*map(len, _)] == [6, 6]
    assert [*map(len, _)] == [9, 9]

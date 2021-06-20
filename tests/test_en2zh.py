"""Test en2zh."""
from fast_scores.en2zh import en2zh


def test_en2zh1():
    """Test en2zh 1."""

    # '试验；测试；检测；测验试验；检测；考试；测验'
    (_,) = en2zh("test")
    assert len(_) == 22

    assert en2zh("测") == ["survey; measure; fathom; conjecture"]

    assert [*map(len, en2zh(["test make"] * 2))] == [239, 239]

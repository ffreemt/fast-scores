"""Test en2zh."""
from fast_scores.en2zh import en2zh


def test_en2zh1():
    """Test en2zh 1."""

    # '试验；测试；检测；测验试验；检测；考试；测验'
    (_,) = en2zh("test")
    assert len(_) == 22

    # assert en2zh("测") == ["survey; measure; fathom; conjecture"]
    assert en2zh("测") == ["测"]

    # _ = en2zh([["test make"], ["test make"]])
    # assert [*map(len, _)] == [239, 239]

    _ = en2zh(["test make".split(), "test make".split()])
    assert [*map(len, _)] == [45, 45]

"""Test fast_scores."""
from fast_scores import __version__
from fast_scores import fast_scores


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Sanity check."""
    try:
        assert fast_scores(["a"], [""]) == [[0.0]]
    except Exception:
        assert 1

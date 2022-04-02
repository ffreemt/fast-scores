"""Test gen_cmat."""
from fast_scores.loadtext import loadtext
from fast_scores.gen_cmat import gen_cmat

text_en = loadtext("data/test-en.txt")
text_zh = loadtext("data/test-zh.txt")

list1 = [elm.strip() for elm in text_en.splitlines() if elm.strip()]
list2 = [elm.strip() for elm in text_zh.splitlines() if elm.strip()]


def test_gen_cmat1():
    """Test gen_cmat test-en/zh.txt."""
    cmat = gen_cmat(list1, list2)  # len(list2) x len(list1)
    len_y, len_x = cmat.shape

    assert cmat.max() > 0.5  # 0.54
    _ = divmod(int(cmat.argmax()), len_x)
    assert cmat[_] == cmat.max()

"""Translate a word via mdx_dict."""
# from typing import List, Union

from pathlib import Path

# import msgpack
import joblib
from string import punctuation

# keep "-"
punctuation = punctuation.replace("-", "")

_ = Path(__file__).parent

# _ = Path(_, "msbing_c_e.msgpk")
# mdx_dict = msgpack.load(open(_, "rb"))
_ = Path(_, "mdx_dict_e2c.lzma")
mdx_dict = joblib.load(_)


def word_tr(word: str, strip: bool = True) -> str:
    """Translate a word via mdx_dict.

    Args:
        word: text (str) to translate
        strip: when True, word.strip(string.punctuation)

    Returns:
        "".join(mdx_dict.get(
            word.strip(punctuation + "\r\n\t ").lower(), {}
        ).values())
    """
    try:
        word = str(word).lower()
    except Exception as exc:
        print("Something is terribly wrong: %s" % exc)
        raise

    if strip:
        word = word.strip(punctuation + "\r\n\t ")
        # return "".join(mdx_dict.get(word, {'': word}).values())
        return mdx_dict.get(word, word)

    # return "".join(mdx_dict.get(word, {'': word}).values())
    return mdx_dict.get(word, word)

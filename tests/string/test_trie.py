from str.trie import Trie

def test_trie():
    words = {"apple", "ape", "art", "plea", "poland"}
    t = Trie(words)
    assert "apple" in t
    assert "plea" in t
    assert "apt" not in t
    assert "polar" not in t
    assert "zap" not in t
    assert set(t.startswith("ap")) == {"apple", "ape"}

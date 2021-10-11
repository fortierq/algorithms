from graph.bst.bst import BST

def test_bst():
    t = BST(0)
    elem = [2, -4, 42, 0]
    for e in elem:
        t.add(e)
    assert all(e in t for e in elem)
    t.rm(42)
    t.rm(2)
    assert all(e not in t for e in [2, 42])
    assert all(e in t for e in [0, -4])

test_bst()

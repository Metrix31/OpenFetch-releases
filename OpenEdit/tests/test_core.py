from src.openedit.document import Document
from src.openedit.search import find_next
def test_edit():
 d=Document(); r,c=d.insert(0,0,'Hello'); r,c=d.enter(r,c); d.insert(r,c,'World'); assert d.lines==['Hello','World']
def test_delete_join():
 d=Document(['abc','def']); d.delete(0,3); assert d.lines==['abcdef']
def test_search():
 d=Document(['one two','three two']); assert find_next(d,'two',0,0)==(0,4)

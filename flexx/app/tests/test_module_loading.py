import time

from flexx.util.testing import run_tests_if_main, raises
from flexx.util.logging import capture_log

from flexx import app
from flexx.app._assetstore import AssetStore, SessionAssets


class FakeModule:
    """ This looks enough like a module for a Bundle to process it.
    """
    def __init__(self, name, deps):
        self.name = name
        self.deps = tuple(deps)
        self.changed_time = time.time()
    
    def get_js(self):
        return '<%s>' % self.name
    
    def get_css(self):
        return '<%s>' % self.name


class FakeModel:
    __jsmodule__ = 'module0'  # needs to be set in each subclass


def test_simple():
    
    store = AssetStore()
    s = SessionAssets(store)
    
    m1 = FakeModule('module1', ())
    
    M1 = type('M1', (FakeModel, ), {'__jsmodule__': m1.name})


test_simple()
#run_tests_if_main()
    
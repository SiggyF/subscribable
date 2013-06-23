from subscribable import subscribable, subscribecall
from nose import with_setup


def setup_func():
    "set up test fixtures"


def teardown_func():
    "tear down test fixtures"


@with_setup(setup_func, teardown_func)
def test_subscribable_method():
    "test subscribable"
    class SomeClass:
        @subscribable
        def somefunction(self):
            return 1

    results = []

    def callback(result):
        """function that appends call result to results"""
        results.append(result)

    obj = SomeClass()
    assert results == []
    obj.somefunction += callback
    obj.somefunction()
    assert results == [1], "expected [1] got {}".format(results)


@with_setup(setup_func, teardown_func)
def test_subscribable_function():
    "test subscribable"

    @subscribable
    def somefunction():
        return 1

    results = []

    def callback(result):
        """function that appends call result to results"""
        results.append(result)

    assert results == []
    somefunction += callback
    somefunction()
    assert results == [1], "expected [1] got {}".format(results)


@with_setup(setup_func, teardown_func)
def test_subscribecall_method():
    "test subscribecall"
    class SomeClass:
        @subscribecall
        def somefunction(self, *args, **kwargs):
            return 1
    calls = []

    def callback(*args, **kwargs):
        """function that appends call arguments to calls"""
        calls.append([args, kwargs])

    obj = SomeClass()
    assert calls == []
    obj.somefunction += callback
    obj.somefunction(1, a=2)
    expected = [[(1,), {'a': 2}]]
    assert calls == expected, "expected {} got {}".format(expected, calls)


@with_setup(setup_func, teardown_func)
def test_subscribecall_function():
    "test subscribecall"

    @subscribecall
    def somefunction(*args, **kwargs):
        """some function that accepts arguments"""
        return 1

    calls = []

    def callback(*args, **kwargs):
        """function that appends call arguments to calls"""
        calls.append([args, kwargs])

    assert calls == []
    somefunction += callback
    somefunction(1, a=2)
    expected = [[(1,), {'a': 2}]]
    assert calls == expected, "expected {} got {}".format(expected, calls)

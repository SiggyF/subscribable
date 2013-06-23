
import functools


class SubscribeResult(object):
    """
    decorator that allows you to subscribe to a function call
    """
    def __init__(self, f, *args, **kwargs):
        self.f = f
        self.subscribers = []

    def __get__(self, obj, objtype):
        """support instance methods."""
        # fill in the instance
        instance = SubscribeResult(functools.partial(self.__call__, obj))
        return instance

    def __call__(self, *args, **kwargs):
        """the function is called"""
        value = self.f(*args, **kwargs)
        for subscriber in self.subscribers:
            subscriber(value)
        return value

    def __iadd__(self, f):
        """add a subscriber"""
        self.subscribers.append(f)
        return self

    def __isub__(self, f):
        """remove a subscriber"""
        self.subscribers.remove(f)
        return self


class SubscribeCall(object):
    """
    decorator that allows you to subscribe to the arguments of a function call
    """
    def __init__(self, f, *args, **kwargs):
        self.f = f
        self.subscribers = []

    def __get__(self, obj, objtype):
        """support instance methods."""
        # fill in the instance
        instance = SubscribeCall(functools.partial(self.__call__, obj))
        return instance

    def __call__(self, *args, **kwargs):
        """the function is called"""
        for subscriber in self.subscribers:
            subscriber(*args, **kwargs)
        value = self.f(*args, **kwargs)
        return value

    def __iadd__(self, f):
        """add a subscriber"""
        self.subscribers.append(f)
        return self

    def __isub__(self, f):
        """remove a subscriber"""
        self.subscribers.remove(f)
        return self

# nicer decorating names
subscribable = SubscribeResult
subscribecall = SubscribeCall
subscriberesult = SubscribeResult


if __name__ == '__main__':
    import doctest
    doctest.testmod()

subscribable
============

This package provides some simple decorators to make functions
subscribable. This is can be used for logging, events and dynamic
extension of functions.

Suppose you want to log the result of a function.

<pre>
import logging
from subscribable import subscribable

@subscribable
def calculate():
    return 1 + 1
</pre>

Now you can subscribe to the calculate function.
<pre>
calculate += logging.info
calculate()
</pre>







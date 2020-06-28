# The __init__ file is executed whenever a module is imported. As
# such, generally this file is kept mostly without any code. However,
# you can use this to import sub-packages in order to clean up your
# codebase.

# For example, suppose you have a set of utility functions, all of
# which you would like to break into multiple files but allow outside
# packages to access these methods as `import
# utils.<function_name>`. This is where using the __init__.py can come
# in handy. The code below is an example of such a pattern.

# now, instead of import
# python_ml_template.utils.hello_world.say_hello_world, you can import
# python_ml_template.utils.say_hello_world

from .hello_world import say_hello_world

__all__ = ['say_hello_world', ]

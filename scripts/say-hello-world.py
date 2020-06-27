# When your package is installed in editable mode, you can call
# instances of that package from any directory. For example, this
# script may be run by calling
#
#     python scripts/say-hello-world.py
#
# and it will call methods inside our python_ml_template project.

from python_ml_template.utils import say_hello_world

if __name__ == '__main__':
    say_hello_world()

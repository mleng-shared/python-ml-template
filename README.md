# python-ml-template
Boilerplate for ML projects in Python, intended for ease of access to
use in dev and production.

The intended goal behind this project structure is to establish
recommended practices for developing and deploying ML projects that
have an active experimentation component to them.

### 1. Team sharing

Code that is built to be shared among team members and beyond. All
code should be designed from the very start to be shared, as in
combination with version control, provides an excellent mechanism
for documenting changes made to the project over time.


### 2. Ease of Dev-to-Prod Deployment

Building codebases that allow for easy deployment of code to a
production environment is very difficult. Often projects have to
struggle between two difficult extremes:

1. Focus on speedy local development, making production deployments
   difficult and unpredictable, hence less frequent. It is especially
   true for Data Science that customer input is crucial to the
   development process. Thus, frequent and reliable deployments are
   necessary to ensure the highest quality feedback is coming back to
   the development team. When projects are eventually migrated into
   production, it is done by another team, which means that the
   creators lose ownership of their product.
2. Some teams prefer to use environments that manage the entire
   deployment process for the user. However, this can often be overly
   restrictive for fast-paced teams. Managed environments often are
   feature-limited, and extending these requirements requires either
   extensive work or may require a feature request to the team
   managing that environment. Complex projects that require robust
   deployment pipelines or unique constraints often cannot advance far
   within these tools. Additionally, these tools are attempting to
   compete with a gigantic ecosystem of local development tools (IDEs,
   testing environments, custom Dockerized workflows) that have
   significantly larger teams backing each component.
3. Finally, there are others that tend to work in copies of production
   which do not have all of the feature offerings of a local
   development environment. For example, testing ETL pipelines by
   directly editing jobs in AWS Glue rather than testing Spark code
   locally, or testing a serverless Lambda by deploying and then
   testing endpoints. These testing patterns tend to slow down the
   development process.
   
This boilerplate is intended to provide some practices that can make
dev-to-prod deployment easier.

### 3. Extensible

The tools and tips provided here are meant to provide some base tools
that can be extended to build more complex workflows. For example,
this workflow could be used to deploy projects onto a Databricks
cluster via a Docker image, or to serve one or more Lambdas, or to be
deployed to Kubernetes. The goal isn't to directly suggest production
workflows, but to eliminate as many constraints and restrictions that
arise in dev environments to make our dev and prod environments as
similar as possible.

## Setup

Clone this repository with

    git clone git@github.com:chadac/python-ml-template.git
    cd python-ml-template

Create a new Python virtualenv with pyenv, and set the default Python
environment for this project directory:

    pyenv install 3.8.3
    pyenv virtualenv 3.8.3 python-ml-template
    pyenv local python-ml-template

Finally, install the dependencies from this project.

    pip install poetry
    poetry install

You can test that it has succeeded with:

    python scripts/say-hello-world.py

## Useful Tools

### pyenv for Python Version Management

[pyenv](https://github.com/pyenv/pyenv) is a utility for managing
multiple Python versions (and virtualenvs!) on one system. Depending
on the system, managing multiple versions of Python can be
difficult. As such, this tool simply moves the Python versions into
your user folder (so your changes don't conflict with others on the
same system) and allows seamless swapping between versions.

It also provides a great utility for managing virtualenvs -- `pyenv
virtualenv <python-version> <virtualenv-name>` creates a new
virtualenv with the given name, and `pyenv local <virtualenv-name>`
sets up your terminal to automatically activate this virtualenv when
entering whatever directory this command was run in.

### Poetry for Dependency Management

[Poetry](https://github.com/python-poetry/poetry) acts as an extra
layer on top of `pip`, giving you the ability to manage your project
dependencies while also tracking these dependencies under version
control, within the `pyproject.toml` file. We have found that this
package is significantly easier to work with rather than manually
managing a `requirements.txt` file or using `Pipenv`, which tends to
be a bit slow when resolving any dependencies.

## Tips & Tricks

### Running code as a module

The most common command for running any Python script is usually:

    python script.py

The disadvantage of this approach is that if you prefer to build a
more complex project with multiple module dependencies, importing code
can be difficult. The most common approaches to deal with this issue
is to either modify `sys.path` to include any desired separate folders
with modules, or placing the scripts in the root of the repository and
storing project-specific code within subfolders. These approaches have
several disadvantages:

1. Both modifying `sys.path` and placing the scripts at the root of
   your project hard-codes dependencies, making it harder to reproduce
   in production. Allowing calling the Python package from any
   location makes it much easier to clone into any environment.
2. In some cases, the `sys.path` must be modified to an absolute path,
   meaning that sharing the code between people is difficult.
3. Finally, storing any entrypoints at the root of the repository can
   create an unreadable mess, or create an unecessary number of COPY
   commands when cloning only what is needed to production. Keeping
   scripts within their own folder cleans up the root and helps others
   identify where the primary entrypoints to the application lie.
   
### Installing editable modules

By default, any scripts are usually not installed on your PYTHONPATH
as modules, hence why the standard approach is to modify the
`sys.path` within the code to deal with this issue. However, you can
actually set up pip to install your modules as packages in an editable
mode so they can be accessed in any location.

The standard approach is to use `pip install -e .` in a folder where
you have a `setup.py` file created. The `setup.py` usually specifies
metadata about a project -- where the project files may be loaded,
what the project is called, and so on.

With Poetry, however, you do not have to worry about
this. `pyproject.toml` is meant to act as a complete replacement for
the standard `setup.py` file. Poetry also automatically installs your
project package in editable mode, meaning that you will be able to
access your Python code from anywhere after running `poetry
install`. The only requirements are:

1. You must have a folder with the name specified in your
   `pyproject.toml` file under the `tool.poetry.name` property. Make
   sure that this is a Python clean name (no dashes, etc). You can
   directly modify `pyproject.toml` whenever needed.
2. Once the folder is created, run `poetry install` for poetry to
   install the module in editable mode. It should have a message
   specifying that it has installed your module.
   
This repository includes an example of such usage --

    python scripts/say-hello-world.py
    
which runs the function `utils.say_hello_world` from the
`python_ml_template` package.

Title: Making Configuration for a Python Application Simple!
Date: 2023-01-17 14:23
Modified: 2023-01-17 14:23
Tags: Python, Toml, Configuration, Development, Environment-Variables, Dot-Files
Category: Python
Slug: making-configuration-for-a-python-application-simple
Authors: Joe Stanley
Summary: If you're a nerd like me, you can probably think of your favorite self-hosted application right now. Better yet, you can probably think of all the reasons you love it. You know, one of the staples of a great self-hosted application is its ability to make the configuration *your own* and do so easily! I've been working on a number of little applications lately and they all need configuration, so I've started setting this up with the help of Python and TOML!

If you know me, you'll know that I often have *way too many projects* all in process *at the same dang time*.

> So proud. So proud...

Well, as a result of this, lately, I've been able to capitalize on some common work. Primarily surrounding the configuration management for these apps.
Configuration is a bit of a tricky subject, sometimes. Because often-times, it depends greatly on how the application will be hosted, how the configuration
should be set-up. But also, different dev-ops folks will like different mechanisms to apply their config. After all, some folks like using nothing more than
environment variables for EVERYTHING. This makes configuring an app with tools like [`docker-compose`](https://docs.docker.com/get-started/08_using_compose/)
a cinch. However, there are others who would rather set up their configuration with the file, itself. Thus, marrying the options can be a bit challenging at times.

I've recently come into the awareness of the Python package [`toml-config`](https://pypi.org/project/toml-config/). This simple little package wraps other
Python libraries to support using TOML as the basis of configuration files.

## What is TOML, anyway?

Well, if you'd like to go read for yourself, you can visit [the TOML website](https://toml.io/en/). But here's a simple example:

```toml
# This is a TOML document

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

[servers.alpha]
ip = "10.0.0.1"
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"
```

TOML is the basis for the modern Python packaging standard providing `pyproject.toml` files in place of the executable `setup.py`. That's another
conversation, for a different day, perhaps I'll dive into that sometime soon.

Anyway, TOML is a nice, concise way of describing settings and configuration options in an easily readable format. I'm a big fan of JSON as a general
rule, but TOML makes configuration pretty easy to get started with.

## How do I connect TOML and Environment Variables Easily?

Well, with that slick little tool, `toml-config`, I've been able to create a really nice little framework.

```python
from typing import List
import os
import pathlib
from toml_config.core import Config


# Inject helper method to simplify modifying values on the fly.
def update(self: Config, key_name: str, value: str):
    """Update the Specified Key Name - Section Independent."""
    for section, data in self.config.items():
        if key_name in list(data.keys()):
            self.get_section(section)
            self.set(**{key_name: value})
Config.update = update



class BaseConfig(object):
    """Base Configuration Object: Used for Inheritance for Additional Config."""
    _config: Config

    @property
    def config(self):
        """Return the Full Configuration."""
        return self._config.config

    def __setattr__(self, name: str, value: Any) -> None:
        """Magic Attribute Setter: Update the Config Object at the Same Time."""
        self.__dict__[name] = value
        self._config.update(name, value)

    def _do_load(self):
        # Load Class Attributes
        for _, data in self._config.config.items():
            for key, value in data.items():
                self.__dict__[key] = value


class ExampleConfiguration(BaseConfig):
    """
    An Example Configuration to Demonstrate the TOML Config Paradigm.
    """
    # Generic Web-Server Parameters
    host: str
    port: int
    # Another Section
    clients: List[str]

    def __init__(self, config_path: str):
        """Construct the Demonstration Configuration."""
        pathlib.Path(config_path).parent.mkdir(parents=True, exist_ok=True)
        self._config = Config(config_path)
        # Generic Web-Server Settings
        self._config.add_section('WebApp').set(
            host=os.getenv("WEB_HOST", "127.0.0.1"),
            port=int(os.getenv("WEB_PORT", "8080")),
        )
        # Another Section of Settings
        self._config.add_section('Clients').set(
            clients=os.getenv("CLIENTS", "").split(',')
        )
        # Populate the Class Variables
        self._do_load()
```

There's a lot to that sample of code, so let me break it down a bit.

### Monkey-Patch an Update Method into the `Config` Class

Alright, so this isn't *entirely* necessary, but I find it to be extremely useful. Furthermore, it isn't entirely necessary to add the monkey-patch
because I've [successfully merged a pull-request](https://github.com/SemenovAV/toml_config/pull/1) into the `toml_config` project that provides this
same functionality, directly. That means that it's not entirely necessary to use this monkey-patch, yourself.

```python
# Inject helper method to simplify modifying values on the fly.
def update(self: Config, key_name: str, value: str):
    """Update the Specified Key Name - Section Independent."""
    for section, data in self.config.items():
        if key_name in list(data.keys()):
            self.get_section(section)
            self.set(**{key_name: value})
Config.update = update
```

What this really does for us, is it provides a convenient mechanism to update values in the config on-the-fly and with relative ease. What's more,
is that it allows us to do a little magic of our own to make attributes a bit more *magic*.

### Making Configuration Attributes *MAGIC*

I'm using this pattern with some high-school students, so I really wanted to impress upon them just how "magic" and easy some things can be in a
solid, modern language like Python. So, I spent some time figuring out how I could make it such that the configuration class would support some
intelligent attribute updates, and save the configuration file when the attributes are applied. To make that happen, and to make it possible to
build upon the framework extensibly, I built a base class.

```python
class BaseConfig(object):
    """Base Configuration Object: Used for Inheritance for Additional Config."""
    _config: Config

    @property
    def config(self):
        """Return the Full Configuration."""
        return self._config.config

    # THIS IS THE IMPORTANT PART, RIGHT HERE!!!
    def __setattr__(self, name: str, value: Any) -> None:
        """Magic Attribute Setter: Update the Config Object at the Same Time."""
        self.__dict__[name] = value
        self._config.update(name, value)

    def _do_load(self):
        # Load Class Attributes
        for _, data in self._config.config.items():
            for key, value in data.items():
                self.__dict__[key] = value
```

The real magic here comes from the use of the Python *magic-method*: `__setattr__`. This method is called when an attribute is modified, and
allows me to do some fun things. Namely when I update a configuration value such as:

```python
>>> my_config = ExampleConfiguration("path/to/config.toml")
>>> my_config.port
8080
>>> my_config.port = 5050 # This will change the value, and modify the config file
>>> my_config.port
5050
```

The configuration will magically apply the change *and* update the configuration file, just to make sure everything's set!

> Marvelous!

### Pre-Loading the Data

Like I mentioned earlier, I want this thing to be somewhat intelligent, allowing me to set environment variables that can pre-load data for me so
that I don't have to deal with constructing the original TOML file, if I don't want to. And let's be honest. I'm lazy, I don't want to.
But setting this up is easy. I just use `os.getenv` to retrieve the necessary values, and use those as defaults for the config file!

```python
class ExampleConfiguration(BaseConfig):
    """
    An Example Configuration to Demonstrate the TOML Config Paradigm.
    """
    # Generic Web-Server Parameters
    host: str
    port: int
    # Another Section
    clients: List[str]

    def __init__(self, config_path: str):
        """Construct the Demonstration Configuration."""
        pathlib.Path(config_path).parent.mkdir(parents=True, exist_ok=True)
        self._config = Config(config_path)
        # Generic Web-Server Settings
        self._config.add_section('WebApp').set(
            host=os.getenv("WEB_HOST", "127.0.0.1"),
            port=int(os.getenv("WEB_PORT", "8080")),
        )
        # Another Section of Settings
        self._config.add_section('Clients').set(
            clients=os.getenv("CLIENTS", "").split(',')
        )
        # Populate the Class Variables
        self._do_load()
```

See in that little snippet, I use `Config`'s system of adding sections with their respective names, then I set the data for each of the fields
contained within each section. Namely, here there's two sections: `WebApp` and `Clients`. For each value in those sections, I use `os.getenv`
to pull in the appropriate initialization value, or fall back to a default if no such environment variable exists.

## Closing Thoughts

I think this is a pretty simple, and convenient code-pattern to support configuration from environment variables and from TOML, while at the
same time, providing a convenient update mechanism. This isn't as secure, or as robust as something with a database might be. After all, it's
entirely possible for on-disk-data to be corrupted because of improper shutdown during the data write; however unlikely that may be.

Either way, it's simple, convenient, and I enjoy it!

Happy coding!

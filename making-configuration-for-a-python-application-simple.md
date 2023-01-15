Title: Making Configuration for a Python Application Simple!
Date: 2023-01-15 14:23
Modified: 2023-01-15 14:23
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
            clients=list(os.getenv("CLIENTS", ""))
        )
```

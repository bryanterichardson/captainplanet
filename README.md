# CaptainPlanet 🌍

Open-source package for loading environment variables easier and in a Pythonic way.

## Installation

```sh
pip install captainplanet
```

Requires Python **3.10+**.

## Getting Started

```pycon
>>> from captainplanet import EnvironmentVariable
>>>
>>> port = EnvironmentVariable("APP_PORT", int, default_value=8080)
>>> host = EnvironmentVariable("APP_HOST", str, default_value="localhost")
>>> debug = EnvironmentVariable("APP_DEBUG", bool, default_value=False)
>>>
>>> port.get()
8080
>>> host.get()
'localhost'
>>> debug.get()
False
```

When the environment variable is set, CaptainPlanet parses it to the specified type:

```pycon
>>> import os
>>> os.environ["APP_PORT"] = "3000"
>>> port.get()
3000
```

You can also set and unset environment variables programmatically:

```pycon
>>> debug.set(True)
>>> os.environ["APP_DEBUG"]
'True'
>>> debug.get()
True
>>> debug.unset()
>>> debug.get()
False  # falls back to default
```

## Usage

### Supported Types

Any callable that accepts a `str` and returns the desired type works:

```python
from captainplanet import EnvironmentVariable

# Strings (no conversion needed)
app_name = EnvironmentVariable("APP_NAME", str)

# Integers
max_retries = EnvironmentVariable("MAX_RETRIES", int, default_value=3)

# Floats
timeout = EnvironmentVariable("TIMEOUT", float, default_value=30.0)

# Booleans (parses common string representations: "true", "1", "yes", "on" / "false", "0", "no", "off")
enable_logging = EnvironmentVariable("ENABLE_LOGGING", bool, default_value=True)

# Custom types; for example, comma-separated list of strings
def comma_separated_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]

urls = EnvironmentVariable("URLS", comma_separated_list, default_value=[])
```

### Boolean Parsing

The `bool` type automatically handles common string representations (case-insensitive):

| Truthy values  | Falsy values |
|----------------|--------------|
| `"true"`       | `"false"`    |
| `"1"`          | `"0"`        |
| `"yes"`        | `"no"`       |
| `"on"`         | `"off"`      |

### Checking if a Variable is Set

```python
from captainplanet import EnvironmentVariable

api_key = EnvironmentVariable("API_KEY", str)

if api_key.is_set:
    key = api_key.get()
else:
    raise EnvironmentError("API_KEY is not set")
```

### Error Handling

If the environment variable's value can't be converted to the requested type, a `ValueError` is raised:

```python
>>> os.environ["COUNT"] = "not-a-number"
>>> count = EnvironmentVariable("COUNT", int, default_value=0)
>>> count.get()
ValueError: Failed to convert 'not-a-number' for COUNT
```

### Obfuscated Mode

When `obfuscated=True`, the value is hidden in error messages and string representation for sensitive fields:


## Development

> [!IMPORTANT]
> We use `uv` for development, from environment setup to test and build/deploy.
>
> See official `uv` [documentation](https://docs.astral.sh/uv/) for more information.

### Initial setup

If it's your first time working on this project, you can run the following command to set up your environment:

```sh
make init
```

> [!TIP]
> We also provide a number of other `make` targets for convenience.
> Run `make` (or `make help`) to see what's available.

### Code format

We use `ruff` for code formatting and linting. You can run the following command to check your code.
A simple way to lint your code is to run the pre-commit hooks using the `format` target:

```sh
make format
```

### Unit tests

We use `pytest` for unit tests, and all tests are in the `tests` directory.

To quickly run unit tests using the development environment, you can run

```sh
make test
```

To make sure that the package works as expected in all supported `python` versions, you can run the `test-all` target.
Note that each `python` version will be tested in an isolated environment, and you can use the `-j, --jobs` option to run tests in parallel
(each `python` version in its own process). For example:

```sh
make -j5 test-all
```

> [!TIP]
> For the `test-all` target, both `stdout` and `stderr` from testing each `python` version are written to respective `.test-{version}.log` files.

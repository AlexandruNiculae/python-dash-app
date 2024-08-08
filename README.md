## Environment variables:

- `HOST` - the host address to run the application on (default 127.0.0.1)
- `PORT` - the port address to run the application on (default 8050)
- `DASH_APP_OWNER` - application owner name to display on the main page

## Docker images:

### `Dockerfile` - the main application image

Contains only the required libraries to run the application.
Does not contain any tests or libraries that are used for maintenance or development.

### `Dockerfile.dev` - the development application image

Contains libraries and tests.
Required to run the application maintenance commands.
Used for development purposes only.

## Application maintenance commands:

- `pylint src` runs the linter to check for code quality
- `mypy src` checks wether there are any type mismatches
- `pytest -s test` runs functional tests of the app

# Run testing and coverage
docker-compose -f ../local.yml run --rm django coverage run -m pytest ; coverage report ; coverage html
chromium-browser ../htmlcov/index.html

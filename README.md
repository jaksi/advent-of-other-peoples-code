# Advent of Other People's Code
Fetches random solutions to a specified Advent of Code puzzle from GitHub and runs them against your input
![Grinch](grinch.png)
## Usage
Let me rephrase. This is going to get some random code from GitHub and run it on your machine. Don't use it.

## Really tho
### Create a virtualenv
```sh
python3 -m venv env
source env/bin/activate
```

### Install requirements
```sh
pip install -r requirements.txt
```

### Genrate a GitHub personal access token
[Right here](https://github.com/settings/tokens/new)

TBA: scopes

### Run it
Please, don't!

### I said run it!
```sh
python advent.py --token $GITHUB_TOKEN --year 2018 --day 1 --input input.txt
```

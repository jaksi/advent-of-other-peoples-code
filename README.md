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
[Right here](https://github.com/settings/tokens/new), with the `public_repo` scope.

### Run it
Please, don't!

### I said run it!
```shellsession
$ python advent.py --token $GITHUB_TOKEN --year 2018 --day 3 --input input.txt
Patching open() to always return your input file
Searching for repositories
Searching for a solution in Karlovsky120/AdventOfCode2018
Searching for a solution in grey-area/advent-of-code-2018
Searching for a solution in stefsiekman/aoc2018
Searching for a solution in BenSchomp/adventofcode2018
Searching for a solution in speedyswimmer1000/AoC2018
About to blindly run https://github.com/speedyswimmer1000/AoC2018/blob/master/day3.py.
Type yes if you think that's a good idea.
Hint: it's not.
yes
Running it, stand back.
It raised an exception.
Searching for a solution in zinh/advent-of-code-2018
Searching for a solution in aaralh/AdventOfCode
Searching for a solution in athas/advent_of_code_2018
Searching for a solution in hawkjo/advent_of_code_2018
Searching for a solution in Landmaj/AoC_2018
Searching for a solution in paiv/aoc2018
Searching for a solution in helenacruz/adventofcode2018
Searching for a solution in StevTheDev/AoC2018
Searching for a solution in zoeimogen/AoC2018
Searching for a solution in awyd234/adventofcode
Searching for a solution in muffinsofgreg/adventcode2018
Searching for a solution in asberk/aoc18
About to blindly run https://github.com/asberk/aoc18/blob/master/03.py.
Type yes if you think that's a good idea.
Hint: it's not.
yes
Running it, stand back.
It raised an exception.
Searching for a solution in coandco/advent2018
Searching for a solution in ChrisDoubleEwe/AdventOfCode2018
Searching for a solution in veeraita/advent_of_code_2018
Searching for a solution in protocol7/advent-of-code-2018
Searching for a solution in SpionSkummis/Advent-of-Code-2018
About to blindly run https://github.com/SpionSkummis/Advent-of-Code-2018/blob/master/Erik/Day3.py.
Type yes if you think that's a good idea.
Hint: it's not.
yes
Running it, stand back.
The number of squares cut more than once is: 119551
The non-overlapping square was found at nr 1124
Was that the right answer?
yes
```

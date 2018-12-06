import argparse
import builtins
import random
import re
import sys

from github import Github


def run(github_file):
    print("About to blindly run {url}.\nType yes if you think that's a good idea.\nHint: it's not.".format(
        url=github_file.html_url
    ))
    if input().strip().lower() != "yes":
        print("Ok, not running it.")
        return False

    print("Running it, stand back.")
    try:
        exec(github_file.decoded_content)
    except Exception as e:
        print(e)
        return False

    print("Was that the right answer?")
    return input().strip().lower() == "yes"


def main():
    parser = argparse.ArgumentParser(description="Advent of Other People's Code")
    parser.add_argument('--token', required=True)
    parser.add_argument('--year', required=True)
    parser.add_argument('--day', required=True)
    parser.add_argument('--input', required=True)
    args = parser.parse_args()

    file_pattern = re.compile(r'[^\d]*[^1-9]{day}\.py'.format(day=args.day))

    original_open = builtins.open
    builtins.open = lambda *_args, **_kwargs: original_open(args.input)

    github = Github(args.token)
    repositories = github.search_repositories('advent of code {year}'.format(year=args.year),
                                              sort='updated',
                                              language='python')
    for repository in repositories:
        tree = repository.get_git_tree('master', recursive=True).tree
        matching_files = [element for element in tree if element.type == 'blob' and file_pattern.match(element.path)]
        success = False
        for matching_file in matching_files:
            if run(repository.get_contents(matching_file.path)):
                success = True
                break
        if success:
            break


if __name__ == '__main__':
    main()

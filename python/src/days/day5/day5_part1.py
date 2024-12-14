from collections import defaultdict
from typing import DefaultDict, Dict, List, Set
from math import floor
from utils.file_utilities import get_root_filepath

# Dictionary where key is page number, value is set of page numbers that CAN'T appear after it
PageRules = DefaultDict[int, Set[int]]


def run_day_5_part_1():
    filepath: str = get_root_filepath()

    with open(filepath + "day5/page_ordering.txt", "r") as file:
        middle_page_numbers = sum_valid_middle_pages(file)
        print(f"Sum of middle page numbers is {middle_page_numbers}")


def sum_valid_middle_pages(file) -> int:
    file_contents: str = file.read()

    # split into two sections. section 1 = list of page ordered rules, section 2 = page numbers updates
    sections: List[str] = file_contents.split("\n\n")
    assert len(sections) == 2

    rules_raw: List[str] = sections[0].splitlines()
    updates_raw: List[str] = sections[1].splitlines()

    page_rules: PageRules = get_page_rules(rules_raw)
    updates: List[List[int]] = get_updates(updates_raw)

    total: int = 0
    for update in updates:
        if is_update_valid(update, page_rules):
            total += get_middle_page_number(update)

    return total


def get_page_rules(rules_raw: List[str]) -> PageRules:
    page_rules: PageRules = defaultdict(set)
    for rule in rules_raw:
        (page_1_str, page_2_str) = rule.split("|")
        (page_1, page_2) = int(page_1_str), int(page_2_str)

        # If page 1 must be before page 2, then page 2 can't have page 1 appear after it
        # E.g. 47 | 53  => { 53: { 47 } }
        page_rules[page_2].add(page_1)
    return page_rules


def get_updates(updates_raw: List[str]) -> List[List[int]]:
    return [
        [int(update_page) for update_page in update.split(",")]
        for update in updates_raw
    ]


def is_update_valid(update: List[int], page_rules: PageRules) -> bool:
    for i, page in enumerate(update):
        rest_of_update = update[i + 1 :]
        invalid_numbers: Set[int] = page_rules[page].intersection(set(rest_of_update))

        if len(invalid_numbers) > 0:
            return False
    return True


def get_middle_page_number(update: List[int]) -> int:
    if len(update) % 2 == 0:
        raise ValueError(
            "Instructions not clear what to do for an even number of pages in an update"
        )

    middle = floor(len(update) / 2)
    return update[middle]


if __name__ == "__main__":
    run_day_5_part_1()

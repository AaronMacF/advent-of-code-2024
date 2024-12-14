from collections import defaultdict
from typing import DefaultDict, List, Set
from math import floor
from utils.file_utilities import get_root_filepath

# Dictionary where key is page number, value is set of page numbers that CAN'T appear after it
PageRules = DefaultDict[int, Set[int]]


def run_day_5_part_2():
    filepath: str = get_root_filepath()

    with open(filepath + "day5/page_ordering.txt", "r") as file:
        middle_page_numbers = sum_middle_pages_of_corrected_updates(file)
        print(f"Sum of middle page numbers is {middle_page_numbers}")


def sum_middle_pages_of_corrected_updates(file) -> int:
    file_contents: str = file.read()

    # split into two sections. section 1 = list of page ordered rules, section 2 = page numbers updates
    sections: List[str] = file_contents.split("\n\n")
    assert len(sections) == 2

    rules_raw: List[str] = sections[0].splitlines()
    updates_raw: List[str] = sections[1].splitlines()

    page_rules = get_page_rules(rules_raw)
    updates: List[List[int]] = get_updates(updates_raw)

    total: int = 0
    for update in updates:
        total += get_middle_page_number_of_corrected_updates(update, page_rules)

    return total


def get_page_rules(rules_raw: List[str]) -> PageRules:
    page_rules: PageRules = defaultdict(
        set
    )  # Value is set of pages that CAN'T appear after key
    for rule in rules_raw:
        (page_1_str, page_2_str) = rule.split("|")
        (page_1, page_2) = int(page_1_str), int(page_2_str)

        page_rules.append((page_1, page_2))
    return page_rules


def get_middle_page_number_of_corrected_updates(
    update: List[str], page_rules: PageRules
) -> int:
    # If update is already valid, return 0
    # If update is not valid, correct it and return the middle page number
    valid_update: List[int] = update.copy()
    is_invalid = False

    i = 0
    while i < len(valid_update):
        current_page = valid_update[i]

        # Get the page numbers after the current page
        next = valid_update[i + 1 :]

        # Get all the page numbers that shouldn't appear after this current one
        invalid_following_pages = page_rules[current_page]

        # If there are no invalid pages, current page is valid so move on to the next one
        if len(set(next).intersection(invalid_following_pages)) == 0:
            i += 1
            continue

        # If there is at least one invalid page, move the current page after the largest one
        for page in reversed(list(invalid_following_pages)):
            if page not in next:
                continue
            is_invalid = True

            # Move current page to be immediately after the largest invalid page
            invalid_page_index = valid_update.index(page)
            valid_update.insert(invalid_page_index + 1, current_page)
            valid_update.pop(i)

            # Once this is done for the largest invalid number, stop
            break

    if is_invalid:
        return get_middle_page_number(valid_update)
    else:
        return 0


def get_updates(updates_raw: List[str]) -> List[List[int]]:
    return [
        [int(update_page) for update_page in update.split(",")]
        for update in updates_raw
    ]


def get_middle_page_number(update: List[int]) -> int:
    if len(update) % 2 == 0:
        raise ValueError(
            "Instructions not clear what to do for an even number of pages in an update"
        )

    middle = floor(len(update) / 2)
    return update[middle]


if __name__ == "__main__":
    run_day_5_part_2()

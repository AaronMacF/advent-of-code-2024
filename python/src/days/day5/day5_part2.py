# from collections import defaultdict
# from typing import DefaultDict, Dict, List, Set, Tuple
# from math import floor
# from utils.file_utilities import get_root_filepath

# PageRules = List[Tuple[int, int]]

# def run_day_5_part_2():
#   filepath: str = get_root_filepath()

#   with open(filepath + 'day5/page_ordering.txt', 'r') as file:
#     middle_page_numbers = sum_middle_pages_of_corrected_updates(file)
#     print(f'Sum of middle page numbers is {middle_page_numbers}')
    

# def sum_middle_pages_of_corrected_updates(file) -> int:
#   file_contents: str = file.read()

#   # split into two sections. section 1 = list of page ordered rules, section 2 = page numbers updates
#   sections: List[str] = file_contents.split("\n\n")
#   assert len(sections) == 2

#   rules_raw: List[str] = sections[0].splitlines()
#   updates_raw: List[str] = sections[1].splitlines()

#   page_rules_bwd = get_page_rules(rules_raw)
#   updates: List[List[int]] = get_updates(updates_raw)

#   total: int = 0
#   for update in updates:
#     if is_update_valid(update, page_rules_fwd):
#       continue
#     corrected_update = correct_invalid_update(update, page_rules_bwd)
#     total += get_middle_page_number(corrected_update)

#   return total


# def get_page_rules(rules_raw: List[str]) -> Tuple[PageRules, PageRules]:
#   page_rules_bwd: PageRules = defaultdict(set) # Value is set of pages that CAN'T appear after key
#   for rule in rules_raw:
#     (page_1_str, page_2_str) = rule.split('|')
#     (page_1, page_2) = int(page_1_str), int(page_2_str)

#     page_rules_bwd[page_2].add(page_1)
#   return (page_rules_bwd)


# def get_updates(updates_raw: List[str]) -> List[List[int]]:
#   return [[int(update_page) for update_page in update.split(',')] for update in updates_raw ]
  

# def is_update_valid(update: List[int], page_rules: PageRules) -> bool:
#   for (i, page) in enumerate(update):
#     rest_of_update = update[i+1:]
#     invalid_numbers: Set[int] = page_rules[page].intersection(set(rest_of_update))

#     if (len(invalid_numbers) > 0):
#       return False
#   return True

# def correct_invalid_update(update: List[int], page_rules_fwd: PageRules) -> List[int]:
#   pages_to_add = update.copy()
#   valid_update = []
#   while (len(pages_to_add) > 0):
#     for page in pages_to_add:
#       # if valid_update contains all page numbers that must appear AFTER the current page, add the current page
      



# def get_middle_page_number(update: List[int]) -> int:
#   if (len(update) % 2 == 0):
#     raise ValueError("Instructions not clear what to do for an even number of pages in an update")
  
#   middle = floor(len(update) / 2)
#   return update[middle]


# if (__name__ == '__main__'):
#   run_day_5_part_1()

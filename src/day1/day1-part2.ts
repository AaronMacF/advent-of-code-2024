import { getFileLines } from '../utils/file-utilities';

const filename = 'src/day1/location-list.txt';

export async function runDay1Part2(): Promise<void> {
  const list1: number[] = [];
  const list2: number[] = [];

  const fileLines = getFileLines(filename);
  const locationIdRegex = /(\d+)\s+(\d+)/;

  // Add the first location id to the list1, the second to list2
  fileLines.forEach((line) => {
    const regexMatches = line.match(locationIdRegex);
    if (regexMatches?.length !== 3) {
      throw new Error(
        'Did not find the right amount of matches for line: ' + line
      );
    }
    list1.push(+regexMatches[1]);
    list2.push(+regexMatches[2]);
  });

  // Build a dictionary of number -> count for all numbers in list2
  const list2NumberToCountDict: { [num: number]: number } = list2.reduce(
    (dict, num) => {
      if (dict[num] !== undefined) {
        dict[num] += 1;
      } else {
        dict[num] = 1;
      }
      return dict;
    },
    {}
  );

  // Calculate the total of list1 multiplied by its count in list2
  const similarityScore = list1.reduce((sum, num) => {
    if (list2NumberToCountDict[num]) {
      return (sum += num * list2NumberToCountDict[num]);
    }
    return sum;
  }, 0);

  console.log('Similarity score is: ' + similarityScore);
}

import { getFileLines, getFilepathRoot } from '../../utils/file-utilities';

const filename = getFilepathRoot() + 'day1/location-list.txt';

export async function runDay1Part1(): Promise<void> {
  const list1: number[] = [];
  const list2: number[] = [];

  const fileLines = getFileLines(filename);
  const locationIdRegex = /(\d+)\s+(\d+)/;

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

  list1.sort();
  list2.sort();

  let totalDistance: number = 0;
  for (let i = 0; i < list1.length; i++) {
    const distance = Math.abs(list1[i] - list2[i]);
    totalDistance += distance;
  }

  console.log('Total distance is: ' + totalDistance);
}

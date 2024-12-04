import { getFileLines } from '../utils/file-utilities';

const filepath = 'src/day4/word-search.txt';

type Coordinates = [i: number, j: number];

export async function runDay4Part1(): Promise<void> {
  const wordSearch: string[] = getFileLines(filepath);
  let xmasCount = 0;

  wordSearch.forEach((line, i) => {
    for (let j = 0; j < line.length; j++) {
      const char = line[j];
      if (char !== 'X') {
        continue;
      }
      xmasCount += findNumberOfXMASMatches(wordSearch, [i, j]);
    }
  });

  console.log('Number of XMAS in word search: ' + xmasCount);
}

function findNumberOfXMASMatches(
  input: string[],
  currentCoordinates: Coordinates
): number {
  let numberOfMatches = 0;

  // coordinates to check for 'M'
  const relativeIndicesToCheck: number[][] = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
    [-1, -1],
    [1, 1],
    [-1, 1],
    [1, -1],
  ];
  relativeIndicesToCheck.forEach((indices) => {
    let coordinatesOfLastLetter = currentCoordinates;
    const letters: string = 'MAS';
    for (let i = 0; i < letters.length; i++) {
      const coordinatesToCheckForLetter = getCoordinatesToCheck(
        coordinatesOfLastLetter,
        indices
      );
      if (!isLetterAdjacent(input, coordinatesToCheckForLetter, letters[i])) {
        // if the next letter of the word isn't found, give up
        break;
      }
      coordinatesOfLastLetter = coordinatesToCheckForLetter;

      // if every letter of the word has been found, it's a match
      if (i === letters.length - 1) {
        numberOfMatches += 1;
      }
    }
  });

  return numberOfMatches;
}

function getCoordinatesToCheck(
  currentCoordinates: Coordinates,
  indices: number[]
): Coordinates {
  return [
    currentCoordinates[0] + indices[0],
    currentCoordinates[1] + indices[1],
  ];
}

function isLetterAdjacent(
  input: string[],
  coordinatesToCheck: Coordinates,
  letterToFind: string
): boolean {
  const [i, j] = coordinatesToCheck;
  if (input[i] !== undefined && input[i][j] === letterToFind) {
    return true;
  }
  return false;
}

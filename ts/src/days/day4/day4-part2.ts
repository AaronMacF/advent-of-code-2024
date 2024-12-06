import { getFileLines, getFilepathRoot } from '../../utils/file-utilities';

const filepath = getFilepathRoot() + 'day4/word-search.txt';

export async function runDay4Part2(): Promise<void> {
  const wordSearch: string[] = getFileLines(filepath);

  // pad edges of word search with filler chars
  const firstAndLastLines = '.'.repeat(wordSearch.length + 2);
  const paddedWordSearch = [firstAndLastLines];
  wordSearch.forEach((line) => {
    paddedWordSearch.push('.' + line + '.');
  });
  paddedWordSearch.push(firstAndLastLines);

  let xmasCount = 0;

  paddedWordSearch.forEach((line, i) => {
    for (let j = 0; j < line.length; j++) {
      const char = line[j];
      if (char !== 'A') {
        continue;
      }

      // get 3x3 window around 'A'
      let window: string[] = new Array(2);
      window[0] = paddedWordSearch[i - 1].slice(j - 1, j + 2);
      window[1] = paddedWordSearch[i].slice(j - 1, j + 2);
      window[2] = paddedWordSearch[i + 1].slice(j - 1, j + 2);

      if (isDiagonalCross(window)) {
        xmasCount += 1;
      }
    }
  });

  console.log('Number of XMAS in word search: ' + xmasCount);
}

function isDiagonalCross(window: string[]): boolean {
  // top left and bottom right
  const pair1 = [window[0][0], window[2][2]];

  // top right and bottom left
  const pair2 = [window[0][2], window[2][0]];

  if (isPairValid(pair1) && isPairValid(pair2)) {
    return true;
  }
  return false;
}

function isPairValid(pair: string[]): boolean {
  return pair.length === 2 && pair.includes('M') && pair.includes('S');
}

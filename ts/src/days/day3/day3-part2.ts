import { readFileSync } from 'fs';
import { getFilepathRoot } from '../../utils/file-utilities';

const filepath = getFilepathRoot() + 'day3/memory.txt';

export async function runDay3Part2(): Promise<void> {
  const fileContents = readFileSync(filepath, 'utf-8');

  const mulRegex = /mul\((\d+),(\d+)\)/g;
  const conditionRegex = /((do\(\))|don\'t\(\))/g;
  const combinedRegex = new RegExp(
    `${mulRegex.source}|${conditionRegex.source}`,
    'g'
  );
  let currentMatch: RegExpExecArray | null;

  let total = 0;
  let mulEnabled = true;

  while ((currentMatch = combinedRegex.exec(fileContents)) != null) {
    if (currentMatch?.length !== 5) {
      throw new Error(
        `Exec match looks dodgy: ${JSON.stringify(currentMatch)}`
      );
    }
    if (isMatchMulExp(currentMatch)) {
      if (mulEnabled) {
        const { arg1, arg2 } = getMulArgs(currentMatch);
        total += arg1 * arg2;
      }
    } else {
      mulEnabled = isConditionDo(currentMatch);
    }
  }

  console.log('Total sum: ' + total);
}

function isMatchMulExp(currentMatch: RegExpExecArray): boolean {
  return currentMatch[1] !== undefined;
}

function getMulArgs(currentMatch: RegExpExecArray): {
  arg1: number;
  arg2: number;
} {
  const arg1: number = +currentMatch[1];
  const arg2: number = +currentMatch[2];
  return { arg1, arg2 };
}

function isConditionDo(currentMatch: RegExpExecArray): boolean {
  return currentMatch[3][2] !== 'n';
}

import { readFileSync } from 'fs';

const filepath = 'src/day3/memory.txt';

export async function runDay3Part1(): Promise<void> {
  const fileContents = readFileSync(filepath, 'utf-8');

  const mulRegex = /mul\((\d+),(\d+)\)/g;
  let currentMatch: RegExpExecArray | null;

  let total: number = 0;

  while ((currentMatch = mulRegex.exec(fileContents)) != null) {
    if (currentMatch?.length !== 3) {
      throw new Error(
        `Exec match looks dodgy: ${JSON.stringify(currentMatch)}`
      );
    }

    const arg1: number = +currentMatch[1];
    const arg2: number = +currentMatch[2];
    total += arg1 * arg2;
  }

  console.log('Total sum: ' + total);
}

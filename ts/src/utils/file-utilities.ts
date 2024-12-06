import { readFileSync } from 'fs';

/**
 *
 * @param filename - The path to the file, starting 'src/...'
 * @returns An string array of each line in the file
 */
export function getFileLines(filename: string): string[] {
  const file = readFileSync(filename, 'utf-8');
  const lines = file.split('\r\n');
  return lines;
}

/**
 *
 * @returns The start of the filepath for days' solutions
 */
export function getFilepathRoot(): string {
  return 'ts/src/days/';
}

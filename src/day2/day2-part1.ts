import { getFileLines } from '../utils/file-utilities';

const filename = 'src/day2/reports.txt';

export async function runDay2Part1(): Promise<void> {
  const lines = getFileLines(filename);

  let safeReports = 0;

  lines.forEach((line) => {
    if (isReportSafe(line)) {
      safeReports += 1;
    }
  });

  console.log('Number of safe reports: ' + safeReports);
}

function isReportSafe(report: string): boolean {
  const levels = report.split(' ').map(Number);

  if (
    !isListIncreasingOrDecreasing(levels, 'increasing') &&
    !isListIncreasingOrDecreasing(levels, 'decreasing')
  ) {
    return false;
  }
  if (!adjacentNumbersInListDifferCorrectly(levels)) {
    return false;
  }
  return true;
}

function isListIncreasingOrDecreasing(
  list: number[],
  mode: 'increasing' | 'decreasing'
): boolean {
  return list.every((val, i) => {
    if (i === list.length - 1) {
      return true;
    }
    if (mode === 'increasing') {
      return list[i + 1] > val;
    } else {
      return list[i + 1] < val;
    }
  });
}

function adjacentNumbersInListDifferCorrectly(list: number[]): boolean {
  return list.every((val, i) => {
    if (i === list.length - 1) {
      return true;
    }
    const nextValue = list[i + 1];
    const diff = Math.abs(nextValue - val);
    return diff >= 1 && diff <= 3;
  });
}

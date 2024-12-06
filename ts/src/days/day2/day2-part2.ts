import { getFileLines, getFilepathRoot } from '../../utils/file-utilities';

const filename = getFilepathRoot() + 'day2/reports.txt';

export async function runDay2Part2(): Promise<void> {
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
  const potentialReports: number[][] = [];

  // get all possible reports with one element removed
  for (let i = 0; i < levels.length; i++) {
    const reportWithoutLevel = [...levels];
    reportWithoutLevel.splice(i, 1);
    potentialReports.push(reportWithoutLevel);
  }

  // don't need to include initial 'levels' - if that works, removing the first level will also work
  return potentialReports.some((reportLevels) => {
    if (
      !isListIncreasingOrDecreasing(reportLevels, 'increasing') &&
      !isListIncreasingOrDecreasing(reportLevels, 'decreasing')
    ) {
      return false;
    }
    if (!adjacentNumbersInListDifferCorrectly(reportLevels)) {
      return false;
    }
    return true;
  });
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

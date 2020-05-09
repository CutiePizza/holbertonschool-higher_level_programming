#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) { console.log('0'); } else {
  let i;
  let first = Number.MIN_VALUE;
  let second = Number.MIN_VALUE;
  for (i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > first) {
      second = first;
      first = process.argv[i];
    } else if (process.argv[i] > second && process.argv[i] !== first) { second = process.argv[i]; }
  }
  console.log(second);
}

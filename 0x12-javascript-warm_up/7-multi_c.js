#!/usr/bin/node
try {
  if (!(process.argv[2])) {
    throw new Error('Missing number of occurences');
  }
  if (isNaN(process.argv[2])) {
    throw new Error('Missing number of occurences');
  }
  const x = process.argv[2];
  let i;
  for (i = 1; i <= x; i++) {
    console.log('C is fun');
  }
} catch (error) {
  console.log('Missing number of occurrences');
}

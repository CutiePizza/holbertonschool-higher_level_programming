#!/usr/bin/node
try {
  if (!(process.argv[2])) {
    throw new Error('Missing size');
  }
  if (isNaN(process.argv[2])) {
    throw new Error('Missing size');
  }
  const x = process.argv[2];
  let i;
  let j;
  for (i = 1; i <= x; i++) {
    for (j = 1; j <= x; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} catch (error) {
  console.log('Missing size');
}

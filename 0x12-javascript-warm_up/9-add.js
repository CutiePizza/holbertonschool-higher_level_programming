#!/usr/bin/node
function add (x, y) {
  return (parseInt(x) + parseInt(y));
}

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('NaN');
} else if (process.argv.length === 4) {
  if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
    console.log('NaN');
  } else {
    console.log(add(process.argv[2], process.argv[3]));
  }
}

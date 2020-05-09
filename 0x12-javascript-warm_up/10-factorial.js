#!/usr/bin/node
function factoriel (x) {
  if (x >= 1) { return (x * factoriel(x - 1)); } else { return (1); }
}

if (process.argv.length === 2) {
  console.log('1');
} else if (process.argv.length === 3) {
  console.log(factoriel(parseInt(process.argv[2])));
}

#!/usr/bin/node
exports.esrever = function (list) {
  const c = [];
  let j = 0;
  for (let i = list.length - 1; i !== -1; i--) {
    c[j] = list[i];
    j++;
  }
  return c;
};

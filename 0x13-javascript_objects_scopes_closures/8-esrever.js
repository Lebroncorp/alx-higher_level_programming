#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (group, newlist) {
    group.push(newlist);
    return group;
  }, []);
};

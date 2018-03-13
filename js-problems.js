// CHAPTER 4 PROBLEMS
function arrayToList(arr, tailPointer = null) {
/* Data structure to convert array to list
   [1, 2, 3] ====>   {val: 1, rest: {
                      val: 2, rest: {
                      val: 3, rest: null}
                      }}
    Tail pointer is what the last thing points to
*/
  if (!arr) return undefined;
  var ret;
  for (var i = arr.length-1; i >= 0; i--) {
      ret = {val: arr[i], rest: ret || tailPointer};
  }
  return ret;
}

function listToArray(list) {
  var arr = [];
  while (list !== null) {
    arr.push(list.val);
    list = list.rest;
  }
  return arr;
}

function prepend(arr, list) {
  //find last elemetn in array, point it to list
  if (!arr.length) return list;
  return arrayToList(arr, list);
}

function nth(list, index, depth = 0) {
  //looks for index-th item in this list
  //base case - found it!
  if (index == depth) return list.val;
  //base case - got to the end
  if (list.rest == null) return undefined;
  //Otherwise, update depth, and call self again.
  depth++;
  return nth(list.rest, index, depth);
}

var x = arrayToList([1, 2, 3, 4]);




// CHAPTER 5 PROBLEMS
function flatten(arr) {
  //flattens an array of arrays (only 1 level deep) into one deep array
  return arr.reduce((acc, val) => acc.concat(val), [])
}

var y = flatten([10, [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]])



//makes ANY and ALL (some and every) functions - they return true if any or all
//values (respectively) are true in the provided iterable
function anyAllMaker(loopBool) {
  return function(arr, func) {
    //check for empty array or non-array things
    if (!arr.length || typeof arr != "object") return false;

    //loop through
    for (var i in arr) {
      if (func(arr[i]) == loopBool) return loopBool;
    }
    //fallback case - all must be true/false
    return !loopBool;
  }
}

//returns true if all things in array are true, when tested with func
const all = anyAllMaker(false);
//returns true if any thing in array is true
const any = anyAllMaker(true);

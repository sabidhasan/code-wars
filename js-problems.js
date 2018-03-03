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

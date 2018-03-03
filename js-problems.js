function arrayToList(arr) {
/* Data structure to convert array to list
   [1, 2, 3] ====>   {val: 1, rest: {
                      val: 2, rest: {
                      val: 3, rest: null}
                      }}
*/
  if (!arr) return undefined;
  var ret;
  for (var i = arr.length-1; i >= 0; i--) {
    //if at beginning, create
    // if (!ret) {
      // ret = {val: arr[i], rest: null}
    // } else {
      // ret = {val: arr[i], rest: ret}
      ret = {val: arr[i], rest: ret || null}
    }
  }
  return ret;
}

function listToArray(list) {

}

function prepend(arr, list) {

}

function nth(list) {

}

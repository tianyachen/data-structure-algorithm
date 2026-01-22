/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let ans = [];
    let subarray = [];

    for (let i = 0; i < arr.length; i++) {
        subarray.push(arr[i]);
        
        if (subarray.length === size) {
            ans.push(subarray);
            subarray = [];
        }
    }

    if (subarray.length > 0) {
        ans.push(subarray);
    }
    return ans;
};

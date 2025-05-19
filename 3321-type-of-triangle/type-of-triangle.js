/**
 * @param {number[]} nums
 * @return {string}
 */
var triangleType = function(nums) {
    const [a, b, c] = nums;
    if (a + b <= c || b + c <= a || a + c <= b) {
        return "none";
    }
    else if (a == b && b == c) {
        return "equilateral";
    }
    else if (a == b || b == c || a == c) {
        return "isosceles";
    } else {
        return "scalene";
    }
};
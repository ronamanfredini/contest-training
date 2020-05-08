let binSearch = (arr, x, start, end) => { 
    let mid=Math.floor((start + end)/2); 
    if (start > end) return [mid, false]; 
    if (arr[mid]===x) return [mid, true]; 
    if(arr[mid] > x)  
        return binSearch(arr, x, start, mid-1); 
    else
        return binSearch(arr, x, mid+1, end); 
} 
   
let arr = [1,3,4,5,6,7,9,8,10,11,12,13,14,16];

function climbingLeaderboard(scores, alice) {



}

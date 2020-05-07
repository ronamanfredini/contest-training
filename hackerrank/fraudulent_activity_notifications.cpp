#include <iostream>
#include <vector>

using namespace std;
/* In case someone wants to pass in the pivValue, I broke partition into 2 pieces.
 */
int pivot(vector<int>& vec, int pivot, int start, int end){
    
    /* Now we need to go into the array with a starting left and right value. */
    int left = start, right = end-1;
    while(left < right){
        /* Increase the left and the right values until inappropriate value comes */
        while(vec.at(left) < pivot && left <= right) left++;
        while(vec.at(right) > pivot && right >= left) right--;
        
        /* In case of duplicate values, we must take care of this special case. */
        if(left >= right) break;
        else if(vec.at(left) == vec.at(right)){ left++; continue; }
        
        /* Do the normal swapping */
        int temp = vec.at(left);
        vec.at(left) = vec.at(right);
        vec.at(right) = temp;
    }
    return right;
}


/* Returns the k-th element of this array. */
int MoM(vector<int>& vec, int k, int start, int end){
    /* Start by base case: Sort if less than 10 size
     * E.x.: Size = 9, 9 - 0 = 9.
     */
    if(end-start < 10){
        sort(vec.begin()+start, vec.begin()+end);
        return vec.at(k);
    }
    
    vector<int> medians;
    /* Now sort every consecutive 5 */
    for(int i = start; i < end; i+=5){
        if(end - i < 10){
            sort(vec.begin()+i, vec.begin()+end);
            medians.push_back(vec.at((i+end)/2));
        }
        else{
            sort(vec.begin()+i, vec.begin()+i+5);
            medians.push_back(vec.at(i+2));
        }
    }
    
    int median = MoM(medians, medians.size()/2, 0, medians.size());
    
    /* use the median to pivot around */
    int piv = pivot(vec, median, start, end);
    int length = piv - start+1;
    
    if(k < length){
        return MoM(vec, k, start, piv);
    }
    else if(k > length){
        return MoM(vec, k-length, piv+1, end);
    }
    else
        return vec[k];
}

	
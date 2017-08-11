/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int x,y,m,n,max;
    int *arr=malloc(2*sizeof(int));

    for(x=0;x<(numsSize-1);x++){
        for(y=(x+1);y<numsSize;y++){
            if((nums[x]+nums[y])==target){
                m=x;
                n=y;
            }
        }
    }
    arr[0]=m;
    arr[1]=n;
    return arr;
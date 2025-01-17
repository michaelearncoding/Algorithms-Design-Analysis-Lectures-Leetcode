// 进一步优化，数组有序时提前终止算法
void sort(int[] nums) {
    int n = nums.length;
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 加一个布尔变量，记录是否进行过交换操作
        boolean swapped = false;
        for (int i = n - 1; i > sortedIndex; i--) {
            if (nums[i] < nums[i - 1]) {
                // swap(nums[i], nums[i - 1])
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
                swapped = true;
            }
        }
        // 如果一次交换操作都没有进行，说明数组已经有序，可以提前终止算法
        if (!swapped) {
            break;
        }
        sortedIndex++;
    }
}
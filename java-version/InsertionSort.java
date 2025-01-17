public class InsertionSort {
    public void sort(int[] nums) {
        int n = nums.length;
        for (int i = 1; i < n; i++) {
            int key = nums[i];
            int j = i - 1;
            // 向前比较并移动元素，直到找到适当的位置插入 key
            while (j >= 0 && nums[j] > key) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        InsertionSort sorter = new InsertionSort();
        int[] nums = {5, 2, 9, 1, 5, 6};
        sorter.sort(nums);
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }
}
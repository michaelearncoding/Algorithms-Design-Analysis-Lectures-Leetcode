// 使用插入排序的桶排序算法
void bucketSort(int[] nums, int bucketCount) {
    // 找到最大和最小元素
    // 用来计算索引偏移量和除数
    int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
    for (int num : nums) {
        min = Math.min(min, num);
        max = Math.max(max, num);
    }

    int offset = -min;

    // 计算理论上每个桶需要装的元素个数
    int bucketSize = (max - min) / bucketCount + 1;

    // 初始化桶
    ArrayList<Integer>[] buckets = new ArrayList[bucketCount];
    for (int i = 0; i < bucketCount; i++) {
        buckets[i] = new ArrayList<>();
    }

    // 将元素分配到桶中
    for (int num : nums) {
        // 用除法向下取整的方式计算桶的索引
        int index = (num + offset) / bucketSize;
        buckets[index].add(num);
    }

    // 对每个桶中的元素进行排序
    for (int i = 0; i < bucketCount; i++) {
        insertSort(buckets[i]);
    }

    // 合并有序桶
    int index = 0;
    for (int i = 0; i < bucketCount; i++) {
        for (int num : buckets[i]) {
            nums[index++] = num;
        }
    }
}

// 插入排序算法，详见前文「插入排序」
void insertSort(ArrayList<Integer> nums) {
    int sortedIndex = 0;
    while (sortedIndex < nums.size()) {
        for (int i = sortedIndex; i > 0; i--) {
            if (nums.get(i) < nums.get(i - 1)) {
                int tmp = nums.get(i);
                nums.set(i, nums.get(i - 1));
                nums.set(i - 1, tmp);
            } else {
                break;
            }
        }
        sortedIndex++;
    }
}
// 使用递归的桶排序算法
void bucketSort(ArrayList<Integer> nums, int bucketCount) {
    // 判断是否所有元素都已经有序
    boolean sorted = true;
    for (int i = 1; i < nums.size(); i++) {
        if (nums.get(i) < nums.get(i - 1)) {
            sorted = false;
            break;
        }
    }
    if (sorted) {
        // 所有元素都已经有序，结束递归
        return;
    }
    // 找到最大和最小元素
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
        int index = (num + offset) / bucketSize;
        buckets[index].add(num);
    }

    // 对每个桶中的元素进行排序
    for (int i = 0; i < bucketCount; i++) {
        bucketSort(buckets[i], bucketCount);
    }

    // 合并有序桶
    int index = 0;
    for (int i = 0; i < bucketCount; i++) {
        for (int num : buckets[i]) {
            nums.set(index++, num);
        }
    }
}
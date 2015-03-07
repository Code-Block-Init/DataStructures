public class bucketSort {
	public static void BucketSort(int[] a, int m) {
		int[] buckets = new int[m];
		for(int j = 0; j < m; ++j) {
			buckets[j] = 0;
		}
		for(int i = 0; i < a.length; ++i) {
			++buckets[a[i]];
		}
		for(int i = 0, j = 0; j < m; ++j) {
			for(int k = buckets[j]; k > 0; --k) {
				a[i++] = j;
			}
		}
	}
}

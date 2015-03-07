public class NonRecFibo {
	public static int fibonacci(int n) {
		int prev = -1;
		int result = 1;
		for(int i = 0; i <= n; ++i) {
			int sum = result + prev;
			prev = result;
			result = sum;
		}
		return result;
	}
}

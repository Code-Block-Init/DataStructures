public class recursiveFibonnaci {
	public static int fibonnaci(int n) {
		if(n == 0 || n == 1) {
			return n;
		} else {
			return fibonnaci(n - 1) + fibonnaci(n - 2);
		}
	}
}

public class constructors {
	protected Object[] data;
	protected int base;
	public Array(int m, int n) {
		data = new Object[n];
		base = m;
	}
	public Array() {
		this(0, 0);
	}
	public Array(int n) {
		this(n, 0);
	}

	// add some more.. (^_^)
}

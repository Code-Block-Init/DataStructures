public interface priorityQueue extends Container {
	void enqueue(Comparable object);
	Comparable findMin();
	Comparable dequeueMin();
}

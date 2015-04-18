public class criticalpath {
	public static digraph criticalpathanalysis(digraph g) {
		int n = g.getNumberOfVertices();
		int[] earliestTime = new int[n];
		earliestTime[0] = 0;
		g.topologicalOrderTraversal(
			new EarliestTimeVisitor(earliestTime));
		int[] latestTime = new int[n];
		latestTime[n-1] = earliestTime[n-1];
		g.depthFirstTraversal(new PostOrder (
			new LatestTimeVisitor(latestTime)), 0);
		digraph slackGraph = new digraphAsLists(n);
		for(int v=0; v<n; ++v)
			slackGraph.addVertex(v);
		Enumeration p = g.getEdges();
		while(p.hasMoreElements()) {
			Edge edge = (Edge) p.nextElement();
			int n0 = edge.getV0().getNumber();
			int n1 = edge.getV1().getNumber();
			int wt = (Int) edge.getWeight();
			int slack = latestTime[n1] - earliestTime[n0] - wt.intValue();
			slackGraph.addEdge(n0, n1, new Int(slack));
		}
		return dijkstras(slackGraph, 0);
	}
}

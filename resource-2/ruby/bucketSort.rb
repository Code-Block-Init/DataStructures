def bucketSort(a, n, bucket, m)
	for j in 0 ... m
		bucket[j] = 0
	end
	for i in 0 ... n
		bucket[a[i]] += 1
	end
	i = 0
	for j in 0 ... m
		for k in 0 ... bucket[j]
			a[i] = j
			i += 1
		end
	end
end

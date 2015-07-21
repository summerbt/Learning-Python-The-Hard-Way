#hashmap
def new(num_buckets=256):
	"""Initializes a Map with a the given number of buckets."""
	#print("""New(%r) is called: creating a list called
	# '/aMap'/ with %r buckets.
	# """ % (num_buckets, num_buckets))
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	#print("""Hash_key(%r, %r) is called: returns a number
	#	that is a result of \'%\' of the hash() and the
	#	 number of buckets in 'aMap' will always be smaller
	#	  than the total number of buckets because \'%\' returns 
	#	  a remainder only.""" % (aMap, key))
	#"""Given a key this will create a number and convert it to an index for the aMap's buckets."""
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	#print("""get_bucket(%r,%r) is called: Uses the hash_key()
	#	function to return an int that becomes the bucket_id.
	#	bucket_id is used to reference an index within aMap.
	#	Then aMap[bucket_id] returns the value at that index.
	#	""" % (aMap,key))
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and values of a slot found in a bucket.
	Returns -1, key, and default (None if not set)
	"""
	#print("""get_slot(%r,%r,%r) is called:
	# This fuctions returns the list that is stored
	# within the given bucket. for every item (tuple) 
	 #in the bucket it iterates through trying to find a match where k = %r
	 #then it return the index, key, and value.""" % (aMap, key, default, key))
	bucket = get_bucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, default

def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	#print("""get(%r, %r, %r) is called: The i, k, v values from get() funtion
	 #are unpacked and only the (v)value is returned.
	 #""" % (aMap, key, default))
	i, k, v = get_slot(aMap, key, default=default)
	return v

def set(aMap, key, value):
	"""	Set the key to the value, replacing any exsisting value."""
	#print("""set(%r,%r,%r) is called: Uses get_bucket(%r, %r)
	#	to return a bucket(list). And then uses get_slot(%r,%r) 
	#	to return (index, key, value) if an index of 0 or greater 
	#	is returned then the k and v are replaced.""" % (aMap, key, value, aMap, key, aMap, key))
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i >=0:
		#the key exists, replace it
		bucket[i]=(key, value)
	else:
		#the key does not exist, append to create it
		bucket.append((key,value))

def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap,key)
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k,v in bucket:
				print(k,v)
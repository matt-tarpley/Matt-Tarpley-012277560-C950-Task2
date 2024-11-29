#Hashtable class
#Citing sources:
    # C950 - Webinar-1 - Let’s Go Hashing
    # W-1_ChainingHashTable_zyBooks_Key-Value.py
    # Ref: zyBooks: Figure 7.8.2: Hash table using chaining.

class HashTable:
    def __init__(self, length=20):
        # initialize the hash table with empty bucket list entries.
        self.length = length
        self.hashTable = []
        for i in range(self.length):
            self.hashTable.append([])
    
    #insert into hashtable
    def insert(self, id, package):
        key = hash(id) % self.length
        if[id, package] not in self.hashTable[key]:
            self.hashTable[key].append([id,package])

    #updates based on id
    def update(self, id, package):
        key = hash(id) % self.length
        for x in self.hashTable[key]:
            if x[0] == id:
                x[1] = package
            return

    #lookup by id
    def lookup(self, id):
        key = hash(id) % self.length
        for x in self.hashTable[key]:
            if x[0] == id:
                return x[1]

        return None

    #remove by id
    def delete(self, id):
        bucket = hash(id) % len(self.hashTable)
        bucket_list = self.hashTable[bucket]
 
        # loop through list checking for key
        for kv in bucket_list:
          if kv[0] == id:
              bucket_list.remove([kv[0],kv[1]]) #remove key and value

    #helper method to print contents
    def printContents(self):
        for bucket in self.hashTable:
            for key, package in bucket:
                package.printDetails() 

 

#Hashtable class
#Citing sources:
    # C950 - Webinar-1 - Let’s Go Hashing
    # W-1_ChainingHashTable_zyBooks_Key-Value.py
    # Ref: zyBooks: Figure 7.8.2: Hash table using chaining.

class HashTable:
    def __init__(self, length=20):
        # initialize the hash table with empty bucket list entries.
        self.hashTable = []
        for i in range(length):
            self.hashTable.append([])
    
    #insert into hashtable
    def insert(self, id, package): # does both insert and update
        bucket = hash(id) % len(self.hashTable)
        bucket_list = self.hashTable[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list: 
            if kv[0] == id:
                kv[1] = package
                return True

        # if not, insert the item to the end of the bucket list
        key_value = [id, package]
        bucket_list.append(key_value)
        return True

    #lookup by id
    def lookup(self, id):
        bucket = hash(id) % len(self.hashTable)
        bucket_list = self.hashTable[bucket]
        for pair in bucket_list:
            if id == pair[0]:
                return pair[1]
        return None  #if no match return none

    #remove by id
    def Delete(self, id):
        bucket = hash(id) % len(self.hashTable)
        bucket_list = self.hashTable[bucket]
 
        # loop through list checking for key
        for kv in bucket_list:
          if kv[0] == id:
              bucket_list.remove([kv[0],kv[1]]) #remove key and value

    #helper method to print contents
    def printContents(self):
        for bucket in self.hashTable:
            for key, value in bucket:
                print(f"Key: {key}, Value: {value}")
 

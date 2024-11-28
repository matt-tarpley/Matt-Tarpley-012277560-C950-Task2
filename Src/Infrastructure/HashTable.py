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
    
    #INSERT
    def insert(self, key, item): #  does both insert and update 
        bucket = hash(key) % len(self.hashTable)
        bucket_list = self.hashTable[bucket]
 
        # update key if it is already in the bucket
        for kv in bucket_list:
          if kv[0] == key:
            kv[1] = item
            return True
        
        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    #LOOKUP
    def lookup(self, key):
        bucket = hash(key) % len(self.hashTable)
        bucket_list = self.hashTable[bucket]
 
        # search for the key in the bucket list
        for kv in bucket_list:
          if kv[0] == key:
            return kv[1] # return associated value
        return None #otherwise nothing matches key, therefore, return not found

    #DELETE
    def DELETE(self, key):
        bucket = hash(key) % len(self.hashTable)
        bucket_list = self.hashTable[bucket]
 
        # loop through list checking for key
        for kv in bucket_list:
          if kv[0] == key:
              bucket_list.remove([kv[0],kv[1]]) #remove key and value
 

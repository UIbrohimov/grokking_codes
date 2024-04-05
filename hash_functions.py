# A hash function is a function where you put in a string and you get back a number

"""
Tasavur qiling bizda array bor, biz shu arrayga biror stringni joylash uchun
u stringni hash functionga tiqamiz va natijasiga integer olamiz, va shu stringni hash
function qaytargan integerga teng bo'lgan indexga joylashtiramiz.

Shunda biz yuqorida qo'ygan stringni arraydan olishimiz uchun biz uni array ichidan izlashimiz kerak emas
biz shu stringni hash functionga tiqsak, hash function bizga ushbu stringni arraydagi indexini beradi.
unutmang bir xil string uchun hash function bir xil integer qaytaradi.
"""

class HashTable:
    def __init__(self):
        self.table = [None] * 1000000
        self.size = 1000000
        self.count = 0
    
    def hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        index = self.hash(key)
        self.table[index] = value
        self.count += 1
    
    def get(self, key):
        index = self.hash(key)
        value = self.table[index]
        return value

    def remove(self, key):
        index = self.hash(key)
        value = self.table[index]
        self.table[index] = None
        self.count -= 1
        return value
    
    def size(self):
        return self.size
    
    def count(self):
        return self.count
    
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def __len__(self):
        return self.count

    def __str__(self):
        return str(self.table)


a = HashTable()

a.put(1, 1)
a.put(2, 2)


print(a.get(2))

"""
For you to not hit the worst case of hash table performace
you need two things, the first is load factor number of items in a hash table/number of slots in a hash table

the second is a good hash function
"""

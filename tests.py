import database

db = database.TransactionalKeyValueStore()

print(db.get("A"))  # Output: None
try:
    db.put("A", 5)  # Error: No transaction in progress
except Exception as e:
    print(e)

db.begin_transaction()
db.put("A", 5)
print(db.get("A"))  # Output: None
db.put("A", 6)
print(db.get("A"))  # Output: None
db.commit()
print(db.get("A"))  # Output: 6
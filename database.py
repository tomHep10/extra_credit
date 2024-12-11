class TransactionalKeyValueStore:
    def __init__(self):
        self._data = {}
        self._transaction_data = None
        self._transaction_original = None

    def begin_transaction(self):
        if self._transaction_data is not None:
            raise Exception("A transaction is already in progress")
        
        self._transaction_original = self._data.copy()
        self._transaction_data = {}

    def put(self, key, value):
        if self._transaction_data is None:
            raise Exception("No transaction in progress")
        
        self._transaction_data[key] = value

    def get(self, key):
        if self._transaction_data is not None:
            return None
        return self._data.get(key)

    def commit(self):
        if self._transaction_data is None:
            raise Exception("No transaction to commit")
        
        self._data.update(self._transaction_data)
        self._transaction_data = None
        self._transaction_original = None

    def rollback(self):
        if self._transaction_data is None:
            raise Exception("No transaction to rollback")
        
        self._data = self._transaction_original
        self._transaction_data = None
        self._transaction_original = None
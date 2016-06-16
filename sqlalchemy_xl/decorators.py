_DISTRIBUTE_HASH = {}


def distribute_by_hash(column_name):
    def _decorator(original_class):
        global _DISTRIBUTE_HASH
        table_name = original_class.__tablename__
        assert table_name not in _DISTRIBUTE_HASH
        _DISTRIBUTE_HASH[table_name] = column_name
        return original_class
    return _decorator

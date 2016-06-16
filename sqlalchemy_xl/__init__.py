from sqlalchemy import create_engine
from decorators import _DISTRIBUTE_HASH


class SqlSchemeDump(object):

    def __init__(self):
        self.engine = create_engine('postgresql://', strategy='mock',
                                    executor=self.dump)
        self.sql = ''

    def dump(self, sql, *multiparams, **params):
        create_table_sql = str(sql.compile(dialect=self.engine.dialect))\
            .rstrip()
        table_name = str(sql.element)
        if table_name in _DISTRIBUTE_HASH:
            # Append DISTRIBUTE instruction to sql scheme.
            column_name = _DISTRIBUTE_HASH[table_name]
            create_table_sql += ' DISTRIBUTE BY HASH(' + column_name + ');'
        self.sql += create_table_sql + "\n"

    def generate(self, metadata):
        '''
        Take sqlachemy Base.metadata to generate Postgres-XL ready SQL scheme.
        '''
        metadata.create_all(self.engine, checkfirst=False)


def generate_sql(metadata):
    sql_scheme = SqlSchemeDump()
    sql_scheme.generate(metadata)
    return sql_scheme.sql



import os
from neo4j import GraphDatabase, basic_auth

db_pass = os.getenv("DB_PASS", "b.2ZeVO4IEjGHA.IyNw24ViPXB1dx0q")
db_url = os.getenv("DB_URL", "bolt://hobby-ebkjiiillfimgbkejcngngcl.dbs.graphenedb.com:24786")

driver = GraphDatabase.driver(db_url,
                              auth=basic_auth("neo4j", db_pass))


class Neo4jConnection:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        if 'db' not in self.__shared_state:
            self.__shared_state['db'] = self._connect()

    def get_db(self):
        return self.__shared_state['db']

    def close_db(self):
        self.__shared_state['db'].close()
        self.__shared_state.pop('db')

    def _connect(self):
        return driver.session()

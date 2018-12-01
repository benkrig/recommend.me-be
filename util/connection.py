import os
from neo4j.v1 import GraphDatabase, basic_auth

password = os.getenv("DB_USER", "root")
driver = GraphDatabase.driver('bolt://localhost',
                              auth=basic_auth("neo4j", password))


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

    def _connect(self):
        return driver.session()

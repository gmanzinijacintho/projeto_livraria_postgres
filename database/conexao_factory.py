import psycopg2


class ConexaoFactory:

    def get_conexao(self):
        return psycopg2.connect(
            host='berry.db.elephantsql.com',
            database='gwrxmpmi',
            user='gwrxmpmi',
            password='l2Hf4Bft8N6qycmfOIUApyVdGiV1O9pf'
        )

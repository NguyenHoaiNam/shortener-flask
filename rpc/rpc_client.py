import oslo_messaging as om
import conf

CONF = conf.CONF

transport = om.get_transport(CONF)
target = om.Target(topic='shortener')


def get_client():
    return om.RPCClient(transport, target)


class TaskClient(object):
    def __init__(self):
        self.rpc_client = get_client()
        self._client = self.rpc_client.prepare()

    def _cast(self, cctx, name, **kwargs):
        return self._client.cast(cctx, name, **kwargs)

    def _call(self, cctx, name, **kwargs):
        return self._client.call(cctx, name, **kwargs)

    def insert_database(self, record):
        return self._call({}, 'insert_database', record=record.to_dict())

    def query_database(self, short_link):
        return self._call({}, 'query_database', short_link=short_link)

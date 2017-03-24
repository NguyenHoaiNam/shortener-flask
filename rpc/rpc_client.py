import oslo_messaging as om
import conf

CONF = conf.CONF

transport = om.get_transport(CONF)
target = om.Target(topic='shortener')


def get_client():
    return om.RPCClient(transport, target)


class TaskClient(object):
    def __init__(self):
        self._client = get_client()

    def _cast(self, cctx, name, **kwargs):
        return self._client.cast(cctx, name, **kwargs)

    def _call(self, cctx, name, **kwargs):
        return self._client.call(cctx, name, **kwargs)

    def insert_database(self, cctx, record):
        return self._cast(cctx, record)

    def query_database(self, cctx, short_link):
        return self._call(cctx, short_link)

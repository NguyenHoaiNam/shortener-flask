import oslo_messaging as om
from oslo_config import cfg

from app import client_config

transport = om.get_transport(cfg.CONF)
client_config.register_configure()
cfg.CONF(['--config-file', 'client.conf'])
transport = om.get_transport(cfg.CONF)
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

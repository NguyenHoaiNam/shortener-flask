import oslo_messaging as om
from oslo_config import cfg
from server import server_config
from app.models import Url

# Register command:
transport = om.get_transport(cfg.CONF)
server_config.register_configure()
cfg.CONF(['--config-file', 'server.conf'])

transport = om.get_transport(cfg.CONF)
target = om.Target(topic='shortener', server='10.164.180.110')


class InteractDB(object):
    def insert_database(self, cctx, record):
        try:
            cctx.add(record)
            cctx.commit()
        except Exception as e:
            raise e

    def querry_database(self, cctx, short_link):
        origin_link = cctx.query(Url).filter(
            Url.short_link == short_link).one()
        return origin_link.org_link

endpoints = [InteractDB(), ]

access_policy = om.rpc.dispatcher.DefaultRPCAccessPolicy
server_rpc = om.get_rpc_server(transport, target, endpoints,
                               executor='eventlet',
                               access_policy=access_policy)

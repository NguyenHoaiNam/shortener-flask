from oslo_config import cfg
from conf import server_conf

CONF = cfg.CONF

server_conf.register_configure(CONF)


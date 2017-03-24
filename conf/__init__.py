from oslo_config import cfg
from conf import server_conf

CONF = cfg.CONF
CONF(['--config-file', 'conf/shortener.conf'])
server_conf.register_configure(CONF)


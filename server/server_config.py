from oslo_config import cfg

oslo_messaging_rabbit_group = cfg.OptGroup('oslo_messaging_rabbit')

rabbit_opts = [
    cfg.StrOpt('rabbit_host', default='localhost'),
    cfg.PortOpt('rabbit_port', default=5672),
    cfg.StrOpt('rabbit_userid', default='guest'),
    cfg.StrOpt('rabbit_password', default='guest'),
    cfg.StrOpt('rabbit_login_method', default='AMQPLAIN'),
    cfg.StrOpt('rabbit_virtual_host', default='/')
]


def register_configure():
    cfg.CONF.register_group(oslo_messaging_rabbit_group)
    cfg.CONF.register_opts(rabbit_opts)

from oslo_config import cfg


pin_version = cfg.StrOpt('pin_release', default=None)


def register_configure(conf):
    conf.register_opt(pin_version)

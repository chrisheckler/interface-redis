from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class RedisProvides(Endpoint):
    def configure(self, host, port, password=None):
        """
        Configure the host-port relation by providing a port and host.
        """
        for relation in self.relations:
            relation.send['host'] = host
            relation.send['port'] = port
            if password:
                relation.send['password'] = password

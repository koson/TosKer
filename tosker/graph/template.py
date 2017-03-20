from .nodes import Container, Software, Volume


class Template:

    def __init__(self, name):
        self._nodes = {}
        self.name = name
        self.deploy_order = []
        self.outputs = []

    @property
    def container_order(self):
        return (i for i in self.deploy_order if type(i) is Container)

    @property
    def volume_order(self):
        return (i for i in self.deploy_order if type(i) is Volume)

    @property
    def software_order(self):
        return (i for i in self.deploy_order if type(i) is Software)

    def push(self, node):
        self._nodes[node.name] = node
        self.deploy_order.append(node)

    def __getitem__(self, name):
        return self._nodes.get(name, None)

    def __str__(self):
        return ', '.join((i.name for i in self.deploy_order))
from ..utility import Logger


class Container_manager:

    def __init__(self, docker):
        self._log = Logger.get(__name__)
        self._docker = docker

    def create(self, node):
        if node.persistent:
            self._docker.create_container(node)
        else:
            if node.to_build:
                self._docker.build_image(node)
            else:
                self._docker.pull_image(node.image)

    def start(self, node):
        stat = self._docker.inspect_container(node)
        if stat is not None:
            node.id = stat['Id']
            self._docker.start_container(node)
        else:
            self._log.error(
                'ERROR: Container "{}" not exists!'.format(node.name))

    def stop(self, node):
        self._docker.stop_container(node)
        self._docker.delete_container(node)
        self._docker.create_container(node, from_saved=True)

    def delete(self, node):
        self._docker.delete_container(node)
        self._docker.delete_image(self._docker.get_saved_image(node))
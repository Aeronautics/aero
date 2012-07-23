class BaseAdapter(object):
    def search(self, query):
        raise NotImplementedError

    def install(self, package):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def upgrade(self, query=None):
        raise NotImplementedError

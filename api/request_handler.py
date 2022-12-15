class RequestHandler:

    def __init__(self, environment):
        self.environment = environment

    @property
    def path(self):
        return self.environment["PATH_INFO"]

"""
    @property
    def args(self):
        return self._get_path_without_args().split('@')

    def path_contain_args(self) -> bool:
        return self.environment["PATH_INFO"].split('/')[-1].find('{') >= 0

    def _get_path_without_args(self):
        return self.environment["PATH_INFO"][self.environment["PATH_INFO"].rfind('/') + 1:]
"""
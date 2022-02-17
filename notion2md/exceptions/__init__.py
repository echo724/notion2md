class UnInitializedConfigException(Exception):
    def __str__(self):
        return "Config is not initialized with values"

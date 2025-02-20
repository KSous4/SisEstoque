import toml


def getConfig(configName: str) -> dict:
    data: dict = toml.load('../config/config.toml')
    data = data.get(configName)
    return data

from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[
        'config/services/default.toml',
        'config/services/.secrets.toml',
        'config/services/code_set.toml',

    ]
)

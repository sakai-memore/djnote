from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[
        'shared/services/default.toml',
        # 'default.toml',
    ]
)

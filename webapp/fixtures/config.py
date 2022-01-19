from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[
        'fixtures/default.toml',
        # 'default.toml',
    ]
)

from decouple import config

if config('ENV_TYPE') == "dev":
    from .dev import *
elif config('ENV_TYPE') == "prod":
    from .prod import *
else:
    print("Error! Invalid Env type!")
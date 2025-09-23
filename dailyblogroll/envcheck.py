import os

vars_to_check = [
    'OPENAI_API_KEY',
    'WP_URL',
    'WP_USER',
    'WP_APP_PASSWORD',
    'WP_STATUS',
    'CABAL_DIR',
    'NUMBER_OF_PROCESSORS',
    'OPENAI_API_KEY'
]

for var in vars_to_check:
    if not os.getenv(var):
        print(f"Environment variable '{var}' is not set.")
    else:
        print(f"Environment variable '{var}' is set.")
        print(f"{var} = {os.getenv(var)}")


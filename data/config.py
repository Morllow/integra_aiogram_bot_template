from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")
ip = env.str("ip")

PG_HOST = env.str('PG_HOST')
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")

REDIS_HOST=env.str('REDIS_HOST')

PROVIDER_TOKEN = env.str('PROVIDER_TOKEN')

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{PG_HOST}/{DATABASE}'

# create a blink batch TableEnvironment
from pyflink.table import EnvironmentSettings, BatchTableEnvironment

env_settings = EnvironmentSettings.new_instance().in_batch_mode().use_blink_planner().build()
table_env = BatchTableEnvironment.create(environment_settings=env_settings)

table = table_env.from_elements([(1, 'Hi'), (2, 'Hello')])
table.to_pandas()

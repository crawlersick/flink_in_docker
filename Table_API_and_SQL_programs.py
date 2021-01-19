from pyflink.table import EnvironmentSettings, StreamTableEnvironment

# 1. create a TableEnvironment
env_settings = EnvironmentSettings.new_instance().in_streaming_mode().use_blink_planner().build()
table_env = StreamTableEnvironment.create(environment_settings=env_settings)

# 2. create source Table
table_env.execute_sql("""
    CREATE TABLE datagen (
        id INT,
        data STRING
    ) WITH (
        'connector' = 'datagen',
        'fields.id.kind' = 'sequence',
        'fields.id.start' = '1',
        'fields.id.end' = '10'
    )
""")

# 3. create sink Table
table_env.execute_sql("""
    CREATE TABLE print (
        id INT,
        data STRING
    ) WITH (
        'connector' = 'print'
    )
""")

# 4. query from source table and perform caculations
# create a Table from a Table API query:
source_table = table_env.from_path("datagen")
# or create a Table from a SQL query:
source_table = table_env.sql_query("SELECT * FROM datagen")

result_table = source_table.select("id + 1, data")

# 5. emit query result to sink table
# emit a Table API result Table to a sink table:
result_table.execute_insert("print").get_job_client().get_job_execution_result().result()
# or emit results via SQL query:
table_env.execute_sql("INSERT INTO print SELECT * FROM datagen").get_job_client().get_job_execution_result().result()


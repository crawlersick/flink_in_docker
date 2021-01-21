from pyflink.common.serialization import SimpleStringEncoder
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import StreamingFileSink
import logging


def tutorial():
    logging.info("#################################11############################3")
    print("#############################5555555555##########################################################33")
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    ds = env.from_collection(
        collection=[(1, 'aaa'), (2, 'bbb')],
        type_info=Types.ROW([Types.INT(), Types.STRING()]))
    ds.add_sink(StreamingFileSink
                .for_row_format('/tmp/output', SimpleStringEncoder())
                .build())
    env.execute("tutorial_job")


if __name__ == '__main__':
    tutorial()

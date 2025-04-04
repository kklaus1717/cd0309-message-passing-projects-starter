import time
from concurrent import futures
import logging

import grpc
import personUsageStatistic_pb2
import personUsageStatistic_pb2_grpc

class PersonUsageStatisticServicer(personUsageStatistic_pb2_grpc.PersonUsageStatisticServiceServicer):

    def Create(self, request, context):
        request_value = {
            "id": request.id,
            "created_at": request.created_at,
        }
        logger.info(f"Received the data: {request_value}")

        return personUsageStatistic_pb2.PersonUsageStatisticMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
personUsageStatistic_pb2_grpc.add_PersonUsageStatisticServiceServicer_to_server(PersonUsageStatisticServicer(), server)

# Set up logging
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)
logger = logging.getLogger(__name__)

server.add_insecure_port("[::]:5005")
server.start()
logger.info(f"gRPC DW server starting on port 5005...")
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

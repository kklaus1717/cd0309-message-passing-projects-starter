import time
from concurrent import futures
import logging

import grpc
import personUsageStatistic_pb2
import personUsageStatistic_pb2_grpc

class PersonUsageStatisticServicer(personUsageStatistic_pb2_grpc.PersonUsageStatisticServiceServicer):

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "created_at": request.created_at,
        }
        print(request_value)

        return personUsageStatistic_pb2.PersonUsageStatisticMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
personUsageStatistic_pb2_grpc.add_PersonUsageStatisticServiceServicer_to_server(PersonUsageStatisticServicer(), server)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Server starting on port 5005...")

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

from datetime import datetime

from app.udaconnect.models import Person
from app.udaconnect.schemas import (
    PersonSchema,
)
from app.udaconnect.services import PersonService
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa



@api.route("/persons")
class PersonsResource(Resource):

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons



import time
from concurrent import futures

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


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
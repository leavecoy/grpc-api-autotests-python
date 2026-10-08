from uuid import UUID

from grpc import Channel
from v1.common_pb2 import Empty
from v1.exercises_pb2 import (
    CreateExerciseRequest,
    DeleteExerciseRequest,
    GetExerciseRequest,
    GetExerciseResponse,
    ListExercisesRequest,
    ListExercisesResponse,
    UpdateExerciseRequest,
)
from v1.exercises_pb2_grpc import ExercisesServiceStub

from clients.client import GRPCTestClient
from clients.types import GRPCMetadata


class ExercisesClient(GRPCTestClient):
    def __init__(self, channel: Channel, metadata: GRPCMetadata):
        super().__init__(channel, metadata)

        self.stub = ExercisesServiceStub(self.channel)

    def create_exercise_api(
        self, request: CreateExerciseRequest
    ) -> GetExerciseResponse:

        return self.call(self.stub.CreateExercise, request)

    def create_exercise(
        self,
        title: str,
        course_id: UUID,
        order_index: int,
        description: str,
        max_score: int | None = None,
        min_score: int | None = None,
        estimated_time: str | None = None,
    ) -> GetExerciseResponse:
        request = CreateExerciseRequest(
            title=title,
            course_id=str(course_id),
            max_score=max_score,
            min_score=min_score,
            order_index=order_index,
            description=description,
            estimated_time=estimated_time,
        )

        response = self.create_exercise_api(request)

        return response

    def get_exercise_api(self, request: GetExerciseRequest) -> GetExerciseResponse:

        return self.call(self.stub.GetExercise, request)

    def get_exercise(self, exercise_id: UUID) -> GetExerciseResponse:

        request = GetExerciseRequest(id=str(exercise_id))
        response = self.get_exercise_api(request)

        return response

    def list_exercises_api(
        self, request: ListExercisesRequest
    ) -> ListExercisesResponse:

        return self.call(self.stub.ListExercises, request)

    def list_exercises(self, course_id: UUID) -> ListExercisesResponse:

        request = ListExercisesRequest(course_id=str(course_id))
        response = self.list_exercises_api(request)
        return response

    def update_exercise_api(
        self, request: UpdateExerciseRequest
    ) -> GetExerciseResponse:

        return self.call(self.stub.UpdateExercise, request)

    def update_exercise(
        self,
        exercise_id: UUID,
        title: str | None = None,
        max_score: int | None = None,
        min_score: int | None = None,
        order_index: int | None = None,
        description: str | None = None,
        estimated_time: str | None = None,
    ) -> GetExerciseResponse:

        request = UpdateExerciseRequest(
            id=str(exercise_id),
            title=title,
            max_score=max_score,
            min_score=min_score,
            order_index=order_index,
            description=description,
            estimated_time=estimated_time,
        )

        response = self.update_exercise_api(request)

        return response

    def delete_exercise_api(self, request: DeleteExerciseRequest) -> Empty:

        return self.call(self.stub.DeleteExercise, request)

    def delete_exercise(self, exercise_id: UUID) -> Empty:

        request = DeleteExerciseRequest(id=str(exercise_id))
        response = self.delete_exercise_api(request)

        return response

from uuid import UUID

from grpc import Channel
from v1.common_pb2 import Empty
from v1.files_pb2 import (
    CreateFileRequest,
    DeleteFileRequest,
    GetFileRequest,
    GetFileResponse,
)
from v1.files_pb2_grpc import FilesServiceStub

from clients.client import GRPCTestClient
from clients.types import GRPCMetadata


class FilesClient(GRPCTestClient):
    def __init__(self, channel: Channel, metadata: GRPCMetadata):
        super().__init__(channel, metadata)
        self.stub = FilesServiceStub(self.channel)

    def create_file_api(self, request: CreateFileRequest) -> GetFileResponse:

        return self.call(self.stub.CreateFile, request)

    def create_file(
        self, filename: str, directory: str, content: bytes
    ) -> GetFileResponse:

        request = CreateFileRequest(
            filename=filename, directory=directory, content=content
        )
        response = self.create_file_api(request)

        return response

    def get_file_api(self, request: GetFileRequest) -> GetFileResponse:

        return self.call(self.stub.GetFile, request)

    def get_file(self, file_id: UUID) -> GetFileResponse:

        request = GetFileRequest(id=str(file_id))
        response = self.get_file_api(request)

        return response

    def delete_file_api(self, request: DeleteFileRequest) -> Empty:

        return self.call(self.stub.DeleteFile, request)

    def delete_file(self, file_id: UUID) -> Empty:

        request = DeleteFileRequest(id=str(file_id))
        response = self.delete_file_api(request)

        return response

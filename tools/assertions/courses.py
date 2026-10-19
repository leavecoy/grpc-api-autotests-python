from v1.common_pb2 import Course, Empty
from v1.courses_pb2 import (
    CreateCourseRequest,
    GetCourseRequest,
    GetCourseResponse,
    ListCoursesRequest,
    ListCoursesResponse,
    UpdateCourseRequest,
)

from tools.assertions.base import assert_equal, assert_is_empty, assert_not_empty


def assert_course(actual: Course, expected: Course):

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.preview_file, expected.preview_file, "preview_file")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.created_by_user, expected.created_by_user, "created_by_user")


def assert_create_course_response(
    request: CreateCourseRequest, response: GetCourseResponse
):

    assert_not_empty(response.course.id, "id")

    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(
        response.course.preview_file.id, request.preview_file_id, "preview_file"
    )
    assert_equal(
        response.course.estimated_time, request.estimated_time, "estimated_time"
    )
    assert_equal(
        response.course.created_by_user.id,
        request.created_by_user_id,
        "created_by_user",
    )


def assert_get_course_response(
    request: GetCourseRequest, response: GetCourseResponse, expected_course: Course
):

    assert_equal(response.course.id, request.id, "id")
    assert_course(response.course, expected_course)


def assert_list_courses_response(
    request: ListCoursesRequest,
    response: ListCoursesResponse,
    expected_courses: list[Course],
):
    assert len(response.courses) == len(expected_courses)

    for i in range(len(response.courses)):
        assert_equal(response.courses[i].created_by_user.id, request.user_id, "user_id")

    courses = 0

    for actual_course in response.courses:
        for expected_course in expected_courses:
            if actual_course.id == expected_course.id:
                assert_course(actual_course, expected_course)
                courses += 1

    assert courses == len(expected_courses)


def assert_update_course_response(
    request: UpdateCourseRequest, response: GetCourseResponse
):

    assert_equal(response.course.id, request.id, "id")

    if request.HasField("title"):
        assert_equal(response.course.title, request.title, "title")

    if request.HasField("max_score"):
        assert_equal(response.course.max_score, request.max_score, "max_score")

    if request.HasField("min_score"):
        assert_equal(response.course.min_score, request.min_score, "min_score")

    if request.HasField("description"):
        assert_equal(response.course.description, request.description, "description")

    if request.HasField("description"):
        assert_equal(
            response.course.estimated_time, request.estimated_time, "estimated_time"
        )


def assert_delete_course_response(response: Empty):
    assert_is_empty(response, "response")

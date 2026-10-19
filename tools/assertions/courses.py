"""Проверки данных курсов и ответов gRPC-сервиса курсов."""

from v1.common_pb2 import Course, Empty
from v1.courses_pb2 import (
    CreateCourseRequest,
    GetCourseRequest,
    GetCourseResponse,
    ListCoursesRequest,
    ListCoursesResponse,
    UpdateCourseRequest,
)

from tools.assertions.base import (
    assert_equal,
    assert_is_empty,
    assert_length,
    assert_not_empty,
)


def assert_course(actual: Course, expected: Course):
    """Сравнивает поля курса, включая сообщения файла превью и создателя.

    Args:
        actual: Фактические данные курса.
        expected: Ожидаемые данные курса.

    Raises:
        AssertionError: Если хотя бы одно из проверяемых полей отличается.
    """

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
    """Проверяет непустой ID созданного курса и соответствие данных запросу.

    Для файла превью и создателя сравниваются только их идентификаторы.

    Args:
        request: Отправленный запрос на создание курса.
        response: Ответ сервиса с созданным курсом.

    Raises:
        AssertionError: Если ID курса пуст или данные не соответствуют запросу.
    """

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
    """Проверяет ID полученного курса и его соответствие ожидаемым данным.

    Args:
        request: Отправленный запрос на получение курса.
        response: Ответ сервиса с полученным курсом.
        expected_course: Ожидаемые данные курса.

    Raises:
        AssertionError: Если ID не совпадает с запрошенным или данные отличаются.
    """

    assert_equal(response.course.id, request.id, "id")
    assert_course(response.course, expected_course)


def assert_list_courses_response(
    request: ListCoursesRequest,
    response: ListCoursesResponse,
    expected_courses: list[Course],
):
    """Проверяет список курсов независимо от порядка элементов.

    Проверяет количество курсов, уникальность ID в обоих списках, совпадение
    наборов ID и данных курсов, а также ID создателя каждого полученного курса.

    Args:
        request: Запрос с идентификатором пользователя, чьи курсы ожидаются.
        response: Ответ сервиса со списком курсов.
        expected_courses: Ожидаемые курсы с уникальными идентификаторами.

    Raises:
        AssertionError: Если списки отличаются, содержат повторяющиеся ID
            или ID создателя полученного курса не совпадает с request.user_id.
    """
    assert len(response.courses) == len(expected_courses)

    actual_by_id = {course.id: course for course in response.courses}
    expected_by_id = {course.id: course for course in expected_courses}

    assert_length(actual_by_id.keys(), len(response.courses), "actual courses count")
    assert_length(
        expected_by_id.keys(), len(expected_courses), "expected courses count"
    )

    assert_equal(actual_by_id.keys(), expected_by_id.keys(), "courses id's")

    for actual_course in response.courses:
        assert_equal(actual_course.created_by_user.id, request.user_id, "user_id")
        expected_course = expected_by_id[actual_course.id]
        assert_course(actual_course, expected_course)



def assert_update_course_response(
    request: UpdateCourseRequest, response: GetCourseResponse, previous_course: Course
):
    """Проверяет курс после применения полей запроса к его предыдущему состоянию.

    Ожидаемый курс формируется из копии previous_course с заменой полей,
    возвращённых request.ListFields(). Затем сравниваются protobuf-сообщения.

    Args:
        request: Отправленный запрос на обновление курса.
        response: Ответ сервиса с обновлённым курсом.
        previous_course: Данные курса до обновления.

    Raises:
        AssertionError: Если обновлённый курс отличается от ожидаемого.
    """
    expected_course = Course()
    expected_course.CopyFrom(previous_course)

    for field, value in request.ListFields():
        setattr(expected_course, field.name, value)

    assert_equal(
        actual=response.course,
        expected=expected_course,
        name="course",
    )

def assert_delete_course_response(response: Empty):
    """Проверяет тип Empty у ответа на удаление курса.

    Args:
        response: Ответ сервиса на запрос удаления курса.

    Raises:
        AssertionError: Если ответ не является экземпляром Empty.
    """
    assert_is_empty(response, "response")

import unittest
from unittest.mock import Mock, patch

from ossfind.github_api import GitHubAPIError, search_repositories


class ErrorResponseTests(unittest.TestCase):
    def assert_api_error(self, response, expected):
        with patch("ossfind.github_api.requests.get", return_value=response):
            try:
                search_repositories("python")
            except Exception as error:
                self.assertIsInstance(error, GitHubAPIError)
                self.assertEqual(str(error), expected)
            else:
                self.fail("An HTTP error must raise GitHubAPIError")

    def test_non_object_error_json_uses_http_reason(self):
        for body in (None, [], "upstream failed", 7, False):
            with self.subTest(body=body):
                response = Mock(status_code=500, headers={}, reason="Server Error")
                response.json.return_value = body
                self.assert_api_error(
                    response,
                    "GitHub API request failed with status 500: Server Error",
                )

    def test_api_error_message_is_preserved(self):
        response = Mock(status_code=422, headers={}, reason="Unprocessable Entity")
        response.json.return_value = {"message": "Validation Failed"}
        self.assert_api_error(
            response, "GitHub API request failed with status 422: Validation Failed"
        )

    def test_missing_or_empty_message_uses_http_reason(self):
        for body in ({}, {"message": ""}, {"message": None}):
            with self.subTest(body=body):
                response = Mock(status_code=500, headers={}, reason="Server Error")
                response.json.return_value = body
                self.assert_api_error(
                    response,
                    "GitHub API request failed with status 500: Server Error",
                )

    def test_invalid_json_uses_http_reason(self):
        response = Mock(status_code=502, headers={}, reason="Bad Gateway")
        response.json.side_effect = ValueError("not JSON")
        self.assert_api_error(
            response, "GitHub API request failed with status 502: Bad Gateway"
        )

    def test_no_message_or_reason_uses_unknown_error(self):
        response = Mock(status_code=500, headers={}, reason="")
        response.json.return_value = None
        self.assert_api_error(
            response, "GitHub API request failed with status 500: unknown error"
        )

    def test_successful_search_is_unchanged(self):
        response = Mock(status_code=200, headers={})
        response.json.return_value = {"items": [{"full_name": "example/project"}]}
        with patch("ossfind.github_api.requests.get", return_value=response):
            self.assertEqual(search_repositories("python"), [{"full_name": "example/project"}])


if __name__ == "__main__":
    unittest.main()

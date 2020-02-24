import unittest

from app import create_app


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        app = create_app()
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

    def test_blog_index(self):
        response = self.app.get("/blog")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

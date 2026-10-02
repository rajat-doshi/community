import unittest

from apps.parent_child_api.main import app


class ParentChildApiTests(unittest.TestCase):
    def test_routes_registered(self):
        paths = app.openapi().get("paths", {})
        self.assertIn("/parent-child/list", paths)
        self.assertIn("/parent-child/create", paths)
        self.assertIn("/parent-child/update", paths)
        self.assertIn("/parent-child/{id}", paths)
        self.assertIn("/parent-child/health", paths)


if __name__ == "__main__":
    unittest.main()

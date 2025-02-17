import unittest
import sys
from ppi import main


class OSTestCase(unittest.TestCase):
    def test_system(self) -> None:
        """Test system compatibility."""
        self.assertTrue(
            sys.platform == "darwin" or sys.platform == "linux",
            f"{main.NAME} is only compatible with macOS and Linux."
        )


if __name__ == "__main__":
    unittest.main()

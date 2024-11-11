import unittest 
import problem1
import logging 
logger=logging.getLogger()
logger.setLevel(logging.INFO)
st_hd = logging.StreamHandler()
st_hd.setLevel(logging.INFO)
fmter = logging.Formatter("%(message)s")
st_hd.setFormatter(fmter)
logger.addHandler(st_hd)

class TestComputeWord(unittest.TestCase):
    def test_compute_word_success(self):
        input_data = "which is better python 2 or python 3"
        with self.assertLogs(logger,level="INFO") as log:
            problem1.compute_word_frequency(input_data)
        self.assertIn("INFO:root:('2' : 1)", log.output)
        self.assertIn("INFO:root:('is' : 1)", log.output)
        self.assertIn("INFO:root:('or' : 1)", log.output)
        self.assertIn("INFO:root:('better' : 1)", log.output)
    
    def test_compute_word_invalid_input(self):
        input_data = 10
        with self.assertRaisesRegex(TypeError, r"Expected string but user provided :.*"):
            problem1.compute_word_frequency(input_data)
        input_data = [1,2,3,4]
        with self.assertRaisesRegex(TypeError, r"Expected string but user provided :.*"):
            problem1.compute_word_frequency(input_data)
        
    def test_compute_word_input_none(self):
        input_data = None
        with self.assertRaisesRegex(TypeError, r"Expected string but user provided :.*"):
            problem1.compute_word_frequency(input_data)
    
    def test_compute_word_case_sensitive(self):
        input_data = "which is better python 2 or PYthon 3"
        with self.assertLogs(logger,level="INFO") as log:
            problem1.compute_word_frequency(input_data)
        self.assertIn("INFO:root:('python' : 1)", log.output)
        self.assertIn("INFO:root:('PYthon' : 1)", log.output)

if __name__ == "__main__":
    unittest.main()
"""
Compute frequency of the words from the input 
Sort the o/p with keys alphanumerically 
Input : "which is better python 2 or python 3"
"""

from collections import Counter
import logging 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
st_hd = logging.StreamHandler()
st_hd.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
st_hd.setFormatter(formatter)
logger.addHandler(st_hd)
import concurrent.futures
def compute_word_frequency(input_string):
    """
    This function is used to compute the frequency of words with key sorted alphanumerically
    Args : input_string (string to process)
    Return : None 
    Exception : TypeError if input is not a string 
    """
    if not isinstance(input_string,str):
        raise TypeError(f"Expected string but user provided : {type(input_string).__name__}")
    
    logger.info("**********************************")
    logger.info(f"Input string : {input_string}")
    logger.info("***********************************")
    input_list = input_string.split()
    compute_data = Counter(input_list)
    sorted_compute_data = { key: compute_data[key] for key in sorted(compute_data.keys())}
    for key, value in sorted_compute_data.items():
        logger.info(f"('{key}' : {value})")


if __name__ == "__main__":
    with open("input_files/input_file.txt") as fp:
        """with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
            for line in fp.readlines():
                print(line)
                executor.submit(compute_word_frequency, line)"""
        with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
            executor.map(compute_word_frequency, fp.readlines())


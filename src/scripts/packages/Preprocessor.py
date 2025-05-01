# Imports
from langdetect import detect

# Class that helps with data preprocessing
# This class mainly processing arrays of character strings.
class Preprocessor:

    # Remove rows that are not strings
    def remove_anomaly_list(self, p_list):

        # Remove objects that are not string
        print(f'Found {sum([0 if isinstance(sentence, str) else 0 for sentence in p_list])} anomalies.')
        processed_list = [sentence if isinstance(sentence, str) else '' for sentence in p_list]

        return processed_list

    # Lower case list
    def lower_case_list(self, p_list):

        #Lower case list
        processed_list = [sentence.lower() for sentence in p_list]
        print(processed_list[:10])

        return processed_list
    
    # Remove songs in foreign languages
    def remove_foreign_lg(self, p_list, lg = 'en'):

        # Replace foreign texts with empty strings.
        processed_list = [sentence if detect(sentence) == lg else '' for sentence in p_list]


    # Main function for data preprocessing
    def process(self, p_list, lower=True):

        p_list = self.remove_anomaly_list(p_list)

        if lower:
            p_list = self.lower_case_list(p_list)
            

        print(p_list[:1])
        return p_list
        

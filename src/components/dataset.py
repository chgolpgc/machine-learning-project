

class Dataset:
    # TODO: Create a config file to dynamically handle categorical columns, numerical columns
    # and possible other Datasets
    # TODO: Modify this simple class to target maybe a dataframe or something? And based
    # on dtypes get categorical and numerical columns - who knows?? 
    def __init__(self):
        self.categorical_columns = ["gender", "race_ethnicity", "parental_level_of_education",
                "lunch", "test_preparation_course"]
        self.numerical_columns = ["writing_score", "reading_score"]

    def get_categorical_columns(self):
        return f"Categorical columns: {self.categorical_columns}"
    
    def get_numerical_columns(self):
        return f"Numerical columns: {self.numerical_columns}"
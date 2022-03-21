import pandas

class Table:

    def __init__(self, name):
        self.name = name
        self.height = 0
        self.width = 0
        self.df = pandas.DataFrame
        self.schools = set()
        self.LEAs = set()

    def set_df(self, df):
        self.df = df
        # reset height and width

    def get_df(self):
        return self.df

    def get_name(self):
        return self.name

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

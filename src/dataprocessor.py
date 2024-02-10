import tabula
import traceback

class DataProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        try:
            self.df = self._get_table_from_pdf()
        except Exception:
            print(traceback.format_exc())
            raise Exception("Invalid PDF File.")
    
    def _get_table_from_pdf(self):
        df = tabula.read_pdf(self.pdf_path, pages='all', multiple_tables=False, pandas_options={'skiprows':3})
        return df
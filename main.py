### THIS IS ONLY FOR CURRENT TESTING
from src.dataprocessor import DataProcessor

pdf_path = "sample_data/Timetable 23-24.pdf"
dp = DataProcessor(pdf_path)

print(dp.df)
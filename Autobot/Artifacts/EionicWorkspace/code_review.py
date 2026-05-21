import os
import pandas as pd
import pylint.lint

def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

def analyze_data(data):
    report = data.describe()
    return report

def write_report(report, file_path):
    try:
        report.to_csv(file_path, index=False)
        print("Laporan berhasil ditulis")
    except Exception as e:
        print(f"Error: {e}")

def analyze_code_quality(file_path):
    try:
        pylint.lint.Run([file_path], exit=False)
        print("Kode telah dianalisis")
    except Exception as e:
        print(f"Error: {e}")

def main():
    file_path = "data.csv"
    data = read_data(file_path)
    if data is not None:
        report = analyze_data(data)
        write_report(report, "report.csv")
    
    code_file_path = "maintenance_script.py"
    analyze_code_quality(code_file_path)

if __name__ == "__main__":
    main()
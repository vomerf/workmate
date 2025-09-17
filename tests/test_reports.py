import pytest
import csv
from reports.student_report import StudentPerformanceReport
from main import get_report

def make_csv(tmp_path, name, rows):
    """Утилита для создания временного CSV"""
    file_path = tmp_path / name
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return str(file_path)


@pytest.fixture
def single_csv(tmp_path):
    """Фикстура: один файл с большим набором студентов"""
    rows = [
        {"student_name": "Alice", "teacher_name": "Smith", "subject": "Math", "date": "2023-10-10", "grade": "5"},
        {"student_name": "Alice", "teacher_name": "Smith", "subject": "Math", "date": "2023-10-12", "grade": "3"},
        {"student_name": "Bob", "teacher_name": "Brown", "subject": "History", "date": "2023-10-13", "grade": "4"},
        {"student_name": "Bob", "teacher_name": "Brown", "subject": "History", "date": "2023-10-14", "grade": "2"},
        {"student_name": "Charlie", "teacher_name": "White", "subject": "Science", "date": "2023-10-15", "grade": "5"},
        {"student_name": "Charlie", "teacher_name": "White", "subject": "Science", "date": "2023-10-16", "grade": "4"},
        {"student_name": "Dana", "teacher_name": "Smith", "subject": "Math", "date": "2023-10-17", "grade": "3"},
        {"student_name": "Dana", "teacher_name": "Smith", "subject": "Math", "date": "2023-10-18", "grade": "4"},
    ]
    return make_csv(tmp_path, "single.csv", rows)


@pytest.fixture
def two_csvs(tmp_path):
    """Фикстура: два файла с пересекающимися студентами"""
    rows1 = [
        {"student_name": "Alice", "teacher_name": "Smith", "subject": "Math", "date": "2023-10-20", "grade": "4"},
        {"student_name": "Eve", "teacher_name": "Brown", "subject": "History", "date": "2023-10-21", "grade": "5"},
    ]
    rows2 = [
        {"student_name": "Alice", "teacher_name": "White", "subject": "Science", "date": "2023-10-22", "grade": "2"},
        {"student_name": "Frank", "teacher_name": "White", "subject": "Science", "date": "2023-10-23", "grade": "3"},
    ]
    file1 = make_csv(tmp_path, "file1.csv", rows1)
    file2 = make_csv(tmp_path, "file2.csv", rows2)
    return [file1, file2]


def test_student_performance_single_file(single_csv):
    report = StudentPerformanceReport()
    data = report.generate_data([single_csv])

    assert data == [
        ["Charlie", 4.5],
        ["Alice", 4.0],
        ["Dana", 3.5],
        ["Bob", 3.0],
    ]


def test_student_performance_two_files(two_csvs):
    report = StudentPerformanceReport()
    data = report.generate_data(two_csvs)

    assert data == [
        ["Eve", 5.0],
        ["Alice", 3.0],
        ["Frank", 3.0],
    ]


def test_get_report_valid():
    report = get_report("students-performance")
    from reports import StudentPerformanceReport  # если он у тебя лежит в reports
    assert isinstance(report, StudentPerformanceReport)


def test_get_report_invalid():
    with pytest.raises(ValueError, match="Unknown report:"):
        get_report("unknown_report")

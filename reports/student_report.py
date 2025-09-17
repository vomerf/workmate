from .base import BaseReport


class StudentPerformanceReport(BaseReport):
    name: str = "students-performance"
    group_field: str = "student_name"
    metric_field: str = "grade"
    headers = ["student_name", "grade"]

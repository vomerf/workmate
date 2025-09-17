from .student_report import StudentPerformanceReport

# from .teacher_report import TeacherPerformanceReport

# Нужно добавить новый класс для нового отчета
REPORTS = {
    StudentPerformanceReport.name: StudentPerformanceReport,
    # TeacherPerformanceReport.name: TeacherPerformanceReport,
}

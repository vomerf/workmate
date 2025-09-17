import csv
from abc import ABC
from collections import defaultdict

from tabulate import tabulate


class BaseReport(ABC):
    """
    Базовый класс для генерации отчетов.

    Атрибуты:
        name (str): Уникальное имя отчета, используется для выбора типа отчета.
        group_field (str):
            Название колонки в CSV-файле, по которой будут группироваться данные.
            Например, "student_name" или "teacher_name".
        metric_field (str): поле метрики, по которому ведем статистику
        headers (list[str]):
            Заголовки для итоговой таблицы.
            Первый элемент — название группы (например, "Name"),
            второй — агрегированный показатель (например, "Average Grade").
    """

    name: str
    group_field: str
    metric_field: str
    headers: list[str] = ["Name", "Average Grade"]

    def generate_data(self, files: list[str]) -> list[list]:
        """Возвращает данные отчета без печати"""
        groups = defaultdict(list)

        for filename in files:
            with open(filename, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    key = row[self.group_field]
                    value = float(row[self.metric_field])
                    groups[key].append(value)

        report_data = [
            [key, round(sum(values) / len(values), 2)] for key, values in groups.items()
        ]
        report_data.sort(key=lambda x: x[1], reverse=True)
        return report_data

    def generate(self, files: list[str]):
        """Выводит таблицу отчета"""
        report_data = self.generate_data(files)
        print(tabulate(report_data, headers=self.headers, tablefmt="pretty"))

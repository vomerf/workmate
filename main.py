import argparse
from pathlib import Path

from reports import REPORTS, StudentPerformanceReport


def parse_args():
    parser = argparse.ArgumentParser(description="Генерация отчета")
    parser.add_argument(
        "--files", nargs="+", required=True, help="Файлы для отчетов"
    )
    parser.add_argument(
        "--report", choices=REPORTS.keys(), required=True, help="Названия отчетов"
    )
    return parser.parse_args()


def get_report(report_name: str) -> StudentPerformanceReport:
    if report_name not in REPORTS:
        raise ValueError(f"Такого отчета не существует: {report_name}")
    return REPORTS[report_name]()


def check_exist_file(files: list[str]) -> None:
    for file in files:
        if not Path(file).exists():
            raise ValueError(f'Файла по такому пути не существует {file}')


def main():
    args = parse_args()
    check_exist_file(args.files)
    report = get_report(args.report)
    report.generate(args.files)


if __name__ == "__main__":
    main()

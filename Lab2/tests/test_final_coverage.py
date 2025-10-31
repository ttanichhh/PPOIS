"""
Финальные тесты для достижения 85% покрытия
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from financial.payroll import PayrollSystem, Payroll
from services.reporting_service import ReportingService
from utils.validation import ValidationUtils
from utils.report import Report

from core.employee import Employee
from core.restaurant import Restaurant
from support.address import Address
from exceptions.restaurant_exceptions import ValidationException


class TestFinalCoverage:
    """Финальные тесты для увеличения покрытия"""

    def test_payroll_operations(self):
        """Тест операций с расчетом зарплаты"""
        payroll_system = PayrollSystem()
        employee = Employee(1, "Test Employee", "+123456789", "employee@test.com",
                            "Waiter", 30000, "2024-01-01")

        # Тест расчета зарплаты
        payroll = Payroll(1, employee, "2024-01-01", "2024-01-31")
        payroll.overtime_hours = 5
        payroll.calculate_net_pay()

        assert payroll.net_pay > 0
        assert payroll.tax_amount > 0

        print("✅ Payroll operations - PASSED")

    def test_reporting_service_operations(self):
        """Тест операций сервиса отчетности"""
        address = Address("Test St", "Test City", "12345")
        restaurant = Restaurant(1, "Test Restaurant", address, "123", "Test")
        reporting_service = ReportingService(restaurant)

        # Тест планирования автоматических отчетов
        reporting_service.schedule_automatic_report("daily", "daily", ["manager@test.com"])
        assert len(reporting_service.scheduled_reports) == 1

        print("✅ Reporting service operations - PASSED")

    def test_validation_utils_edge_cases(self):
        """Тест граничных случаев валидации"""
        # Тест валидации емкости
        assert ValidationUtils.validate_capacity(4, 4) == True

        try:
            ValidationUtils.validate_capacity(4, 5)
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        # Тест валидации непустой строки
        assert ValidationUtils.validate_string_not_empty("Hello", "Name") == True

        try:
            ValidationUtils.validate_string_not_empty("", "Name")
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        try:
            ValidationUtils.validate_string_not_empty("   ", "Description")
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        print("✅ Validation utils edge cases - PASSED")

    def test_report_operations(self):
        """Тест операций с отчетами"""
        report = Report(1, "test_report", {"data": "test"}, "2024-01-20")

        # Тест атрибутов отчета
        assert report.report_id == 1
        assert report.report_type == "test_report"
        assert report.content["data"] == "test"

        print("✅ Report operations - PASSED")


if __name__ == "__main__":
    test_instance = TestFinalCoverage()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")
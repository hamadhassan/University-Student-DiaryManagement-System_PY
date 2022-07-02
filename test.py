class UniversityStudentDiaryManagementSystem: #this class replaces the original namespace 'UniversityStudentDiaryManagementSystem'
    class BL: #this class replaces the original namespace 'BL'
        class Fee:
            def __init__(self, feeType, semester, challanNo, amount, date, remarks):
                #instance fields found by C# to Python Converter:
                self._feeType = None
                self._semester = None
                self._challanNo = None
                self._amount = 0
                self._date = None
                self._remarks = None

                self._feeType = feeType
                self._semester = semester
                self._challanNo = challanNo
                self._amount = amount
                self._date = date
                self._remarks = remarks

            def get_fee_type(self):
                return self._feeType
            def set_fee_type(self, value):
                self._feeType = value
            def get_semester(self):
                return self._semester
            def set_semester(self, value):
                self._semester = value
            def get_challan_no(self):
                return self._challanNo
            def set_challan_no(self, value):
                self._challanNo = value
            def get_amount(self):
                return self._amount
            def set_amount(self, value):
                self._amount = value
            def get_date(self):
                return self._date
            def set_date(self, value):
                self._date = value
            def get_remarks(self):
                return self._remarks
            def set_remarks(self, value):
                self._remarks = value

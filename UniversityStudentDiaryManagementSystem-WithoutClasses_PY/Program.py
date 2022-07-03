import imp
import os

from  pip import main


class OutObject:
    def __init__(self):
        self.arg_value = None
class TryParseHelper:
    @staticmethod
    def try_parse_int(s, result):
        try:
            result.arg_value = int(s)
            return True
        except:
            return False

    @staticmethod
    def try_parse_float(s, result):
        try:
            result.arg_value = float(s)
            return True
        except:
            return False

    @staticmethod
    def try_parse_bool(s, result):
        try:
            result.arg_value = bool(s)
            return True
        except:
            return False

class Program:
    #****************** GLOBAL DATA STRUCTURE *****************
    _LENGTH = 20 # lenght of arrays
    #****************** SECURITY-ARRAYS ******************
    _firstname = [None for _ in range(_LENGTH)] # create an account store firstname
    _lastname = [None for _ in range(_LENGTH)] # create an account store lastname
    _username = [None for _ in range(_LENGTH)] # create an account store username
    _password = [None for _ in range(_LENGTH)] # create an account store password
    _firstname_Agent = [None for _ in range(_LENGTH)] # create an account store firstname
    _lastname_Agent = [None for _ in range(_LENGTH)] # create an account store lastname
    _username_Agent = [None for _ in range(_LENGTH)] # create an account store username
    _password_Agent = [None for _ in range(_LENGTH)] # create an account store password
    #****************** ADMIN-ARRAYS ******************
    _semesterType = [None for _ in range(_LENGTH)] # academic fee variables , opAdmin >> opAcademicFee
    _challanNo = [None for _ in range(_LENGTH)]
    _date = [None for _ in range(_LENGTH)]
    _remarks = [None for _ in range(_LENGTH)]
    _amountacademic = [0 for _ in range(_LENGTH)] # academic fee variables , opAdmin >> opAcademicFee
    _menuBreakfast = [None for _ in range(_LENGTH)] # meal breakfast charges , opHostel >> opMeal >> opMealBreakfast
    _remarksBreakfast = [None for _ in range(_LENGTH)]
    _chargesBreakfast = [0 for _ in range(_LENGTH)] # meal breakfast charges , opHostel >> opMeal >> opMealBreakfast
    _menuLunch = [None for _ in range(_LENGTH)] # meal lunch charges , opHostel >> opMeal >> opMealLunch
    _remarksLunch = [None for _ in range(_LENGTH)]
    _chargesLunch = [0 for _ in range(_LENGTH)] # meal lunch charges , opHostel >> opMeal >> opMealLunch
    _menuDinner = [None for _ in range(_LENGTH)] # meal dinner charges , opHostel >> opMeal >> opMealDinner
    _remarksDinner = [None for _ in range(_LENGTH)]
    _chargesDinner = [0 for _ in range(_LENGTH)] # meal dinner charges , opHostel >> opMeal >> opMealDinner
    _monthlyMealExpenses = [None for _ in range(_LENGTH)] # monthly meal charges , opHostel >> opMealCharges
    _remarksMealExpenses = [None for _ in range(_LENGTH)]
    _chargesMealMonthly = [0 for _ in range(_LENGTH)] # monthly meal charges , opHostel >> opMealCharges
    _monthLivingExpenses = [None for _ in range(_LENGTH)] # monthly living charges , opHostel >> opLivingCharges
    _remarksLivingExpenses = [None for _ in range(_LENGTH)]
    _chargesLivingExpenses = [0 for _ in range(_LENGTH)] # monthly living charges , opHostel >> opLivingCharges
    _monthServiceExpenses = [None for _ in range(_LENGTH)] # monthly service charges , opHostel >> opServiceCharges
    _remarksServiceExpenses = [None for _ in range(_LENGTH)]
    _chargesServiceMonthly = [0 for _ in range(_LENGTH)] # monthly service charges , opHostel >> opServiceCharges
    _remarksRenovationExpenses = [None for _ in range(_LENGTH)] # renovation charges , opHostel >> opRenovationCharges
    _chargesRenovationMonthly = [0 for _ in range(_LENGTH)] # renovation charges , opHostel >> opRenovationCharges
    _remarksLaundryExpenses = [None for _ in range(_LENGTH)] # laundry charges , opHostel >> opLaundryCharges
    _chargesLaundryMonthly = [0 for _ in range(_LENGTH)] # laundry charges , opHostel >> opLaundryCharges
    _remarksBarberExpenses = [None for _ in range(_LENGTH)] # barber charges , opHostel >> opBarberCharges
    _chargesBarberMonthly = [0 for _ in range(_LENGTH)] # barber charges , opHostel >> opBarberCharges
    _remarksNotesExpenses = [None for _ in range(_LENGTH)] # notes charges , opHelpingMaterial >> opNotesHelpingMaterial
    _chargesNotesMonthly = [0 for _ in range(_LENGTH)] # notes charges , opHelpingMaterial >> opNotesHelpingMaterial
    _remarksRegisterExpenses = [None for _ in range(_LENGTH)] # register charges , opHelpingMaterial >> opRegisterHelpingMaterial
    _chargesRegisterMonthly = [0 for _ in range(_LENGTH)] # register charges , opHelpingMaterial >> opRegisterHelpingMaterial
    _remarksStationaryExpenses = [None for _ in range(_LENGTH)] # stationary charges , opHelpingMaterial >> opStationaryHelpingMaterial
    _chargesStationaryMonthly = [0 for _ in range(_LENGTH)] # stationary charges , opHelpingMaterial >> opStationaryHelpingMaterial
    _remarksFriendsRecreationalExpenses = [None for _ in range(_LENGTH)] # friend recreational expenses , opRecreationalExpenses >> opFriendsRecreationalExpenses
    _chargesFriendsRecreationalExpenses = [0 for _ in range(_LENGTH)] # friend recreational expenses , opRecreationalExpenses >> opFriendsRecreationalExpenses
    _remarksFamilyRecreationalExpenses = [None for _ in range(_LENGTH)] # family recreational expenses , opRecreationalExpenses >> opFamilyRecreationalExpenses
    _chargesFamilyRecreationalExpenses = [0 for _ in range(_LENGTH)] # family recreational expenses , opRecreationalExpenses >> opFamilyRecreationalExpenses
    _remarksClassCommunityFund = [None for _ in range(_LENGTH)] # class community fund , opCommunityFund >> opClassCommunityFund
    _chargesClassCommunityFund = [0 for _ in range(_LENGTH)] # class community fund , opCommunityFund >> opClassCommunityFund
    _remarksSocietiesCommunityFund = [None for _ in range(_LENGTH)] # class community fund , opCommunityFund >> opSocietiesCommunityFund
    _chargesSocietiesCommunityFund = [0 for _ in range(_LENGTH)] # class community fund , opCommunityFund >> opSocietiesCommunityFund
    _titleDailyGoals = [None for _ in range(_LENGTH)] # daily goals , opGoals >> opDailyGoals
    _descriptionDailyGoals = [None for _ in range(_LENGTH)]
    _titleWeeklyGoals = [None for _ in range(_LENGTH)] # weekly goals , opGoals >> opWeeklyGoals
    _descriptionWeeklyGoals = [None for _ in range(_LENGTH)]
    _titleMonthlyGoals = [None for _ in range(_LENGTH)] # monthly goals , opGoals >> opMonthlyGoals
    _descriptionMonthlyGoals = [None for _ in range(_LENGTH)]
    _titleYearlyGoals = [None for _ in range(_LENGTH)] # yearly goals , opGoals >> opYearlyGoals
    _descriptionYearlyGoals = [None for _ in range(_LENGTH)]
    _nameCallPakage = [None for _ in range(_LENGTH)] # call package , opCellPhone >> opCall_CellPhone
    _amountCallPakage = [0 for _ in range(_LENGTH)] # call pacage ,  opCellPhone >> opCall_CellPhone
    _durationCallPakage = [None for _ in range(_LENGTH)] #durationCallPakage
    _nameInternetPakage = [None for _ in range(_LENGTH)] # internet package , opCellPhone >> opInternet_CellPhone
    _durationInternetPakage = [None for _ in range(_LENGTH)]
    _amountInternetPakage = [0 for _ in range(_LENGTH)] # internet package , opCellPhone >> opInternet_CellPhone
    _nameMessagePakage = [None for _ in range(_LENGTH)] # message package , opCellPhone >> opMessage_CellPhone
    _durationMessagePakage = [None for _ in range(_LENGTH)]
    _amountMessagePakage = [0 for _ in range(_LENGTH)] # message package , opCellPhone >> opMessage_CellPhone
    _titleBorrowBook = [None for _ in range(_LENGTH)] # borrow book , opBook >> opBookBorrow
    _authorBorrowBook = [None for _ in range(_LENGTH)]
    _friendnameBorrowBook = [None for _ in range(_LENGTH)]
    _remarksBorrowBook = [None for _ in range(_LENGTH)]
    _titlePurchaseBook = [None for _ in range(_LENGTH)] # purchase book , opBook >> opBookPurchase
    _authorPurchaseBook = [None for _ in range(_LENGTH)]
    _remarksPurchaseBook = [None for _ in range(_LENGTH)]
    _amountPurchaseBook = [0 for _ in range(_LENGTH)] # purchase book , opBook >> opBookPurchase
    _five_time_Prayer = [None for _ in range(_LENGTH)] # five time prayer , opSelfMotivational >> opFiveTimePrayer
    _Quran_e_Pak = [None for _ in range(_LENGTH)] # quran e pak , opSelfMotivational >> opQuran_e_Pak
    _Durood_e_Pak = [None for _ in range(_LENGTH)] # durood e pak , opSelfMotivational >> opDurood_e_Pak
    _locationFromUber = [None for _ in range(_LENGTH)] # transport uber/cream/bykea , opTransport >> opUberTransport
    _locationToUber = [None for _ in range(_LENGTH)]
    _purposeUber = [None for _ in range(_LENGTH)]
    _amountUber = [0 for _ in range(_LENGTH)] # transport uber/cream/bykea , opTransport >> opUberTransport
    _locationFromBus = [None for _ in range(_LENGTH)] # transport bus , opTransport >> opBusTransport
    _locationToBus = [None for _ in range(_LENGTH)]
    _purposeBus = [None for _ in range(_LENGTH)]
    _amountBus = [0 for _ in range(_LENGTH)] # transport bus , opTransport >> opBusTransport
    _minutiesSporties = [0 for _ in range(_LENGTH)] # sporties recreational activities , opRecreationalActivities >> opSportiesActivities
    _minutiesSocieties = [0 for _ in range(_LENGTH)] # societies recreational activities , opRecreationalActivities >> opSocietiesActivities
    _purposeSocieties = [None for _ in range(_LENGTH)] # societies recreational activities , opRecreationalActivities >> opSocietiesActivities
    _awardCo_Curricular = [None for _ in range(_LENGTH)] # achievements co-curricular , opAchievements >> opCoCurricular
    _presentCo_Curricular = [None for _ in range(_LENGTH)]
    _remarksCo_Curricular = [None for _ in range(_LENGTH)]
    _awardExtra_Curricular = [None for _ in range(_LENGTH)] #  achievements extra-curricular , opAchievements >> opExtraCurricular
    _presentExtra_Curricular = [None for _ in range(_LENGTH)]
    _remarksExtra_Curricular = [None for _ in range(_LENGTH)]
    _gpa = [0 for _ in range(_LENGTH)] # result grades , opResultGrades
    _cgpa = [0 for _ in range(_LENGTH)]
    _remarksResult = [None for _ in range(_LENGTH)] # result grades , opResultGrades
    _titleGoldenLines = [None for _ in range(_LENGTH)] # golden lines , opGoldenLines
    _descriptionGoldenLines = [None for _ in range(_LENGTH)]
    _titleLifelongEvents = [None for _ in range(_LENGTH)] # life long events , opLifelongEvents
    _descriptionLifelongEvents = [None for _ in range(_LENGTH)]
    _titleNotes = [None for _ in range(_LENGTH)] # notes , opNotes
    _descriptionNotes = [None for _ in range(_LENGTH)]
    # ****************** INCREMENT-VARIABLES ******************
    _inc_opAddUser = 0 # increment in the array index
    _inc_opAgentAddUser = 0 # increment in the array index
    _increment_opAcademicFee = 0 # increment in the array index
    _increment_opMealBreakfast = 0 # increment in the array index
    _increment_opMealLunch = 0 # increment in the array index
    _increment_opMealDinner = 0 # increment in the array index
    _increment_opMealCharges = 0 # increment in the array index
    _inc_opLivingCharges = 0 # increment in the array index
    _inc_opServiceCharges = 0 # increment in the array index
    _inc_opRenovationCharges = 0 # increment in the array index
    _inc_opLaundryCharges = 0 # increment in the array index
    _inc_opBarberCharges = 0 # increment in the array index
    _inc_opNotesHelpingMaterial = 0 # increment in the array index
    _inc_opRegisterHelpingMaterial = 0 # increment in the array index
    _inc_opStationaryHelpingMaterial = 0 # increment in the array index
    _inc_opFriendsRecreationalExpenses = 0 # increment in the array index
    _inc_opFamilyRecreationalExpenses = 0 # increment in the array index
    _inc_opClassCommunityFund = 0 # increment in the array index
    _inc_opSocietiesCommunityFund = 0 # increment in the array index
    _inc_opDailyGoals = 0 # increment in the array index
    _inc_opWeeklyGoals = 0 # increment in the array index
    _inc_opMonthlyGoals = 0 # increment in the array index
    _inc_opYearlyGoals = 0 # increment in the array index
    _inc_opCall_CellPhone = 0 # increment in the array index
    _inc_opInternet_CellPhone = 0 # increment in the array index
    _inc_opMessage_CellPhone = 0 # increment in the array index
    _inc_opBookBorrow = 0 # increment in the array index
    _inc_opBookPurchase = 0 # increment in the array index
    _inc_opFiveTimePrayer = 0 # increment in the array index
    _inc_opQuran_e_Pak = 0 # increment in the array index
    _inc_opDurood_e_Pak = 0 # increment in the array index
    _inc_opUberTransport = 0 # increment in the array index
    _inc_opBusTransport = 0 # increment in the array index
    _inc_opSportiesActivities = 0 # increment in the array index
    _inc_opSocietiesActivities = 0 # increment in the array index
    _inc_opCoCurricular = 0 # increment in the array index
    _inc_opExtraCurricular = 0 # increment in the array index
    _inc_opResultGrades = 0 # increment in the array index
    _inc_opGoldenLines = 0 # increment in the array index
    _inc_opLifelongEvents = 0 # increment in the array index
    _inc_opNotes = 0 # increment in the array index
    #****************** ADMIN & AGENT-VARIABLES ******************
    _addWalletMoney = 0 # this used to add money from agent and show in balance
    _walletRemarks = " " # this used to add remarks from agent and show in balance
    @staticmethod
    def main():
        Program.read_adminSecurityFile() # file handling, load data from files into arrays and variables before running program
        Program.read_agentSecurityFile() # file handling, load data from files into arrays and variables before running program
        Program.read_agentWalletMoney() # file handling, load data from files into arrays and variables before running program
        Program.read_admin3AcadmicFee() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_1Meal_1Breakfast() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_1Meal_2Lunch() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_1Meal_3Dinner() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_2MealChargesMonthly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_3LivingChargesMonthly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_4ServiceChargesMonthly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_5RenovationChargesMonthly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_6LaundryChargesMonthly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_4Hostel_7BarberChargesMonthly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_5HelpingMaterial_1Notes() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_5HelpingMaterial_2Register() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_5HelpingMaterial_3Stationary() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_6RecreationalExpenses_1Friends() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_6RecreationalExpenses_2Family() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_7CommunityFund_1Class() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_7CommunityFund_2Societies() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_8Goals_1Daily() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_8Goals_2Weekly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_8Goals_3Monthly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_8Goals_4Yearly() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_9CellPhone_1Call() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_9CellPhone_2Internet() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_9CellPhone_3Message() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_10Book_1Borrow() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_10Book_2Purchase() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_11SelfMotivational_1FiveTimePrayer() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_11SelfMotivational_2Quran_e_Pak() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_11SelfMotivational_3Durood_e_Pak() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_12Transport_1Uber() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_12Transport_2Bus() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_13RecreationalActivities_1Sporties() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_13RecreationalActivities_2Socities() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_14Achievments_1CoCurricular() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_14Achievments_2ExtraCurricular() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_15ResultGrades() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_16GoldenLines() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_17LifelongEvents() # file handling, load data from files into arrays and variables before running program
        Program.read_admin_18Notes() # file handling, load data from files into arrays and variables before running program

        opMain = ' ' # Main menu options, store user input
        while True:
            Program._header_Welcome() # welcome header function  is called
            print("Main Menu > Home ", end = '')
            print("\n", end = '')
            print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
            print("\n", end = '')
            opMain = Program._admin_HomeMenu() # admin home menu is called
            if opMain == '1':
                opLogin = None # login option, store user input
                opLogin = ' '
                while True:
                    Program._header() # header function is called
                    print("Main Menu > Login ", end = '')
                    print("\n", end = '')
                    print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                    print("\n", end = '')
                    print("Login As", end = '')
                    print("\n", end = '')
                    print("   1. Admin ", end = '')
                    print("\n", end = '')
                    print("   2. Agent ", end = '')
                    print("\n", end = '')
                    print("Press 0 to Go Back...", end = '')
                    opLogin = input()
                    if opLogin == '0':
                        break
                    elif opLogin == '1':
                        adminUsername = "" # admin sig-in variable to store username and password
                        adminPassword = ""
                        Program._header() # header function is called
                        print("Main Menu > Login > Admin ", end = '')
                        print("\n", end = '')
                        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                        print("\n", end = '')
                        print("Sign-In", end = '')
                        print("\n", end = '')
                        print("Username : ", end = '')
                        adminUsername = input()
                        print("Password : ", end = '')
                        adminPassword = input()
                        index = Program._checkuser(adminUsername, adminPassword) # check the username and password in the array and make descion upon it
                        if Program._username[index] == adminUsername and Program._password[index] == adminPassword:
                            opAdmin = " " # admin option, store return value of function admin menu
                            while True:
                                Program._header() # header function is called
                                print("Main Menu > Admin > Menu ", end = '')
                                print("\n", end = '')
                                print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                                print("\n", end = '')
                                opAdmin = Program._admin_Menu() # admin menu function is called
                                if opAdmin == "0":
                                    opProfile = ' '
                                    while opProfile != '1':
                                        Program._admin_0Profile(index) # function called
                                        print("Press 0 to go back...", end = '')
                                        opProfile = input()
                                        if opProfile == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option()
                                elif opAdmin == "1":
                                    opWalletStatus = ' ' #// wallet status option, store user input
                                    while opWalletStatus != '1':
                                        Program.read_agentWalletMoney()
                                        Program._admin_1WalletStatus() # function called
                                        print("Press 0 to go back...", end = '')
                                        opWalletStatus = input()
                                        if opWalletStatus == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of opWalletStatus option
# end of wallet status option of admin menu option

                                elif opAdmin == "2":
                                    opExpensesReport = ' ' # expenses report option , store return value of function admin expenses report
                                    while opExpensesReport != '4':
                                        Program._admin_2ExpensesReport() # function called
                                        opExpensesReport = Program._admin_ExpensesReportMenu() # admin expenses report function is called
                                        if opExpensesReport == '0':
                                            break
                                        elif opExpensesReport == '1':
                                            opTodayExpenses = ' ' # today expenses option , store user input
                                            while opTodayExpenses != '1':
                                                Program._admin_2ExpensesReportToday()
                                                print("Press 0 to Go Back...", end = '')
                                                opTodayExpenses = input()
                                                if opTodayExpenses == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of today expenses report of admin menu option
                                        elif opExpensesReport == '2':
                                            opExpensesReport1 = ' ' # monthly expenses option , store user input
                                            while opExpensesReport != '1':
                                                Program._admin_2ExpensesReportMonthly()
                                                print("Press 0 to go back...", end = '')
                                                opExpensesReport1 = input()
                                                if opExpensesReport1 == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop of opExpenses Report
# end of monthly expense report
                                        elif opExpensesReport == '3':
                                            opYearExpenses = ' ' # yearly expenses option , store user input
                                            while opYearExpenses != '1':
                                                Program._admin_2ExpensesReportYearly()
                                                print("Press 0 to Go Back...", end = '')
                                                opYearExpenses = input()
                                                if opYearExpenses == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of yealy expense report
# end of while loop of opYearExpenses
# end of while loop of opExpensesReport
# end of expenses report option of admin menu option
                                elif opAdmin == "3":
                                    opAcademicFee = ' ' # academic fee option , store user input
                                    while opAcademicFee != '1':
                                        Program._admin_3AcademicFee() # fimction called
                                        print("Press 0 to Go Back...", end = '')
                                        opAcademicFee = input()
                                        if opAcademicFee == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop of opAcademicFee
# end of academic fee option of admin menu option

                                elif opAdmin == "4":
                                    opHostel = ' ' # Hostel option, store return value of hostel menu function
                                    while opHostel != '8':
                                        Program._admin_4Hostel()
                                        opHostel = Program._admin_HostelMenu() # hostel menu function is called
                                        if opHostel == '0':
                                            break
                                        elif opHostel == '1':
                                            opMeal = ' ' # meal option, store return value of admin, hostel option of meal menu function
                                            while True:
                                                Program._admin_4Hostel_1Meal() # function called
                                                opMeal = Program._admin_Hostel_MealMenu() # admin, hostel option of meal menu function is called
                                                if opMeal == '0':
                                                    break
                                                elif opMeal == '1':
                                                    opMealBreakfast = ' ' # meal breakfast option under meal option, store user input
                                                    while opMealBreakfast != '1':
                                                        Program._admin_4Hostel_1Meal_1Breakfast()
                                                        print("Press 0 to Go Back...", end = '')
                                                        opMealBreakfast = input()
                                                        if opMealBreakfast == '0':
                                                            break
                                                        else:
                                                            print("Incorrect option", end = '')
                                                            print("\n", end = '')
                                                            Program._hold_Option() # end of while loop opMealBreakfast
# end of breakfast option of meal option of hostel option in admin menu option
                                                elif opMeal == '2':
                                                    opMealLunch = ' ' # meal lunch option under meal option, store user input
                                                    while opMealLunch != '1':
                                                        Program._admin_4Hostel_1Meal_2Lunch()
                                                        print("Press 0 to Go Back...", end = '')
                                                        opMealLunch =input()
                                                        if opMealLunch == '0':
                                                            break
                                                        else:
                                                            print("Incorrect option", end = '')
                                                            print("\n", end = '')
                                                            Program._hold_Option() # end of while loop of opMealLunch
# end of lunch option of meal option of hostel option in admin menu option
                                                elif opMeal == '3':
                                                    opMealDinner = ' ' # meal dinner option under meal option, store user input
                                                    while opMealDinner != '1':
                                                        Program._admin_4Hostel_1Meal_3Dinner()
                                                        print("Press 0 to Go Back...", end = '')
                                                        opMealDinner = input()
                                                        if opMealDinner == '0':
                                                            break
                                                        else:
                                                            print("Incorrect option", end = '')
                                                            print("\n", end = '')
                                                            Program._hold_Option() # end of while loop of opMealDinner
# end of dinner option of meal option of hostel option in admin menu option
# end of while loop of opMeal
# end of meal option of hostel option in admin menu option
                                        elif opHostel == '2':
                                            Program._admin_4Hostel_2MealChargesMonthly()
                                            opMealCharges = ' ' # monthly meal fee charges  option, store user input
                                            while opMealCharges != '1':

                                                print("Press 0 to Go Back...", end = '')
                                                opMealCharges = input()
                                                if opMealCharges == '0':
                                                    break
                                                else:

                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop of opMealCharges
# end of monthly meal option
                                        elif opHostel == '3':
                                            Program._admin_4Hostel_3LivingChargesMonthly()
                                            opLivingCharges = ' ' # monthly living fee charges  option, store user input
                                            while opLivingCharges != '1':

                                                print("Press 0 to Go Back...", end = '')
                                                opLivingCharges =input()
                                                if opLivingCharges == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop of opLivingCharges
# end of living charges
                                        elif opHostel == '4':
                                            Program._admin_4Hostel_4ServiceChargesMonthly()
                                            opServiceCharges = ' ' # monthly service charges option, store user
                                            while opServiceCharges != '1':

                                                print("Press 0 to Go Back...", end = '')
                                                opServiceCharges = input()
                                                if opServiceCharges == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop of opServiceCharges
# end of service charges of hostel option
                                        elif opHostel == '5':
                                            Program._admin_4Hostel_5RenovationChargesMonthly()
                                            opRenovationCharges = ' ' #/ monthly renovation charges option, store user input
                                            while opRenovationCharges != '1':

                                                print("Press 0 to Go Back...", end = '')
                                                opRenovationCharges =input()
                                                if opRenovationCharges == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop of opRenovationCharges
# end of renovation charges of hostel option
                                        elif opHostel == '6':
                                            Program._admin_4Hostel_6LaundryChargesMonthly()
                                            opLaundryCharges = ' ' # monthly laundry charges option, store user input
                                            while opLaundryCharges != '1':
                                                opLaundryCharges = input()
                                                if opLaundryCharges == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opLaundryCharges
# end of lundry charges of hostel option
                                        elif opHostel == '7':
                                            Program._admin_4Hostel_7BarberChargesMonthly()
                                            opBarberCharges = ' ' # barber charges, store user input
                                            while opBarberCharges != '1':

                                                print("Press 0 to Go Back...", end = '')
                                                opBarberCharges = input()
                                                if opBarberCharges == '0':

                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of barber charges
# end of while loop of opBarberCharges
# end of while loop of opHostel
# end of hostel option of admin menu option
                                elif opAdmin == "5":
                                    opHelpingMaterial = '1' # helping material, store return value of admin,helping material menu
                                    while opHelpingMaterial != '4':
                                        Program._admin_5HelpingMaterial()
                                        opHelpingMaterial = Program._admin_HelpingMaterialMenu() # admin,helping material menu is called
                                        if opHelpingMaterial == '0':
                                            break
                                        elif opHelpingMaterial == '1':
                                            opNotesHelpingMaterial = ' ' # notes option  of helping material option, store user input
                                            while opNotesHelpingMaterial != '1':
                                                Program._admin_5HelpingMaterial_1Notes()

                                                print("Press 0 to Go Back...", end = '')
                                                opNotesHelpingMaterial = input()
                                                if opNotesHelpingMaterial == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opNotesHelpingMaterial
# end of notes option
                                        elif opHelpingMaterial == '2':
                                            opRegisterHelpingMaterial = ' ' # register option  of helping material option, store user input
                                            while opRegisterHelpingMaterial != '1':
                                                Program._admin_5HelpingMaterial_2Register()
                                                print("Press 0 to Go Back...", end = '')
                                                opRegisterHelpingMaterial = input()
                                                if opRegisterHelpingMaterial == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opRegisterHelpingMaterial
# end of register option
                                        elif opHelpingMaterial == '3':
                                            opStationaryHelpingMaterial = ' ' # stationary option  of helping material option, store user input
                                            while opStationaryHelpingMaterial != '1':
                                                Program._admin_5HelpingMaterial_3Stationary()
                                                print("Press 0 to Go Back...", end = '')
                                                opStationaryHelpingMaterial = input()
                                                if opStationaryHelpingMaterial == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opStationaryHelpingMaterial
# end of stationary option
# end of while loop of opHelpingMaterial
# end of helping material

                                elif opAdmin == "6":
                                    opRecreationalExpenses = ' ' # recreational expenses option, store return value of admin,recreational expenses menu
                                    while opRecreationalExpenses != '3':
                                        Program._admin_6RecreationalExpenses()
                                        opRecreationalExpenses = Program._admin_RecreationalExpesesMenu() # admin,recreational expenses menu is called
                                        if opRecreationalExpenses == '0':
                                            break
                                        elif opRecreationalExpenses == '1':
                                            opFriendsRecreationalExpenses = ' ' #  friends recreational expenses option,store user input
                                            while opFriendsRecreationalExpenses != '1':
                                                Program._admin_6RecreationalExpenses_1Friends()
                                                print("Press 0 to Go Back...", end = '')
                                                opFriendsRecreationalExpenses = input()
                                                if opFriendsRecreationalExpenses == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opFriendsRecreationalExpenses
# end of  friends recreational expenses option
                                        elif opRecreationalExpenses == '2':
                                            opFamilyRecreationalExpenses = ' ' #  family recreational expenses option,store user input
                                            while opFamilyRecreationalExpenses != '1':
                                                Program._admin_6RecreationalExpenses_2Family()
                                                print("Press 0 to Go Back...", end = '')
                                                opFamilyRecreationalExpenses = input()
                                                if opFamilyRecreationalExpenses == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opFamilyRecreationalExpenses
# end of family recreational expenses option
# end of while loop opRecreationalExpenses
# end of recreatiobnal expenses
                                elif opAdmin == "7":
                                    opCommunityFund = ' ' # community fund option, store return value of admin,community fund function
                                    while opCommunityFund != '3':
                                        Program._admin_7CommunityFund()
                                        opCommunityFund = Program._admin_CommunityFundMenu() # admin,community fund function is called
                                        if opCommunityFund == '0':
                                            break
                                        elif opCommunityFund == '1':
                                            opClassCommunityFund = ' ' # class community fund option, store user input
                                            while opClassCommunityFund != '1':
                                                Program._admin_7CommunityFund_1Class()
                                                print("Press 0 to Go Back...", end = '')
                                                opClassCommunityFund = input()
                                                if opClassCommunityFund == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opClassCommunityFund
# end of class option of community fund
                                        elif opCommunityFund == '2':
                                            opSocietiesCommunityFund = ' ' # Socirties fund option, store user input
                                            while opSocietiesCommunityFund != '1':
                                                Program._admin_7CommunityFund_2Societies()
                                                print("Press 0 to Go Back...", end = '')
                                                opSocietiesCommunityFund = input()
                                                if opSocietiesCommunityFund == '0':
                                                    break

                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opSocietiesCommunityFund
# end of societies of
# end of while loop opCommunityFund
# end of community fund
                                elif opAdmin == "8":
                                    opGoals = ' ' # goals option,store return value of admin, goals menu function
                                    while opGoals != '5':
                                        Program._admin_8Goals()
                                        opGoals = Program._admin_GoalsMenu() # admin, goals menu function is called
                                        if opGoals == '0':
                                            break
                                        elif opGoals == '1':
                                            opDailyGoals = ' ' # daiy option of goals option, store user input
                                            while opDailyGoals != '1':
                                                Program._admin_8Goals_1Daily()
                                                print("Press 0 to Go Back...", end = '')
                                                opDailyGoals = input()
                                                if opDailyGoals == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opDailyGoals
# end of daily option of goals option of admin login
                                        elif opGoals == '2':
                                            opWeeklyGoals = None # weekly option of goals option, store user input
                                            while True:
                                                Program._admin_8Goals_2Weekly()
                                                print("Press 0 to Go Back...", end = '')
                                                opWeeklyGoals = input()
                                                if opWeeklyGoals == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opWeeklyGoals
# end of weekly option of goals option of admin login
                                        elif opGoals == '3':
                                            opMonthlyGoals = ' ' # monthly option of goals option, store user input
                                            while opMonthlyGoals != '1':
                                                Program._admin_8Goals_3Monthly()
                                                print("Press 0 to Go Back...", end = '')
                                                opMonthlyGoals = input()
                                                if opMonthlyGoals == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opMonthlyGoals
# end of monthly option of goals option of admin login
                                        elif opGoals == '4':
                                            opYearlyGoals = ' ' # yearly option of goals option, store user input
                                            while opYearlyGoals != '1':
                                                Program._admin_8Goals_4Yearly()
                                                print("Press 0 to Go Back...", end = '')
                                                opYearlyGoals = input()
                                                if opYearlyGoals == '0':

                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opYearlyGoals
# end of yearly  option of goals option of admin login
# end of while loop opGoals
# end of goals option
                                elif opAdmin == "9":
                                    opCellPhone = ' ' # cell phone option,store return value admin,cell phone menu function
                                    while opCellPhone != '4':
                                        Program._admin_9CellPhone()
                                        opCellPhone = Program._admin_CellPhoneMenu() # admin,cell phone menu function  called
                                        if opCellPhone == '0':
                                            break
                                        elif opCellPhone == '1':
                                            opCall_CellPhone = ' ' # call pakage option of cell option, store user input
                                            while opCall_CellPhone != '1':
                                                Program._admin_9CellPhone_1Call()
                                                print("Press 0 to Go Back...", end = '')
                                                opCall_CellPhone = input()
                                                if opCall_CellPhone == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opCall_CellPhone
# end of call pakage option of cell phone option
                                        elif opCellPhone == '2':
                                            opInternet_CellPhone = ' ' # internet option of cell phone, store user input
                                            while opInternet_CellPhone != '1':
                                                Program._admin_9CellPhone_2Internet()
                                                print("Press 0 to Go Back...", end = '')
                                                opInternet_CellPhone = input()
                                                if opInternet_CellPhone == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opInternet_CellPhone
# end of  internet option of cell phone
                                        elif opCellPhone == '3':
                                            opMessage_CellPhone = ' ' # message option of cell phone, store user input
                                            while opMessage_CellPhone != '1':
                                                Program._admin_9CellPhone_3Message()
                                                print("Press 0 to Go Back...", end = '')
                                                opMessage_CellPhone = input()
                                                if opMessage_CellPhone == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opMessage_CellPhone
# end of message option of cell phone
# end of while loop opCellPhone
# end of cell phone option of admin option

                                elif opAdmin == "10":
                                    opBook = ' ' # book option,store return vale of admin, book menu function
                                    while opBook != '3':
                                        Program._admin_10Book()
                                        opBook = Program._admin_BookMenu() # admin, book menu function called
                                        if opBook == '0':
                                            break
                                        elif opBook == '1':
                                            opBookBorrow = ' ' # book borrow option of book option,store user input
                                            while opBookBorrow != '1':
                                                Program._admin_10Book_1Borrow()
                                                print("Press 0 to Go Back...", end = '')
                                                opBookBorrow = input()
                                                if opBookBorrow == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opBookBorrow
# book borrow option of book option,store user input
                                        elif opBook == '2':
                                            opBookPurchase = ' ' #  book purchase option of book option,store user input
                                            while opBookPurchase != '1':
                                                Program._admin_10Book_2Purchase()
                                                print("Press 0 to Go Back...", end = '')
                                                opBookPurchase = input()
                                                if opBookPurchase == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opBookPurchase
# book purchase option of book option,store user input
# end of while loop opBook
# end of book option of admin menu option
                                elif opAdmin == "11":
                                    opSelfMotivational = ' ' # self motivational option, store return value of admin,self motivational menu function
                                    while opSelfMotivational != '4':
                                        Program._admin_11SelfMotivational()
                                        opSelfMotivational = Program._admin_SelfMotivationalMenu() # admin,self motivational menu function called
                                        if opSelfMotivational == '0':
                                            break
                                        elif opSelfMotivational == '1':
                                            opFiveTimePrayer = ' ' # five time prayer option of self motivstional ,store user input
                                            while opFiveTimePrayer != '3':
                                                Program._admin_11SelfMotivational_1FiveTimePrayer()
                                                print("Press 0 to Go Back...", end = '')
                                                opFiveTimePrayer = input()
                                                if opFiveTimePrayer == '0':
                                                    break
                                                elif opFiveTimePrayer == '1':

                                                    Program._five_time_Prayer[Program._inc_opFiveTimePrayer] = "Yes I Prayer five times! Alhamdulillah."
                                                    # File Handling
                                                    file = open("admin_11SelfMotivational_1FiveTimePrayer.txt",'a')
                                                    file.WriteLine(Program._five_time_Prayer[Program._inc_opFiveTimePrayer])
                                                    file.Flush()
                                                    file.Close()
                                                    print("Data sucessfully saved")
                                                    Program._inc_opFiveTimePrayer += 1
                                                    Program._hold_Option()
                                                    break

                                                elif opFiveTimePrayer == '2':
                                                    Program._five_time_Prayer[Program._inc_opFiveTimePrayer] = "No I Prayer five times! InshaAllah."
                                                    # File Handling
                                                    file = open("admin_11SelfMotivational_1FiveTimePrayer.txt", 'a')
                                                    file.WriteLine(Program._five_time_Prayer[Program._inc_opFiveTimePrayer])
                                                    file.Flush()
                                                    file.Close()
                                                    print("Data sucessfully saved")
                                                    Program._inc_opFiveTimePrayer += 1
                                                    Program._hold_Option()
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opFiveTimePrayer
# five time prayer option of self motivstional option
                                        elif opSelfMotivational == '2':
                                            opQuran_e_Pak = ' ' # Quran-e-ePak option of self motivational option , store user input
                                            while opQuran_e_Pak != '3':
                                                Program._admin_11SelfMotivational_2Quran_e_Pak()
                                                print("Press 0 to Go Back...", end = '')
                                                opQuran_e_Pak = input()
                                                if opQuran_e_Pak == '0':
                                                    break
                                                elif opQuran_e_Pak == '1':
                                                    Program._Quran_e_Pak[Program._inc_opQuran_e_Pak] = "Yes I recite Quran-e-Pak! Alhamdulillah. "
                                                    # File Handling
                                                    file = open("admin_11SelfMotivational_2Quran_e_Pak.txt", 'a')
                                                    file.WriteLine(Program._Quran_e_Pak[Program._inc_opQuran_e_Pak])
                                                    file.Flush()
                                                    file.Close()
                                                    print("Data sucessfully saved")
                                                    Program._inc_opQuran_e_Pak += 1
                                                    Program._hold_Option()
                                                    break
                                                elif opQuran_e_Pak == '2':
                                                    Program._Quran_e_Pak[Program._inc_opQuran_e_Pak] = "No I will recite Quran-e-Pak! InshaAllah. "
                                                    # File Handling
                                                    file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_11SelfMotivational_2Quran_e_Pak.txt", True)
                                                    file.WriteLine(Program._Quran_e_Pak[Program._inc_opQuran_e_Pak])
                                                    file.Flush()
                                                    file.Close()
                                                    print("Data sucessfully saved")
                                                    Program._inc_opQuran_e_Pak += 1
                                                    Program._hold_Option()
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opQuran_e_Pak
# end of Quran-e-ePak option of self motivational option
                                        elif opSelfMotivational == '3':
                                            opDurood_e_Pak = ' ' # Durood e Pak option of self motivational option,store user input
                                            while opDurood_e_Pak != '3':
                                                Program._admin_11SelfMotivational_3Durood_e_Pak()
                                                print("Press 0 to Go Back...", end = '')
                                                opDurood_e_Pak = input()
                                                if opDurood_e_Pak == '0':
                                                    break
                                                elif opDurood_e_Pak == '1':
                                                    Program._Durood_e_Pak[Program._inc_opDurood_e_Pak] = "Yes I sent Durood-e-Pak to Beloved Prophet peace be upon him! Alhamdulillah."
                                                    # File Handling
                                                    file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_11SelfMotivational_3Durood_e_Pak.txt", True)
                                                    file.WriteLine(Program._Durood_e_Pak[Program._inc_opDurood_e_Pak])
                                                    file.Flush()
                                                    file.Close()
                                                    print("Data sucessfully saved")
                                                    Program._inc_opDurood_e_Pak += 1
                                                    Program._hold_Option()
                                                    break

                                                elif opDurood_e_Pak == '2':
                                                    Program._Durood_e_Pak[Program._inc_opDurood_e_Pak] = "No I will send Durood-e-Pak to Beloved Prophet peace be upon him! InshaAllah."
                                                    # File Handling
                                                    file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_11SelfMotivational_3Durood_e_Pak.txt", True)
                                                    file.WriteLine(Program._Durood_e_Pak[Program._inc_opDurood_e_Pak])
                                                    file.Flush()
                                                    file.Close()
                                                    print("Data sucessfully saved")
                                                    Program._inc_opDurood_e_Pak += 1
                                                    Program._hold_Option()
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opDurood_e_Pak
# end of Durood e Pak option of self motivational option
# end of while loop opSelfMotivational
# end of  self motivational option of admin menu option
                                elif opAdmin == "12":
                                    opTransport = ' ' # transport option, store return value of admin, transport menu funtion
                                    while opTransport != '3':
                                        Program._admin_12Transport()
                                        opTransport = Program._admin_TransportMenu() # admin, transport menu funtion called
                                        if opTransport == '0':
                                            break
                                        elif opTransport == '1':
                                            opUberTransport1 = None # Uber/Cream/Bykea option of tansport option,store user input
                                            while opTransport != '1':
                                                Program._admin_12Transport_1Uber()
                                                print("Press 0 to Go Back...", end = '')
                                                opUberTransport1 = input()
                                                if opUberTransport1 == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opUberTransport
# end of Uber/Cream/Bykea option of tansport option
                                        elif opTransport == '2':
                                            opBusTransport = ' ' #  bus option of of transport option,store user input
                                            while opBusTransport != '1':
                                                Program._admin_12Transport_2Bus()
                                                print("Press 0 to Go Back...", end = '')
                                                opBusTransport = input()
                                                if opBusTransport == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opBusTransport
# end of bus option of of transport option
# end of while loop opTransport
# end of transport option of admin menu option
                                elif opAdmin == "13":
                                    opRecreationalActivities = ' ' # recreational activities option , store return value of admin, recreational activities menu function
                                    while opRecreationalActivities != '3':
                                        Program._admin_13RecreationalActivities()
                                        opRecreationalActivities = Program._admin_RecerationActivitiesMenu() # admin, recreational activities menu function called
                                        if opRecreationalActivities == '0':
                                            break
                                        elif opRecreationalActivities == '1':
                                            opSportiesActivities = ' ' # sporties activities option of recreational activities option,store user input
                                            while opSportiesActivities != '1':
                                                Program._admin_13RecreationalActivities_1Sporties()
                                                print("Press 0 to Go Back...", end = '')
                                                opSportiesActivities = input()

                                                if opSportiesActivities == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opSportiesActivities
# end of Sporties activities option of recreational activities option
                                        elif opRecreationalActivities == '2':
                                            opSocietiesActivities = ' ' # societies activities option of recreational activities option,store user input
                                            while opSocietiesActivities != '1':
                                                Program._admin_13RecreationalActivities_2Socities()
                                                print("Press 0 to Go Back...", end = '')
                                                opSocietiesActivities = input()
                                                if opSocietiesActivities == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opSocietiesActivities
# end of societies activities option of recreational activities option
# end of while loop opRecreationalActivities
# end of recreational activities option of admin menu option
                                elif opAdmin == "14":
                                    opAchievements = ' ' # achievments option , store return value of admin,achievments menu function
                                    while opAchievements != '2':
                                        Program._admin_14Achievments()
                                        opAchievements = Program._admin_Achievemnets() # admin,achievments menu function called
                                        if opAchievements == '0':
                                            break
                                        elif opAchievements == '1':
                                            opCoCurricular1 = None # co-curricular option of achievments option, store user input
                                            while True:
                                                Program._admin_14Achievments_1CoCurricular()
                                                print("Press 0 to Go Back...", end = '')
                                                opCoCurricular1 = input()
                                                if opCoCurricular1 == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop opCoCurricular
# end of co-curricular option of achievments option
                                        elif opAchievements == '2':
                                            opExtraCurricular = ' ' # extra-curricular option of achievments option, store user input
                                            while opExtraCurricular != '1':
                                                Program._admin_14Achievments_2ExtraCurricular()
                                                print("Press 0 to Go Back...", end = '')
                                                opExtraCurricular = input()
                                                if opExtraCurricular == '0':
                                                    break
                                                else:
                                                    print("Incorrect option", end = '')
                                                    print("\n", end = '')
                                                    Program._hold_Option() # end of while loop of opExtraCurricular
# end of extra-curricular option of achievments option
# end of while loop opAchievements
# end of achievments option of admin menu option
                                elif opAdmin == "15":
                                    opResultGrades = ' ' # result grades option of admin menu option, store user input
                                    while opResultGrades != '1':
                                        Program._admin_15ResultGrades()
                                        print("Press 0 to Go Back...", end = '')
                                        opResultGrades = input()

                                        if opResultGrades == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opResultGrades
# end of result grades option of admin menu option
                                elif opAdmin == "16":
                                    opGoldenLines = ' ' # golden lines option of admin menu option, store user input
                                    while opGoldenLines != '1':
                                        Program._admin_16GoldenLines()
                                        print("Press 0 to Go Back...", end = '')
                                        opGoldenLines = input()
                                        if opGoldenLines == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opGoldenLines
# end of golden lines option of admin menu option
                                elif opAdmin == "17":
                                    opLifelongEvents = ' ' # lifelong events  option of admin menu option, store user input
                                    while opLifelongEvents != '1':
                                        Program._admin_17LifelongEvents()
                                        print("Press 0 to Go Back...", end = '')
                                        opLifelongEvents = input()
                                        if opLifelongEvents == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opLifelongEvents
# end of lifelong events  option of admin menu option
                                elif opAdmin == "18":

                                    opNotes = ' ' # notes option of admin menu option, store user input
                                    while opNotes != '1':
                                        Program._admin_18Notes()
                                        print("Press 0 to Go Back...", end = '')
                                        opNotes = input()
                                        if opNotes == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opNotes
# end of notes option of admin menu option
                                elif opAdmin == "19":
                                    opAgentAddUser = ' ' # notes option of admin menu option, store user input
                                    while opAgentAddUser != '1':
                                        Program._admin_19CreateAgentAccount()
                                        print("Press 0 to Go Back...", end = '')
                                        opAgentAddUser = input()
                                        if opAgentAddUser == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opNotes
# end of notes option of admin menu option
                                elif opAdmin == "20":

                                    break
# end of logout option

                                else:
                                    print("Incorrect option", end = '')
                                    print("\n", end = '')
                                    Program._hold_Option() # end of While loop of opAdmin menu
#  end of option admin login true securty code
                        else:
                            print("Incorrect Username and Password", end = '')
                            print("\n", end = '')
                            Program._hold_Option()
# end of option admin login false security code
# end of admin login option
                    #******************************* END OF ADMIN MENU OPTION *******************************************
                    elif opLogin == '2':
                        agentUsername = "" # Agent sig-in variable
                        agentPassword = ""
                        agentUsername = agentPassword = "" # variable initiation
                        Program._header() # header function is called
                        print("Main Menu > Login > Agent", end = '')
                        print("\n", end = '')
                        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                        print("\n", end = '')
                        print("Sign-In", end = '')
                        print("\n", end = '')
                        print("Username : ", end = '')
                        agentUsername = input()
                        print("Password : ", end = '')
                        agentPassword = input()
                        agentindex = Program._checkuser_agent(agentUsername, agentPassword) # check the username and password in the array and make descion upon it
                        if Program._username_Agent[agentindex] == agentUsername and Program._password_Agent[agentindex] == agentPassword:
                            opAgent = " " # Agent option , store return value of agent menu function
                            while True:
                                Program._header() # header function is called
                                print("Main Menu > Menu ", end = '')
                                print("\n", end = '')
                                print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                                print("\n", end = '')
                                opAgent = Program._agent_Menu() # agent menu function called
                                if opAgent == "0":
                                    opProfile = ' '
                                    while opProfile != '1':
                                        Program._agent_0Profile(agentindex)
                                        print("Press 0 to go back...", end = '')
                                        opProfile = input()
                                        if opProfile == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option()
                                elif opAgent == "1":
                                    opWallet = ' ' # wallet option, store user input
                                    while opWallet != '1':
                                        Program._agent_1Wallet()
                                        print("Press 0 to go back...", end = '')
                                        opWallet = input()
                                        if opWallet == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opWallet
# enf of wallet option of agent option
                                elif opAgent == "2":
                                    opAcademicReport = ' ' # acsdemic report, store user input
                                    while opAcademicReport != '1':
                                        Program._agent_2AcademicReport()
                                        print("Press 0 to go back...", end = '')
                                        opAcademicReport = input()
                                        if opAcademicReport == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opAcademicReport
# end of academic report option of agent option

                                elif opAgent == "3":
                                    opExpensesReport = None # monthly expenses option , store user input
                                    while True:
                                        Program._agent_3ExpensesReport()
                                        print("Press 0 to go back...", end = '')
                                        opExpensesReport = input()
                                        if opExpensesReport == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opExpensesReport
# end of expenses report of agent option
                                elif opAgent == "4":
                                    opMealReport = None # meal option ,store user input
                                    while True:
                                        Program._agent_4MealReport()
                                        print("Press 0 to go back...", end = '')
                                        opMealReport = input()
                                        if opMealReport == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opMealReport
# end of meal option of agent option
                                elif opAgent == "5":
                                    opTracker = None # salah tracker ,store user input
                                    while True:
                                        Program._agent_5SpiritualTracker()
                                        print("Press 0 to go back...", end = '')
                                        opTracker = input()
                                        if opTracker == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opTracker
# salah tracker option of agent option
                                elif opAgent == "6":
                                    opAachievmentsReport = ' ' # achivements report,store user input
                                    while opAachievmentsReport != '1':
                                        Program._agent_6AachieventsReport()
                                        print("Press 0 to go back...", end = '')
                                        opAachievmentsReport = input()
                                        if opAachievmentsReport == '0':
                                            break
                                        else:
                                            print("Incorrect option", end = '')
                                            print("\n", end = '')
                                            Program._hold_Option() # end of while loop opAachievmentsReport
# end of achivements report option of agent option
                                elif opAgent == "7":
                                    break # end of agent function
                                else:
                                    print("Incorrect option", end = '')
                                    print("\n", end = '')
                                    Program._hold_Option() # end of while loop opAgent
# end of agent login true securty code

                        else:
                            print("Incorrect Username and Password", end = '')
                            print("\n", end = '')
                            Program._hold_Option()
# end of agent login False security code
# end of agent login option

                    else:
                        print("Incorrect option", end = '')
                        print("\n", end = '')
                        Program._hold_Option()

                    #******************************* END OF AGENT OPTION *******************************************c
# end of login option of main menu
# end of While loop of opLogin
            elif opMain == '2':
                opAbout = ' ' # about options, store user input
                while opAbout != '3':
                    Program._header() # header function is called
                    print("Main Menu > About ", end = '')
                    print("\n", end = '')
                    print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                    print("\n", end = '')
                    print("1. Version ", end = '')
                    print("\n", end = '')
                    print("2. Developer ", end = '')
                    print("\n", end = '')
                    print("Press 0 to Go Back...", end = '')
                    opAbout = input()

                    if opAbout == '0':
                        break
# end of Go Back of about option
                    elif opAbout == '1':
                        opVersion = ' ' # option version, store user input
                        while opVersion != '1':
                            Program._header() # header function is called
                            print("Main Menu > About > Version", end = '')
                            print("\n", end = '')
                            print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                            print("\n", end = '')
                            print("Version : 4.0", end = '')
                            print("\n", end = '')
                            print("Version 04 is developed with the concept of Conditional statments,", end = '')
                            print("\n", end = '')
                            print("Functions, loops, Arrays and File Handling...", end = '')
                            print("\n", end = '')
                            print("Press 0 to Go Back...", end = '')
                            opVersion = input()
                            if opVersion == '0':
                                break
                            else:
                                print("Incorrect option", end = '')
                                print("\n", end = '')
                                Program._hold_Option() # end of while loop opVersion
# end of version of about option
                    elif opAbout == '2':
                        opDeveloper = None # option developer, store user input
                        while True:
                            Program._header() # header function is called
                            print("Main Menu > About > Developer", end = '')
                            print("\n", end = '')
                            print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                            print("\n", end = '')
                            print("Instructor     : Dr Awais Hassan", end = '')
                            print("\n", end = '')
                            print("Special thanks : Laeeq Khan Niazi ", end = '')
                            print("\n", end = '')
                            print("Developer      : Muhammad Hammad Hassan", end = '')
                            print("\n", end = '')
                            print("Contact        : +923030299365 ", end = '')
                            print("\n", end = '')
                            print("Press 0 to Go Back...", end = '')
                            opDeveloper = input()
                            if opDeveloper == '0':
                                break
                            else:
                                print("Incorrect option", end = '')
                                print("\n", end = '')
                                Program._hold_Option() # end of while loop opDeveloper
# end of developer of about option
# end of while loop opAbout
# end of about option of menu menu
            elif opMain == '3':
                opAccount = ' ' # create new account  option, store user input
                while opAccount != '1':
                    Program._header() # header function is called
                    print("Main Menu > Create an acount ", end = '')
                    print("\n", end = '')
                    print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                    print("\n", end = '')
                    print("Enter first name : ", end = '')
                    Program._firstname[Program._inc_opAddUser] = input()
                    print("Enter last name : ", end = '')
                    Program._lastname[Program._inc_opAddUser] = input()
                    print("Enter username : ", end = '')
                    Program._username[Program._inc_opAddUser] = input()
                    check = Program._check_Existing(Program._username[Program._inc_opAddUser])
                    while Program._check_Existing(Program._username[Program._inc_opAddUser]) == True:
                        print("Username is already exist try another once", end = '')
                        print("\n", end = '')
                        print("Enter username : ", end = '')
                        Program._username[Program._inc_opAddUser] = input()
                    print("Enter password :", end = '')
                    Program._password[Program._inc_opAddUser] = input()
                    # File Handling
                    file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\adminSecurityFile.txt", True)
                    file.WriteLine(Program._firstname[Program._inc_opAddUser] + "," + Program._lastname[Program._inc_opAddUser] + "," + Program._username[Program._inc_opAddUser] + "," + Program._password[Program._inc_opAddUser])
                    file.Flush()
                    file.Close()
                    print("Data sucessfully saved")
                    Program._inc_opAddUser += 1
                    print("Press 0 to Go Back...", end = '')
                    opAccount = input()
                    if opAccount == '0':
                        break
                    else:
                        print("Incorrect option", end = '')
                        print("\n", end = '')
                        Program._hold_Option()
                        break # end of create new account option
            elif opMain == '4':
                opExit = ' ' # Exit options, store user input
                Program._header() # header function is called
                print("Main Menu > Exit ", end = '')
                print("\n", end = '')
                print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
                print("\n", end = '')
                print("Are you sure to want to Exit?", end = '')
                print("\n", end = '')
                print("1. Yes ", end = '')
                print("\n", end = '')
                print("2. No ", end = '')
                print("\n", end = '')
                print("Press 0 to Go Back...", end = '')
                opExit = input()
                if opExit == '0':
                    continue
                elif opExit == '1':
                    Program._header() # header is called
                    print("Thanks for using University Student Diary Managment System", end = '')
                    print("\n", end = '')
                    print("Take Care...Allah Hafiz", end = '')
                    input()
                    break # end of exit Yes, Program will terminate
                elif opExit == '2':
                    continue
                else:
                    print("Incorrect option", end = '')
                    print("\n", end = '')
                    Program._hold_Option()
# exit option of admin home menu
            else:
                print("Invalid option...", end = '')
                print("\n", end = '')
                Program._hold_Option()
# message show  invalid option of option main screen
# end while loop main menu
        input() #end of main functio
    #********************* Functions Definition ************************
    @staticmethod
    def _header():
        os.system("cls")
        print("*************************************************************************************")
        print("*************                                                           *************")
        print("********                                                                     ********")
        print("***                  University Student Diary Management System                   ***")
        print("********                                                                     ********")
        print("*************                                                           *************")
        print("*************************************************************************************")
# header funtion end
    @staticmethod
    def _header_Welcome():
        os.system("cls")
        print("*************************************************************************************")
        print("*************                                                           *************")
        print("********                                                                     ********")
        print("***             Welcome to University Student Diary Management System             ***")
        print("********                                                                     ********")
        print("*************                                                           *************")
        print("*************************************************************************************") # end of header welcome funtion
    @staticmethod
    def _admin_HomeMenu():
        opMain = None
        print("1. Login")
        print("2. About")
        print("3. Create an acount")
        print("4. Exit")
        print("Press the number... ", end = '')
        opMain =input()
        return opMain # end of admin home menu
    @staticmethod
    def _hold_Option():
        print("Press anykey to continue...")
        input() # end of hold option function
    #********************* SECURITY ************************
    @staticmethod
    def _checkuser(user_name, pass_word):
        index = -1
        for i in range(0, 20):
            if user_name == Program._username[i] and pass_word == Program._password[i]:
                index = i
        return index # end of check username
    @staticmethod
    def _check_Existing(username_check):
        i = 0
        while i < Program._inc_opAddUser:
            if username_check == Program._username[i]:
                return True
            i += 1
        return False
# end of check exiting username
    @staticmethod
    def _checkuser_agent(agent_user_name, agent_pass_word):
        index_agent = -1
        for i in range(0, 20):
            if agent_user_name == Program._username_Agent[i] and agent_pass_word == Program._password_Agent[i]:
                index_agent = i

        return index_agent
    @staticmethod
    def _check_Existing_agent(agent_username_check):
        i = 0
        while i < Program._inc_opAgentAddUser:
            if agent_username_check == Program._username_Agent[i]:
                return True
            i += 1
        return False
    #****************** ADMIN ******************
    @staticmethod
    def _admin_0Profile(indexValue):

        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Profile")
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________")
        print("                                   __WELCOME ON BOARD__                             ")
        print("First name : ")
        print(Program._firstname[indexValue], end = '')
        print("\t", end = '')
        print("Last name : ", end = '')
        print(Program._lastname[indexValue])
        print("_____________________________________________________________________________________")
        print("Recommendations:-")
        Program._admin_Recommendation()
        print("_____________________________________________________________________________________")
        Program._display_profile_admin() # end of option 0 profle of admin
    @staticmethod
    def _admin_1WalletStatus():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Wallet Status ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Current Blance:", end = '')
        print(Program._addWalletMoney - Program._total_Expenses(), end = '')
        print("\n", end = '')
        print("Remarks from Agent:", end = '')
        print(Program._walletRemarks, end = '')
        print("\n", end = '') # end of admin option 1
    @staticmethod
    def _admin_2ExpensesReport():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Expenses Report ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of admin option 1
    @staticmethod
    def _admin_2ExpensesReportToday():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Expenses Report > Today  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        Program._display_breakfast()
        print("_____________________________________________________________________________________", end = '')
        print("\n", end = '')
        Program._display_lunch()
        print("_____________________________________________________________________________________", end = '')
        print("\n", end = '')
        Program._display_dinner() # end of admin option 2 of today report
    @staticmethod
    def _admin_2ExpensesReportMonthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > ExpensesReport > Monthly", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Monthly Report :- ", end = '')
        print("\n", end = '')
        print("Personal................: ", end = '')
        print(Program._personal_Expenses(), end = '')
        print("\n", end = '')
        print("Hostel..................: ", end = '')
        print(Program._hostel_Expenses(), end = '')
        print("\n", end = '')
        print("Helping Material........: ", end = '')
        print(Program._helpingmaterial_Expenses(), end = '')
        print("\n", end = '')
        print("Recreational Expenses...: ", end = '')
        print(Program._recreational_Expenses(), end = '')
        print("\n", end = '')
        print("Fund....................: ", end = '')
        print(Program._communityfund_Expenses(), end = '')
        print("\n", end = '')
        print("Cell Phone..............: ", end = '')
        print(Program._cellphone_Expenses(), end = '')
        print("\n", end = '')
        print("Transport...............: ", end = '')
        print(Program._transport_Expenses(), end = '')
        print("\n", end = '')
        print("                   Total: ", end = '')
        print(Program._total_Expenses(), end = '')
        print("\n", end = '') # end of admin option 2 of monthly option
    @staticmethod
    def _admin_2ExpensesReportYearly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > ExpensesReport > Year  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        Program._display_academicFee() # sorted academic fee function called // end of admin option 2 of yearly
    @staticmethod
    def _admin_3AcademicFee():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Academic Fee ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Semester type : ", end = '')
        Program._semesterType[Program._increment_opAcademicFee] =input()
        print("Challan no : ", end = '')
        Program._challanNo[Program._increment_opAcademicFee] = input()
        print("Amount : ", end = '')
        Program._amountacademic[Program._increment_opAcademicFee] = Program._float_Validaion("Amount : ", input())
        print("Date : ", end = '')
        Program._date[Program._increment_opAcademicFee] = input()
        print("Remarks  : ", end = '')
        Program._remarks[Program._increment_opAcademicFee] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin3AcadmicFee.txt", True)
        file.WriteLine(Program._semesterType[Program._increment_opAcademicFee] + "," + str(Program._amountacademic[Program._increment_opAcademicFee])+","+ Program._date[Program._increment_opAcademicFee]+""+ Program._remarks[Program._increment_opAcademicFee])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._increment_opAcademicFee += 1 # after storing data successfully,increase the index by 1 // end of admin option 3
    @staticmethod
    def _admin_4Hostel():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of admin 4 option
    @staticmethod
    def _admin_4Hostel_1Meal():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Meal  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of admin 4 option of sub option 1 meal
    @staticmethod
    def _admin_4Hostel_1Meal_1Breakfast():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Meal > Breakfast Charges ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Note: If you Hostilities, add 000 in charges.", end = '')
        print("\n", end = '')
        print("Menu : ", end = '')
        Program._menuBreakfast[Program._increment_opMealBreakfast] = input()
        print("Charges : ", end = '')
        Program._chargesBreakfast[Program._increment_opMealBreakfast] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksBreakfast[Program._increment_opMealBreakfast] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_1Meal_1Breakfast.txt", True)
        file.WriteLine(Program._menuBreakfast[Program._increment_opMealBreakfast] + "," + str(Program._chargesBreakfast[Program._increment_opMealBreakfast]) + "," + Program._remarksBreakfast[Program._increment_opMealBreakfast])
        file.Flush()
        file.Close()
        Program._increment_opMealBreakfast += 1 # end of function
    @staticmethod
    def _admin_4Hostel_1Meal_2Lunch():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Meal > Lunch Charges ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Note: If you Hostilities, add 000 in charges.", end = '')
        print("\n", end = '')
        print("Menu : ", end = '')
        Program._menuLunch[Program._increment_opMealLunch] = input()
        print("Charges : ", end = '')
        Program._chargesLunch[Program._increment_opMealLunch] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksLunch[Program._increment_opMealLunch] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_1Meal_2Lunch.txt", True)
        file.WriteLine(Program._menuLunch[Program._increment_opMealLunch] + "," + str(Program._chargesLunch[Program._increment_opMealLunch]) + "," + Program._remarksLunch[Program._increment_opMealLunch])
        file.Flush()
        file.Close()
        Program._increment_opMealLunch += 1 # end of function
    @staticmethod
    def _admin_4Hostel_1Meal_3Dinner():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Meal > Dinner Charges ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Note: If you Hostilities, add 000 in charges.", end = '')
        print("\n", end = '')
        print("Menu : ", end = '')
        Program._menuDinner[Program._increment_opMealDinner] = input()
        print("Charges : ", end = '')
        Program._chargesDinner[Program._increment_opMealDinner] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksDinner[Program._increment_opMealDinner] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_1Meal_3Dinner.txt", True)
        file.WriteLine(Program._menuDinner[Program._increment_opMealDinner] + "," + str(Program._chargesDinner[Program._increment_opMealDinner]) + "," + Program._remarksDinner[Program._increment_opMealDinner])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._increment_opMealDinner += 1 # end of function
    @staticmethod
    def _admin_4Hostel_2MealChargesMonthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Monthly fee Charges  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Month : ", end = '')
        Program._monthlyMealExpenses[Program._increment_opMealCharges] = input()
        print("Charges : ", end = '')
        Program._chargesMealMonthly[Program._increment_opMealCharges] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksMealExpenses[Program._increment_opMealCharges] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_2MealChargesMonthly.txt", True)
        file.WriteLine(Program._monthlyMealExpenses[Program._increment_opMealCharges] + "," + str(Program._chargesMealMonthly[Program._increment_opMealCharges]) + "," + Program._remarksMealExpenses[Program._increment_opMealCharges])
        file.Flush()
        file.Close()
        Program._increment_opMealCharges += 1 # end of function
    @staticmethod
    def _admin_4Hostel_3LivingChargesMonthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Living Charges  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Month : ", end = '')
        Program._monthLivingExpenses[Program._inc_opLivingCharges] = input()
        print("Charges : ", end = '')
        Program._chargesLivingExpenses[Program._inc_opLivingCharges] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksLivingExpenses[Program._inc_opLivingCharges] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_3LivingChargesMonthly.txt", True)
        file.WriteLine(Program._monthLivingExpenses[Program._inc_opLivingCharges] + "," + str(Program._chargesLivingExpenses[Program._inc_opLivingCharges]) + "," + Program._remarksLivingExpenses[Program._inc_opLivingCharges])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opLivingCharges += 1 # end of function
    @staticmethod
    def _admin_4Hostel_4ServiceChargesMonthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Service Charges  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Month : ", end = '')
        Program._monthServiceExpenses[Program._inc_opServiceCharges] = input()
        print("Charges : ", end = '')
        Program._chargesServiceMonthly[Program._inc_opServiceCharges] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksServiceExpenses[Program._inc_opServiceCharges] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_4ServiceChargesMonthly.txt", True)
        file.WriteLine(Program._monthServiceExpenses[Program._inc_opServiceCharges] + "," + str(Program._chargesServiceMonthly[Program._inc_opServiceCharges]) + "," + Program._remarksServiceExpenses[Program._inc_opServiceCharges])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opServiceCharges += 1 # end of function
    @staticmethod
    def _admin_4Hostel_5RenovationChargesMonthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Renovation Charges  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesRenovationMonthly[Program._inc_opRenovationCharges] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksRenovationExpenses[Program._inc_opRenovationCharges] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_5RenovationChargesMonthly.txt", True)
        file.WriteLine(str(Program._chargesRenovationMonthly[Program._inc_opRenovationCharges]) + "," + Program._remarksRenovationExpenses[Program._inc_opRenovationCharges])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opRenovationCharges += 1 # end of function
    @staticmethod
    def _admin_4Hostel_6LaundryChargesMonthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Laundry Charges  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesLaundryMonthly[Program._inc_opLaundryCharges] = Program._float_Validaion("Charges : ", input())
        Program._remarksLaundryExpenses[Program._inc_opLaundryCharges] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_6LaundryChargesMonthly.txt", True)
        file.WriteLine(str(Program._chargesLaundryMonthly[Program._inc_opLaundryCharges]) + "," + Program._remarksLaundryExpenses[Program._inc_opLaundryCharges])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opLaundryCharges += 1
        print("Press 0 to Go Back...", end = '') # end of function
    @staticmethod
    def _admin_4Hostel_7BarberChargesMonthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Hostel > Laundry Charges  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesBarberMonthly[Program._inc_opBarberCharges] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksBarberExpenses[Program._inc_opBarberCharges] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_7BarberChargesMonthly.txt", True)
        file.WriteLine(str(Program._chargesBarberMonthly[Program._inc_opBarberCharges]) + "," + Program._remarksBarberExpenses[Program._inc_opBarberCharges])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opBarberCharges += 1 # end of function
    @staticmethod
    def _admin_5HelpingMaterial():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Helping Material  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_5HelpingMaterial_1Notes():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Helping Material > Notes ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesNotesMonthly[Program._inc_opNotesHelpingMaterial] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksNotesExpenses[Program._inc_opNotesHelpingMaterial] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_5HelpingMaterial_1Notes.txt", True)
        file.WriteLine(str(Program._chargesNotesMonthly[Program._inc_opNotesHelpingMaterial]) + "," + Program._remarksNotesExpenses[Program._inc_opNotesHelpingMaterial])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opNotesHelpingMaterial += 1 # end of function
    @staticmethod
    def _admin_5HelpingMaterial_2Register():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Helping Material > Register ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesRegisterMonthly[Program._inc_opRegisterHelpingMaterial] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksRegisterExpenses[Program._inc_opRegisterHelpingMaterial] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_5HelpingMaterial_2Register.txt", True)
        file.WriteLine(str(Program._chargesRegisterMonthly[Program._inc_opRegisterHelpingMaterial]) + "," + Program._remarksRegisterExpenses[Program._inc_opRegisterHelpingMaterial])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opRegisterHelpingMaterial += 1 # end of function
    @staticmethod
    def _admin_5HelpingMaterial_3Stationary():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Helping Material > Stationary ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesStationaryMonthly[Program._inc_opStationaryHelpingMaterial] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksStationaryExpenses[Program._inc_opStationaryHelpingMaterial] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_5HelpingMaterial_3Stationary.txt", True)
        file.WriteLine(str(Program._chargesStationaryMonthly[Program._inc_opStationaryHelpingMaterial]) + "," + Program._remarksStationaryExpenses[Program._inc_opStationaryHelpingMaterial])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opStationaryHelpingMaterial += 1 # end of function
    @staticmethod
    def _admin_6RecreationalExpenses():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Recreational Expenses  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_6RecreationalExpenses_1Friends():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Recreational Expenses > Friends  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesFriendsRecreationalExpenses[Program._inc_opFriendsRecreationalExpenses] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksFriendsRecreationalExpenses[Program._inc_opFriendsRecreationalExpenses] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_6RecreationalExpenses_1Friends.txt", True)
        file.WriteLine(str(Program._chargesFriendsRecreationalExpenses[Program._inc_opFriendsRecreationalExpenses]) + "," + Program._remarksFriendsRecreationalExpenses[Program._inc_opFriendsRecreationalExpenses])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opFriendsRecreationalExpenses += 1 # end of function
    @staticmethod
    def _admin_6RecreationalExpenses_2Family():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Recreational Expenses > Family  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Charges : ", end = '')
        Program._chargesFamilyRecreationalExpenses[Program._inc_opFamilyRecreationalExpenses] = Program._float_Validaion("Charges : ", input())
        print("Remarks : ", end = '')
        Program._remarksFamilyRecreationalExpenses[Program._inc_opFamilyRecreationalExpenses] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_6RecreationalExpenses_2Family.txt", True)
        file.WriteLine(str(Program._chargesFamilyRecreationalExpenses[Program._inc_opFamilyRecreationalExpenses]) + "," + Program._remarksFamilyRecreationalExpenses[Program._inc_opFamilyRecreationalExpenses])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opFamilyRecreationalExpenses += 1 # end of function
    @staticmethod
    def _admin_7CommunityFund():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Community Fund  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_7CommunityFund_1Class():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Community Fund ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Objective : ", end = '')
        Program._remarksClassCommunityFund[Program._inc_opClassCommunityFund] = input()
        print("Charges : ", end = '')
        Program._chargesClassCommunityFund[Program._inc_opClassCommunityFund] = Program._float_Validaion("Charges : ", input())
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_7CommunityFund_1Class.txt", True)
        file.WriteLine(Program._remarksClassCommunityFund[Program._inc_opClassCommunityFund] + "," + str(Program._chargesClassCommunityFund[Program._inc_opClassCommunityFund]))
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opClassCommunityFund += 1 # end of function
    @staticmethod
    def _admin_7CommunityFund_2Societies():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Community Fund ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Objective : ", end = '')
        Program._remarksSocietiesCommunityFund[Program._inc_opSocietiesCommunityFund] = input()
        print("Charges : ", end = '')
        Program._chargesSocietiesCommunityFund[Program._inc_opSocietiesCommunityFund] = Program._float_Validaion("Charges : ", input())
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_7CommunityFund_2Societies.txt", True)
        file.WriteLine(Program._remarksSocietiesCommunityFund[Program._inc_opSocietiesCommunityFund] + "," + str(Program._chargesSocietiesCommunityFund[Program._inc_opSocietiesCommunityFund]))
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opSocietiesCommunityFund += 1 # end of function
    @staticmethod
    def _admin_8Goals():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Goals ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_8Goals_1Daily():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Goals > Daily ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleDailyGoals[Program._inc_opDailyGoals] = input()
        print("Description : ", end = '')
        Program._descriptionDailyGoals[Program._inc_opDailyGoals] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_1Daily.txt", True)
        file.WriteLine(Program._titleDailyGoals[Program._inc_opDailyGoals] + "," + Program._descriptionDailyGoals[Program._inc_opDailyGoals])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opDailyGoals += 1 # end of function
    @staticmethod
    def _admin_8Goals_2Weekly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Goals > Weekly ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleWeeklyGoals[Program._inc_opWeeklyGoals] = input()
        print("Description : ", end = '')
        Program._descriptionWeeklyGoals[Program._inc_opWeeklyGoals] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_2Weekly.txt", True)
        file.WriteLine(Program._titleWeeklyGoals[Program._inc_opWeeklyGoals] + "," + Program._descriptionWeeklyGoals[Program._inc_opWeeklyGoals])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opWeeklyGoals += 1 # end of function
    @staticmethod
    def _admin_8Goals_3Monthly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Goals > Monthly ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleMonthlyGoals[Program._inc_opMonthlyGoals] = input()
        print("Description : ", end = '')
        Program._descriptionMonthlyGoals[Program._inc_opMonthlyGoals] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_3Monthly.txt", True)
        file.WriteLine(Program._titleMonthlyGoals[Program._inc_opMonthlyGoals] + "," + Program._descriptionMonthlyGoals[Program._inc_opMonthlyGoals])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opMonthlyGoals += 1 # end of function
    @staticmethod
    def _admin_8Goals_4Yearly():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Goals > Monthly ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleYearlyGoals[Program._inc_opYearlyGoals] = input()
        print("Description : ", end = '')
        Program._descriptionYearlyGoals[Program._inc_opYearlyGoals] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_4Yearly.txt", True)
        file.WriteLine(Program._titleYearlyGoals[Program._inc_opYearlyGoals] + "," + Program._descriptionYearlyGoals[Program._inc_opYearlyGoals])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opYearlyGoals += 1 # end of function
    @staticmethod
    def _admin_9CellPhone():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Cell Phone ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_9CellPhone_1Call():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Cell Phone > Call Pakage ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Name : ", end = '')
        Program._nameCallPakage[Program._inc_opCall_CellPhone] = input()
        print("Amount : ", end = '')
        Program._amountCallPakage[Program._inc_opCall_CellPhone] = Program._float_Validaion("Amount : ", input())
        print("Duration : ", end = '')
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_9CellPhone_1Call.txt", True)
        file.WriteLine(Program._nameCallPakage[Program._inc_opCall_CellPhone] + "," + str(Program._amountCallPakage[Program._inc_opCall_CellPhone])+","+ Program._durationCallPakage[Program._inc_opCall_CellPhone])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opCall_CellPhone += 1 # end of function
    @staticmethod
    def _admin_9CellPhone_2Internet():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Cell Phone > Internet Pakage ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Name : ", end = '')
        Program._nameInternetPakage[Program._inc_opInternet_CellPhone] = input()
        print("Amount : ", end = '')
        Program._amountInternetPakage[Program._inc_opInternet_CellPhone] = Program._float_Validaion("Amount : ", input())
        print("Duration : ", end = '')
        Program._durationInternetPakage[Program._inc_opInternet_CellPhone] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_9CellPhone_2Internet.txt", True)
        file.WriteLine(Program._nameInternetPakage[Program._inc_opInternet_CellPhone] + "," + str(Program._amountInternetPakage[Program._inc_opInternet_CellPhone]) + ","+ Program._durationInternetPakage[Program._inc_opInternet_CellPhone])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opInternet_CellPhone += 1 # end of function
    @staticmethod
    def _admin_9CellPhone_3Message():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Cell Phone > Message Pakage ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Name : ", end = '')
        Program._nameMessagePakage[Program._inc_opMessage_CellPhone] = input()
        print("Amount : ", end = '')
        Program._amountMessagePakage[Program._inc_opMessage_CellPhone] = Program._float_Validaion("Amount : ", input())
        print("Duration : ", end = '')
        Program._durationMessagePakage[Program._inc_opMessage_CellPhone] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_9CellPhone_3Message.txt", True)
        file.WriteLine(Program._nameMessagePakage[Program._inc_opMessage_CellPhone] + "," + str(Program._amountMessagePakage[Program._inc_opMessage_CellPhone]) + "," + Program._durationMessagePakage[Program._inc_opMessage_CellPhone])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opMessage_CellPhone += 1 # end of function
    @staticmethod
    def _admin_10Book():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Book ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_10Book_1Borrow():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Book > Borrow ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleBorrowBook[Program._inc_opBookBorrow] = input()
        print("Author: : ", end = '')
        Program._authorBorrowBook[Program._inc_opBookBorrow] = input()
        print("Friend Name : ", end = '')
        Program._friendnameBorrowBook[Program._inc_opBookBorrow] = input()
        print("Remarks : ", end = '')
        Program._remarksBorrowBook[Program._inc_opBookBorrow] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_10Book_1Borrow.txt", True)
        file.WriteLine(Program._titleBorrowBook[Program._inc_opBookBorrow] + "," + Program._authorBorrowBook[Program._inc_opBookBorrow] + "," + Program._friendnameBorrowBook[Program._inc_opBookBorrow]+","+ Program._remarksBorrowBook[Program._inc_opBookBorrow])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opBookBorrow += 1 # end of function
    @staticmethod
    def _admin_10Book_2Purchase():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Book > Purchase ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titlePurchaseBook[Program._inc_opBookPurchase] = input()
        print("Author: : ", end = '')
        Program._authorPurchaseBook[Program._inc_opBookPurchase] = input()
        print("Purchase : ", end = '')
        Program._amountPurchaseBook[Program._inc_opBookPurchase] = Program._float_Validaion("Purchase : ", input())
        print("Remarks : ", end = '')
        Program._remarksPurchaseBook[Program._inc_opBookPurchase] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_10Book_2Purchase.txt", True)
        file.WriteLine(Program._titlePurchaseBook[Program._inc_opBookPurchase] + "," + Program._authorPurchaseBook[Program._inc_opBookPurchase] + "," + str(Program._amountPurchaseBook[Program._inc_opBookPurchase]) + "," + Program._remarksPurchaseBook[Program._inc_opBookPurchase])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opBookPurchase = +1 # end of function
    @staticmethod
    def _admin_11SelfMotivational():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Spiritual Food ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_11SelfMotivational_1FiveTimePrayer():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Spiritual Food > Five-time Prayer ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Is you prayer five times?", end = '')
        print("\n", end = '')
        print("   1. Yes", end = '')
        print("\n", end = '')
        print("   2. No", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_11SelfMotivational_2Quran_e_Pak():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Spiritual Food > Quran-e-Pak ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Is you Recite Quran-e-Pak?", end = '')
        print("\n", end = '')
        print("   1. Yes", end = '')
        print("\n", end = '')
        print("   2. No", end = '')
        print("\n", end = '') # header function is called
    @staticmethod
    def _admin_11SelfMotivational_3Durood_e_Pak():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Spiritual Food > Quran-e-Pak ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Is you send Durood-e-Pak to Beloved Prophet peace be upon him", end = '')
        print("\n", end = '')
        print("   1. Yes", end = '')
        print("\n", end = '')
        print("   2. No", end = '')
        print("\n", end = '') # header function is called
    @staticmethod
    def _admin_12Transport():
        Program._header() # header function is called;
        print("Main Menu > Admin > Menu > Transport ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_12Transport_1Uber():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Transport > Uber/Cream/Bykea ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Location from : ", end = '')
        Program._locationFromUber[Program._inc_opUberTransport] = input()
        print("Location to: ", end = '')
        Program._locationToUber[Program._inc_opUberTransport] = input()
        print("Amount : ", end = '')
        Program._amountUber[Program._inc_opUberTransport] = Program._float_Validaion("Amount : ", input())
        print("Purpose : ", end = '')
        Program._purposeUber[Program._inc_opUberTransport] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_12Transport_1Uber.txt", True)
        file.WriteLine(Program._locationFromUber[Program._inc_opUberTransport] + "," + Program._locationToUber[Program._inc_opUberTransport] + "," + str(Program._amountUber[Program._inc_opUberTransport]) + "," + Program._purposeUber[Program._inc_opUberTransport])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opUberTransport += 1 # end of function
    @staticmethod
    def _admin_12Transport_2Bus():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Transport > Bus ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Location from : ", end = '')
        Program._locationFromBus[Program._inc_opBusTransport] = input()
        print("Location to: ", end = '')
        Program._locationToBus[Program._inc_opBusTransport] = input()
        print("Ticket Price : ", end = '')
        Program._amountBus[Program._inc_opBusTransport] = Program._float_Validaion("Ticket Price : ", input())
        print("Purpose : ", end = '')
        Program._purposeBus[Program._inc_opBusTransport] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_12Transport_2Bus.txt", True)
        file.WriteLine(Program._locationFromBus[Program._inc_opBusTransport] + "," + Program._locationToBus[Program._inc_opBusTransport] + "," + str(Program._amountBus[Program._inc_opBusTransport]) + "," + Program._purposeBus[Program._inc_opBusTransport])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opBusTransport += 1 # end of function
    @staticmethod
    def _admin_13RecreationalActivities():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Recreational Activities ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_13RecreationalActivities_1Sporties():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Recreational Activities > Sporties ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("How much time you service?", end = '')
        print("\n", end = '')
        print("Minuties: ", end = '')
        Program._minutiesSporties[Program._inc_opSportiesActivities] = Program._float_Validaion("Minuties: ", input())
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_13RecreationalActivities_1Sporties.txt", True)
        file.WriteLine(Program._minutiesSporties[Program._inc_opSportiesActivities])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opSportiesActivities += 1 # end of function
    @staticmethod
    def _admin_13RecreationalActivities_2Socities():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Recreational Activities > Societies ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("How much time you service?", end = '')
        print("\n", end = '')
        print("Minuties: ", end = '')
        Program._minutiesSocieties[Program._inc_opSocietiesActivities] = Program._float_Validaion("Minuties: ", input())
        print("Purpose: ", end = '')
        Program._purposeSocieties[Program._inc_opSocietiesActivities] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_13RecreationalActivities_2Socities.txt", True)
        file.WriteLine(str(Program._minutiesSocieties[Program._inc_opSocietiesActivities]) + "," + Program._purposeSocieties[Program._inc_opSocietiesActivities])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opSocietiesActivities += 1 # end of function
    @staticmethod
    def _admin_14Achievments():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Achievements ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '') # end of function
    @staticmethod
    def _admin_14Achievments_1CoCurricular():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Achievements > Co-Curricular ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Award/Certificate: ", end = '')
        Program._awardCo_Curricular[Program._inc_opCoCurricular] = input()
        print("Presented by: ", end = '')
        Program._presentCo_Curricular[Program._inc_opCoCurricular] = input()
        print("Remarks: ", end = '')
        Program._remarksCo_Curricular[Program._inc_opCoCurricular] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_14Achievments_1CoCurricular.txt", True)
        file.WriteLine(Program._awardCo_Curricular[Program._inc_opCoCurricular] + "," + Program._presentCo_Curricular[Program._inc_opCoCurricular]+","+ Program._remarksCo_Curricular[Program._inc_opCoCurricular])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opCoCurricular += 1 # end of function
    @staticmethod
    def _admin_14Achievments_2ExtraCurricular():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Achievements > Extra-Curricular ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Award/Certificate: ", end = '')
        Program._awardExtra_Curricular[Program._inc_opExtraCurricular] = input()
        print("Presented by: ", end = '')
        Program._presentExtra_Curricular[Program._inc_opExtraCurricular] = input()
        print("Remarks: ", end = '')
        Program._remarksExtra_Curricular[Program._inc_opExtraCurricular] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_14Achievments_2ExtraCurricular.txt", True)
        file.WriteLine(Program._awardExtra_Curricular[Program._inc_opExtraCurricular] + "," + Program._presentExtra_Curricular[Program._inc_opExtraCurricular] + "," + Program._remarksExtra_Curricular[Program._inc_opExtraCurricular])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opExtraCurricular += 1 # end of function
    @staticmethod
    def _admin_15ResultGrades():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Result Grades ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("GPA : ", end = '')
        Program._gpa[Program._inc_opResultGrades] = Program._float_Validaion("GPA : ", input())
        print("CGPA : ", end = '')
        Program._cgpa[Program._inc_opResultGrades] = Program._float_Validaion("CGPA : ", input())
        print("Remarks : ", end = '')
        Program._remarksResult[Program._inc_opResultGrades] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_15ResultGrades.txt", True)
        file.WriteLine(str(Program._gpa[Program._inc_opResultGrades]) + "," + str(Program._cgpa[Program._inc_opResultGrades]) + "," + Program._remarksResult[Program._inc_opResultGrades])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opResultGrades += 1 # end of function
    @staticmethod
    def _admin_16GoldenLines():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Golden Lines ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleGoldenLines[Program._inc_opGoldenLines] = input()
        print("Description:", end = '')
        Program._descriptionGoldenLines[Program._inc_opGoldenLines] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_16GoldenLines.txt", True)
        file.WriteLine(Program._titleGoldenLines[Program._inc_opGoldenLines] + "," + Program._descriptionGoldenLines[Program._inc_opGoldenLines])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opGoldenLines += 1 # end of function
    @staticmethod
    def _admin_17LifelongEvents():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Lifelong Events ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleLifelongEvents[Program._inc_opLifelongEvents] = input()
        print("Description:", end = '')
        Program._descriptionLifelongEvents[Program._inc_opLifelongEvents] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_17LifelongEvents.txt", True)
        file.WriteLine(Program._titleLifelongEvents[Program._inc_opLifelongEvents] + "," + Program._descriptionLifelongEvents[Program._inc_opLifelongEvents])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opLifelongEvents += 1 # end of function
    @staticmethod
    def _admin_18Notes():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Notes ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Title : ", end = '')
        Program._titleNotes[Program._inc_opNotes] = input()
        print("Description:", end = '')
        Program._descriptionNotes[Program._inc_opNotes] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_18Notes.txt", True)
        file.WriteLine(Program._titleNotes[Program._inc_opNotes] + "," + Program._descriptionNotes[Program._inc_opNotes])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opNotes += 1 # end of function
    @staticmethod
    def _admin_19CreateAgentAccount():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > Create agent account", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Enter first name : ", end = '')
        Program._firstname_Agent[Program._inc_opAgentAddUser] = input()
        print("Enter last name : ", end = '')
        Program._lastname_Agent[Program._inc_opAgentAddUser] = input()
        print("Enter username : ", end = '')
        Program._username_Agent[Program._inc_opAgentAddUser] = input()
        # bool agent_check = check_Existing_agent(username_Agent[inc_opAgentAddUser]); // to make username unique
        while Program._check_Existing_agent(Program._username_Agent[Program._inc_opAgentAddUser]) == True:
            print("Username is already exist try another once", end = '')
            print("\n", end = '')
            print("Enter username : ", end = '')
            Program._username_Agent[Program._inc_opAgentAddUser] = input()
        print("Enter password :", end = '')
        Program._password_Agent[Program._inc_opAgentAddUser] = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\agentSecurityFile.txt", True)
        file.WriteLine(Program._firstname_Agent[Program._inc_opAgentAddUser] + "," + Program._lastname_Agent[Program._inc_opAgentAddUser]+"," + Program._username_Agent[Program._inc_opAgentAddUser]+"," + Program._password_Agent[Program._inc_opAgentAddUser])
        file.Flush()
        file.Close()
        print("Data sucessfully saved")
        Program._inc_opAgentAddUser += 1 # end of function
    #****************** ADMIN EXPLANATION ******************
    @staticmethod
    def _admin_Menu():
        opAdmin = "" # admin option, store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   0. Profile", end = '')
        print("\n", end = '')
        print("   1. Wallet Status ", end = '')
        print("\n", end = '')
        print("   2. Expenses Report ", end = '')
        print("\n", end = '')
        print("   3. Academic Fee ", end = '')
        print("\n", end = '')
        print("   4. Hostel ", end = '')
        print("\n", end = '')
        print("   5. Helping Material", end = '')
        print("\n", end = '')
        print("   6. Recreational Expenses", end = '')
        print("\n", end = '')
        print("   7. Community Fund", end = '')
        print("\n", end = '')
        print("   8. Goals", end = '')
        print("\n", end = '')
        print("   9. Cell Phone", end = '')
        print("\n", end = '')
        print("   10.Books", end = '')
        print("\n", end = '')
        print("   11.Spiritual Food", end = '')
        print("\n", end = '')
        print("   12.Transport", end = '')
        print("\n", end = '')
        print("   13.Recreational Activities", end = '')
        print("\n", end = '')
        print("   14.Achievements", end = '')
        print("\n", end = '')
        print("   15.Result Grades", end = '')
        print("\n", end = '')
        print("   16.Golden Lines", end = '')
        print("\n", end = '')
        print("   17.Lifelong Events", end = '')
        print("\n", end = '')
        print("   18.Notes", end = '')
        print("\n", end = '')
        print("   19.Create agent account", end = '')
        print("\n", end = '')
        print("   20.Logout", end = '')
        print("\n", end = '')
        print("Choose option...", end = '')
        opAdmin = input()
        return opAdmin # end of admin menu
    @staticmethod
    def _admin_ExpensesReportMenu():
        opExpensesReport = None # expenses report option , store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Today", end = '')
        print("\n", end = '')
        print("   2. Month", end = '')
        print("\n", end = '')
        print("   3. Year", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opExpensesReport =input()
        return opExpensesReport # end of admin expenses report menu function
    @staticmethod
    def _admin_HostelMenu():
        opHostel = None # Hostel option, store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Meal", end = '')
        print("\n", end = '')
        print("   2. Monthly Meal Charges", end = '')
        print("\n", end = '')
        print("   3. Living Charges", end = '')
        print("\n", end = '')
        print("   4. Service  Charges", end = '')
        print("\n", end = '')
        print("   5. Renovation Charges", end = '')
        print("\n", end = '')
        print("   6. Laundry Charges", end = '')
        print("\n", end = '')
        print("   7. Barber Charges", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opHostel = input()
        return opHostel # end of admin hostel menu function
    @staticmethod
    def _admin_Hostel_MealMenu():
        opMeal = None # meal option, store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Breakfast Charges", end = '')
        print("\n", end = '')
        print("   2. Lunch Charges", end = '')
        print("\n", end = '')
        print("   3. Dinner Charges", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opMeal =input()
        return opMeal # end of admin, hostel option of meal menu function
    @staticmethod
    def _admin_HelpingMaterialMenu():
        opHelpingMaterial = None # helping material, store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Notes", end = '')
        print("\n", end = '')
        print("   2. Register", end = '')
        print("\n", end = '')
        print("   3. Stationary", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opHelpingMaterial =input()
        return opHelpingMaterial # end of admin,helping material menu function
    @staticmethod
    def _admin_RecreationalExpesesMenu():
        opRecreationalExpenses = None # recreational expenses option, store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Friend", end = '')
        print("\n", end = '')
        print("   2. Family", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opRecreationalExpenses = input()
        return opRecreationalExpenses # end of admin,recreational expenses menu function
    @staticmethod
    def _admin_CommunityFundMenu():
        opCommunityFund = None # community fund option, store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Class", end = '')
        print("\n", end = '')
        print("   2. Societies", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opCommunityFund = input()
        return opCommunityFund # end of admin,community fund function
    @staticmethod
    def _admin_GoalsMenu():
        opGoals = None # goals, store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Daily", end = '')
        print("\n", end = '')
        print("   2. Weekly", end = '')
        print("\n", end = '')
        print("   3. Monthly", end = '')
        print("\n", end = '')
        print("   4. Yearly", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opGoals = input()
        return opGoals # end of admin, goals menu function
    @staticmethod
    def _admin_CellPhoneMenu():
        opCellPhone = None # cell phone option,store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Call Package", end = '')
        print("\n", end = '')
        print("   2. Internet Package", end = '')
        print("\n", end = '')
        print("   3. Message Package", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opCellPhone = input()
        return opCellPhone # end of admin,cell phone menu function
    @staticmethod
    def _admin_BookMenu():
        opBook = None # book option of admin option
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Borrow", end = '')
        print("\n", end = '')
        print("   2. Purchase", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opBook = input()
        return opBook # end of admin, book menu function
    @staticmethod
    def _admin_SelfMotivationalMenu():
        opSelfMotivational = None # self motivational option of admin menu option,store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Five-time Prayer", end = '')
        print("\n", end = '')
        print("   2. Quran-e-Pak Recitation", end = '')
        print("\n", end = '')
        print("   3. Durood-e-Pak", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opSelfMotivational = input()
        return opSelfMotivational # end of admin,self motivational menu function
    @staticmethod
    def _admin_TransportMenu():
        opTransport = None # transport option of admin menu option
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Uber/Cream/Bykea", end = '')
        print("\n", end = '')
        print("   2. Bus", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opTransport = input()
        return opTransport # end of admin, transport menu funtion
    @staticmethod
    def _admin_RecerationActivitiesMenu():
        opRecreationalActivities = None # recreational activities option of admin menu option,store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Sporties", end = '')
        print("\n", end = '')
        print("   2. Societies", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opRecreationalActivities = input()
        return opRecreationalActivities # end of admin, recreational activities menu function
    @staticmethod
    def _admin_Achievemnets():
        opAchievements = None # achievments option of admin menu option,store user input
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   1. Co-Curricular", end = '')
        print("\n", end = '')
        print("   2. Extra- Curricular", end = '')
        print("\n", end = '')
        print("Press 0 to Go Back...", end = '')
        opAchievements = input()
        return opAchievements # end of admin,achievments menu function
    @staticmethod
    def _display_profile_admin():
        if Program._titleDailyGoals is None and Program._descriptionDailyGoals is None:
            print("Today goals data is not avilable", end = '')
            print("\n", end = '')
        else:
            if Program._descriptionDailyGoals is None:
                print("Today goals data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("Today Goals...", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opDailyGoals:
                    print("        Title:", end = '')
                    print(Program._titleDailyGoals[i], end = '')
                    print("\n", end = '')
                    print("Discription:", end = '')
                    print(Program._descriptionDailyGoals[i], end = '')
                    print("\n", end = '')
                    i += 1
        print("_____________________________________________________________________________________", end = '')
        print("\n", end = '')
        if Program._titleWeeklyGoals is None and Program._descriptionWeeklyGoals is None:
            print("Weekly goals data is not avilable", end = '')
            print("\n", end = '')
        else:
            if Program._descriptionWeeklyGoals is None:
                print("Weekly goals data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("Weekly Goals...", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opWeeklyGoals:
                    print("        Title:", end = '')
                    print(Program._titleWeeklyGoals[i], end = '')
                    print("\n", end = '')
                    print("Discription:", end = '')
                    print(Program._descriptionWeeklyGoals[i], end = '')
                    print("\n", end = '')
                    i += 1
        print("_____________________________________________________________________________________", end = '')
        print("\n", end = '')
        if Program._titleMonthlyGoals is None and Program._descriptionMonthlyGoals is None:
            print("Monthly goals data is not avilable", end = '')
            print("\n", end = '')
        else:
            if Program._descriptionMonthlyGoals is None:
                print("Monthly goals data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("Monthly Goals...", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opMonthlyGoals:
                    print("        Title:", end = '')
                    print(Program._titleMonthlyGoals[i], end = '')
                    print("\n", end = '')
                    print("Discription:", end = '')
                    print(Program._descriptionMonthlyGoals[i], end = '')
                    print("\n", end = '')
                    i += 1
        print("_____________________________________________________________________________________", end = '')
        print("\n", end = '')
        if Program._titleYearlyGoals is None and Program._descriptionYearlyGoals is None:
            print("Yearly goals data is not avilable", end = '')
            print("\n", end = '')
        else:
            if Program._descriptionYearlyGoals is None:
                print("Yearly goals data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("Yearly Goals...", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opYearlyGoals:
                    print("        Title:", end = '')
                    print(Program._titleYearlyGoals[i], end = '')
                    print("\n", end = '')
                    print("Discription:", end = '')
                    print(Program._descriptionYearlyGoals[i], end = '')
                    print("\n", end = '')
                    i += 1
        print("_____________________________________________________________________________________", end = '')
        print("\n", end = '') # end of profile admin option
    #****************** RECOMMENDATIOM ******************
    @staticmethod
    def _admin_Recommendation():
        if Program._addWalletMoney >= 0 and Program._addWalletMoney <= 200:
            print("You have low money...!", end = '')
            print("\n", end = '')
        i = 0
        while i < Program._inc_opResultGrades:
            if Program._gpa[i] < 2.0 or Program._cgpa[i] < 2.0:
                print("Work hard...You can do it!!!", end = '')
                print("\n", end = '')
            i += 1
    #********************* AGENT FUNCTIONS ************************
    @staticmethod
    def _agent_0Profile(agentindex):
        Program._header() # header function is called
        print("Main Menu > Agent > Menu > Profile", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("                                 __WELCOME ON BOARD__                             ", end = '')
        print("\n", end = '')
        print("First name : ", end = '')
        print(Program._firstname_Agent[agentindex], end = '')
        print("\t", end = '')
        print("Last name : ", end = '')
        print(Program._lastname_Agent[agentindex], end = '')
        print("\n", end = '') # end of functions
    @staticmethod
    def _agent_1Wallet():
        Program._header() # header function is called
        print("Main Menu > Agent > Menu > Wallet  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Current Balance:", end = '')
        print("\n", end = '')
        print("Add Balance: ", end = '')
        Program._addWalletMoney = Program._float_Validaion("Add Balance: ", input()) # wallet money will show in admin wallet status
        print("Remarks: ", end = '')
        Program._walletRemarks = input()
        # File Handling
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\agentWalletMoney.txt")
        file.WriteLine(str(Program._addWalletMoney)+","+ Program._walletRemarks)
        file.Flush()
        file.Close()
        print("Data sucessfully saved") # end of functions
    @staticmethod
    def _agent_2AcademicReport():
        Program._header() # header function is called
        print("Main Menu > Agent > Menu > Academic Report  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        if Program._gpa[0] == 0 and Program._cgpa[0] == 0:
            print("Data is not avilable", end = '')
            print("\n", end = '')
        else:
            print("Sr.No \tGPA \tCGPA \tRemarks", end = '')
            print("\n", end = '')
            i = 0
            while i < Program._inc_opResultGrades:
                print(i + 1, end = '')
                print("\t", end = '')
                print(Program._gpa[i], end = '')
                print("\t", end = '')
                print(Program._cgpa[i], end = '')
                print("\t", end = '')
                print(Program._remarksResult[i], end = '')
                print("\n", end = '')
                i += 1 # end of functions
    @staticmethod
    def _agent_3ExpensesReport():
        Program._header() # header function is called
        print("Main Menu > Admin > Menu > ExpensesReport > Monthly", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Monthly Report :- ", end = '')
        print("\n", end = '')
        print("Personal................: ", end = '')
        print(Program._personal_Expenses(), end = '')
        print("\n", end = '')
        print("Hostel..................: ", end = '')
        print(Program._hostel_Expenses(), end = '')
        print("\n", end = '')
        print("Helping Material........: ", end = '')
        print(Program._helpingmaterial_Expenses(), end = '')
        print("\n", end = '')
        print("Recreational Expenses...: ", end = '')
        print(Program._recreational_Expenses(), end = '')
        print("\n", end = '')
        print("Fund....................: ", end = '')
        print(Program._communityfund_Expenses(), end = '')
        print("\n", end = '')
        print("Cell Phone..............: ", end = '')
        print(Program._cellphone_Expenses(), end = '')
        print("\n", end = '')
        print("Transport...............: ", end = '')
        print(Program._transport_Expenses(), end = '')
        print("\n", end = '')
        print("                   Total: ", end = '')
        print(Program._total_Expenses(), end = '')
        print("\n", end = '') # end of functions
    @staticmethod
    def _agent_4MealReport():
        Program._header() # header function is called
        print("Main Menu > Agent > Menu >  Meal Report  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        if Program._menuBreakfast is None and Program._menuLunch is None and Program._menuDinner is None:
            print("Data is not avilable", end = '')
            print("\n", end = '')
        else:
            if Program._menuBreakfast is None:
                print("Breakfast data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("Sr.No \tBreakfast Menu \tRemarks \tCharges", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._increment_opMealBreakfast:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._menuBreakfast[i], end = '')
                    print("\t\t", end = '')
                    print(Program._remarksBreakfast[i], end = '')
                    print("\t\t", end = '')
                    print(Program._chargesBreakfast[i], end = '')
                    print("\n", end = '')
                    i += 1
            if Program._menuLunch is None:
                print("__________________________", end = '')
                print("\n", end = '')
                print("Lunch data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("________________________________________________", end = '')
                print("\n", end = '')
                print("Sr.No \tLunch Menu \tRemarks \tCharges", end = '')
                print("\n", end = '')

                i = 0
                while i < Program._increment_opMealLunch:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._menuLunch[i], end = '')
                    print("\t\t", end = '')
                    print(Program._remarksLunch[i], end = '')
                    print("\t\t", end = '')
                    print(Program._chargesLunch[i], end = '')
                    print("\n", end = '')
                    i += 1
            if Program._menuDinner is None:
                print("____________________________", end = '')
                print("\n", end = '')
                print("Dinner data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("________________________________________________", end = '')
                print("\n", end = '')
                print("Sr.No \tDinner Menu \tRemarks \tCharges", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._increment_opMealDinner:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._menuDinner[i], end = '')
                    print("\t\t", end = '')
                    print(Program._remarksDinner[i], end = '')
                    print("\t\t", end = '')
                    print(Program._chargesDinner[i], end = '')
                    print("\n", end = '')
                    i += 1
        print("________________________________________________", end = '')
        print("\n", end = '') # end of functions
    @staticmethod
    def _agent_5SpiritualTracker():
        Program._header() # header function is called
        print("Main Menu > Agent > Menu > Spiritual Tracker  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        print("Summary...", end = '')
        print("\n", end = '')
        if Program._five_time_Prayer is None and Program._Quran_e_Pak is None and Program._Durood_e_Pak is None:
            print("Data is not avilable", end = '')
            print("\n", end = '')
        else:
            if Program._five_time_Prayer is None:
                print("Salah tracker data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("Sr.No \tSalah Tracker...", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opFiveTimePrayer:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._five_time_Prayer[i], end = '')
                    print("\n", end = '')
                    i += 1
            if Program._Quran_e_Pak is None:
                print("Quran-e-Pak tracker data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("__________________________________", end = '')
                print("\n", end = '')
                print("Sr.No \tQuran-e-Pak Tracker...", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opQuran_e_Pak:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._Quran_e_Pak[i], end = '')
                    print("\n", end = '')
                    i += 1
            if Program._Durood_e_Pak is None:
                print("Durood-e-Pak tracker data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("__________________________________", end = '')
                print("\n", end = '')
                print("Sr.No \tDurood-e-Pak Tracker...", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opDurood_e_Pak:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._Durood_e_Pak[i], end = '')
                    print("\n", end = '')
                    i += 1
        print("__________________________________", end = '')
        print("\n", end = '') # end of functions
    @staticmethod
    def _agent_6AachieventsReport():
        Program._header() # header function is called
        print("Main Menu > Agent > Menu > Achievments Report  ", end = '')
        print("\n", end = '')
        print("__________ . __________ . __________ . _________ . __________ . _________ . _________", end = '')
        print("\n", end = '')
        if Program._awardCo_Curricular is None and Program._awardExtra_Curricular is None and Program._remarksCo_Curricular is None and Program._remarksExtra_Curricular is None:
            print("Data is not avilable", end = '')
            print("\n", end = '')
        else:
            if Program._awardCo_Curricular is None:
                print("Co-curricular achievements data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("Co-Curricular Achievements...", end = '')
                print("\n", end = '')
                print("Sr.No \tAward/Certificate \tPresented by \tRemarks ", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opCoCurricular:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._awardCo_Curricular[i], end = '')
                    print("\t\t\t", end = '')
                    print(Program._presentCo_Curricular[i], end = '')
                    print("\t\t", end = '')
                    print(Program._remarksCo_Curricular[i], end = '')
                    print("\n", end = '')
                    i += 1
            if Program._awardExtra_Curricular is None:
                print("Extra-curricular achievements data is not avilable", end = '')
                print("\n", end = '')
            else:
                print("________________________________________________", end = '')
                print("\n", end = '')
                print("Sr.No \tAward/Certificate \tPresented by \tRemarks ", end = '')
                print("\n", end = '')
                i = 0
                while i < Program._inc_opExtraCurricular:
                    print(i + 1, end = '')
                    print("\t", end = '')
                    print(Program._awardExtra_Curricular[i], end = '')
                    print("\t\t\t", end = '')
                    print(Program._presentExtra_Curricular[i], end = '')
                    print("\t\t", end = '')
                    print(Program._remarksExtra_Curricular[i], end = '')
                    print("\n", end = '')
                    i += 1
        print("________________________________________________", end = '')
        print("\n", end = '') # end of functions
    #****************** AGENT FUNCTION EXPLANATION ******************
    @staticmethod
    def _agent_Menu():
        opAgent = "" # option Agent
        print("Choose Option", end = '')
        print("\n", end = '')
        print("   0. Profile", end = '')
        print("\n", end = '')
        print("   1. Wallet", end = '')
        print("\n", end = '')
        print("   2. Academic Report", end = '')
        print("\n", end = '')
        print("   3. Expenese Report", end = '')
        print("\n", end = '')
        print("   4. Meal Report", end = '')
        print("\n", end = '')
        print("   5. Spiritual Tracker", end = '')
        print("\n", end = '')
        print("   6. Aachievments Report", end = '')
        print("\n", end = '')
        print("   7. Logout", end = '')
        print("\n", end = '')
        print("Choose option...", end = '')
        opAgent = input()
        return opAgent # end of agent menu function
    #********************* ADMIN & AGENT FUNCTION ************************
    @staticmethod
    def _personal_Expenses():
        personalExpenses = 0.0 # sum of purchase book + academic fee
        purchasebook = 0.0
        academicfee = 0.0
        i = 0
        while i < Program._inc_opBookPurchase:
            purchasebook += Program._amountPurchaseBook[i]
            i += 1
        i = 0
        while i < Program._increment_opAcademicFee:
            academicfee += Program._amountacademic[i]
            i += 1
        personalExpenses = purchasebook + (academicfee / 6)
        return int(personalExpenses) # end of personal expenses function
    @staticmethod
    def _hostel_Expenses():
        hostelExpenses = 0.0 # sum of breakfast + lunch + dinner + mealMonthly + livingMonthly + serviceMonthly + renovationMonthly + laundryMonthly + barbermonthly
        breakfast = 0.0
        lunch = 0.0
        dinner = 0.0
        mealMonthly = 0.0
        livingMonthly = 0.0
        serviceMonthly = 0.0
        renovationMonthly = 0.0
        laundryMonthly = 0.0
        barbermonthly = 0.0
        i = 0
        while i < Program._increment_opMealBreakfast:
            breakfast += Program._chargesBreakfast[i]
            i += 1
        i = 0
        while i < Program._increment_opMealLunch:
            lunch += Program._chargesLunch[i]
            i += 1
        i = 0
        while i < Program._increment_opMealDinner:
            dinner += Program._chargesDinner[i]
            i += 1
        i = 0
        while i < Program._increment_opMealCharges:
            mealMonthly += Program._chargesMealMonthly[i]
            i += 1
        i = 0
        while i < Program._inc_opLivingCharges:
            livingMonthly += Program._chargesLivingExpenses[i]
            i += 1
        i = 0
        while i < Program._inc_opServiceCharges:
            serviceMonthly += Program._chargesServiceMonthly[i]
            i += 1
        i = 0
        while i < Program._inc_opRenovationCharges:
            renovationMonthly += Program._chargesRenovationMonthly[i]
            i += 1
        i = 0
        while i < Program._inc_opLaundryCharges:
            laundryMonthly += Program._chargesLaundryMonthly[i]
            i += 1
        i = 0
        while i < Program._inc_opBarberCharges:
            barbermonthly += Program._chargesBarberMonthly[i]
            i += 1
        hostelExpenses = breakfast + lunch + dinner + mealMonthly + livingMonthly + serviceMonthly + renovationMonthly + laundryMonthly + barbermonthly
        return int(hostelExpenses) # end of hostel expenses function
    @staticmethod
    def _helpingmaterial_Expenses():
        helpingmaterialExpenses = 0.0 # sum of notes + register_ + stationary
        notes = 0.0
        register_ = 0.0
        stationary = 0.0
        i = 0
        while i < Program._inc_opNotesHelpingMaterial:
            notes = Program._chargesNotesMonthly[i]
            i += 1
        i = 0
        while i < Program._inc_opRegisterHelpingMaterial:
            register_ = Program._chargesRegisterMonthly[i]
            i += 1
        i = 0
        while i < Program._inc_opStationaryHelpingMaterial:
            stationary = Program._chargesStationaryMonthly[i]
            i += 1
        helpingmaterialExpenses = notes + register_ + stationary
        return int(helpingmaterialExpenses) # end of helping material function
    @staticmethod
    def _recreational_Expenses():
        recreationalExpenses = 0.0 # sum of friends + family
        friends = 0.0
        family = 0.0
        i = 0
        while i < Program._inc_opFriendsRecreationalExpenses:
            friends = Program._chargesFriendsRecreationalExpenses[i]
            i += 1
        i = 0
        while i < Program._inc_opFamilyRecreationalExpenses:
            family = Program._chargesFamilyRecreationalExpenses[i]
            i += 1
        recreationalExpenses = friends + family
        return int(recreationalExpenses) # end of recreational expenses function
    @staticmethod
    def _communityfund_Expenses():
        communityfundExpenses = 0.0 # sum of classes + socities
        classes = 0.0
        socities = 0.0
        i = 0
        while i < Program._inc_opClassCommunityFund:
            classes = Program._chargesClassCommunityFund[i]
            i += 1
        i = 0
        while i < Program._inc_opSocietiesCommunityFund:
            socities = Program._chargesSocietiesCommunityFund[i]
            i += 1
        communityfundExpenses = classes + socities
        return int(communityfundExpenses) # end of community fund expenses function
    @staticmethod
    def _cellphone_Expenses():
        cellphoneExpenses = 0.0 # sum of call + internet + message
        call = 0.0
        internet = 0.0
        message = 0.0
        i = 0
        while i < Program._inc_opCall_CellPhone:
            call = Program._amountCallPakage[i]
            i += 1
        i = 0
        while i < Program._inc_opInternet_CellPhone:
            internet = Program._amountInternetPakage[i]
            i += 1
        i = 0
        while i < Program._inc_opMessage_CellPhone:
            message = Program._amountMessagePakage[i]
            i += 1
        cellphoneExpenses = call + internet + message
        return int(cellphoneExpenses) # end of cell phone expenses function
    @staticmethod
    def _transport_Expenses():
        transportExpenses = 0.0 # sum of uber + bus
        uber = 0.0
        bus = 0.0
        i = 0
        while i < Program._inc_opUberTransport:
            uber = Program._amountUber[i]
            i += 1
        i = 0
        while i < Program._inc_opBusTransport:
            bus = Program._amountBus[i]
            i += 1
        transportExpenses = uber + bus
        return int(transportExpenses) # end of transport expenses function
    @staticmethod
    def _total_Expenses():

        totalExpenses = int(0.0) # sum of  personalExpenses + hostelExpenses + helpingmaterialExpenses + recreationalExpenses + communityfundExpenses + cellphoneExpenses + transportExpenses
        totalExpenses = Program._personal_Expenses() + Program._hostel_Expenses() + Program._helpingmaterial_Expenses() + Program._recreational_Expenses() + Program._communityfund_Expenses() + Program._cellphone_Expenses() + Program._transport_Expenses()
        #totalExpenses = totalExpenses - addWalletMoney
        return totalExpenses # end of total expneses function
    #********************* SORTING FUNCTION ************************
    @staticmethod
    def _sort_academicFee():
        i = 0
        while i < Program._increment_opAcademicFee:
            j = i + 1
            while j < Program._increment_opAcademicFee:
                if Program._amountacademic[j] > Program._amountacademic[i]:
                    temp = Program._amountacademic[i]
                    Program._amountacademic[i] = Program._amountacademic[j]
                    Program._amountacademic[j] = temp
                    # semester type sort
                    temp_type = Program._semesterType[i]
                    Program._semesterType[i] = Program._semesterType[j]
                    Program._semesterType[j] = temp_type
                    # challan no sort
                    temp_type = Program._challanNo[i]
                    Program._challanNo[i] = Program._challanNo[j]
                    Program._challanNo[j] = temp_type
                    # date sort
                    temp_type = Program._date[i]
                    Program._date[i] = Program._date[j]
                    Program._date[j] = temp_type
                    # remarks sort
                    temp_type = Program._remarks[i]
                    Program._remarks[i] = Program._remarks[j]
                    Program._remarks[j] = temp_type
                j += 1
            i += 1 # end of academic fee function
    @staticmethod
    def _display_academicFee():
        Program._sort_academicFee()
        print("Sr.No \tSemester type \tChallan no \tDate \tAmount \tRemarks", end = '')
        print("\n", end = '')
        i = 0
        while i < Program._increment_opAcademicFee:
            print(i + 1, end = '')
            print("\t", end = '')
            print(Program._semesterType[i], end = '')
            print("\t\t", end = '')
            print(Program._challanNo[i], end = '')
            print("\t\t", end = '')
            print(Program._date[i], end = '')
            print("\t", end = '')
            print(Program._amountacademic[i], end = '')
            print("\t", end = '')
            print(Program._remarks[i], end = '')
            print("\n", end = '')
            i += 1 # end of display academic fee function
    @staticmethod
    def _sort_breakfast():
        i = 0
        while i < Program._increment_opMealBreakfast:
            j = i + 1
            while j < Program._increment_opMealBreakfast:
                if Program._chargesBreakfast[j] > Program._chargesBreakfast[i]:
                    temp = Program._chargesBreakfast[i]
                    Program._chargesBreakfast[i] = Program._chargesBreakfast[j]
                    Program._chargesBreakfast[j] = temp
                    #  menu sort
                    temp_st = Program._menuBreakfast[i]
                    Program._menuBreakfast[i] = Program._menuBreakfast[j]
                    Program._menuBreakfast[j] = temp_st
                    # remarks no sort
                    temp_st = Program._remarksBreakfast[i]
                    Program._remarksBreakfast[i] = Program._remarksBreakfast[j]
                    Program._remarksBreakfast[j] = temp_st
                j += 1
            i += 1 # end of sorting breakfast function
    @staticmethod
    def _display_breakfast():
        Program._sort_breakfast()
        print("Sr.No \tBreakfast menu \tCharges\tRemarks", end = '')
        print("\n", end = '')
        i = 0
        while i < Program._increment_opMealBreakfast:
            print(i + 1, end = '')
            print("\t", end = '')
            print(Program._menuBreakfast[i], end = '')
            print("\t\t", end = '')
            print(Program._chargesBreakfast[i], end = '')
            print("\t", end = '')
            print(Program._remarksBreakfast[i], end = '')
            print("\n", end = '')
            i += 1 # end of display breakfast function
    @staticmethod
    def _sort_lunch():
        i = 0
        while i < Program._increment_opMealLunch:
            j = i + 1
            while j < Program._increment_opMealLunch:
                if Program._chargesLunch[j] > Program._chargesLunch[i]:
                    temp = Program._chargesLunch[i]
                    Program._chargesLunch[i] = Program._chargesLunch[j]
                    Program._chargesLunch[j] = temp
                    #  menu sort
                    temp_st = Program._menuLunch[i]
                    Program._menuLunch[i] = Program._menuLunch[j]
                    Program._menuLunch[j] = temp_st
                    # remarks no sort
                    temp_st = Program._remarksLunch[i]
                    Program._remarksLunch[i] = Program._remarksLunch[j]
                    Program._remarksLunch[j] = temp_st
                j += 1
            i += 1 # end of sort of lunch function
    @staticmethod
    def _display_lunch():
        Program._sort_lunch()
        print("Sr.No \tLunch menu \tCharges\tRemarks", end = '')
        print("\n", end = '')
        i = 0
        while i < Program._increment_opMealLunch:
            print(i + 1, end = '')
            print("\t", end = '')
            print(Program._menuLunch[i], end = '')
            print("\t\t", end = '')
            print(Program._chargesLunch[i], end = '')
            print("\t", end = '')
            print(Program._remarksLunch[i], end = '')
            print("\n", end = '')
            i += 1 # end of display function
    @staticmethod
    def _sort_dinner():
        i = 0
        while i < Program._increment_opMealDinner:
            j = i + 1
            while j < Program._increment_opMealDinner:
                if Program._chargesDinner[j] > Program._chargesDinner[i]:
                    temp = Program._chargesDinner[i]
                    Program._chargesDinner[i] = Program._chargesDinner[j]
                    Program._chargesDinner[j] = temp
                    #  menu sort
                    temp_st = Program._menuDinner[i]
                    Program._menuDinner[i] = Program._menuDinner[j]
                    Program._menuDinner[j] = temp_st
                    # remarks no sort
                    temp_st = Program._remarksDinner[i]
                    Program._remarksDinner[i] = Program._remarksDinner[j]
                    Program._remarksDinner[j] = temp_st
                j += 1
            i += 1 # end of sort dinner function
    @staticmethod
    def _display_dinner():
        Program._sort_dinner()
        print("Sr.No \tDinner menu \tCharges\tRemarks", end = '')
        print("\n", end = '')
        i = 0
        while i < Program._increment_opMealDinner:
            print(i + 1, end = '')
            print("\t", end = '')
            print(Program._menuDinner[i], end = '')
            print("\t\t", end = '')
            print(Program._chargesDinner[i], end = '')
            print("\t", end = '')
            print(Program._remarksDinner[i], end = '')
            print("\n", end = '')
            i += 1 # display dinner function
    # ****************** FILE HANDLING ******************
    @staticmethod
    def _seperateField(record, field):
        comma = 1
        item = ""
        x = 0
        while x < len(record):
            if record[x] == ',':
                comma += 1
            elif comma == field:
                item = item + record[x]
            x += 1
        return item # end of function
    @staticmethod
    def read_adminSecurityFile():
        # File Handling
        file = open("adminSecurityFile.txt",'r')
        record = file.read().split("\n")
        i = 0
        for line in record:

            Program._firstname[i] = Program._seperateField(record, 1) # username field
            Program._lastname[i] = Program._seperateField(record, 2) # password field
            Program._username[i] = Program._seperateField(record, 3) # username field
            Program._password[i] = Program._seperateField(record, 4) # password field
            i += 1
        file.Close() # end of function
    @staticmethod
    def read_agentSecurityFile():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\agentSecurityFile.txt")
        record = file.read().split("\n")
        i = 0
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._firstname_Agent[i] = Program._seperateField(record, 1) # create an account store firstname
            Program._lastname_Agent[i] = Program._seperateField(record, 2) # create an account store lastname
            Program._username_Agent[i] = Program._seperateField(record, 3) # username field
            Program._password_Agent[i] = Program._seperateField(record, 4) # password field
            i += 1
        file.Close() # end of function
    @staticmethod
    def read_agentWalletMoney():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\agentWalletMoney.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._addWalletMoney = float.Parse((Program._seperateField(record, 1)))
            Program._walletRemarks = Program._seperateField(record, 2)
        file.Close() # end of function
    @staticmethod
    def read_admin3AcadmicFee():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin3AcadmicFee.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._semesterType[Program._increment_opAcademicFee] = Program._seperateField(record, 1)
            Program._challanNo[Program._increment_opAcademicFee] = Program._seperateField(record, 2)
            Program._amountacademic[Program._increment_opAcademicFee] = float.Parse((Program._seperateField(record, 3)))
            Program._date[Program._increment_opAcademicFee] = Program._seperateField(record, 4)
            Program._remarks[Program._increment_opAcademicFee] = Program._seperateField(record, 5)
            Program._increment_opAcademicFee += 1
        file.Close() # end of function
    @staticmethod
    def read_admin_4Hostel_1Meal_1Breakfast():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_1Meal_1Breakfast.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._menuBreakfast[Program._increment_opMealBreakfast] = Program._seperateField(record, 1)
            Program._chargesBreakfast[Program._increment_opMealBreakfast] =float.Parse((Program._seperateField(record, 2)))
            Program._remarksBreakfast[Program._increment_opMealBreakfast] = Program._seperateField(record, 3)
            Program._increment_opMealBreakfast += 1
        file.Close() # end of function
    @staticmethod
    def read_admin_4Hostel_1Meal_2Lunch():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_1Meal_1Breakfast.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._menuLunch[Program._increment_opMealLunch] = Program._seperateField(record, 1)
            Program._chargesLunch[Program._increment_opMealLunch] = float.Parse((Program._seperateField(record, 2)))
            Program._remarksLunch[Program._increment_opMealLunch] = Program._seperateField(record, 3)
            Program._increment_opMealLunch += 1
        file.Close() # end of function
    @staticmethod
    def read_admin_4Hostel_1Meal_3Dinner():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_1Meal_3Dinner.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._menuDinner[Program._increment_opMealDinner] = Program._seperateField(record, 1)
            Program._chargesDinner[Program._increment_opMealDinner] =float.Parse((Program._seperateField(record, 2)))
            Program._remarksDinner[Program._increment_opMealDinner] = Program._seperateField(record, 3)
            Program._increment_opMealDinner += 1
        file.Close() # end of function
    @staticmethod
    def read_admin_4Hostel_2MealChargesMonthly():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_2MealChargesMonthly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._monthlyMealExpenses[Program._increment_opMealCharges] = Program._seperateField(record, 1)
            Program._chargesMealMonthly[Program._increment_opMealCharges] = float.Parse((Program._seperateField(record, 2)))
            Program._remarksMealExpenses[Program._increment_opMealCharges] = Program._seperateField(record, 3)
            Program._increment_opMealCharges += 1
        file.Close() # end of function
    @staticmethod
    def read_admin_4Hostel_3LivingChargesMonthly():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_3LivingChargesMonthly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._monthLivingExpenses[Program._inc_opLivingCharges] = Program._seperateField(record, 1)
            Program._chargesLivingExpenses[Program._inc_opLivingCharges] = float.Parse((Program._seperateField(record, 2)))
            Program._remarksLivingExpenses[Program._inc_opLivingCharges] = Program._seperateField(record, 3)
            Program._inc_opLivingCharges += 1
        file.Close()
    @staticmethod
    def read_admin_4Hostel_4ServiceChargesMonthly():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_4ServiceChargesMonthly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._monthServiceExpenses[Program._inc_opServiceCharges] = Program._seperateField(record, 1)
            Program._chargesServiceMonthly[Program._inc_opServiceCharges] =float.Parse((Program._seperateField(record, 2)))
            Program._remarksServiceExpenses[Program._inc_opServiceCharges] = Program._seperateField(record, 3)
            Program._inc_opServiceCharges += 1
        file.Close()
    @staticmethod
    def read_admin_4Hostel_5RenovationChargesMonthly():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_5RenovationChargesMonthly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesRenovationMonthly[Program._inc_opRenovationCharges] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksRenovationExpenses[Program._inc_opRenovationCharges] = Program._seperateField(record, 2)
            Program._inc_opRenovationCharges += 1
        file.Close()
    @staticmethod
    def read_admin_4Hostel_6LaundryChargesMonthly():
        file = open("admin_4Hostel_6LaundryChargesMonthly.txt",'r')
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesLaundryMonthly[Program._inc_opLaundryCharges] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksLaundryExpenses[Program._inc_opLaundryCharges] = Program._seperateField(record, 2)
            Program._inc_opLaundryCharges += 1
        file.Close()
    @staticmethod
    def read_admin_4Hostel_7BarberChargesMonthly():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_4Hostel_7BarberChargesMonthly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesBarberMonthly[Program._inc_opBarberCharges] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksBarberExpenses[Program._inc_opBarberCharges] = Program._seperateField(record, 2)
            Program._inc_opBarberCharges += 1
        file.Close()
    @staticmethod
    def read_admin_5HelpingMaterial_1Notes():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_5HelpingMaterial_1Notes.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesNotesMonthly[Program._inc_opNotesHelpingMaterial] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksNotesExpenses[Program._inc_opNotesHelpingMaterial] = Program._seperateField(record, 2)
            Program._inc_opNotesHelpingMaterial += 1
        file.Close()
    @staticmethod
    def read_admin_5HelpingMaterial_2Register():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_5HelpingMaterial_2Register.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesRegisterMonthly[Program._inc_opRegisterHelpingMaterial] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksRegisterExpenses[Program._inc_opRegisterHelpingMaterial] = Program._seperateField(record, 2)
            Program._inc_opRegisterHelpingMaterial += 1
        file.Close()
    @staticmethod
    def read_admin_5HelpingMaterial_3Stationary():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_5HelpingMaterial_3Stationary.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesStationaryMonthly[Program._inc_opStationaryHelpingMaterial] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksStationaryExpenses[Program._inc_opStationaryHelpingMaterial] = Program._seperateField(record, 2)
            Program._inc_opStationaryHelpingMaterial += 1
        file.Close()
    @staticmethod
    def read_admin_6RecreationalExpenses_1Friends():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_6RecreationalExpenses_1Friends.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesFriendsRecreationalExpenses[Program._inc_opFriendsRecreationalExpenses] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksFriendsRecreationalExpenses[Program._inc_opFriendsRecreationalExpenses] = Program._seperateField(record, 2)
            Program._inc_opFriendsRecreationalExpenses += 1
        file.Close()
    @staticmethod
    def read_admin_6RecreationalExpenses_2Family():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_6RecreationalExpenses_2Family.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._chargesFamilyRecreationalExpenses[Program._inc_opFamilyRecreationalExpenses] = float.Parse((Program._seperateField(record, 1)))
            Program._remarksFamilyRecreationalExpenses[Program._inc_opFamilyRecreationalExpenses] = Program._seperateField(record, 2)
            Program._inc_opFamilyRecreationalExpenses += 1
        file.Close()
    @staticmethod
    def read_admin_7CommunityFund_1Class():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_7CommunityFund_1Class.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._remarksClassCommunityFund[Program._inc_opClassCommunityFund] = Program._seperateField(record, 1)
            Program._chargesClassCommunityFund[Program._inc_opClassCommunityFund] = float.Parse((Program._seperateField(record, 2)))
            Program._inc_opClassCommunityFund += 1
        file.Close()
    @staticmethod
    def read_admin_7CommunityFund_2Societies():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_7CommunityFund_2Societies.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._remarksSocietiesCommunityFund[Program._inc_opSocietiesCommunityFund] = Program._seperateField(record, 1)
            Program._chargesSocietiesCommunityFund[Program._inc_opSocietiesCommunityFund] = float.Parse((Program._seperateField(record, 2)))
            Program._inc_opSocietiesCommunityFund += 1
        file.Close()
    @staticmethod
    def read_admin_8Goals_1Daily():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_1Daily.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleDailyGoals[Program._inc_opDailyGoals] = Program._seperateField(record, 1)
            Program._descriptionDailyGoals[Program._inc_opDailyGoals] = Program._seperateField(record, 2)
            Program._inc_opDailyGoals += 1
        file.Close()
    @staticmethod
    def read_admin_8Goals_2Weekly():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_2Weekly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleWeeklyGoals[Program._inc_opWeeklyGoals] = Program._seperateField(record, 1)
            Program._descriptionWeeklyGoals[Program._inc_opWeeklyGoals] = Program._seperateField(record, 2)
            Program._inc_opWeeklyGoals += 1
        file.Close()
    @staticmethod
    def read_admin_8Goals_3Monthly():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_3Monthly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleMonthlyGoals[Program._inc_opMonthlyGoals] = Program._seperateField(record, 1)
            Program._descriptionMonthlyGoals[Program._inc_opMonthlyGoals] = Program._seperateField(record, 2)
            Program._inc_opMonthlyGoals += 1
        file.Close()
    @staticmethod
    def read_admin_8Goals_4Yearly():

        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_8Goals_4Yearly.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleYearlyGoals[Program._inc_opYearlyGoals] = Program._seperateField(record, 1)
            Program._descriptionYearlyGoals[Program._inc_opYearlyGoals] = Program._seperateField(record, 2)
            Program._inc_opYearlyGoals += 1
        file.Close()
    @staticmethod
    def read_admin_9CellPhone_1Call():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_9CellPhone_1Call.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._nameCallPakage[Program._inc_opCall_CellPhone] = Program._seperateField(record, 1)
            Program._amountCallPakage[Program._inc_opCall_CellPhone] = float.Parse((Program._seperateField(record, 2)))
            Program._durationCallPakage[Program._inc_opCall_CellPhone] = Program._seperateField(record, 3)
            Program._inc_opCall_CellPhone += 1
        file.Close()
    @staticmethod
    def read_admin_9CellPhone_2Internet():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_9CellPhone_2Internet.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._nameInternetPakage[Program._inc_opInternet_CellPhone] = Program._seperateField(record, 1)
            Program._amountInternetPakage[Program._inc_opInternet_CellPhone] = float.Parse((Program._seperateField(record, 2)))
            Program._durationInternetPakage[Program._inc_opInternet_CellPhone] = Program._seperateField(record, 3)
            Program._inc_opInternet_CellPhone += 1
        file.Close()
    @staticmethod
    def read_admin_9CellPhone_3Message():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_9CellPhone_3Message.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._nameMessagePakage[Program._inc_opMessage_CellPhone] = Program._seperateField(record, 1)
            Program._amountMessagePakage[Program._inc_opMessage_CellPhone] = float.Parse((Program._seperateField(record, 2)))
            Program._durationMessagePakage[Program._inc_opMessage_CellPhone] = Program._seperateField(record, 3)
            Program._inc_opMessage_CellPhone += 1
        file.Close()
    @staticmethod
    def read_admin_10Book_1Borrow():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_10Book_1Borrow.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleBorrowBook[Program._inc_opBookBorrow] = Program._seperateField(record, 1)
            Program._authorBorrowBook[Program._inc_opBookBorrow] = Program._seperateField(record, 2)
            Program._friendnameBorrowBook[Program._inc_opBookBorrow] = Program._seperateField(record, 3)
            Program._remarksBorrowBook[Program._inc_opBookBorrow] = Program._seperateField(record, 4)
            Program._inc_opBookBorrow += 1
        file.Close()
    @staticmethod
    def read_admin_10Book_2Purchase():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_10Book_2Purchase.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titlePurchaseBook[Program._inc_opBookPurchase] = Program._seperateField(record, 1)
            Program._authorPurchaseBook[Program._inc_opBookPurchase] = Program._seperateField(record, 2)
            Program._amountPurchaseBook[Program._inc_opBookPurchase] = float.Parse((Program._seperateField(record, 3)))
            Program._remarksPurchaseBook[Program._inc_opBookPurchase] = Program._seperateField(record, 4)
            Program._inc_opBookPurchase += 1
        file.Close()
    @staticmethod
    def read_admin_11SelfMotivational_1FiveTimePrayer():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_11SelfMotivational_1FiveTimePrayer.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._five_time_Prayer[Program._inc_opFiveTimePrayer] = Program._seperateField(record, 1)
            Program._inc_opFiveTimePrayer += 1
        file.Close()
    @staticmethod
    def read_admin_11SelfMotivational_2Quran_e_Pak():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_11SelfMotivational_2Quran_e_Pak.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._Quran_e_Pak[Program._inc_opQuran_e_Pak] = Program._seperateField(record, 1)
            Program._inc_opQuran_e_Pak += 1
        file.Close()
    @staticmethod
    def read_admin_11SelfMotivational_3Durood_e_Pak():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_11SelfMotivational_3Durood_e_Pak.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._Durood_e_Pak[Program._inc_opDurood_e_Pak] = Program._seperateField(record, 1)
            Program._inc_opDurood_e_Pak += 1
        file.Close()
    @staticmethod
    def read_admin_12Transport_1Uber():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_12Transport_1Uber.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._locationFromUber[Program._inc_opUberTransport] = Program._seperateField(record, 1)
            Program._locationToUber[Program._inc_opUberTransport] = Program._seperateField(record, 2)
            Program._amountUber[Program._inc_opUberTransport] = float.Parse((Program._seperateField(record, 3)))
            Program._purposeUber[Program._inc_opUberTransport] = Program._seperateField(record, 4)
            Program._inc_opUberTransport += 1
        file.Close()
    @staticmethod
    def read_admin_12Transport_2Bus():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_12Transport_2Bus.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._locationFromBus[Program._inc_opBusTransport] = Program._seperateField(record, 1)
            Program._locationToBus[Program._inc_opBusTransport] = Program._seperateField(record, 2)
            Program._amountBus[Program._inc_opBusTransport] = float.Parse((Program._seperateField(record, 3)))
            Program._purposeBus[Program._inc_opBusTransport] = Program._seperateField(record, 4)
            Program._inc_opBusTransport += 1
        file.Close()
    @staticmethod
    def read_admin_13RecreationalActivities_1Sporties():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_13RecreationalActivities_1Sporties.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._minutiesSporties[Program._inc_opSportiesActivities] = float.Parse((Program._seperateField(record, 1)))
            Program._inc_opSportiesActivities += 1
        file.Close()
    @staticmethod
    def read_admin_13RecreationalActivities_2Socities():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_13RecreationalActivities_2Socities.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._minutiesSocieties[Program._inc_opSocietiesActivities] = float.Parse((Program._seperateField(record, 1)))
            Program._purposeSocieties[Program._inc_opSocietiesActivities] = Program._seperateField(record, 2)
            Program._inc_opSocietiesActivities += 1
        file.Close()
    @staticmethod
    def read_admin_14Achievments_1CoCurricular():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_14Achievments_1CoCurricular.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._awardCo_Curricular[Program._inc_opCoCurricular] = Program._seperateField(record, 1)
            Program._presentCo_Curricular[Program._inc_opCoCurricular] = Program._seperateField(record, 2)
            Program._remarksCo_Curricular[Program._inc_opCoCurricular] = Program._seperateField(record, 3)
            Program._inc_opCoCurricular += 1
        file.Close()
    @staticmethod
    def read_admin_14Achievments_2ExtraCurricular():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_14Achievments_2ExtraCurricular.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._awardExtra_Curricular[Program._inc_opExtraCurricular] = Program._seperateField(record, 1)
            Program._presentExtra_Curricular[Program._inc_opExtraCurricular] = Program._seperateField(record, 2)
            Program._remarksExtra_Curricular[Program._inc_opExtraCurricular] = Program._seperateField(record, 3)
            Program._inc_opExtraCurricular += 1
        file.Close()
    @staticmethod
    def read_admin_15ResultGrades():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_15ResultGrades.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._gpa[Program._inc_opResultGrades] = float.Parse((Program._seperateField(record, 1)))
            Program._cgpa[Program._inc_opResultGrades] = float.Parse((Program._seperateField(record, 2)))
            Program._remarksResult[Program._inc_opResultGrades] = Program._seperateField(record, 3)
            Program._inc_opResultGrades += 1
        file.Close()
    @staticmethod
    def read_admin_16GoldenLines():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_16GoldenLines.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleGoldenLines[Program._inc_opGoldenLines] = Program._seperateField(record, 1)
            Program._descriptionGoldenLines[Program._inc_opGoldenLines] = Program._seperateField(record, 2)
            Program._inc_opGoldenLines += 1
        file.Close()
    @staticmethod
    def read_admin_17LifelongEvents():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_17LifelongEvents.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleLifelongEvents[Program._inc_opLifelongEvents] = Program._seperateField(record, 1)
            Program._descriptionLifelongEvents[Program._inc_opLifelongEvents] = Program._seperateField(record, 2)
            Program._inc_opLifelongEvents += 1
        file.Close()
    @staticmethod
    def read_admin_18Notes():
        file = open("D:\\COMPUTER SCIENCE\\PD\\Business Application\\University Student Diary Management System\\Version_1\\USDMSVersion01\\File Handling\\admin_18Notes.txt")
        record = file.read().split("\n")
#C# TO PYTHON CONVERTER TODO TASK: The following assignments within expression was not converted by C# to Python Converter:
#ORIGINAL LINE: while ((record = file.ReadLine()) != null)
        for line in record:
            Program._titleNotes[Program._inc_opNotes] = Program._seperateField(record, 1)
            Program._descriptionNotes[Program._inc_opNotes] = Program._seperateField(record, 2)
            Program._inc_opNotes += 1
        file.Close()
    #****************** VALIDATIONS ******************
    @staticmethod
    def _float_Validaion(about, variable):
        temp = None
        temp_out_temp = OutObject()
        while not TryParseHelper.try_parse_float(variable, temp_out_temp): # check the validation of correct data type
            temp = temp_out_temp.arg_value
            print("Invalid entry.Please reenter.", end = '')
            print("\n", end = '')
            print(about, end = '')
            variable=input()
        temp = temp_out_temp.arg_value
        return float.Parse(variable)
    #********************************************************************************** END OF PROGEAM CODE *********************************************************************

if __name__ == "__main__":
    main()
import unittest
from unittest.mock import patch
import cli

class TestCLI(unittest.TestCase):

    ###################
    # Test print_menu #
    ###################
    @patch('builtins.print')
    def test_print_menu(self, mock_print):
        cli.print_menu()
        mock_print.assert_any_call("BMI Calculator")
        mock_print.assert_any_call("\t(1) Calculate BMI")
        mock_print.assert_any_call("\t(0) Exit")

    ###########################
    # Test main (Exit Choice) #
    ###########################
    @patch('builtins.input', side_effect=['0'])
    @patch('builtins.print')
    def test_main_exit(self, mock_print, mock_input):
        cli.main()
        mock_print.assert_any_call("Exiting the program...")

    ##############################
    # Test main (Invalid Choice) #
    ##############################
    @patch('builtins.input', side_effect=['9', '0'])
    @patch('builtins.print')
    def test_main_invalid_choice(self, mock_print, mock_input):
        cli.main()
        mock_print.assert_any_call("\n[Error] Invalid choice. Please select 1 or 0.\n")

if __name__ == "__main__":
    unittest.main()
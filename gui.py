__author__ = 'Uyuni'
import Tkinter
import ttk
import re_notation
import regex_to_nfa
import tkMessageBox
import unittest
from StringIO import StringIO
from tests import test_re_notation
from tests import test_regex_to_nfa



class GUI(Tkinter.Frame):
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.init_gui_grid()

        #self.centerWindow()

    def init_gui_grid(self):
        self.parent.title("Fundamentos de la computacion")
        self.style = ttk.Style().configure("TButton", padding=(0, 5, 0, 5))

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        # First regex label
        self.first_regex_label = Tkinter.Label(self)
        self.first_regex_label["text"] = "1ra Expresion regular"
        self.first_regex_label.grid(row=0, column=0)

        # First regex text field
        self.first_regex = Tkinter.Entry(self)
        self.first_regex["text"] = "ab*"  # <--- does not work
        self.first_regex.insert(0, "ab*")
        self.first_regex["width"] = 30
        self.first_regex.grid(row=0, column=1)

        # Second regex label
        self.second_regex_label = Tkinter.Label(self)
        self.second_regex_label["text"] = "2da Expresion regular"
        self.second_regex_label.grid(row=1, column=0)

        # Second regex text field
        self.second_regex = Tkinter.Entry(self)
        self.second_regex["text"] = "(a+b)*"  # <--- does not work
        self.second_regex.insert(0, "(a+b)*")
        self.second_regex["width"] = 30
        self.second_regex.grid(row=1, column=1)


        #Boton comparar
        self.compare_button = Tkinter.Button(self)
        self.compare_button["text"] = "Comparar"
        self.compare_button["fg"] = "red"

        self.compare_button.grid(row=3, column=2)

        # Quit button
        self.quit_button = Tkinter.Button(self)
        self.quit_button["text"] = "Salir",
        self.quit_button["command"] = self.quit
        self.quit_button.grid(row=3, column=3)



        # Run tests button
        self.run_test_button = Tkinter.Button(self)
        self.run_test_button["text"] = "Test",
        self.run_test_button.grid(row=3, column=0)



        self.pack()

    def center_window(self):
        w = 400
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


class Controller():
    def __init__(self):
        self.root = Tkinter.Tk()
        self.gui = GUI(parent=self.root)
        self.binding()
        self.gui.mainloop()

    def binding(self):
        self.gui.compare_button["command"] = self.compare
        self.gui.run_test_button["command"] = self.run_test

    def compare(self):
        # Model is actually called from here
        first_regex = self.gui.first_regex.get().strip()
        second_regex = self.gui.second_regex.get().strip()

        print "--------------------------------------------"
        print "Regular expressions received from the user:"
        print first_regex
        print second_regex

        regex1 = re_notation.infix_to_prefix(first_regex)
        regex2 = re_notation.infix_to_prefix(second_regex)

        print "--------------------------------------------"
        print "Converted regular expressions to prefix notation:"
        print regex1
        print regex2

        first_dfa = regex_to_nfa.build_dfa(regex1)
        second_dfa = regex_to_nfa.build_dfa(regex2)

        result, diff_string = regex_to_nfa.compare_dfas(first_dfa, second_dfa)
        print "--------------------------------------------"
        print "Do the regular expressions recognize the same language?"
        print result

        print "--------------------------------------------"
        if result:
            message = "Las expresiones regulares son equivalentes"
        else:
            message = "Las expresiones regulares no son equivalentes. \n"
            message += "La cadena que los diferencia es: {0}".format(diff_string)

        tkMessageBox.showinfo("Fundamentos de la computacion", message)

    def run_test(self):
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        re_notation_test_results = runner.run(unittest.makeSuite(test_re_notation.TestReNotation))

        stream.seek(0)
        print stream.read()
        stream.seek(0)

        # Commented the next lines because it hangs
        regex_to_nfa_test_results = runner.run(unittest.makeSuite(test_regex_to_nfa.TestRegexToNfa))
        stream.seek(0)
        print stream.read()
        stream.seek(0)

        # Commented the next lines because it hangs

        # re_notation_suite = unittest.TestSuite()
        # re_notation_suite.addTest(test_re_notation.TestReNotation())
        #
        # regex_to_nfa_suite = unittest.TestSuite()
        # regex_to_nfa_suite.addTest(test_regex_to_nfa.TestRegexToNfa())

        #test_suite = unittest.TestLoader().discover("./tests")
        #re_notation = unittest.TextTestRunner(verbosity=1).run(test_suite)
        #regex_to_nfa = unittest.TextTestRunner(verbosity=1).run(regex_to_nfa_suite)
        #print re_notation
        #print regex_to_nfa

def main():
    controller = Controller()


if __name__ == '__main__':
    main()
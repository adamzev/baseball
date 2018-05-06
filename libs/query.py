import sys

from libs import func


class Query(object):
    ''' query the user for multiple datatypes in a testable manner '''
    try:
        input_func = raw_input
    except NameError:
        input_func = input

    def __init__(self):
        pass

    @classmethod
    def change_input_func(cls, input_func):
        ''' change the input method '''
        cls.input_func = staticmethod(input_func)

    @classmethod
    def query_unknown_type(cls, question, sample_data):
        ''' query for a value of unknown type (primarily used to replace a value with
        another value of the same type) '''
        if isinstance(sample_data, float):
            result = cls.query_float(question)
        elif isinstance(sample_data, bool):
            result = cls.query_float(question)
        elif isinstance(sample_data, int):
            result = cls.query_int(question)
        else:
            result = cls.query_string(question)
        return result

    @classmethod
    def query_string(cls, question, default=None):
        ''' takes a question, default value and input func and returns a string value '''
        while True:
            ans = cls.input_func(question)
            if ans != "":
                return ans
            if ans == "" and default:
                return default
            print("Please enter a valid string.")

    @classmethod
    def query_yes_no(cls, question, default="yes"):
        """Ask a yes/no question and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

        The "answer" return value is True for "yes" or False for "no".

        From: http://code.activestate.com/recipes/577058/
        """
        valid = {"yes": True, "y": True, "ye": True,
                "no": False, "n": False}
        if default is None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            sys.stdout.write(question + prompt)
            choice = cls.input_func().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' "
                                "(or 'y' or 'n').\n")

    @classmethod
    def query_float(cls, question, default=None):
        """Ask a question via cls.input_func() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be any float or None

        The "answer" return value is a float value.
        """

        while True:
            sys.stdout.write(question)
            choice = cls.input_func()
            choice = choice.replace(",", "")
            if default is not None and choice == '':
                return default
            elif func.is_float(choice):
                return float(choice)
            else:
                sys.stdout.write("Please respond with a valid number.\n")

    @classmethod
    def query_int(cls, question, default=None, min_num=None, max_num=None):
        """Ask a question via cls.input_func() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be any float or None

        The "answer" return value is a float value.
        """
        while True:
            sys.stdout.write(question)
            choice = cls.input_func()
            choice = choice.replace(",", "")
            if default is not None and choice == '':
                return default
            if func.is_int(choice):
                choice = int(choice)
                if min_num is None and max_num is None:
                    return choice
                elif min_num is None and choice <= max_num:
                    return choice
                elif max_num is None and choice >= min_num:
                    return choice
                elif min_num <= choice <= max_num:
                    return choice
            sys.stdout.write("Please respond with a valid number.\n")

    @classmethod
    def query_min_max(cls, question, min_num=0.0, max_num=1.0):
        """Ask a question via cls.input_func() where "min", "max", "off" or a number
        in a range are valid and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

        The "answer" return value is True for "yes" or False for "no".

        From: http://code.activestate.com/recipes/577058/
        """
        prompt = " [min/max/off/{}-{}] ".format(min_num, max_num)

        while True:
            sys.stdout.write(question + prompt)
            choice = cls.input_func().lower()
            choice = choice.replace(",", "")
            if choice == 'min' or choice == 'max' or choice == 'off':
                return choice
            elif func.is_float(choice) and min_num <= float(choice) <= max_num:
                return float(choice)
            else:
                sys.stdout.write(
                    "Please respond with 'min', 'max', 'off' or a number between \
                    {} and {}. \n".format(min_num, max_num))

    @classmethod
    def query_from_list(cls, list_name, intro, options, select_multiple=True,
            callback=None, min_selections=1):
        ''' Creates a simple text menu that numbers options
            Options are either a dict containting a "name" key or list of strings
            Can be used to select one option or an array of multiple options
        '''
        if select_multiple:
            results = []

        while True:
            print("\n{}\n".format(intro))
            n = 1

            for option in options:
                try:
                    item_name = option["name"]
                except TypeError:
                    item_name = option
                except KeyError:
                    item_name = list(option)[0]
                print("{}) {}".format(n, item_name))
                n += 1

            if select_multiple:
                print("{}) Finished entering {}s".format(n, list_name))
            option_num = cls.query_int("Select an {} number: ".format(list_name), None, 1, n)

            if 0 <= option_num < n:
                selection = options[option_num - 1]
                if select_multiple:
                    if callback:
                        results.append(callback(selection))
                    else:
                        results.append(selection)
                else:
                    return selection
            elif option_num == n and select_multiple:
                if len(results) >= min_selections:
                    return results
                else:
                    print("Please select at least {} {}s".format(min_selections, list_name))
            else:
                print("Please enter a valid number.")

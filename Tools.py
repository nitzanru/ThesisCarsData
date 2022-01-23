class Tools:

    @staticmethod
    def clean_make(make):
        """
        handle specific common mistakes in the make name and clean it from unnecessary chars
        :return: make as clean as possible - no weird chars and one of the main makes if possible
        """
        try:
            make_clean_symbols = Tools.clean_symbols(make)
            if 'mercedes' in make_clean_symbols or 'mcc' in make_clean_symbols:
                return 'mercedes benz'
            elif make_clean_symbols.__eq__('chrysler jeep'):
                return 'jeep'
            elif 'rover' in make_clean_symbols or 'jaguar' in make_clean_symbols:
                return 'jaguar land rover'
            elif make_clean_symbols.__eq__('mini'):
                return 'bmw'
            elif make_clean_symbols.__eq__('lexus'):
                return 'toyota'
            elif 'bedford' in make_clean_symbols:
                return 'vauxhall'
            elif 'lincoln' in make_clean_symbols:
                return 'ford'
            elif 'pontiac' in make_clean_symbols or 'general' in make_clean_symbols or 'gm ' in make_clean_symbols:
                return 'general motors'
        except Exception:
            return make_clean_symbols
        return make_clean_symbols

    @staticmethod
    def clean_model(model):
        """
        :return: make as clean as possible - no weird chars and one of the main makes if possible
        """
        try:
            model_clean_symbols = Tools.clean_symbols(model)
        except Exception:
            return model_clean_symbols
        return model_clean_symbols


    @staticmethod
    def clean_symbols(make):
        """
        changes the make to be lower cased and cleans the symbols of the make - removes '-' ',' and spaces
        returns the clean make
        """
        try:
            parsed = make.lower()
        except AttributeError:  # no maker (nan)
            return make
        parsed = parsed.replace('-', ' ')
        parsed = parsed.replace(',', ' ')
        parsed = parsed.replace(';', ' ')
        parsed = parsed.replace('/', ' ')
        parsed = parsed.replace('\\', ' ')
        parsed = ' '.join(parsed.split())  # replace multiple spaces by one
        return parsed

class Validate:
    NOT_VALID_PREFIX_CHARACTER = "!#$%&'*+-/=?^_`{|}~"
    NOT_VALID_DOMAIN_CHARACTER = "!#$%&'*+/=?^_`{|}~"

    def __init__(self, email):
        self._email = email
        if self._email.find('@') > 0:
            email_prefix, email_domain = self._email.split('@')
            for i in email_prefix:
                if i in self.NOT_VALID_PREFIX_CHARACTER:
                    raise Exception(f'Not Valid e-mail address. '
                                    f'Character "{i}" not valid.')
            if email_prefix.find("..") > 0 or email_prefix[0] == '.' or \
                    email_prefix[-1] == '.':
                raise Exception(f"Not Valid e-mail address.")

            for i in email_domain:
                if i in self.NOT_VALID_DOMAIN_CHARACTER:
                    raise Exception(f'Not Valid e-mail domain. '
                                    f'Character "{i}" not valid.')
            if email_prefix.find("..") > 0 or email_prefix[0] == '.' or \
                    email_prefix[-1] == '.':
                raise Exception(f"Not Valid e-mail address.")
            if email_domain.find(".") > 0:
                domain_name, domain_zone = email_domain.split('.')
                if len(domain_zone) < 2:
                    raise Exception("Not valid domaine zone")
            print(f'Your email "{self._email}" is valid')
        else:
            raise Exception("Not Valid e-mail address. @ character not found")

mail = Validate('kholod@to.com')

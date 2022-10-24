class Bill:
    """
    object containing data about a bill, such as the total amount
    and period of the bill,
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    """
    create a flatmate who lives in and pays a share of the bill.

    """

    def __init__(self,name,days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        weight = (self.days_in_house)/(self.days_in_house + flatmate2.days_in_house)
        to_pay= bill.amount * weight
        return round(to_pay,2)
    def pays1(self, bill, flatmate1):
        weight = (self.days_in_house)/(self.days_in_house + flatmate1.days_in_house)
        to_pay1= bill.amount * weight
        return round(to_pay1,2)

class FileSharer:
    def __init__(self, filepath, api_keys="A2eXTHhtSSVGwzo73q05Vz"):
        self.filepath=filepath
        self.api_key=api_keys

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath =self.filepath')
        return new_filelink.url

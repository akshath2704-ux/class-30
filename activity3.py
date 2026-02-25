class singapore():
    def capital(self):
        print("marina bay is the capital of singapore.")
    def language(self):
        print("english and chinese is the most widely spoken language of singapore.")
    def type(self):
        print("singapore is a developed country.")
class malaysia():
    def capital(self):
        print("kuala lumpur is the capital of malaysia.")
    def language(self):
        print("malay is the primary language of malaysia.")
    def type(self):
        print("malaysia is a developed country.")
obj_singapore=singapore()
obj_malaysia=malaysia()
for country in (obj_singapore,obj_malaysia):
    country.capital()
    country.language()
    country.type()
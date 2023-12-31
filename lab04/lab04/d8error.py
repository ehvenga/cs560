from IPython.core.display import display, HTML, Markdown
import json

class Announce:
    def __init__(self, etype, value):
        self.etype = etype
        self.value = value
        self.errorname = str(etype().__class__.__name__)
    def tips(self):
        etype = self.etype
        value = self.value
        with open("errorConfig.json", "r") as f:
            diction = json.load(f)
        exceptionClass = diction.get(self.errorname)
        if exceptionClass is not None:
            self.default()
            for i in exceptionClass:
                key, items = list(i.items())[0]
                if (key in str(value)):
                    c=1
                    for j in items.get("helptext"):

                        display(Markdown(str(c)+". "+j))
                        c += 1
    def data8(self):
        display(Markdown("The Data 8 Reference might be helpful to look over for examples and usage: [Data 8 Reference](http://data8.org/fa21/python-reference.html)"))
    def furtherTips(self):
        display(Markdown("If you are having more trouble please feel free to consult a staff member at [Office Hours](https://oh.data8.org)\
                        \n or see the error message below "))
    def print(self, i):
        display(Markdown)
    def title(self):
        display(Markdown("## **Uh-o it seems we have an error!**"))
    def default(self):
        display(Markdown("It seems we have a "+self.errorname+ ". " +self.errorname+ "s are usually because of:"))
    def feedback(self):
        display(Markdown("Please fill out this quick survey to help us improve the the error feedback [Data 8 Error Feedback Survey](https://forms.gle/4d8CQG1p3SHL9zfV7)"))

def test_exception(self, etype, value, tb, tb_offset=None):
    try:
        announce = Announce(etype, value)
        announce.title()
        announce.tips()
        #announce.data8()
        #announce.furtherTips()
        #announce.feedback()
        self.showtraceback((etype, value, tb), tb_offset=tb_offset)
    except:
        self.showtraceback((etype, value, tb), tb_offset=tb_offset)
    
get_ipython().set_custom_exc((Exception,), test_exception)
    

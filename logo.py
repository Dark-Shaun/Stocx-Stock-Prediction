import urllib
import urllib.request

def logo(company_name_1,ticker_sym):
    name,name_2=company_name_1,ticker_sym
    name=name.lower()

    try:
        resource = urllib.request.urlopen("https://logo.clearbit.com/{}.com".format(name))
        output = open("file01.png","wb")
        output.write(resource.read())
        output.close()
        name_1="file01.png"
        return name_1
    except:
        resource = urllib.request.urlopen("https://logo.clearbit.com/{}.com".format(name_2))
        output = open("file01.png","wb")
        output.write(resource.read())
        output.close()
        name_1="file01.png"
        return name_1

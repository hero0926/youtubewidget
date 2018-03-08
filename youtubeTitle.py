from __future__ import print_function
from pywinauto import Desktop
import platform
import appscript

def FormatUrl(url):
    if url and not url.startswith("https://"): 
        return "http://" + url
    return url

def GetURL() :  
    
    if platform.system() == "Darwin" :
        urls = appscript.app('Google Chrome').windows.tabs.URL()
        print(platform)
        
    else :
        urls = appscript.app('Google Chrome').windows.tabs.URL()

        chrome_window = Desktop(backend="uia").window(class_name_re='Chrome')
        chrome = chrome_window['Google Chrome']

        address_bar_wrapper = chrome_window['Google Chrome'].main.Edit.wrapper_object()

        url = address_bar_wrapper.legacy_properties()

        print(url['Value'])


    
    
    def GetTitle() 
:    pass

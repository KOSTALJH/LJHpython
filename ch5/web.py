#webbrowser
import webbrowser

MSEdge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
Chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

#webbrowser.register(name, constructor, instance=None, *, preferred=False)
webbrowser.register(Chrome, None, webbrowser.BackgroundBrowser(Chrome))

#webbrowser.open(url,new=0,autoraise=True)
webbrowser.open("https://www.google.co.kr",new=0,autoraise=True)

#webbrowser.open_new(url)
webbrowser.open_new("https://www.daum.net")

#webbrowser.open_new_tap(url)
webbrowser.open_new_tab("https://www.bing.com")

#webbrowser.get(using=None).open(url,new=0,autoraise=True)
webbrowser.get(Chrome).open("https://naver.com")

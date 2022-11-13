"""""""""
利用fake_useragent產生個瀏覽器的user_agent
"""""""""
from fake_useragent import UserAgent
ua=UserAgent()
print(ua.ie,"\n")#IE的user_agent
print(ua.google,"\n")#Chrome的user_agent
print(ua.firefox,"\n")#firefox的user_agent
print(ua.safari,"\n")#safari的user_agent
print(ua.random)#隨機產生user_agent

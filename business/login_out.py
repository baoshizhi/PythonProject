#导入自定义封装过的对元素的基本操作类CommShare
from commonlib.commonfun import CommShare
#创建一个继承于基本操作类CommShare的登陆类login
import time
class Login_Out(CommShare):
    def login(self,user,pwd):
        # 打开目标网站地址
        self.open_url("http://10.45.138.39:8380/cscweb/#/login")
        #打开浏览器之后清空缓存
        self.driver.delete_all_cookies()

        #输入账号
        self.input("xpath","//*[@id='app']/div/div[2]/div/div/form/div[1]/div/div[1]/input",user)
        #输入密码
        self.input("xpath","//*[@id='app']/div/div[2]/div/div/form/div[2]/div/div/input",pwd)
        time.sleep(15) #用于输入界面上显示的校验码
        #点击登陆
        self.click("css","button>span")
        time.sleep(3) #登陆后等待3秒钟等待页面所有元素加载

if __name__ == '__main__':
    log=Login_Out()
    log.login("baoshizhi","123qweQWE+")

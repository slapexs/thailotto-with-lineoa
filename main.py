import requests
class Checklotto:

    def __init__(self):
        self.money = 0
        # response
        self.response = {"status": "", "message": "", "sticker": ""}
        

    def CheckRunningNumber(self, number, members):
        return number in members
    
    def SetResponse(self, name, money, status, package_id, sticker_id):
        self.money = "{:,.0f}".format(int(money))
        self.response['status'] = status
        self.response['message'] = f"ยินดีด้วย!! คุณถูก{name} มูลค่า {self.money} บาท"
        self.response['sticker'] = {"package_id": package_id, "sticker_id": sticker_id}

    def CheckIsWonlotto(self, number:str):
        self.url_api = "https://lotto.api.rayriffy.com/latest"

        self.res = requests.get(self.url_api).json()['response']
        self.date = self.res['date']
        self.prizes = self.res['prizes']
        self.isWon = ""
        for i in range(0, len(self.prizes)):
            if number in self.prizes[i]['number']:
                self.isWon = i

        # Check running number
        self.runningNumber = self.res['runningNumbers']    
        self.threeNumber = {'front': number[:3], 'back': number[3:]}
        self.twoNumber = number[4:]
        
        if self.isWon != "":
            self.SetResponse(self.prizes[self.isWon]['name'], self.prizes[self.isWon]['reward'], 'Won', "1070", "17854")
        else:
            # Check three number
            if self.CheckRunningNumber(self.threeNumber['front'], self.runningNumber[0]['number']):
                self.SetResponse(self.runningNumber[0]['name'], self.runningNumber[0]['reward'], 'Won', "1070", "17854")
                
                
            elif self.CheckRunningNumber(self.threeNumber['back'], self.runningNumber[1]['number']):
                self.SetResponse(self.runningNumber[1]['name'], self.runningNumber[1]['reward'], 'Won', "1070", "17854")
                
            elif self.CheckRunningNumber(self.twoNumber, self.runningNumber[2]['number']):
                self.SetResponse(self.runningNumber[2]['name'], self.runningNumber[2]['reward'], 'Won', "1070", "17854")
                
            else:
                self.response['status'] = "Lose"
                self.response['message'] = "เสียใจด้วยค่ะ...คุณไม่ถูกรางวัล งวดหน้าเอาใหม่นะคะ"
                self.response['sticker'] = {"package_id": "1070", "sticker_id": "17859"}

        return self.response
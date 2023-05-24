import requests
class Checklotto:
    def CheckIsWonlotto(self, number:str):
        self.url_api = "https://lotto.api.rayriffy.com/latest"

        self.res = requests.get(self.url_api).json()['response']
        self.date = self.res['date']
        self.prizes = self.res['prizes']
        self.isWon = ""
        for i in range(0, len(self.prizes)):
            print(self.prizes[i])
            if number in self.prizes[i]['number']:
                self.isWon = i
                
        if self.isWon != "":
            return {'status': 'Won','message': f"ยินดีด้วย!! คุณถูก{self.prizes[self.isWon]['name']} มูลค่า {self.prizes[self.isWon]['reward']} บาท"}
        else:
            
            return {'status': 'Lose','message': "เสียใจด้วยค่ะ...คุณไม่ถูกรางวัล งวดหน้าเอาใหม่นะ🥲"}
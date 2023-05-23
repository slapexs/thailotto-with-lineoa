import requests
class Checklotto:
    def CheckIsWonlotto(self, number:str):
        self.url_api = "https://lotto.api.rayriffy.com/latest"

        self.res = requests.get(self.url_api).json()['response']
        self.date = self.res['date']
        self.prizes = self.res['prizes']
        self.isWon = False
        for i in range(len(self.prizes)):
            if number in self.prizes[i]['number']:
                self.isWon = i

        if self.isWon != False:
            return {'status': 'Won','message': f"ยินดีด้วย!! คุณถูก{self.prizes[self.isWon]['name']} มูลค่า {self.prizes[self.isWon]['reward']} บาท"}
        else:
            
            return {'status': 'Lose','message': "Sorry is not your time, GG Go next"}
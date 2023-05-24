import requests
class Checklotto:
    def CheckIsWonlotto(self, number:str):
        self.url_api = "https://lotto.api.rayriffy.com/latest"

        self.res = requests.get(self.url_api).json()['response']
        self.date = self.res['date']
        self.prizes = self.res['prizes']
        self.isWon = ""
        self.configSticker = {"package_id": "", "sticker_id": ""}
        for i in range(0, len(self.prizes)):
            if number in self.prizes[i]['number']:
                self.isWon = i

        if self.isWon != "":
            self.configSticker['package_id'] = "1070"
            self.configSticker['sticker_id'] = "17854"
            self.money = "{:,.0f}".format(int(self.prizes[self.isWon]['reward']))

            return {"status": 'Won',"message": f"ยินดีด้วย!! คุณถูก{self.prizes[self.isWon]['name']} มูลค่า {self.money} บาท", "sticker": self.configSticker}
        else:
            self.configSticker['package_id'] = "1070"
            self.configSticker['sticker_id'] = "17859"
            return {"status": 'Lose',"message": "เสียใจด้วยค่ะ...คุณไม่ถูกรางวัล งวดหน้าเอาใหม่นะคะ", "sticker": self.configSticker}
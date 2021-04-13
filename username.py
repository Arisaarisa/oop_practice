# データ型の定義
class UserName:
    def __init__(self, name):
        # もしnameの文字数が4文字以上20文字以下でなければ
        if not (4 <= len(name) <= 20):
            # エラー文を表示して終了する
            raise ValueError(f'{name}はルール違反です')

        self.name = name

    # screen_nameメソッドの作成
    def screen_name(self):
        # upperは大文字に変換する
        return self.name.upper()


# UserNameクラスのインスタンス化
tanaka = UserName(name='tanaka')
# bob = UserName(name='bob')
# 普通に出力
# print(tanaka)
# typeを入れデータ型を出力
# print(type(tanaka))
# print(tanaka.name)
# print(bob.name)
print(tanaka.screen_name())

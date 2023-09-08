# 4-3 集約・コンポジション
どちらもクラス間の関連を表現する言葉である.
- 集約（aggregation）
  - 所有者が既存のオブジェクトへの参照を保持する関係
  - 独立して存在できる何かのコレクションがある場合（空港とそこに駐機されている飛行機, 学校と生徒等）
  - 所有者がいなくなっても既存オブジェクトの存亡にはなんの関係もない
- 合成（composition）
  - 所有者がオブジェクトを占有する主体になる関係
  - 保持されているものが保持しているものの一部である場合（自動車とそれを構成するエンジン等）
  - 所有者がいなくなると所有されていたオブジェクトの存在意義も消滅する
## 参考リンク
https://python.ms/composition-over-inheritance/ : 合成と移譲, 継承が悪であることを非常にわかりやすく書いている. 自分も今後は継承は使わないようにしようと思える.  
https://techblog.asahi-net.co.jp/entry/2022/09/15/153403  
https://qiita.com/aki3061/items/5d94f4024cc78852010f
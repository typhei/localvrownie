#-*- coding: utf-8 -*-
from summpy.lexrank import summarize

text = u"「ジレット プロシールド」を体験した後に、「スッキリされました？」と声をかけられると、そこにはイエローナース...ではなく、スーツの女性が。発売元のプロクター・アンド・ギャンブル・ジャパンの成瀬さんでした。「すごく気持ちよかったです！」と答えつつ、そのままいくつかお話を伺いました。成瀬さん：「ジレット プロシールド」は研究開発に4年ほどかかりましたが、「史上最高のやさしさ」だと自負しております！ 日本のユーザーさんが求める「深剃り」と「肌へのやさしさ」を、いっぺんに解決する目的が達成できたのかなと感じています。ジレットというブランドは、消費者が抱えている悩みや問題を解決するために、どんどん技術を革新していくことで成長してきました。創業者のキング C.ジレットから続く「そうでなければいる意味がない」という強い思いを引き継いで、今後も消費者の方に寄り添っていけたらと思っています。── 研究開発に4年を費やしたポイントはどこにあったのでしょう？成瀬：T字カミソリでは「肌を引っ張りながら剃る」必要があるんです。刃の下にあるラバーがその役割を担うのですが、このラバーとジェルスムーサーのバランスを取るのにもっとも試行錯誤がありました。ラバーを控えめにすれば肌が引っ張れないので深く剃れない、逆にすれば肌へのやさしさが減ってしまうからです。"
text=u"地雷魚 @Jiraygyoうああああああああああ動画で既にしんどい！ 『バーチャルハルシネーションについて ～統合失調症の幻覚疑似体験～』 http://www.mental-navi.net/togoshicchosho/virtual/ … http://pbs.twimg.com/media/CvgJxqaVUAAZ_RO.jpgバーチャルハルシネーションについて～統合失調症の幻覚疑似体験～ バーチャルハルシネーションは、専用のゴーグルとヘッドホンを装着して体験しますが、ここでは、そこで流れる画像と音声を掲載しています。（ゴーグルとヘッドホンは必要としません。)http://www.mental-navi.net/togoshicchosho/virtual/2: 2016/10/24(月) 22:36:58.41 ID:XRqSwyuS0俺は最初は時計の針の音だった実際にあった時計の音に耳を澄ませていたら、時計の無い所でも聞こえるようになってきた3: 2016/10/24(月) 22:47:10.01 ID:iHbJVSuw0気配→だんだん現実味を帯びてくる4: 2016/10/24(月) 22:48:35.76 ID:FcgkCiTk0現実とVRの区別が付かなくなってマジ糖質になったらどうするの？6: 2016/10/24(月) 22:54:48.18 ID:knYykJSJ0俺は職場の女が髪をかきあげるかきあげる動作が始まりだった7: 2016/10/24(月) 22:55:57.68 ID:ILnL2B2R0集団ストーカーに襲われてまーす！8: 2016/10/24(月) 23:01:41.55 ID:F9I9P9g40なんか動画見てから声が聞こえるようになったんだが…9: 2016/10/24(月) 23:06:40.69 ID:MhxxyKWd0怖いから見ない11: 2016/10/24(月) 23:27:39.03 ID:iHbJVSuw0逆に治療に活かせるかもな。神経症ぐらいならイケるだろ15: 2016/10/25(火) 00:37:07.04 ID:VYOStl9g0頑張れ16: 2016/10/25(火) 01:36:06.67 ID:/MOGv8J00うぜー17: 2016/10/25(火) 02:35:06.84 ID:aHCCaWyc0ありえない18: 2016/10/25(火) 02:37:11.23 ID:w7QP1/990誰かが私のことを笑っているとか？27: 2016/10/25(火) 04:13:07.44 ID:eEmR1uBj0うらやましい28: 2016/10/25(火) 05:12:06.95 ID:75ptVjAR0こんにちは "
# ensure type(text) is unicode
sentences, debug_info = summarize(
    text, sent_limit=5, continuous=True, debug=True
)

for sent in sentences:
    print sent.strip().encode("utf-8")
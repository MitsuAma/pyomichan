import re

SSList = []
with open('ReplaceTag.dic', 'r', encoding='utf-8') as f1:
    for line in f1:
        spr = r"N\t(.+?)\t\(SoundW"
        # 単語の抜き出し
        ss = re.findall(spr, line)
        ssStr = "".join(ss)
        SS = ssStr.upper()
        SS = SS.replace('-', '－')
        SS = SS.replace('!', '！')
        SS = SS.replace('?', '？')
        SSLine = re.sub(r"N\t(.+)\t\(SoundW", 'N\t'+SS+'\t(SoundW', line)

        SSList.append(SSLine)

with open('ReplaceTag.dic.output', 'w', encoding='utf-8') as f2:
    f2.writelines(SSList)

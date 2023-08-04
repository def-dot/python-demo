import jieba
import jieba.analyse


class JieBaT:
    def cut_t(self):
        r = jieba.cut("我的名字叫施得而啊")  # cut_all=False 默认精准模式
        print('/'.join(r))  # 我/的/名字/叫施/得/而/啊 （叫施？）

        r = jieba.cut("我的名字是李晶晶")  # 匹配优先级：李晶晶 ，若在字典中完全匹配，则识别为一个词；若在字典中部分匹配，则部分匹配的部分识别为一个词，其余识别为另外的词；若在字典中不存在，则依据语义划词（？如我 是 李晶晶）
        print('/'.join(r))

        r = jieba.cut("欢迎来到清华大学！")
        print('/'.join(r))  # 欢迎/来到/清华大学/！

        r = jieba.cut("欢迎来到清华大学！", cut_all=True)
        print('/'.join(r))  # 欢迎/迎来/来到/清华/清华大学/华大/大学/！

        r = jieba.cut("他来到了网易杭研大厦！")
        print('/'.join(r))  # 他/来到/了/网易/杭研/大厦/！

        r = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造！")
        print('/'.join(r))  # 小明/硕士/毕业/于/中国/科学/学院/科学院/中国科学院/计算/计算所/，/后/在/日本/京都/大学/日本京都大学/深造/！

    def add_word_t(self):
        r = jieba.cut("李小福是创新办主任也是云计算方面的专家")
        print('/'.join(r))  # 李小福/是/创新/办/主任/也/是/云/计算/方面/的/专家
        jieba.load_userdict("append_dict.txt")
        r = jieba.cut("李小福是创新办主任也是云计算方面的专家")
        print('/'.join(r))  # 李小福/是/创新办/主任/也/是/云计算/方面/的/专家
        jieba.add_word("创新办主任")
        r = jieba.cut("李小福是创新办主任也是云计算方面的专家")
        print('/'.join(r))  # 李小福/是/创新办主任/也/是/云计算/方面/的/专家

    def suggest_freq_t(self):
        r = jieba.cut("我不喜欢也不高兴")
        print('/'.join(r))  # 我/不/喜欢/也/不/高兴

        jieba.suggest_freq("不喜欢", tune=True)  # 等价add_word?
        jieba.suggest_freq("不高兴", tune=True)
        r = jieba.cut("我不喜欢也不高兴")
        print('/'.join(r))  # 我/不喜欢/也/不高兴

        jieba.suggest_freq(("喜", "欢"), tune=True)
        r = jieba.cut("我不喜欢也不高兴")
        print('/'.join(r))  # 我/不/喜/欢/也/不/高兴

        jieba.suggest_freq(("喜", "欢"), tune=True)  # 等价add_word?
        r = jieba.cut("我不喜欢也不高兴")
        print('/'.join(r))  # 我/不/喜/欢/也/不/高兴

        jieba.add_word("不喜欢")
        jieba.add_word("不高兴")
        r = jieba.cut("我不喜欢也不高兴")
        print('/'.join(r))  # 我/不喜欢/也/不高兴

    def tf_idf_t(self):
        content = open("test.txt", "rb").read()
        tags = jieba.analyse.extract_tags(content, withWeight=True)
        print(tags)

    def text_rank_t(self):
        content = "中国科学报本报讯又有一位中国科学家喜获小行星命名殊荣！"
        # 基于jieba的textrank算法实现
        keywords = jieba.analyse.textrank(content, withWeight=True)
        print(keywords)


if __name__ == '__main__':
    # JieBaT().cut_t()
    # JieBaT().add_word_t()
    # JieBaT().suggest_freq_t()
    # JieBaT().tf_idf_t()
    JieBaT().text_rank_t()

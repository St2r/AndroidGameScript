from CORE.Engine import BaseButton, Point

NullButton = BaseButton(Point(0, 0), Point(0, 0))


class OnBattle:
    class Skill:
        Skill1 = BaseButton(Point(60, 820), Point(140, 910))
        Skill2 = BaseButton(Point(200, 820), Point(280, 910))
        Skill3 = BaseButton(Point(345, 820), Point(425, 910))
        Skill4 = BaseButton(Point(540, 820), Point(620, 910))
        Skill5 = BaseButton(Point(680, 820), Point(760, 910))
        Skill6 = BaseButton(Point(820, 820), Point(900, 910))
        Skill7 = BaseButton(Point(1020, 820), Point(1100, 910))
        Skill8 = BaseButton(Point(1160, 820), Point(1240, 910))
        Skill9 = BaseButton(Point(1290, 820), Point(1370, 910))

        class Servant:
            p1 = BaseButton(Point(400, 500), Point(600, 800))
            p2 = BaseButton(Point(860, 500), Point(1060, 800))
            p3 = BaseButton(Point(1330, 500), Point(1530, 800))

    class Card:
        Card1 = BaseButton(Point(90, 640), Point(290, 900))
        Card2 = BaseButton(Point(480, 640), Point(680, 900))
        Card3 = BaseButton(Point(860, 640), Point(1060, 900))
        Card4 = BaseButton(Point(1240, 640), Point(1440, 900))
        Card5 = BaseButton(Point(1620, 640),Point(1820, 900))

    class NoblePhantasm:
        NP1 = BaseButton(Point(510, 195), Point(720, 435))
        NP2 = BaseButton(Point(860, 195), Point(1070, 435))
        NP3 = BaseButton(Point(1210, 195), Point(1420, 435))

    Attack = BaseButton(Point(1540, 780), Point(1840, 1000))
    BattleMenu = BaseButton(Point(1730, 240), Point(1850, 360))

    class MasterMenu:
        Open = BaseButton(Point(1730, 420), Point(1850, 540))
        Skill1 = BaseButton(Point(1315, 430), Point(1400, 510))
        Skill2 = BaseButton(Point(1450, 430), Point(1530, 510))
        Skill3 = BaseButton(Point(1580, 430), Point(1660, 510))

        class Exchange:
            p1 = BaseButton(Point(100, 410), Point(310, 630))
            p2 = BaseButton(Point(400, 410), Point(610, 630))
            p3 = BaseButton(Point(700, 410), Point(910, 630))
            p4 = BaseButton(Point(900, 410), Point(1210, 630))
            p5 = BaseButton(Point(1200, 410), Point(1510, 630))
            p6 = BaseButton(Point(1500, 410), Point(1810, 630))
            Change = BaseButton(Point(760, 900), Point(1160, 980))


class WorkFlow:
    GuanQia = BaseButton(Point(990, 290), Point(1800, 440))
    KaiShiRenWu = BaseButton(Point(1700, 970), Point(1860, 1050))
    DianJiHuaMian = BaseButton(Point(760, 880), Point(1160, 1040))
    XiaYiBu = BaseButton(Point(1470, 970), Point(1850, 1050))

    class Apple:
        Golden = BaseButton(Point(500, 400), Point(1400, 560))

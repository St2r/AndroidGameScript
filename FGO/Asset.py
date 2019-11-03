from CORE.Engine import BaseAsset, Point


class OnBattle:
    BattleMenu = BaseAsset(Point(1730, 240), Point(1850, 360),
                           '10111100100111101101100110100001011000001110100110011010')
    Attack = BaseAsset(Point(1580, 800), Point(1820, 1000),
                       '00011010110101000010110010010011001000110100110111110011')


class WorkFlow:
    LieBiaoGengXin = BaseAsset(Point(1180, 150), Point(1320, 240),
                               '11101001101010110101011100001101100110101011110101111100')
    KaiShiRenWu = BaseAsset(Point(1700, 970), Point(1860, 1050),
                            '00000001000000001010101010010100101010100100101000000100')
    ZhanDouJieGuo = BaseAsset(Point(790, 50), Point(1120, 130),
                              '11001101100010110001011000100100100010011001001100100110')
    XiaYiBu = BaseAsset(Point(1470, 970), Point(1850, 1050),
                        '00000000101000110100001111000110000010100001010000110101')
    ApNotEnough = BaseAsset(Point(820, 56), Point(1250, 148),
                            '11010000011000101100010010010111010001100001001000001000')


class RenWuXvanZe:
    class ShanShanJi:
        ZhengSai = BaseAsset(Point(990, 290), Point(1150, 440),
                             '11101001101011111011010010110001011010001101001110001101')
        JueSai_GuangChangHuaYuan = BaseAsset(Point(990, 290), Point(1150, 440),
                             '10100110100011001001111000101011010011001000100101110000')
        test = BaseAsset(Point(990, 290), Point(1800, 440),
                             '10011011010110111111010010110101111001101110100111001101')
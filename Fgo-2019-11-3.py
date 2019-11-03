from CORE.Engine import AdbServer
from FGO import Asset, Button
from FGO.BaseFunction import *


def battle_start():
    wait_appear(Asset.RenWuXvanZe.ShanShanJi.JueSai_GuangChangHuaYuan, 1)
    AdbServer.tap(Button.WorkFlow.GuanQia.random_point)
    AdbServer.wait_second(0.5)
    if not check_ap():
        AdbServer.tap(Button.WorkFlow.GuanQia.random_point)


def choose_support():
    Log.record('ChooseSupportServant')
    wait_appear(Asset.WorkFlow.KaiShiRenWu, 1)


def one_battle():
    AdbServer.tap(Button.WorkFlow.KaiShiRenWu.random_point)
    wait_action()

    servant_skill(Button.OnBattle.Skill.Skill8)
    servant_skill(Button.OnBattle.Skill.Skill9)
    servant_skill(Button.OnBattle.Skill.Skill1, Button.OnBattle.Skill.Servant.p2)
    choose_card(Button.OnBattle.NoblePhantasm.NP2,
                Button.OnBattle.Card.Card1,
                Button.OnBattle.Card.Card2)
    servant_skill(Button.OnBattle.Skill.Skill7, Button.OnBattle.Skill.Servant.p2)
    change_servant(Button.OnBattle.MasterMenu.Exchange.p3, Button.OnBattle.MasterMenu.Exchange.p4)
    servant_skill(Button.OnBattle.Skill.Skill7, Button.OnBattle.Skill.Servant.p2)
    servant_skill(Button.OnBattle.Skill.Skill9, Button.OnBattle.Skill.Servant.p2)
    servant_skill(Button.OnBattle.Skill.Skill6)
    choose_card(Button.OnBattle.NoblePhantasm.NP2,
                Button.OnBattle.Card.Card1,
                Button.OnBattle.Card.Card2)
    servant_skill(Button.OnBattle.Skill.Skill3, Button.OnBattle.Skill.Servant.p2)
    servant_skill(Button.OnBattle.Skill.Skill2)
    servant_skill(Button.OnBattle.Skill.Skill8)
    master_skill(Button.OnBattle.MasterMenu.Skill1)
    choose_card(Button.OnBattle.NoblePhantasm.NP2,
                Button.OnBattle.Card.Card1,
                Button.OnBattle.Card.Card2)


if __name__ == '__main__':
    AdbServer.start_server()
    while True:
        battle_start()
        choose_support()
        one_battle()
        end_battle()

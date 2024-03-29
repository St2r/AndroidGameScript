from CORE.Engine import AdbServer, BaseButton, Log
from FGO import Asset, Button


def wait_appear(asset, wait_time):
    AdbServer.screen_cap()
    while not asset.match():
        AdbServer.wait_second(wait_time)
        AdbServer.screen_cap()


def wait_action():
    AdbServer.screen_cap()
    while not Asset.OnBattle.Attack.match():
        Log.record('waiting...')
        AdbServer.wait_second(0.5)
        AdbServer.screen_cap()
    AdbServer.wait_second(1)  # 这个地方要加一点延迟,否则会有BUG，具体的原因我也不是很清楚


def choose_card(card1: BaseButton, card2: BaseButton, card3: BaseButton):
    wait_action()
    Log.record('choosing cards')
    AdbServer.tap(Button.OnBattle.Attack.random_point)
    AdbServer.wait_second(1)
    AdbServer.tap(card3.random_point)
    AdbServer.wait_second(0.2)
    AdbServer.tap(card3.random_point)
    AdbServer.wait_second(0.2)
    AdbServer.tap(card1.random_point)
    AdbServer.wait_second(0.2)
    AdbServer.tap(card2.random_point)
    AdbServer.wait_second(0.2)
    AdbServer.tap(card3.random_point)
    AdbServer.wait_second(10)


def servant_skill(skill: BaseButton, servant=Button.NullButton):
    wait_action()
    Log.record('servant_skill')
    AdbServer.tap(skill.random_point)
    if servant != Button.NullButton:
        AdbServer.wait_second(0.25)
        AdbServer.tap(servant.random_point)


def master_skill(skill: BaseButton):
    wait_action()
    Log.record('master_skill')
    AdbServer.tap(Button.OnBattle.MasterMenu.Open.random_point)
    AdbServer.wait_second(0.25)
    AdbServer.tap(skill.random_point)


def change_servant(servant1: BaseButton, servant2: BaseButton):
    wait_action()
    Log.record('change_servant')
    AdbServer.tap(Button.OnBattle.MasterMenu.Open.random_point)
    AdbServer.wait_second(0.25)
    AdbServer.tap(Button.OnBattle.MasterMenu.Skill3.random_point)
    AdbServer.wait_second(0.5)
    AdbServer.tap(servant1.random_point)
    AdbServer.wait_second(0.1)
    AdbServer.tap(servant2.random_point)
    AdbServer.wait_second(0.1)
    AdbServer.tap(Button.OnBattle.MasterMenu.Exchange.Change.random_point)
    AdbServer.wait_second(5)


def check_ap() -> bool:
    AdbServer.screen_cap()
    if Asset.WorkFlow.ApNotEnough.match():
        Log.record('ApNotEnough')
        AdbServer.tap(Button.WorkFlow.Apple.Golden.random_point)
        AdbServer.wait_second(0.5)
        AdbServer.tap(Button.WorkFlow.Apple.JueDing.random_point)
        return False
    else:
        return True


def end_battle():
    wait_appear(Asset.WorkFlow.ZhanDouJieGuo, 1)
    while Asset.WorkFlow.ZhanDouJieGuo.match():
        AdbServer.tap(Button.WorkFlow.DianJiHuaMian.random_point)
        AdbServer.screen_cap()
    while Asset.WorkFlow.XiaYiBu.match():
        AdbServer.tap(Button.WorkFlow.XiaYiBu.random_point)
        AdbServer.screen_cap()
    AdbServer.wait_second(10)

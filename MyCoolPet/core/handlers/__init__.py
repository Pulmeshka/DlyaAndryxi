from aiogram import Dispatcher
from . import (
    start_help, updates, rp_commands, inventorys,
    shop, pets_eggs, wearpet, goldPet, grass,
    eggs, admin, pay, DiamondInCoin, Torgoves, petid,
    givepet, viper, gift, 
)
from utilis import filters



def register_handlers(dp: Dispatcher):
    # all commands
    dp.register_message_handler(
        start_help.start,
        filters.Command(('start', 'help', 'хэлп', 'хелп'), prefixes=('/', '')))

    dp.register_message_handler(
        start_help.me,
        filters.Command(('профиль', 'profile', 'ми', 'me'), prefixes=('/', '')))

    dp.register_message_handler(
    updates.updates_command,
    filters.Command(('updates', 'обновы'), prefixes=('/', '')))

    dp.register_message_handler(
    inventorys.inventory,
    filters.Command(('inventory', 'инвентарь', 'инв'), prefixes=('/', '')))

    dp.register_message_handler(
    pets_eggs.pets_comamnd,
    filters.Command(('pets', 'петы', 'пет'), prefixes=('/', '')))

    dp.register_message_handler(
    shop.shop_comamnd,
    filters.Command(('shop', 'магазин', 'шоп'), prefixes=('/', '')))

    dp.register_message_handler(
    wearpet.wear_list_command,
    filters.Command(('одеть', 'wearpet'), prefixes=('/', '')))

    dp.register_message_handler(
    wearpet.wear_pet_command,
    filters.Command(('wear'), prefixes=('/')))

    dp.register_message_handler(
    goldPet.gold_pet_comamnd,
    filters.Command(('скрестить', 'gold'), prefixes=('/', '')))

    dp.register_message_handler(
    grass.grass_game,
    filters.Command(('grass', 'травка'), prefixes=('/', '')))

    dp.register_message_handler(
    grass.grass_help,
    filters.Command(('helpgrass'), prefixes=('/')))

    dp.register_message_handler(
    eggs.open_egg,
    filters.Command(('открыть', 'open'), prefixes=('/', '')))

    dp.register_message_handler(
        admin.ban_player,
        filters.Command(('MyBan', 'МайБан', 'блокнуть'), prefixes=('/', '')))

    dp.register_message_handler(
        admin.unban_player,
        filters.Command(('MyUnban', 'майанбан', 'разблокать'), prefixes=('/', '')))

    dp.register_message_handler(
        admin.admin_comamnds,
        filters.Command(('AdminHelp', 'админс', 'админхелп'), prefixes=('/', '')))

    dp.register_message_handler(
        admin.give_coin_diamond,
        filters.Command(('give', 'выдать'), prefixes=('/', '')))
    
    dp.register_message_handler(
        admin.give_pet2,
        filters.Command(('givepet', 'выдатьпет'), prefixes=('/', '')))

    dp.register_message_handler(
        pay.pay_coin,
        filters.Command(('pay', 'пей', 'закинуть'), prefixes=('/', '')))

    dp.register_message_handler(
        DiamondInCoin.DiamondCoin,
        filters.Command(('перевести'), prefixes=('', '/')))

    dp.register_message_handler(
        start_help.all_users,
        filters.Command(('все', 'all'), prefixes=('', '/')))

    dp.register_message_handler(
        Torgoves.torgoves_command,
        filters.Command(('торговец'), prefixes=('')))
    
    dp.register_message_handler(
        petid.check_pet_id,
        filters.Command(('PetId', 'чекпет'), prefixes=('/', '')))
    
    dp.register_message_handler(
        givepet.give_pet,
        filters.Command(('GivePet', 'Передать'), prefixes=('/', '')))
    
    dp.register_message_handler(
        start_help.bot_command,
        filters.Command(('bot', 'бот'), prefixes=('/', '')))
    
    dp.register_message_handler(
        start_help.promo_command,
        filters.Command(('промо', 'promo'), prefixes=('/', '')))
    
    # dp.register_message_handler(
    #     start_help.channel_bonus,
    #     filters.Command(('channelBonus'), prefixes=('/')))
    
    dp.register_message_handler(
        viper.viper,
        filters.Command(('viper', 'випер'), prefixes=('/', '')))
    
    dp.register_message_handler(
        gift.gift_vip_command,
        filters.Command(('giftvip'), prefixes=('/')))
    
    dp.register_message_handler(
        start_help.donate,
        filters.Command(('donate', 'донат'), prefixes=('/', '')))
    
    dp.register_message_handler(
        gift.gift_premium_egg_command,
        filters.Command(('giftPremiumEgg'), prefixes=('/')))
    


    #https://telegra.ph/Gajd-MyCoolPet-bot-10-09 - НЕ ЗАБЫВАЙ

    # buttons
    
    #goldPet.py
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(goldPet.GOLDbutterfly), lambda q: q.data.startswith("go1"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(goldPet.GOLDdog), lambda q: q.data.startswith("go2"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(goldPet.GOLDpig), lambda q: q.data.startswith("go3"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(goldPet.GOLDcow), lambda q: q.data.startswith("go4"))

    #more
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(start_help.error), lambda q: q.data.startswith("error"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.eggs), lambda q: q.data.startswith("egg"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.egg1), lambda q: q.data.startswith("EggOne"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.egg2), lambda q: q.data.startswith("EggTwo"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.actions), lambda q: q.data.startswith("action"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.items_shop), lambda q: q.data.startswith("items"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(grass.Grass_random), lambda q: q.data.startswith("grassOne"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(grass.Grass_random2), lambda q: q.data.startswith("grassTwo"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(eggs.OpenDefEgg), lambda q: q.data.startswith("DefEgg"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(eggs.OpenPremEgg), lambda q: q.data.startswith("PremEgg"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.glove_buy), lambda q: q.data.startswith("gloveItems"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.back_button), lambda q: q.data.startswith("back"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(Torgoves.sell_gold_dog), lambda q: q.data.startswith("sell"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.vipn), lambda q: q.data.startswith("vipnext"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(shop.buy_vip), lambda q: q.data.startswith("buyvip"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(viper.viper_random1), lambda q: q.data.startswith("randomOne"))
    dp.register_callback_query_handler(
        dp.throttled(rate=2)(viper.viper_random2), lambda q: q.data.startswith("randomTwo"))



    # rp commands
    dp.register_message_handler(
    rp_commands.obnyt,
    filters.Command(('обнять', 'j,yznm'), prefixes=''))

    dp.register_message_handler(
    rp_commands.poselovat,
    filters.Command(('поцеловать', 'gjwtkjdfnm'), prefixes=''))

    dp.register_message_handler(
    rp_commands.ydarit,
    filters.Command(('ударить', 'elfhbnm'), prefixes=''))

    dp.register_message_handler(
    rp_commands.napast,
    filters.Command(('напасть', 'yfgfcnm'), prefixes=''))

    dp.register_message_handler(
    rp_commands.poglidit,
    filters.Command(('погладить', 'gjukflbnm'), prefixes=''))

    dp.register_message_handler(
    rp_commands.vipit,
    filters.Command(('бухнуть', 'выпить', ',e[yenm', 'dsgbnm'), prefixes=''))

    dp.register_message_handler(
    rp_commands.vikinyt,
    filters.Command(('выкинуть', 'dsrbyenm'), prefixes=''))
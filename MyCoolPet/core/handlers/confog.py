from aiogram import types, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="6126740167:AAF195WT8uuCaJ1R4c7Y1juC8wP8hQxeG6s")
dp = Dispatcher(bot, storage=MemoryStorage())

admin_id_list = [1355948406, 5234721702]

pets_id = {
    1:'батерфри',
    2:'золотой батерфри',
    3:'собака',
    4:'золотая собака',
    5:'свинья',
    6:'золотая свинья',
    7:'тыква',
    8:'корова',
    9:'золотая корова',
    10:'VIP',
    11:'лугия',
    12:'бульбозавр',
    13:'тортанк',
    14:'сквиртл',
}

#https://telegra.ph/Vse-pitomcy-10-09 - НЕ ЗАБУДЬ

pets_all = 14

wear_pet = {
    1:'CAACAgIAAxkBAAGpNwNkFH2wlIW5M0XR81GUR5nDjU1RtgACWygAAtjHqEiiLCBHHlqIzi8E', #батерфри
    2:'CAACAgIAAxkBAAGpdRBkFZdF29B0TTXcQ_G-hgszIuV-OgAC-iYAAmrRsUhZwh-m8CZxbC8E', #золотой батерфри
    3:'CAACAgIAAxkBAAGrgLFkHDjXOGRLPUvvO3-_7b2ZfhlIowACESsAAnd84UiDMreXoOmF6i8E', #собака
    4:'CAACAgIAAxkBAAGrgLtkHDjeENk-1hOLq8X65VQI2blicAACPC0AAnRC4UieO75hKA8HrC8E', #золотая собака
    5:'CAACAgIAAxkBAAGtS81kIrJf_fhVkM5l2_8b0r0wNouNowACZSgAAoY6EEndYn3NOjvzDy8E', #свинья
    6:'CAACAgIAAxkBAAGtS9NkIrJt37w_YwABS1qcDrtDlMB2cdsAAmApAAJNpRhJ3DKZS9cfkOsvBA', #золотая свинья
    7:'CAACAgIAAxkBAQO4hGUjyZGpUJrrinTT1UFb6yjqEGnEAAJhNQACLaYgSVioliw8m4RcMAQ', #тыква
    8:'CAACAgIAAxkBAQPAlGUj4P6Y021LrbhCD2UsGHxd_w3uAAK2OgACP48gSRBryxxN3lIBMAQ', #корова
    9:'CAACAgIAAxkBAQPCdWUj5-NagNFuk_AFqjFyvms279bmAAJ-OQACknohSRJ4bLMlRuIHMAQ', #золотая корова
    10:'CAACAgIAAxkBAQQp12UlHcXBTqGKNf1tRQ7TNBpxz6sGAALaOAACuf0oSWdKyhjljQlmMAQ', #VIP
    11:'CAACAgIAAxkBAQRBamUlUdDY2FwBA1wG0h0jDHIj8d7NAAKkPwACO9EoST4ZQJAlz6j7MAQ', #лугия
    12:'CAACAgIAAxkBAQRBbGUlUdP8alTLpp-c6XkZEURx1XIzAAK1OwAC6EkxSVF4OfY6syaMMAQ',
    13:'CAACAgIAAxkBAQRBbmUlUdWLCUqgs1gnh7_C-YBPpirnAALcNgACZJ8pSWS01eiPEjLgMAQ',
    14:'CAACAgIAAxkBAQRBXmUlUa2IWAABKy7jO-NuZTqws_dlRQACmjcAAk3GMUl6WU4xWJEqFjAE',
}

rare_pet = {
    1:'🤍', #батерфри
    2:'⭐', #золотой батерфри
    3:'🤍', #собака
    4:'⭐', #золотая собака
    5:'🤍', #свинья
    6:'⭐', #золотая свинья
    7:'🤍', #тыква
    8:'🤍', #корова
    9:'⭐', #золотая корова
    10:'🤍', #VIP
    11:'🤍',
    12:'🤍',
    13:'🤍',
    14:'🤍',
}

common = [1,2,3,4,5,6,8,9,]
rare = []
legendary = [11,12,13]
mystic = [14]
exclusive_id = [7, 10]

x1 = [1,2,3,4,5,6,8,9,]
x2 = [10,11,12,13,14,]
x3 = [7]
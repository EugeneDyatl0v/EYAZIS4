from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

text = """
It is impossible to imagine our civilization without electricity: economic and social progress will be turned to the past and our daily lives completely transformed. Electrical power has become universal. Thousands of applications of electricity such as lighting, electrochemistry and electrometallurgy are longstanding and unquestionable. With the appearance of the electrical motor, power cables replaced transmission shafts, gear wheels, belts and pulleys in the 19-th century workshops. And in the home a whole range of various time and labour saving appliances have become a part of our everyday lives. Other devices are based on specific properties of electricity: electrostatics in the case of photocopying machine and electromagnetism in the case of radar and television. These applications have made electricity most widely used. The first industrial application was in the silver workshops in Paris. The generator – a new compact source of electricity – was also developed there. The generator replaced the batteries and other devices that had been used before. Electric lighting came into wide use at the end of the last century with the development of the electric lamp by Thomas Edison. Then the transformer was invented, the first electric lines and networks were set up, dynamos and induction motors were designed. Since the beginning of the 20-th century the successful development of electricity has begun throughout the industrial world. The consumption of electricity has doubled every ten years. Today consumption of electricity per capita is an indicator of the state of development and economic health of a nation. Electricity has replaced other sources of energy as it has been realized that it offers improved service and reduced cost. One of the greatest advantages of electricity is that it is clean, easilyregulated and generates no by-products . Applications of electricity now cover all fields of human activity from house washing machines to the latest laser devices. Electricity is the efficient source of some of the most recent technological advances such as the laser and electron beams. Truly electricity provides mankind with the energy of the future.
"""
translated_text = translate_text(text, 'ru')
print(text.replace('\n', ' '))

"""Невозможно представить нашу цивилизацию без электричества: экономический и социальный прогресс будет превращен в прошлое, и наша повседневная жизнь полностью преобразована. Электрическая мощность стала универсальной. Тысячи применений электроэнергии, такие как освещение, электрохимия и электрометаллургия, давние и неоспоримые. С появлением электрического двигателя кабели силовых валов трансмиссии, колеса передач, ремни и шкивы на семинарах 19-го века. И в доме целый ряд различных времен и технических приборов стал частью нашей повседневной жизни. Другие устройства основаны на конкретных свойствах электричества: электростатика в случае фотокопирующей машины и электромагнетизма в случае радара и телевидения. Эти приложения сделали электроэнергию наиболее широко использоваться. Первое промышленное применение было в серебряных семинарах в Париже. Генератор - новый компактный источник электричества - также был разработан там. Генератор заменил батареи и другие устройства, которые использовались ранее. Электрическое освещение стало широко использоваться в конце прошлого века с разработкой электрической лампы Томаса Эдисона. Затем был изобретен трансформатор, были созданы первые электрические линии и сети, были разработаны динамо и индукционные двигатели. С начала 20-го века успешное развитие электроэнергии началось во всем промышленном мире. Потребление электроэнергии удвоилось каждые десять лет. Сегодня потребление электроэнергии на душу населения является показателем состояния развития и экономического здоровья нации. Электричество заменило другие источники энергии, так как было понятно, что он предлагает улучшенное обслуживание и снижение затрат. Одним из величайших преимуществ электричества является то, что оно чистое, легко регулируется и не генерирует побочных продуктов. Применение электроэнергии теперь охватывает все области человеческой деятельности от домашних стиральных машин до последних лазерных устройств. Электричество является эффективным источником некоторых из самых последних технологических достижений, таких как лазерные и электронные балки. Поистине электричество дает человечеству энергию будущего."""
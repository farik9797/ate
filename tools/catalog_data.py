"""Русские тексты для каталога: переводы данных ESPA и данные Hidrostal.

Источники:
  ESPA      — espa.com (раздел UK), страницы серий: Information / Specifications / Literature.
  Hidrostal — hidrostal.com, страницы семейств насосов (официальный RU-текст для погружных
              насосов, остальное — перевод с EN-версии сайта производителя).
Цифры не придумываются: всё, чего нет у производителя, на сайте не выводится.
"""

# ---------------------------------------------------------------- ESPA: категории
ESPA_CATEGORIES = [
    ("skvazhinnye", "Скважинные насосы", "Моноблочные многоступенчатые насосы Acuaria 5–6\" для скважин"),
    ("skvazhinnye-chasti", "Скважинные гидравлические части и двигатели", "Гидравлические части ES4 4\" и погружные двигатели 4\""),
    ("gorizontalnye", "Горизонтальные поверхностные насосы", "Многоступенчатые самовсасывающие насосы Aspri и Tecno"),
    ("vertikalnye", "Вертикальные поверхностные насосы", "Многоступенчатые насосы Multi, VE и Multi VS (In-Line)"),
    ("stancii", "Насосы и установки повышения давления", "Автоматические насосы Tecnopres, Tecnoplus, Acuapres, установки Sub-tank и CKE"),
    ("avtomatika", "Устройства управления и автоматики", "Реле Pressdrive, гидроаккумуляторы CIMM, преобразователь частоты Speedrive"),
    ("basseyny", "Насосы для бассейнов", "Насосы Silen для рециркуляции и фильтрации воды"),
    ("drenazh", "Дренажные и канализационные насосы", "Vigila, Drain, Drainex, Draincor для сточных и грязных вод"),
]

# ---------------------------------------------------------------- ESPA: переводы
SUBTITLES = {
    '5,5" submersible monoblock centrifugal multistage pump for water supply.': 'Скважинный моноблочный центробежный многоступенчатый насос 5,5" для водоснабжения.',
    '6" submersible monoblock centrifugal multistage pump for water supply.': 'Скважинный моноблочный центробежный многоступенчатый насос 6" для водоснабжения.',
    '5" submersible monoblock centrifugal multistage pump for water supply.': 'Скважинный моноблочный центробежный многоступенчатый насос 5" для водоснабжения.',
    '4" submersible centrifugal multistage wet end with floating impellers for water supply.': 'Скважинная гидравлическая часть 4": центробежная многоступенчатая, с плавающими рабочими колёсами, для водоснабжения.',
    'Submersible motor for 4” wet end.': 'Погружной электродвигатель для гидравлической части 4".',
    'Horizontal centrifugal multistage pump for water supply, self-priming up to 9m.': 'Горизонтальный центробежный многоступенчатый насос для водоснабжения, самовсасывание до 9 м.',
    'Vertical centrifugal multistage pump for water supply.': 'Вертикальный центробежный многоступенчатый насос для водоснабжения.',
    'In-Line vertical centrifugal multistage pump for water supply.': 'Вертикальный центробежный многоступенчатый насос In-Line для водоснабжения.',
    'In-Line vertical centrifugal multistage pump for water supply, 100% stainless steel.': 'Вертикальный центробежный многоступенчатый насос In-Line для водоснабжения, полностью из нержавеющей стали.',
    'Automatic centrifugal multistage pump for water supply.': 'Автоматический центробежный многоступенчатый насос для водоснабжения.',
    'Automatic centrifugal multistage pump with variable speed for water supply.': 'Автоматический центробежный многоступенчатый насос с регулируемой частотой вращения для водоснабжения.',
    'Automatic submersible monoblock centrifugal multistage pump for water supply.': 'Автоматический погружной моноблочный центробежный многоступенчатый насос для водоснабжения.',
    'Automatic set with fixed speed for water supply.': 'Автоматическая установка с постоянной частотой вращения для водоснабжения.',
    'Automatic set with variable speed for water supply.': 'Автоматическая установка с регулируемой частотой вращения для водоснабжения.',
    'Automatic booster set with variable speed for water supply.': 'Автоматическая установка повышения давления с регулируемой частотой вращения.',
    'Automatic start and stop device.': 'Устройство автоматического пуска и останова насоса.',
    'Pressure vessels.': 'Гидроаккумуляторы (напорные баки).',
    'Variable frequency drive.': 'Преобразователь частоты.',
    'Centrifugal single stage pump with variable speed for water recirculation and filtration.': 'Центробежный одноступенчатый насос с регулируемой частотой вращения для рециркуляции и фильтрации воды.',
    'Centrifugal single stage pump for water recirculation and filtration.': 'Центробежный одноступенчатый насос для рециркуляции и фильтрации воды.',
    'Portable submersible pump for wastewater.': 'Переносной погружной насос для сточных вод.',
    'Portable submersible pump for wastewater with solids in suspension, vortex system.': 'Переносной погружной насос для сточных вод со взвешенными частицами, вихревое рабочее колесо (Vortex).',
    'Submersible pump for wastewater with solids in suspension, grinder system.': 'Погружной насос для сточных вод со взвешенными частицами, с режущим механизмом.',
    'Submersible pump for wastewater.': 'Погружной насос для сточных вод.',
    'Submersible pump for wastewater with solids in suspension, vortex system.': 'Погружной насос для сточных вод со взвешенными частицами, вихревое рабочее колесо (Vortex).',
}

_CLEAN = "Перекачивание чистой воды для бытовых, промышленных, сельскохозяйственных и садовых нужд."
_APPS = "Подходит для перекачки воды, дождевального и капельного полива, повышения давления в доме и установок повышения давления."
_AUTO = "Автоматическая подача чистой воды для бытовых, промышленных, сельскохозяйственных и садовых нужд."
_VS = "Регулирование частоты вращения поддерживает постоянное давление и расход, которые требуются квартире, зданию или установке в каждый момент времени."
_AUTO_APPS = "Подходит для дождевального и капельного полива, перекачки воды и повышения давления в доме."
_DRAIN_APPS = "Применение: откачка воды из затопленных гаражей и подвалов, дренажи, бытовые приямки, резервуары, перекачка воды из баков и цистерн."

DESCRIPTIONS = {
    "Pumping of clean water for domestic, industrial, agricultural and gardening purposes. Suitable for open wells, ponds and tanks in applications like water transfer, sprinkler or drip irrigation, domestic booster or booster sets.":
        f"{_CLEAN} Подходит для открытых колодцев, водоёмов и резервуаров: перекачка воды, дождевальный и капельный полив, повышение давления в доме и установки повышения давления.",
    "Assembled on a motor, pumping of clean water for domestic, industrial, agricultural and gardening purposes. Suitable for boreholes in applications like water transfer, sprinkler or drip irrigation, domestic booster or booster sets. Joint kit wet end-motor according NEMA MG1-18.388 regulation.":
        f"Монтируется на электродвигатель. {_CLEAN} Подходит для скважин: перекачка воды, дождевальный и капельный полив, повышение давления в доме и установки повышения давления. Соединение гидравлической части с двигателем — по стандарту NEMA MG1-18.388.",
    "To be assembled on 4” submersible wet end.": "Устанавливается на погружную гидравлическую часть 4\".",
    "Water cooled encapsulated PSC motors.": "Герметичные двигатели PSC с водяным охлаждением.",
    "4” NEMA flange.": "Фланец 4\" NEMA.",
    "Pumping of clean water for domestic, industrial, agricultural and gardening purposes. Suitable for applications like water transfer, sprinkler or drip irrigation, domestic booster or booster sets. Silent. Self-priming up to 9m.":
        f"{_CLEAN} {_APPS} Низкий уровень шума. Самовсасывание до 9 м.",
    "Pumping of clean water for domestic, industrial, agricultural and gardening purposes. Suitable for applications like water transfer, sprinkler or drip irrigation, domestic booster or booster sets. Silent.":
        f"{_CLEAN} {_APPS} Низкий уровень шума.",
    "Pumping of clean water for domestic, industrial, agricultural and gardening purposes. Suitable for applications like water transfer, sprinkler or drip irrigation, domestic booster or booster sets.":
        f"{_CLEAN} {_APPS}",
    "Automatic pumping of clean water for domestic, industrial, agricultural and gardening purposes. Operation is automatic start and stop based on water demand. Suitable for applications like sprinkler or drip irrigation, water transfer or domestic booster. Silent. Self-priming up to 2m. Starting pressure 2 bar.":
        f"{_AUTO} Насос автоматически включается и отключается в зависимости от водоразбора. {_AUTO_APPS} Низкий уровень шума. Самовсасывание до 2 м. Давление включения 2 бар.",
    "Automatic pumping of clean water for domestic, industrial, agricultural and gardening purposes. Operation is variable speed to maintain the constant pressure and flow that apartment, building or installation demands at every moment. Suitable for applications like sprinkler or drip irrigation, water transfer or domestic booster. Silent. Self-priming up to 2m. Adjustable working pressure range from 1,5 to 3,5 bar.":
        f"{_AUTO} {_VS} {_AUTO_APPS} Низкий уровень шума. Самовсасывание до 2 м. Рабочее давление настраивается в диапазоне 1,5–3,5 бар.",
    "Automatic pumping of clean water for domestic, industrial, agricultural and gardening purposes. Operation is variable speed to maintain the constant pressure and flow that apartment, building or installation demands at every moment. Suitable for applications like sprinkler or drip irrigation, water transfer or domestic booster. Silent. Self-priming up to 2m. Adjustable working pressure range from 1,5 to 4 bar.":
        f"{_AUTO} {_VS} {_AUTO_APPS} Низкий уровень шума. Самовсасывание до 2 м. Рабочее давление настраивается в диапазоне 1,5–4 бар.",
    "Automatic pumping of clean water for domestic, industrial, agricultural and gardening purposes. Operation is automatic start and stop based on water demand. Suitable for open wells, ponds and tanks in applications like sprinkler or drip irrigation, water transfer or domestic booster. Starting pressure 2 bar.":
        f"{_AUTO} Насос автоматически включается и отключается в зависимости от водоразбора. Подходит для открытых колодцев, водоёмов и резервуаров: дождевальный и капельный полив, перекачка воды, повышение давления в доме. Давление включения 2 бар.",
    "To restore system pressure when the mains supply is insufficient, a pump may be used. However to comply with Water Authority Byelaws, a break tank must be incorporated, as the pump may not be connected directly to the mains water supply.":
        "Установка восстанавливает давление в системе, когда давления в водопроводе недостаточно. По требованиям водоснабжающих организаций (нормы Великобритании) насос подключается через разрывной бак, а не напрямую к водопроводной сети.",
    "Automatic pumping of clean water for domestic, industrial, agricultural and gardening purposes. Operation is variable speed to maintain the constant pressure and flow that apartment, building or installation demands at every moment. Suitable for applications like sprinkler or drip irrigation, water transfer or domestic booster. Silent. Adjustable working pressure.":
        f"{_AUTO} {_VS} {_AUTO_APPS} Низкий уровень шума. Рабочее давление настраивается.",
    "Assembled on a pump, automatic start and stop based on water demand. Adjustable starting pressure range from 1,5 to 2,5 bar. 90º pump-pipe connection.":
        "Монтируется на насос и автоматически включает и отключает его в зависимости от водоразбора. Давление включения настраивается в диапазоне 1,5–2,5 бар. Подключение насос–трубопровод под углом 90°.",
    "Assembled on a pump, automatic start and stop based on water demand. Adjustable starting pressure range from 1,5 to 2,5 bar. In-Line pump-pipe connection.":
        "Монтируется на насос и автоматически включает и отключает его в зависимости от водоразбора. Давление включения настраивается в диапазоне 1,5–2,5 бар. Подключение насос–трубопровод соосное (In-Line).",
    "Accumulation of pressurised water for all hydraulic domestic, agricultural and industrial applications.":
        "Накопление воды под давлением для бытовых, сельскохозяйственных и промышленных гидравлических систем.",
    "Assembled on a pump or booster set, adjusts the speed automatically to maintain the constant pressure and flow that apartment, building or installation demands at every moment. Adjustable working pressure.":
        "Монтируется на насос или установку повышения давления и автоматически регулирует частоту вращения, поддерживая постоянное давление и расход, которые требуются квартире, зданию или установке в каждый момент времени. Рабочее давление настраивается.",
    "Water recirculation and filtration for small, medium and large residential swimming pools. Silent. Self-priming up to 4m.":
        "Рециркуляция и фильтрация воды в малых, средних и больших частных бассейнах. Низкий уровень шума. Самовсасывание до 4 м.",
    "Water recirculation and filtration for small residential swimming pools. Silent. Self-priming up to 4m.":
        "Рециркуляция и фильтрация воды в малых частных бассейнах. Низкий уровень шума. Самовсасывание до 4 м.",
    "Water recirculation and filtration for medium residential swimming pools. Silent. Self-priming up to 4m.":
        "Рециркуляция и фильтрация воды в частных бассейнах среднего размера. Низкий уровень шума. Самовсасывание до 4 м.",
    "Water recirculation and filtration for large residential swimming pools. Silent. Self-priming up to 4m.":
        "Рециркуляция и фильтрация воды в больших частных бассейнах. Низкий уровень шума. Самовсасывание до 4 м.",
    "Pumping for evacuation, transfer and emptying of wastewater and emptying of swimming pools. Applications like emptying of flooded garages or basements, drains, residential sumps, water tanks or transfer of water from tanks and cisterns.":
        f"Откачка, перекачка и опорожнение: сточные воды, опорожнение бассейнов. {_DRAIN_APPS}",
    "Pumping of evacuation, transfer and emptying of wastewater with solids in suspension. Applications like emptying of flooded garages or basements, drains, residential sumps, water tanks or transfer of water from tanks and cisterns.":
        f"Откачка, перекачка и опорожнение сточных вод со взвешенными частицами. {_DRAIN_APPS}",
    "Pumping for evacuation, transfer and emptying of wastewater. Applications like emptying of flooded garages or basements, drains, residential sumps, water tanks or transfer of water from tanks and cisterns.":
        f"Откачка, перекачка и опорожнение сточных вод. {_DRAIN_APPS}",
}

GROUPS = {
    "Electrical features": "Электрические характеристики",
    "Equipment": "Комплектация",
    "Limitations": "Ограничения",
    "Manufacturing features": "Конструкция",
    "Materials": "Материалы",
}

KEYS = {
    "Ambient temperature (ºC)": "Температура окружающей среды, °C",
    "Check valve": "Обратный клапан",
    "Counter flanges": "Ответные фланцы",
    "Diffuser/s": "Диффузоры",
    "Discharge body": "Напорный корпус",
    "Discharge connection type": "Тип напорного соединения",
    "Discharge diameter": "Диаметр напорного патрубка",
    "Electrical isolation": "Класс изоляции",
    "Impeller/s": "Рабочие колёса",
    "Maximum sand quantity in suspension (g/m3)": "Макс. содержание песка, г/м³",
    "Maximum solids passage (mm)": "Макс. размер твёрдых частиц, мм",
    "Maximum submersion (m)": "Макс. глубина погружения, м",
    "Maximum suction (m)": "Макс. высота всасывания, м",
    "Maximum working pressure (bar)": "Макс. рабочее давление, бар",
    "Mechanical seal": "Торцевое уплотнение",
    "Motor casing": "Корпус двигателя",
    "Motor cooling": "Охлаждение двигателя",
    "Motor type": "Тип двигателя",
    "O-rings": "Уплотнительные кольца",
    "Pre-filter": "Префильтр",
    "Pressure gauge": "Манометр",
    "Pressure sensor": "Датчик давления",
    "Protection rating": "Степень защиты",
    "Pump body": "Корпус насоса",
    "Pump shaft": "Вал насоса",
    "Reset": "Сброс тепловой защиты",
    "Seal type": "Тип уплотнения",
    "Service factor": "Режим работы",
    "Starting pressure": "Давление включения",
    "Suction body": "Всасывающий корпус",
    "Suction connection type": "Тип всасывающего соединения",
    "Suction diameter": "Диаметр всасывающего патрубка",
    "Tank capacity (l)": "Объём бака, л",
    "Water temperature (ºC)": "Температура воды, °C",
}

VALUES = {
    "Not included": "Не входит",
    "Included": "Входит",
    "Thread": "Резьбовое",
    "Thread (3-piece union)": "Резьбовое (разъёмное соединение из 3 частей)",
    "Flange": "Фланцевое",
    "Glue union": "Клеевое соединение",
    "Hose connector": "Штуцер для шланга",
    "Water": "Водяное",
    "Fan": "Вентилятор",
    "Double mechanical seal": "Двойное торцевое уплотнение",
    "Mechanical seal": "Торцевое уплотнение",
    "Double lip seal": "Двойное манжетное уплотнение",
    "F Class": "Класс F",
    "Asynchronous": "Асинхронный",
    "Automatic": "Автоматический",
    "S1": "S1 (продолжительный)",
    "Technopolymer": "Технополимер",
    "Technopolymer reinforced with steel": "Технополимер, армированный сталью",
    "Stainless steel AISI 304": "Нержавеющая сталь AISI 304",
    "Stainless steel AISI 420": "Нержавеющая сталь AISI 420",
    "Stainless Steel AISI 420": "Нержавеющая сталь AISI 420",
    "Stainless steel AISI 431": "Нержавеющая сталь AISI 431",
    "AISI 304": "Нержавеющая сталь AISI 304",
    "Aluminium-Graphite": "Оксид алюминия — графит",
    "Aluminium": "Алюминий",
    "Cast iron": "Чугун",
    "Brass": "Латунь",
    "10 bar": "10 бар",
    "1,5 - 2,5 bar": "1,5–2,5 бар",
    "Dual 50mm - 63mm": "Двойное: 50 мм / 63 мм",
}

TABLE_HEADS = {
    "Single-phase models": "Однофазные модели",
    "Three-phase models": "Трёхфазные модели",
    "Intensity [A]": "Ток, А",
    "Input power P1 [kW]": "Потребляемая мощность P1, кВт",
    "Motor power P2": "Мощность двигателя P2",
    "50 Hz": "50 Гц",
    "[kW]": "кВт",
    "[HP]": "л.с.",
}

DOC_TYPES = [  # (признак в имени файла, подпись)
    ("instruction", "Инструкция по эксплуатации (EN)"),
    ("manual", "Инструкция по эксплуатации (EN)"),
    ("spare-parts", "Деталировка и запасные части"),
    ("catalogue-espa-pool", "Каталог ESPA Pool 2026 (EN)"),
    ("catalogue-espa-corporate", "Технический каталог ESPA 2025, 50 Гц (EN)"),
    (".zip", "3D-модель (архив)"),
    ("certf-9001", "Сертификат ISO 9001"),
    ("certf-14001", "Сертификат ISO 14001"),
    ("certif", "Сертификат"),
]

ESPA_CATALOGUE_PDF = "https://www.espa.com/download/docs/7622/catalogue-espa-corporate-2025-50hz-eng.pdf"
ESPA_POOL_PDF = "https://www.espa.com/download/docs/7658/catalogue-espa-pool-2026-eng.pdf"

# ---------------------------------------------------------------- Hidrostal
HIDROSTAL_CATEGORIES = [
    ("centrobezhnye", "Центробежные насосы с винтовым рабочим колесом", "Погружные, с рубашкой охлаждения, компактные и консольные насосы"),
    ("osevye", "Осевые и вертикальные турбинные насосы", "Большие расходы при малом напоре и высоконапорные вертикальные насосы"),
    ("sistemy", "Насосные системы и перемешивание", "PreroClean, Prerostal, SuperBetsy, плавучие станции, HidroMix"),
]

HS = "https://www.hidrostal.com/"
HIDROSTAL = [
    {
        "slug": "submersible", "category": "centrobezhnye", "name": "Погружные насосы Hidrostal",
        "short": "Погружные насосы",
        "page": HS + "submersiblepumps.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/submersiblepumps_1/Thumb/submersible-pump.jpg",
        "subtitle": "Работают непрерывно, погружёнными в перекачиваемую среду.",
        "description": [
            "Погружные насосы Hidrostal оснащены уникальным винтовым центробежным рабочим колесом. Они подходят как для обычной грязной воды, так и для технологических жидкостей с высоким содержанием твёрдых частиц или волокон. Насос перекачивает высококонцентрированные шламы и жидкости в сложных условиях.",
            "Погружные насосы Hidrostal долговечны, не засоряются и просты в обслуживании. Погружные электродвигатели разработаны и изготовлены компанией Hidrostal, механические торцевые уплотнения обеспечивают длительный срок службы. Модульная конструкция и собственное производство двигателей позволяют адаптировать насос к конкретному применению.",
            "Насосы устанавливаются непосредственно в приямок, что снижает инвестиционные затраты. Опционально доступна автоматическая трубная муфта с направляющими: она упрощает монтаж и доступ для обслуживания. Для абразивных и коррозионно-активных сред доступны регулировка зазора между рабочим колесом и конусом и различные материалы исполнения.",
        ],
        "highlights": [
            "Компактный интегрированный дизайн",
            "Нет открытых вращающихся валов и муфт",
            "Минимальный уровень шума",
            "Гидравлика без засоров",
            "Надёжная конструкция для требовательных задач",
            "Эффективное охлаждение снижает тепловую нагрузку на двигатель и температуру поверхности",
            "Автоматическая трубная муфта упрощает установку и обслуживание",
            "Множество опций контроля и защиты",
            "Вертикальная установка",
        ],
        "applications": [],
        "specs": [
            ("Размер напорного патрубка", "50–700 мм"),
            ("Напор", "до 100 м"),
            ("Подача", "до 2500 л/с"),
            ("Мощность", "0,55–400 кВт"),
            ("Частота", "50 Гц, 60 Гц, ЧРП"),
            ("Материалы", "чугун, высокопрочный чугун, хромистый чугун, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 2500 л/с", "h": "до 100 м", "p": "0,55–400 кВт"},
        "docs": [("Брошюра «Погружные насосы» (RU)", HS + "Dokumente/Download_325/submersible-pumps-pr09194_ru.pdf"),
                 ("Брошюра: погружные насосы и насосы сухой установки (EN)", HS + "Dokumente/Download_342/submersibledrywellimmersiblepumps.pdf"),
                 ("Брошюра: насосы со спиральным корпусом (EN)", HS + "Dokumente/Download_344/volutepumps.pdf")],
    },
    {
        "slug": "immersible", "category": "centrobezhnye", "name": "Погружные насосы с рубашкой охлаждения Hidrostal",
        "short": "Насосы с рубашкой охлаждения",
        "page": HS + "immersiblepumps.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/immersiblepumps_1/Thumb/immersible-pump.jpg",
        "subtitle": "Работают непрерывно — и на воздухе, и под водой.",
        "description": [
            "Насосы Hidrostal с рубашкой охлаждения (Immersible) справляются со сложными коммунальными и промышленными сточными водами. Вязкие жидкости, хрупкие хлопья и даже живая рыба не представляют для них проблемы.",
            "Независимая замкнутая система охлаждения позволяет двигателю работать как в мокрой, так и в сухой камере. Двигатель не охлаждается перекачиваемой средой, поэтому нет перегрева из-за отложений в каналах охлаждения. Утечки исключены благодаря тандемным уплотнениям в масляной ванне. Насосы особенно подходят там, где нужны тихая работа, чистота помещения и длительная безотказная эксплуатация.",
        ],
        "highlights": [
            "Сухая установка: защита от затопления",
            "Вертикальная или горизонтальная установка",
            "Компактный и простой монтаж",
            "Тихая работа, холодный корпус",
            "Нет утечек перекачиваемой среды",
            "Нет открытых вращающихся валов и муфт",
            "Насос легко вскрыть для осмотра",
            "Мокрая установка: монтаж как у погружных насосов",
            "Уровень жидкости можно опускать до корпуса насоса без риска перегрева двигателя",
            "Более мелкие приямки по сравнению с обычными погружными насосами",
        ],
        "applications": [],
        "specs": [
            ("Размер напорного патрубка", "50–700 мм"),
            ("Размер всасывающего патрубка", "65–700 мм"),
            ("Напор", "0,5–90 м"),
            ("Подача", "0,5–3000 л/с"),
            ("Мощность", "0,1–650 кВт"),
            ("Частота", "50 Гц, 60 Гц, ЧРП"),
            ("Материалы", "чугун, высокопрочный чугун, хромистый чугун, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 3000 л/с", "h": "до 90 м", "p": "0,1–650 кВт"},
        "docs": [("Брошюра «Насосы с рубашкой охлаждения» (EN)", HS + "Dokumente/Download_176/immersible-pumps-pr08974_en.pdf"),
                 ("Брошюра «Двигатели Tuma» (EN)", HS + "Dokumente/Download_225/submersible-motors-tuma-pr10265_en.pdf")],
    },
    {
        "slug": "compact", "category": "centrobezhnye", "name": "Компактные насосы Hidrostal",
        "short": "Компактные насосы",
        "page": HS + "compactpumps.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/compactpumps_1/Thumb/hidrostal-kompaktpumpe-a2u-e1ev3-pz_highres-kopie.jpg",
        "subtitle": "Небольшие, переносные и всегда готовые к работе.",
        "description": [
            "Компактные насосы Hidrostal работают без засоров в сложных условиях. Их используют для шламов и сточных вод, в службах ЧС и пожарных частях, на стройплощадках и даже в частных домах.",
            "Это прочные полевые агрегаты, которые сочетают удобство с гидравликой винтового центробежного колеса. Подходят для коммунальных и промышленных сточных вод, шламов и грязи, а также для защиты от наводнений — в переносном и стационарном исполнении.",
        ],
        "highlights": [
            "Напор до 17,7 м или подача до 24,6 л/с",
            "Масса 23 кг вместе с кабелем 5 м",
            "Свободный проход для твёрдых частиц 50–75 мм",
            "Перекачивает жидкости с волокнистыми включениями",
            "Крутая характеристика: запас давления и мощности на густых средах",
            "КПД двигателя до уровня IE3",
            "Неперегружаемая кривая мощности",
            "Двойное торцевое уплотнение",
            "Доступно взрывозащищённое исполнение",
        ],
        "applications": ["Промышленные стоки", "Вязкий ил", "Возвратный активный ил", "Дренаж", "Технологические отходы",
                          "Очистка приямков", "Стройплощадки", "Защита от наводнений", "Службы ЧС и пожарные части"],
        "specs": [
            ("Размер напорного патрубка", "50–80 мм"),
            ("Размер всасывающего патрубка", "50–80 мм"),
            ("Напор", "0,5–17,7 м"),
            ("Подача", "0,8–24,6 л/с"),
            ("Мощность", "0,1–2,4 кВт"),
            ("Частота", "50 Гц, 60 Гц, ЧРП"),
            ("Напряжение, 3 фазы", "380, 400, 415, 460, 480, 575 В"),
            ("Материалы", "чугун, высокопрочный чугун, хромистый чугун, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 24,6 л/с", "h": "до 17,7 м", "p": "0,1–2,4 кВт"},
        "docs": [("Брошюра «Компактные насосы» (EN)", HS + "Dokumente/Download_174/compact-pumps-pr08975_en.pdf")],
    },
    {
        "slug": "end-suction", "category": "centrobezhnye", "name": "Консольные насосы Hidrostal",
        "short": "Консольные насосы",
        "page": HS + "bearingframepumps.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/bearingframepumps_1/Thumb/lagerstuhl_optionparallel.jpg",
        "subtitle": "Горизонтальная и вертикальная установка, три варианта конструкции.",
        "description": [
            "Hidrostal выпускает консольные насосы в трёх исполнениях; все подходят для горизонтального и вертикального монтажа.",
            "С прямым соединением: двигатель крепится фланцем к подшипниковому узлу, что исключает несоосность валов; дополнительно применяется упругая муфта. Конструкция Back pull-out позволяет извлечь весь ротор вместе с двигателем для осмотра гидравлической части. Напорный патрубок 50–700 мм.",
            "Со свободным концом вала: подшипниковые узлы такие же, как у исполнения с прямым соединением, но со свободным концом вала. Напорный патрубок 50–700 мм.",
            "С удлинённым валом: традиционная прочная конструкция для долгой работы. Подшипники со смазкой, для горизонтальных агрегатов возможна масляная смазка. Модульный корпус подшипников допускает разные схемы торцевых уплотнений; подшипники рассчитаны на ремённый привод.",
        ],
        "highlights": [
            "Прямой доступ к насосу и КИП",
            "Обслуживание в чистом помещении",
            "Можно использовать стандартные приводы",
            "Прочная конструкция, плавная работа",
            "Конструкция Back pull-out: ротор извлекается для обслуживания гидравлики",
            "Усиленные подшипники с высоким ресурсом L-10 при прямом и ремённом приводе",
        ],
        "applications": ["Промышленные стоки", "Неочищенные сточные воды", "Вязкий ил", "Возвратный активный ил",
                          "Дренажные и ливневые воды", "Технологические отходы", "Очистка приямков",
                          "Бактериальные хлопья", "Живая рыба", "Фрукты и овощи"],
        "specs": [
            ("Размер напорного патрубка", "32–700 мм"),
            ("Размер всасывающего патрубка", "32–700 мм"),
            ("Напор", "0,5–90 м"),
            ("Подача", "0,5–3000 л/с"),
            ("Мощность", "0,1–650 кВт"),
            ("Частота", "50 Гц, 60 Гц, ЧРП"),
            ("Материалы", "чугун, высокопрочный чугун, хромистый чугун, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 3000 л/с", "h": "до 90 м", "p": "0,1–650 кВт"},
        "docs": [("Брошюра «Консольные насосы» (EN)", HS + "Dokumente/Download_175/horizontal-vertikal-end-suction-pumps-pr08977_en.pdf")],
    },
    {
        "slug": "axial-column", "category": "osevye", "name": "Осевые трубно-шахтные насосы Hidrostal",
        "short": "Осевые трубно-шахтные насосы",
        "page": HS + "axialcolumnpump.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/axialcolumnpump_1/Thumb/axial-pump.jpg",
        "subtitle": "Для больших объёмов воды при низком напоре.",
        "description": [
            "Осевой насос Hidrostal рассчитан на низкий напор и применяется, когда нужно перекачивать большие объёмы жидкости на небольшую высоту — например, на станциях мелиоративного дренажа. Конструкция простая, монтаж несложный, решение экономичное.",
            "Насос построен на стандартной линейке погружных двигателей: вместо спирального корпуса используется корпус с осевым выходом, что позволяет ставить насос в трубную или бетонную шахту. Для больших расходов дочерняя компания Bedford Pumps выпускает погружные осевые насосы с подачей до 10 000 л/с.",
            "Монтаж: насос опускается в вертикальную трубную шахту и опирается на горизонтальную поверхность. Эластомерное уплотнительное кольцо, прижатое массой насоса, герметизирует приямок; от проворота защищает простое механическое устройство.",
        ],
        "highlights": [
            "Компактная интегрированная конструкция",
            "Минимальный шум",
            "Большой свободный проход",
            "Гидравлика с низкой склонностью к засорению",
            "Высокий гидравлический КПД",
            "Крутая и стабильная напорная характеристика",
            "Пологая кривая мощности: нет перегрузки двигателя во всём рабочем диапазоне",
            "Сменный, опционально регулируемый износный конус",
            "Охлаждение двигателя перекачиваемой жидкостью",
            "Малая занимаемая площадь и низкие затраты на монтаж",
        ],
        "applications": ["Насосные станции ливневых и паводковых вод", "Ирригационные и дренажные системы",
                          "Бережная перекачка возвратного активного ила", "Перекачка нефтесодержащих вод без образования эмульсии",
                          "Защита побережья и от наводнений", "Регулирование уровня воды", "Перекачка ливневых вод, безопасная для рыбы"],
        "specs": [
            ("Диаметр трубной шахты", "400–1500 мм"),
            ("Подача", "6–1500 л/с"),
            ("Напор", "до 20 м"),
            ("Материалы", "чугун, высокопрочный чугун, Hidrohard, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 1500 л/с", "h": "до 20 м", "p": ""},
        "docs": [("Брошюра «Осевой трубно-шахтный насос» (EN)", HS + "Dokumente/Download_185/axial-column-pump-pr09437_en.pdf")],
    },
    {
        "slug": "vertical-turbine", "category": "osevye", "name": "Вертикальные турбинные насосы Hidrostal",
        "short": "Вертикальные турбинные насосы",
        "page": HS + "verticalturbinepumps.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/verticalturbinepumps_1/Thumb/vtp-daf-pump-bedford.jpg",
        "subtitle": "Многоступенчатые насосы диагонального типа для высокого напора.",
        "description": [
            "Вертикальные турбинные насосы — центробежные насосы диагонального типа для подъёма воды из скважин и резервуаров. Их применяют, когда уровень воды ниже предела для насосов со спиральным корпусом.",
            "Высоконапорные вертикальные турбинные насосы Hidrostal подходят для большинства задач водоснабжения и водоотведения: занимают мало места, не требуют заливки (рабочие колёса погружены в жидкость), первую ступень можно опустить для нужного запаса по NPSH, многоступенчатая конструкция даёт высокий КПД на высоком напоре, модульность позволяет адаптировать насос под задачу.",
        ],
        "highlights": [],
        "applications": [],
        "specs": [],
        "kpi": {"q": "", "h": "", "p": ""},
        "docs": [("Брошюра «Вертикальные турбинные насосы» (EN)", HS + "Dokumente/Download_343/verticalturbinepumps.pdf"),
                 ("Брошюра: насосы с монолитным бетонным корпусом (EN)", HS + "Dokumente/Download_341/monolithicconcretecasingpumps.pdf")],
    },
    {
        "slug": "preroclean", "category": "sistemy", "name": "PreroClean — самоочищающийся приямок",
        "short": "PreroClean",
        "page": HS + "preroclean.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/preroclean_1/Thumb/preroclean-tanks-hidrostal.jpg",
        "subtitle": "Самоочищающийся насосный приямок на базе винтового центробежного насоса.",
        "description": [
            "PreroClean — упрощённая стандартизированная версия системы Prerostal. Вращение среды перед входом в насос подаёт в него все взвешенные частицы; очистка происходит за каждый цикл работы насоса, поэтому в приямке не скапливаются отложения и загрязнения.",
            "Ядро системы — винтовой центробежный насос Hidrostal: большой свободный канал от входа до напорного патрубка обеспечивает работу без засоров даже при крупных включениях и длинных волокнах.",
            "Двойной бассейн рассчитан на установку в стандартную шахту 1,2, 1,5 или 2 м; частичный перелив и спиральный подводящий канал снимают плавающий слой в конце цикла.",
        ],
        "highlights": [
            "Большое свободное сечение для крупных включений",
            "Крутая стабильная характеристика",
            "Напор при закрытой задвижке обычно вдвое выше напора в оптимальной точке",
            "Высокий КПД снижает энергопотребление",
            "Неперегружаемая кривая мощности позволяет ставить двигатели меньшей мощности",
            "Низкий кавитационный запас NPSHR",
        ],
        "applications": ["Канализационные насосные станции и шахты", "Приямки с нефтесодержащей водой",
                          "Высокопроизводительные моечные системы", "Приямки с высоким содержанием жиров",
                          "Приямки, где нужно удалять плавающие предметы"],
        "specs": [
            ("Размер напорного патрубка", "50–200 мм"),
            ("Размер всасывающего патрубка", "50–200 мм"),
            ("Напор", "0,5–60 м"),
            ("Подача", "2–180 л/с"),
            ("Мощность", "0,2–18 кВт"),
            ("Частота", "50 Гц, 60 Гц, ЧРП"),
            ("Материалы", "чугун, высокопрочный чугун, хромистый чугун, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 180 л/с", "h": "до 60 м", "p": "0,2–18 кВт"},
        "docs": [("Брошюра PreroClean (EN)", HS + "Dokumente/Download_178/preroclean-pr08859_en.pdf")],
    },
    {
        "slug": "prerostal", "category": "sistemy", "name": "Prerostal — согласование притока и очистка приямка",
        "short": "Prerostal",
        "page": HS + "prerostal.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/prerostal_1/Thumb/prerotation.jpg",
        "subtitle": "Подача насоса подстраивается под приток без частотного привода.",
        "description": [
            "Система предвращения Prerostal автоматически подстраивает подачу насоса с постоянной частотой вращения под изменяющийся приток. Винтовое колесо Hidrostal работает в паре со специальной камерой вокруг всасывающей трубы: камера закручивает поток в сторону вращения колеса, и подача снижается без изменения частоты вращения — частотный преобразователь не нужен.",
            "Prerostal также эффективно очищает приямок без дополнительных механизмов и подвижных частей. Это проверенная экономичная альтернатива шнековым насосам Архимеда и схемам со сложным управлением.",
        ],
        "highlights": [
            "Подача станции соответствует притоку при двигателях с постоянной скоростью",
            "Автоматически удаляет плавающие и осевшие загрязнения",
            "Менее глубокие станции по сравнению с погружными насосами в режиме вкл/выкл",
            "Альтернатива шнековым насосам Архимеда",
            "Ниже затраты на строительство благодаря сборному бассейну",
            "Энергопотребление станции автоматически подстраивается под приток",
        ],
        "applications": [],
        "specs": [
            ("Размер напорного патрубка", "80–500 мм"),
            ("Размер всасывающего патрубка", "80–500 мм"),
            ("Напор", "0,5–60 м"),
            ("Подача", "2–1350 л/с"),
            ("Мощность", "0,1–320 кВт"),
            ("Частота", "50 Гц, 60 Гц, ЧРП"),
            ("Материалы", "чугун, высокопрочный чугун, хромистый чугун, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 1350 л/с", "h": "до 60 м", "p": "0,1–320 кВт"},
        "docs": [("Брошюра Prerostal (EN)", HS + "Dokumente/Download_179/prerostal-pr08976_en.pdf")],
    },
    {
        "slug": "superbetsy", "category": "sistemy", "name": "SuperBetsy — мобильная насосная установка",
        "short": "SuperBetsy",
        "page": HS + "superbetsy.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/SpaltenBoxen_212/Thumb/superbetsy_thumbnail_de.jpg",
        "subtitle": "Автономная мобильная насосная система с винтовым центробежным насосом Hidrostal.",
        "description": [
            "IPS SuperBetsy создана для самых тяжёлых условий: стройплощадки, промышленность, защита от наводнений, горное дело, водопонижение. Винтовое центробежное колесо со свободным проходом 75–120 мм обеспечивает работу без засоров.",
            "Доступны исполнения с дизельным двигателем и с электродвигателем (класс IE3 с частотным преобразователем IP66). Вакуумная система заливки BetsyPrime с интеллектуальным управлением включает вакуумный насос только при необходимости. Хорошая шумоизоляция позволяет работать в жилых районах.",
            "Производительность установок — от 100 до 1100 м³/ч; доступны мониторинг и управление через GSM и GPS. Сделано в Германии с «сердцем» из Швейцарии.",
        ],
        "highlights": [
            "Низкая общая масса, установки штабелируются",
            "Износостойкая гидравлика",
            "Удалённый мониторинг через GPS/GSM-модем",
            "Большой коррозионностойкий пластиковый топливный бак",
            "Современные двигатели (стандарты EU и US EPA)",
        ],
        "applications": ["Строительство", "Промышленность", "Защита от наводнений", "Горное дело", "Водопонижение и дренаж"],
        "specs": [
            ("Напор", "до 62 м"),
            ("Подача", "до 1100 м³/ч"),
            ("Свободный проход", "75–120 мм"),
            ("Привод", "дизельный двигатель или электродвигатель IE3"),
        ],
        "kpi": {"q": "до 1100 м³/ч", "h": "до 62 м", "p": ""},
        "docs": [("Брошюра SuperBetsy (EN)", HS + "Dokumente/Download_183/superbetsy-pr10069d-en.pdf")],
    },
    {
        "slug": "floating-station", "category": "sistemy", "name": "Плавучие насосные станции Hidrostal",
        "short": "Плавучие насосные станции",
        "page": HS + "floatingpumpsystem.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/floatingpumpsystem_1/Thumb/hidrostal-floating-station-2.jpg",
        "subtitle": "Мощные и мобильные станции для водохранилищ, прудов и рек.",
        "description": [
            "Плавучие насосные станции Hidrostal — комплексные решения для работы на водохранилищах, лагунах и реках. Они оснащены судовыми, механическими, гидравлическими, электрическими и электронными системами и работают как высокопроизводительные и надёжные насосные станции.",
        ],
        "highlights": [
            "Мобильность: перемещаются на новое место без строительных работ",
            "Экономичность: не нужны дорогие сооружения и простои, как у стационарной станции",
            "Забор воды у поверхности: не засасываются донные отложения",
            "Высокий общий КПД всей системы",
            "Самовсасывание по конструкции, без сложных систем заливки",
            "Те же строгие проверки качества, что и для насосов Hidrostal",
        ],
        "applications": ["Горнодобывающая отрасль", "Водоснабжение", "Забор речной воды для систем питьевого водоснабжения",
                          "Забор речной воды для ирригации в агропромышленности"],
        "specs": [],
        "kpi": {"q": "", "h": "", "p": ""},
        "docs": [],
    },
    {
        "slug": "hidromix", "category": "sistemy", "name": "HidroMix — внешнее перемешивание резервуаров",
        "short": "HidroMix",
        "page": HS + "hidromix.php?Lang=ru",
        "image_src": HS + "Pictures/Bilder/hidromix_1/Thumb/lagerstuhl-verrohrung_2b.jpg",
        "subtitle": "Насосная система перемешивания для иловых резервуаров и метантенков.",
        "description": [
            "HidroMix — эффективная, безопасная и экономичная альтернатива погружным и газовым мешалкам для иловых резервуаров и метантенков. Винтовой центробежный насос Hidrostal забирает ил из резервуара и возвращает его через сопло, размер и положение которого подобраны для оптимального перемешивания и циркуляции.",
            "Каждая установка проектируется индивидуально с учётом свойств ила и геометрии резервуара. Внутри резервуара не нужны металлоконструкции: трубы входа и выхода крепятся на стенках, поэтому нечему собирать тряпки и задерживать песок. Для больших резервуаров предлагаются двухнасосные системы.",
        ],
        "highlights": [
            "Нет движущихся частей внутри резервуара",
            "Простой доступ для осмотра и обслуживания",
            "Подходит для новых и существующих резервуаров",
            "Безопаснее для персонала",
            "Трубы и сопла большого диаметра для твёрдых включений",
            "Сопла снимаются снаружи, без входа в резервуар",
            "Двигатели IP55 дешевле и проще в ремонте, чем погружные",
        ],
        "applications": ["Первичные и вторичные метантенки", "Резервуары хранения ила", "Усреднители", "Перекачка ила и загрузка цистерн"],
        "specs": [
            ("Размер напорного патрубка", "100–300 мм"),
            ("Напор", "до 11 м"),
            ("Подача", "до 300 л/с"),
            ("Мощность", "2,2–37 кВт"),
            ("Частота", "50 Гц, 60 Гц (США), ЧРП"),
            ("Материалы", "чугун, высокопрочный чугун, нержавеющая сталь, дуплекс"),
        ],
        "kpi": {"q": "до 300 л/с", "h": "до 11 м", "p": "2,2–37 кВт"},
        "docs": [("Брошюра HidroMix (EN)", HS + "Dokumente/Download_221/hidromix-10387_en.pdf")],
    },
]

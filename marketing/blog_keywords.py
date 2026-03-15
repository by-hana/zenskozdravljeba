"""
201 SEO keywords for ZenskoZdravlje.ba — imported from keyword CSV.
Source: zensko_zdravlje_keywords.csv
Columns: Kategorija, Kljucna rijec, Tip klastera (Stub=pillar / Podrska=supporting), Predlozeni naslov

Language: Bosnian Latin script only
"""

import re


def _slug(text):
    """Generate URL-safe slug from Bosnian text."""
    t = text.lower()
    for src, dst in [('š','s'),('č','c'),('ž','z'),('ć','c'),('đ','dj'),
                     ('ş','s'),('ı','i'),('ğ','g'),('ü','u'),('ö','o'),('ä','a')]:
        t = t.replace(src, dst)
    t = re.sub(r'[^a-z0-9]+', '-', t)
    return t.strip('-')[:80]


CLUSTERS = [
    {
        'cluster': 'hormoni-menstrualni-ciklus',
        'posts': [
            {'keyword': 'hormoni i menstrualni ciklus', 'title': 'Hormoni i menstrualni ciklus: Kompletan vodič za svaku ženu', 'is_pillar': True},
            {'keyword': 'faze menstrualnog ciklusa', 'title': '4 faze menstrualnog ciklusa i šta se dešava u svakoj', 'is_pillar': False},
            {'keyword': 'kako uravnotežiti hormone prirodno', 'title': 'Kako prirodno uravnotežiti hormone: 10 dokazanih metoda', 'is_pillar': False},
            {'keyword': 'estrogen i progesteron odnos', 'title': 'Estrogen i progesteron: Zašto je njihov odnos ključan', 'is_pillar': False},
            {'keyword': 'PMS simptomi i olakšanje', 'title': 'PMS simptomi: Uzroci i prirodni načini olakšanja', 'is_pillar': False},
            {'keyword': 'neredovne menstruacije uzroci', 'title': 'Zašto su tvoje menstruacije neredovne: 8 mogućih uzroka', 'is_pillar': False},
            {'keyword': 'obilna menstruacija šta raditi', 'title': 'Obilna menstruacija: Kada je normalna a kada treba reagovati', 'is_pillar': False},
            {'keyword': 'bolne menstruacije prirodni lijekovi', 'title': 'Bolne menstruacije: 12 prirodnih načina za olakšanje bola', 'is_pillar': False},
            {'keyword': 'hormonske promjene tokom života žene', 'title': 'Hormonske promjene od puberteta do menopauze', 'is_pillar': False},
            {'keyword': 'kortizol i ženski hormoni', 'title': 'Kako kortizol utiče na tvoje ženske hormone', 'is_pillar': False},
            {'keyword': 'luteinizujući hormon LH kod žena', 'title': 'Luteinizujući hormon (LH): Šta pokazuje o tvom zdravlju', 'is_pillar': False},
            {'keyword': 'folikulostimulirajući hormon FSH', 'title': 'FSH hormon kod žena: Sve što trebate znati', 'is_pillar': False},
            {'keyword': 'amenoreja uzroci i liječenje', 'title': 'Amenoreja: Zašto je izostala menstruacija i šta to znači', 'is_pillar': False},
            {'keyword': 'ciklično življenje prema menstruaciji', 'title': 'Ciklično življenje: Kako prilagoditi život fazama ciklusa', 'is_pillar': False},
            {'keyword': 'sindrom predmenstrualne disforije PMDD', 'title': 'PMDD: Kada je PMS mnogo više od običnog PMS-a', 'is_pillar': False},
            {'keyword': 'menstrualna higijena savjeti', 'title': 'Menstrualna higijena: Šta svaka žena treba znati', 'is_pillar': False},
            {'keyword': 'praćenje menstrualnog ciklusa', 'title': 'Zašto i kako pratiti svoj menstrualni ciklus', 'is_pillar': False},
            {'keyword': 'krvavi ugrušci tokom menstruacije', 'title': 'Krvavi ugrušci tokom menstruacije: Kada se zabrinuti', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'pcos-hormonski-poremecaji',
        'posts': [
            {'keyword': 'PCOS sindrom policističnih jajnika', 'title': 'PCOS: Kompletan vodič o sindromu policističnih jajnika', 'is_pillar': True},
            {'keyword': 'simptomi PCOS-a', 'title': '10 najčešćih simptoma PCOS-a koje žene ignorišu', 'is_pillar': False},
            {'keyword': 'PCOS dijeta i ishrana', 'title': 'PCOS dijeta: Šta jesti a šta izbjegavati', 'is_pillar': False},
            {'keyword': 'inzulinska rezistencija i PCOS', 'title': 'Inzulinska rezistencija kod PCOS-a: Povezanost i rješenja', 'is_pillar': False},
            {'keyword': 'PCOS i gubitak težine', 'title': 'Kako mršaviti sa PCOS-om: Strategije koje funkcionišu', 'is_pillar': False},
            {'keyword': 'hiperandrogenizam kod žena', 'title': 'Višak muških hormona kod žena: Uzroci i liječenje', 'is_pillar': False},
            {'keyword': 'PCOS i plodnost', 'title': 'PCOS i trudnoća: Kako povećati šanse za začeće', 'is_pillar': False},
            {'keyword': 'endometrioza simptomi i liječenje', 'title': 'Endometrioza: Simptomi koje ne smijete ignorisati', 'is_pillar': False},
            {'keyword': 'hipotireoza kod žena', 'title': 'Hipotireoza kod žena: Simptomi i prirodno liječenje', 'is_pillar': False},
            {'keyword': 'hipertireoza simptomi', 'title': 'Hipertireoza kod žena: Kako prepoznati i liječiti', 'is_pillar': False},
            {'keyword': 'Hashimoto tireoiditis', 'title': 'Hashimoto bolest: Vodič za žene sa autoimunim tireoiditisom', 'is_pillar': False},
            {'keyword': 'dominacija estrogena', 'title': 'Dominacija estrogena: Simptomi i kako je smanjiti', 'is_pillar': False},
            {'keyword': 'nizak progesteron simptomi', 'title': 'Nizak progesteron: Znakovi i prirodni načini podizanja', 'is_pillar': False},
            {'keyword': 'adrenalna iscrpljenost kod žena', 'title': 'Adrenalna iscrpljenost: Zašto si stalno umorna i šta pomaže', 'is_pillar': False},
            {'keyword': 'miomi materice prirodno liječenje', 'title': 'Miomi materice: Simptomi i prirodni pristupi liječenju', 'is_pillar': False},
            {'keyword': 'hormonski disbalans testovi', 'title': 'Koji testovi otkrivaju hormonski disbalans kod žena', 'is_pillar': False},
            {'keyword': 'PCOS suplementi koji pomažu', 'title': 'Najbolji suplementi za PCOS: Naučno dokazani', 'is_pillar': False},
            {'keyword': 'razlika PCOS i hipotireoza', 'title': 'PCOS ili hipotireoza: Kako razlikovati slične simptome', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'ginekolosko-zdravlje',
        'posts': [
            {'keyword': 'ginekološko zdravlje žena', 'title': 'Ginekološko zdravlje: Sve što svaka žena mora znati', 'is_pillar': True},
            {'keyword': 'redovni ginekološki pregled značaj', 'title': 'Zašto je redovni ginekološki pregled neophodan', 'is_pillar': False},
            {'keyword': 'PAPA test šta pokazuje', 'title': 'PAPA test: Šta pokazuje i koliko često ga raditi', 'is_pillar': False},
            {'keyword': 'vaginalne infekcije vrste i liječenje', 'title': 'Vaginalne infekcije: Vrste, simptomi i kako ih liječiti', 'is_pillar': False},
            {'keyword': 'kandidijaza uzroci i prevencija', 'title': 'Kandidijaza: Uzroci, simptomi i kako je spriječiti', 'is_pillar': False},
            {'keyword': 'bakterijska vaginoza', 'title': 'Bakterijska vaginoza: Simptomi i prirodno liječenje', 'is_pillar': False},
            {'keyword': 'HPV virus kod žena', 'title': 'HPV virus: Šta svaka žena treba znati o prevenciji', 'is_pillar': False},
            {'keyword': 'vaginalna suhoća uzroci', 'title': 'Vaginalna suhoća: Uzroci i rješenja za svaku dob', 'is_pillar': False},
            {'keyword': 'zdrava vaginalna flora', 'title': 'Vaginalna flora: Kako je održati zdravom', 'is_pillar': False},
            {'keyword': 'ciste na jajnicima', 'title': 'Ciste na jajnicima: Vrste, simptomi i kada liječiti', 'is_pillar': False},
            {'keyword': 'intimna higijena savjeti', 'title': 'Intimna higijena: Greške koje većina žena pravi', 'is_pillar': False},
            {'keyword': 'rak grlića materice prevencija', 'title': 'Rak grlića materice: Kako se zaštititi i rano otkriti', 'is_pillar': False},
            {'keyword': 'bol tokom odnosa uzroci', 'title': 'Bol tokom intimnog odnosa: Uzroci i rješenja', 'is_pillar': False},
            {'keyword': 'menopauza simptomi i savjeti', 'title': 'Menopauza: Simptomi, faze i kako lakše kroz nju proći', 'is_pillar': False},
            {'keyword': 'perimenopauza rani znakovi', 'title': 'Perimenopauza: 10 ranih znakova koje većina žena ne prepoznaje', 'is_pillar': False},
            {'keyword': 'inkontinencija kod žena', 'title': 'Urinarna inkontinencija kod žena: Uzroci i vježbe koje pomažu', 'is_pillar': False},
            {'keyword': 'kegel vježbe pravilno izvođenje', 'title': 'Kegel vježbe: Kako ih pravilno izvoditi za rezultate', 'is_pillar': False},
            {'keyword': 'cervikalna sluz i plodnost', 'title': 'Cervikalna sluz: Šta govori o plodnosti i zdravlju', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'ishrana-zensko-zdravlje',
        'posts': [
            {'keyword': 'ishrana za žensko zdravlje', 'title': 'Ishrana za žensko zdravlje: Kompletan vodič po fazama života', 'is_pillar': True},
            {'keyword': 'namirnice za balansiranje hormona', 'title': '15 namirnica koje prirodno balansiraju ženske hormone', 'is_pillar': False},
            {'keyword': 'antiinflamatorna ishrana za žene', 'title': 'Antiinflamatorna ishrana: Ključ za žensko zdravlje', 'is_pillar': False},
            {'keyword': 'ishrana tokom menstruacije', 'title': 'Šta jesti tokom menstruacije za manje bolova i više energije', 'is_pillar': False},
            {'keyword': 'ishrana za plodnost', 'title': 'Ishrana za plodnost: Namirnice koje povećavaju šanse za začeće', 'is_pillar': False},
            {'keyword': 'namirnice bogate željezom za žene', 'title': 'Namirnice bogate željezom: Prevencija anemije kod žena', 'is_pillar': False},
            {'keyword': 'omega 3 za žensko zdravlje', 'title': 'Omega 3 masne kiseline: Zašto su ključne za žene', 'is_pillar': False},
            {'keyword': 'šećer i hormoni kod žena', 'title': 'Kako šećer utiče na ženske hormone i šta raditi', 'is_pillar': False},
            {'keyword': 'bezglutenska ishrana i hormoni', 'title': 'Bezglutenska ishrana: Da li pomaže kod hormonskih problema', 'is_pillar': False},
            {'keyword': 'probiotici za žensko zdravlje', 'title': 'Probiotici za žene: Koji su najbolji i zašto ih trebate', 'is_pillar': False},
            {'keyword': 'ishrana u menopauzi', 'title': 'Ishrana u menopauzi: Šta jesti za manje simptoma', 'is_pillar': False},
            {'keyword': 'adaptogene biljke za žene', 'title': 'Adaptogene biljke za žene: Ashwagandha, maca i druge', 'is_pillar': False},
            {'keyword': 'zeleni smoothie za hormone', 'title': 'Zeleni smoothie recepti za balansiranje hormona', 'is_pillar': False},
            {'keyword': 'ishrana za zdravu kožu žene', 'title': 'Ishrana za zdravu kožu: Namirnice za sjaj iznutra', 'is_pillar': False},
            {'keyword': 'post i žensko zdravlje', 'title': 'Intermitentni post i žene: Koristi, rizici i savjeti', 'is_pillar': False},
            {'keyword': 'kalcijum i žensko zdravlje', 'title': 'Kalcijum za žene: Koliko vam treba i odakle ga dobiti', 'is_pillar': False},
            {'keyword': 'vlakna i probava kod žena', 'title': 'Vlakna u ishrani: Zašto su ključna za probavu i hormone', 'is_pillar': False},
            {'keyword': 'hidratacija i žensko zdravlje', 'title': 'Hidratacija za žene: Koliko vode zaista trebate piti', 'is_pillar': False},
            {'keyword': 'namirnice za zdravu jetru žene', 'title': 'Namirnice za zdravu jetru: Podrška detoksikaciji hormona', 'is_pillar': False},
            {'keyword': 'proteini za žene koliko i odakle', 'title': 'Proteini za žene: Koliko trebate i najbolji izvori', 'is_pillar': False},
            {'keyword': 'zdrave masti za ženske hormone', 'title': 'Zdrave masti i ženski hormoni: Zašto ih ne izbjegavati', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'vitamini-suplementi-minerali',
        'posts': [
            {'keyword': 'vitamini i suplementi za žene', 'title': 'Vitamini i suplementi za žene: Kompletan vodič', 'is_pillar': True},
            {'keyword': 'vitamin D za žene', 'title': 'Vitamin D kod žena: Zašto je nedostatak tako čest i šta raditi', 'is_pillar': False},
            {'keyword': 'magnezijum za žene', 'title': 'Magnezijum za žene: Vrste, doziranje i koristi', 'is_pillar': False},
            {'keyword': 'cink za ženske hormone', 'title': 'Cink i ženski hormoni: Zašto je ovaj mineral ključan', 'is_pillar': False},
            {'keyword': 'folna kiselina značaj za žene', 'title': 'Folna kiselina: Nije samo za trudnoću', 'is_pillar': False},
            {'keyword': 'vitamin B12 nedostatak simptomi', 'title': 'Nedostatak vitamina B12: Simptomi koje žene često ignorišu', 'is_pillar': False},
            {'keyword': 'vitamin B kompleks za žene', 'title': 'Vitamin B kompleks: Zašto je bitan za energiju i hormone', 'is_pillar': False},
            {'keyword': 'željezo suplementacija žene', 'title': 'Željezo za žene: Kada i kako ga pravilno uzimati', 'is_pillar': False},
            {'keyword': 'selen za štitnu žlijezdu', 'title': 'Selen za štitnu žlijezdu: Doziranje i koristi za žene', 'is_pillar': False},
            {'keyword': 'inozitol za PCOS', 'title': 'Inozitol za PCOS: Kako djeluje i koliko uzimati', 'is_pillar': False},
            {'keyword': 'vitex za regulaciju ciklusa', 'title': 'Vitex (konopljika): Prirodni lijek za regulaciju ciklusa', 'is_pillar': False},
            {'keyword': 'kolagen za žene', 'title': 'Kolagen za žene: Koristi za kožu, kosu i zglobove', 'is_pillar': False},
            {'keyword': 'vitamin C za imunitet i kožu', 'title': 'Vitamin C za žene: Od imuniteta do ljepše kože', 'is_pillar': False},
            {'keyword': 'DIM suplement za estrogen', 'title': 'DIM suplement: Kako pomaže kod viška estrogena', 'is_pillar': False},
            {'keyword': 'ulje večernje jagorčevine', 'title': 'Ulje večernje jagorčevine: Koristi za ženske tegobe', 'is_pillar': False},
            {'keyword': 'berberin za inzulinsku rezistenciju', 'title': 'Berberin: Prirodna pomoć kod inzulinske rezistencije', 'is_pillar': False},
            {'keyword': 'NAC za PCOS i plodnost', 'title': 'NAC (N-acetilcistein): Suplement za PCOS i plodnost', 'is_pillar': False},
            {'keyword': 'vitamin E za reproduktivno zdravlje', 'title': 'Vitamin E: Zašto je važan za reproduktivno zdravlje žena', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'mentalno-zdravlje-zena',
        'posts': [
            {'keyword': 'mentalno zdravlje žena', 'title': 'Mentalno zdravlje žena: Zašto je drukčije i kako ga čuvati', 'is_pillar': True},
            {'keyword': 'anksioznost kod žena', 'title': 'Anksioznost kod žena: Zašto je češća i kako je smanjiti', 'is_pillar': False},
            {'keyword': 'depresija i hormoni', 'title': 'Depresija i hormoni: Povezanost koju žene moraju razumjeti', 'is_pillar': False},
            {'keyword': 'stres i žensko zdravlje', 'title': 'Kako stres utiče na žensko tijelo: Od hormona do imuniteta', 'is_pillar': False},
            {'keyword': 'burnout kod žena', 'title': 'Burnout kod žena: Kako prepoznati i oporaviti se', 'is_pillar': False},
            {'keyword': 'emocionalno jedenje kod žena', 'title': 'Emocionalno jedenje: Kako prekinuti ciklus', 'is_pillar': False},
            {'keyword': 'hormoni i raspoloženje', 'title': 'Hormoni i raspoloženje: Zašto se osjećaš kao na ringišpilu', 'is_pillar': False},
            {'keyword': 'postporođajna depresija', 'title': 'Postporođajna depresija: Znakovi i kako potražiti pomoć', 'is_pillar': False},
            {'keyword': 'san i žensko zdravlje', 'title': 'San i ženski hormoni: Kako poboljšati kvalitet spavanja', 'is_pillar': False},
            {'keyword': 'meditacija za žene', 'title': 'Meditacija za žene: Tehnike za hormonski balans i mir', 'is_pillar': False},
            {'keyword': 'brain fog kod žena', 'title': 'Moždana magla kod žena: Uzroci i kako je riješiti', 'is_pillar': False},
            {'keyword': 'samopouzdanje i hormoni', 'title': 'Kako hormoni utiču na samopouzdanje žena', 'is_pillar': False},
            {'keyword': 'PMS i mentalno zdravlje', 'title': 'PMS i mentalno zdravlje: Strategije za teške dane', 'is_pillar': False},
            {'keyword': 'tehnika disanja za smirenje', 'title': 'Tehnike disanja za žene: Smirite hormone i um', 'is_pillar': False},
            {'keyword': 'menopauza i mentalno zdravlje', 'title': 'Mentalno zdravlje u menopauzi: Izazovi i rješenja', 'is_pillar': False},
            {'keyword': 'journaling za žensko zdravlje', 'title': 'Dnevnik zdravlja: Kako pisanje pomaže ženskom zdravlju', 'is_pillar': False},
            {'keyword': 'digitalni detox za žene', 'title': 'Digitalni detox: Kako društvene mreže utiču na žensko zdravlje', 'is_pillar': False},
            {'keyword': 'sindrom lažnog ja kod žena', 'title': 'Sindrom lažnog ja: Kada žene gube sebe ugađajući drugima', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'plodnost-trudnoca',
        'posts': [
            {'keyword': 'plodnost i trudnoća vodič', 'title': 'Plodnost i trudnoća: Kompletan vodič za žene', 'is_pillar': True},
            {'keyword': 'kako povećati plodnost prirodno', 'title': 'Kako prirodno povećati plodnost: 15 dokazanih savjeta', 'is_pillar': False},
            {'keyword': 'ovulacija znakovi i praćenje', 'title': 'Ovulacija: Kako prepoznati znakove i pratiti plodne dane', 'is_pillar': False},
            {'keyword': 'bazalna temperatura praćenje', 'title': 'Praćenje bazalne temperature: Vodič za početnike', 'is_pillar': False},
            {'keyword': 'neplodnost uzroci kod žena', 'title': 'Neplodnost kod žena: Najčešći uzroci i opcije liječenja', 'is_pillar': False},
            {'keyword': 'priprema za trudnoću', 'title': 'Priprema za trudnoću: Šta raditi 3-6 mjeseci prije začeća', 'is_pillar': False},
            {'keyword': 'ishrana u trudnoći', 'title': 'Ishrana u trudnoći: Šta jesti trimester po trimester', 'is_pillar': False},
            {'keyword': 'suplementi u trudnoći', 'title': 'Suplementi u trudnoći: Koji su neophodni a koji opcionalni', 'is_pillar': False},
            {'keyword': 'rani znakovi trudnoće', 'title': 'Rani znakovi trudnoće: Simptomi prije izostanka menstruacije', 'is_pillar': False},
            {'keyword': 'mučnina u trudnoći savjeti', 'title': 'Mučnina u trudnoći: Prirodni načini za olakšanje', 'is_pillar': False},
            {'keyword': 'spontani pobačaj uzroci i oporavak', 'title': 'Spontani pobačaj: Uzroci, oporavak i ponovna trudnoća', 'is_pillar': False},
            {'keyword': 'trudnoća nakon 35 godina', 'title': 'Trudnoća nakon 35: Rizici, savjeti i priprema', 'is_pillar': False},
            {'keyword': 'dojenje i ishrana majke', 'title': 'Dojenje i ishrana: Šta jesti za zdravo mlijeko', 'is_pillar': False},
            {'keyword': 'oporavak nakon poroda', 'title': 'Oporavak nakon poroda: Tijelo, hormoni i um', 'is_pillar': False},
            {'keyword': 'hormoni nakon poroda', 'title': 'Hormoni nakon poroda: Šta očekivati i kako se nositi', 'is_pillar': False},
            {'keyword': 'IVF proces i priprema', 'title': 'IVF: Priprema, proces i šta očekivati', 'is_pillar': False},
            {'keyword': 'plodnost i stres povezanost', 'title': 'Stres i plodnost: Kako stres smanjuje šanse za začeće', 'is_pillar': False},
            {'keyword': 'gestacijski dijabetes', 'title': 'Gestacijski dijabetes: Simptomi, ishrana i upravljanje', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'fitness-kretanje-zene',
        'posts': [
            {'keyword': 'fitness za žensko zdravlje', 'title': 'Fitness za žene: Kako vježbati u skladu sa tijelom', 'is_pillar': True},
            {'keyword': 'trening prema fazama ciklusa', 'title': 'Trening prema fazama ciklusa: Vodič za svaku fazu', 'is_pillar': False},
            {'keyword': 'trening snage za žene', 'title': 'Trening snage za žene: Zašto ne trebate izbjegavati tegove', 'is_pillar': False},
            {'keyword': 'yoga za hormonski balans', 'title': 'Yoga za hormone: Poze koje balansiraju žensko zdravlje', 'is_pillar': False},
            {'keyword': 'hodanje za žensko zdravlje', 'title': 'Hodanje za zdravlje: Najjednostavnija vježba za žene', 'is_pillar': False},
            {'keyword': 'pilates za žene', 'title': 'Pilates za žene: Koristi za tijelo, hormone i um', 'is_pillar': False},
            {'keyword': 'vježbanje i PCOS', 'title': 'Vježbanje sa PCOS-om: Šta raditi a šta izbjegavati', 'is_pillar': False},
            {'keyword': 'vježbanje u trudnoći', 'title': 'Vježbanje u trudnoći: Sigurne vježbe trimester po trimester', 'is_pillar': False},
            {'keyword': 'diastaza recti vježbe', 'title': 'Diastaza recti: Vježbe za oporavak trbušnih mišića', 'is_pillar': False},
            {'keyword': 'vježbanje u menopauzi', 'title': 'Vježbanje u menopauzi: Najbolji treninzi za ovo razdoblje', 'is_pillar': False},
            {'keyword': 'kardio vs snaga za žene', 'title': 'Kardio ili snaga: Šta je bolje za žensko zdravlje', 'is_pillar': False},
            {'keyword': 'pretjerano vježbanje i hormoni', 'title': 'Pretjerano vježbanje: Kako previše treninga škodi hormonima', 'is_pillar': False},
            {'keyword': 'vježbe za dno zdjelice', 'title': 'Vježbe za dno zdjelice: Prevencija i liječenje', 'is_pillar': False},
            {'keyword': 'jutarnja rutina vježbi za žene', 'title': 'Jutarnja rutina: 15-minutni trening za energiju cijeli dan', 'is_pillar': False},
            {'keyword': 'stretching za žensko tijelo', 'title': 'Stretching za žene: Istezanje za fleksibilnost i opuštanje', 'is_pillar': False},
            {'keyword': 'HIIT trening za žene', 'title': 'HIIT trening za žene: Kada je koristan a kada štetan', 'is_pillar': False},
            {'keyword': 'vježbanje i gubitak težine žene', 'title': 'Vježbanje i mršavljenje: Zašto žene trebaju drukčiji pristup', 'is_pillar': False},
            {'keyword': 'osteoporoza prevencija vježbama', 'title': 'Osteoporoza: Vježbe koje jačaju kosti kod žena', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'prirodni-pristupi-zdravlju',
        'posts': [
            {'keyword': 'prirodni pristupi ženskom zdravlju', 'title': 'Prirodni pristupi ženskom zdravlju: Kompletan vodič', 'is_pillar': True},
            {'keyword': 'biljni čajevi za ženske tegobe', 'title': 'Biljni čajevi za ženske tegobe: 10 najdjelotvornijih', 'is_pillar': False},
            {'keyword': 'aromaterapija za žene', 'title': 'Aromaterapija za žene: Eterična ulja za hormonski balans', 'is_pillar': False},
            {'keyword': 'akupunktura za žensko zdravlje', 'title': 'Akupunktura za žene: Koristi za plodnost i hormone', 'is_pillar': False},
            {'keyword': 'detoksikacija estrogena prirodno', 'title': 'Detoksikacija estrogena: Prirodni načini čišćenja viška', 'is_pillar': False},
            {'keyword': 'jetra i ženski hormoni', 'title': 'Jetra i hormoni: Zašto je čišćenje jetre važno za žene', 'is_pillar': False},
            {'keyword': 'seed cycling za hormone', 'title': 'Seed cycling: Može li rotacija sjemenki uravnotežiti hormone', 'is_pillar': False},
            {'keyword': 'kineska medicina za žene', 'title': 'Kineska medicina za žene: Principi i koristi', 'is_pillar': False},
            {'keyword': 'ayurveda za žensko zdravlje', 'title': 'Ayurveda za žene: Drevna mudrost za moderno zdravlje', 'is_pillar': False},
            {'keyword': 'kurkuma za upalu kod žena', 'title': 'Kurkuma za žene: Antiinflamatorno djelovanje i recepti', 'is_pillar': False},
            {'keyword': 'maca korijen za hormone', 'title': 'Maca korijen: Koristi za energiju i hormonski balans', 'is_pillar': False},
            {'keyword': 'crvena djetelina za menopauzu', 'title': 'Crvena djetelina: Prirodna pomoć u menopauzi', 'is_pillar': False},
            {'keyword': 'magnezijumove kupke', 'title': 'Magnezijumove kupke: Relaksacija i zdravlje za žene', 'is_pillar': False},
            {'keyword': 'endokrini disruptori u okolini', 'title': 'Endokrini disruptori: Hemikalije koje remete hormone', 'is_pillar': False},
            {'keyword': 'prirodna kozmetika i hormoni', 'title': 'Prirodna kozmetika: Zašto je važna za hormonsko zdravlje', 'is_pillar': False},
            {'keyword': 'holističko liječenje ženskih tegoba', 'title': 'Holistički pristup ženskom zdravlju: Tijelo, um i duša', 'is_pillar': False},
            {'keyword': 'grounding i žensko zdravlje', 'title': 'Grounding (uzemljenje): Kako pomaže ženskom zdravlju', 'is_pillar': False},
            {'keyword': 'sok od celera za hormone', 'title': 'Sok od celera: Da li zaista pomaže hormonima', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'koza-kosa-hormoni',
        'posts': [
            {'keyword': 'koža kosa i hormoni vodič', 'title': 'Koža, kosa i hormoni: Kako su povezani i šta raditi', 'is_pillar': True},
            {'keyword': 'hormonski akne uzroci i liječenje', 'title': 'Hormonski akne: Uzroci i kako ih liječiti iznutra', 'is_pillar': False},
            {'keyword': 'akne na bradi i vilici hormoni', 'title': 'Akne na bradi i vilici: Šta govore o vašim hormonima', 'is_pillar': False},
            {'keyword': 'gubitak kose kod žena', 'title': 'Gubitak kose kod žena: Hormonski uzroci i rješenja', 'is_pillar': False},
            {'keyword': 'hirzutizam višak dlaka žene', 'title': 'Hirzutizam: Višak dlačica kod žena i hormonski uzroci', 'is_pillar': False},
            {'keyword': 'suha koža i hormoni', 'title': 'Suha koža i hormoni: Uzroci i kako je prirodno hidratizirati', 'is_pillar': False},
            {'keyword': 'starenje kože i estrogen', 'title': 'Starenje kože i estrogen: Šta se dešava u menopauzi', 'is_pillar': False},
            {'keyword': 'celulit i hormoni', 'title': 'Celulit i hormoni: Uzroci i prirodni pristupi smanjenju', 'is_pillar': False},
            {'keyword': 'koža i crijeva povezanost', 'title': 'Os crijeva-koža: Kako probava utiče na izgled kože', 'is_pillar': False},
            {'keyword': 'rosacea i hormoni', 'title': 'Rozacea kod žena: Hormonski okidači i prirodni tretmani', 'is_pillar': False},
            {'keyword': 'ekcemi i ženski hormoni', 'title': 'Ekcemi i hormoni: Zašto se pogoršavaju tokom ciklusa', 'is_pillar': False},
            {'keyword': 'pigmentacija kože hormoni', 'title': 'Hiperpigmentacija kod žena: Hormonski uzroci i rješenja', 'is_pillar': False},
            {'keyword': 'njega kože prema fazi ciklusa', 'title': 'Njega kože prema fazi ciklusa: Prilagodite rutinu hormonima', 'is_pillar': False},
            {'keyword': 'lomljivi nokti i nedostatak minerala', 'title': 'Lomljivi nokti: Koji nedostaci minerala su uzrok', 'is_pillar': False},
            {'keyword': 'biotin za kosu i nokte', 'title': 'Biotin za kosu i nokte: Da li zaista funkcioniše', 'is_pillar': False},
            {'keyword': 'kolagen i ženski hormoni', 'title': 'Kolagen i estrogen: Kako hormoni utiču na elastičnost kože', 'is_pillar': False},
            {'keyword': 'masna kosa i hormoni', 'title': 'Masna kosa i hormoni: Uzroci i prirodna rješenja', 'is_pillar': False},
            {'keyword': 'tamni kolutovi oko očiju žene', 'title': 'Tamni kolutovi oko očiju: Hormonski i nutritivni uzroci', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'medicinski-testovi-analize',
        'posts': [
            {'keyword': 'medicinski testovi za žene', 'title': 'Medicinski testovi za žene: Kompletan vodič po godinama', 'is_pillar': True},
            {'keyword': 'hormonski panel krvi šta testirati', 'title': 'Hormonski panel krvi: Koji testovi su neophodni za žene', 'is_pillar': False},
            {'keyword': 'analiza štitne žlijezde TSH T3 T4', 'title': 'Analiza štitne žlijezde: TSH, T3, T4 i šta znače rezultati', 'is_pillar': False},
            {'keyword': 'vitamin D testiranje', 'title': 'Testiranje vitamina D: Zašto je važno i kako čitati rezultate', 'is_pillar': False},
            {'keyword': 'kompletna krvna slika žene', 'title': 'Kompletna krvna slika: Šta svaki parametar znači za žene', 'is_pillar': False},
            {'keyword': 'HOMA indeks inzulinska rezistencija', 'title': 'HOMA indeks: Rani pokazatelj inzulinske rezistencije', 'is_pillar': False},
            {'keyword': 'testosteron kod žena normalne vrijednosti', 'title': 'Testosteron kod žena: Normalne vrijednosti i šta pokazuje', 'is_pillar': False},
            {'keyword': 'DHEA-S hormon značaj', 'title': 'DHEA-S hormon: Šta pokazuje i zašto je važan za žene', 'is_pillar': False},
            {'keyword': 'prolaktin povišen uzroci', 'title': 'Povišen prolaktin: Uzroci, simptomi i liječenje', 'is_pillar': False},
            {'keyword': 'AMH test rezerva jajnika', 'title': 'AMH test: Šta govori o rezervi jajnika', 'is_pillar': False},
            {'keyword': 'ultrazvuk zdjelice značaj', 'title': 'Ultrazvuk zdjelice: Zašto je važan i šta pokazuje', 'is_pillar': False},
            {'keyword': 'mamografija kada i zašto', 'title': 'Mamografija: Kada početi i koliko često je raditi', 'is_pillar': False},
            {'keyword': 'CRP i upala u tijelu', 'title': 'CRP marker: Šta pokazuje o upali u ženskom tijelu', 'is_pillar': False},
            {'keyword': 'test intolerancije na hranu', 'title': 'Testovi intolerancije na hranu: Koji su pouzdani', 'is_pillar': False},
            {'keyword': 'gustoća kostiju DEXA sken', 'title': 'DEXA sken: Test gustoće kostiju za žene', 'is_pillar': False},
            {'keyword': 'lipidni profil žene', 'title': 'Lipidni profil: Holesterol i trigliceridi kod žena', 'is_pillar': False},
            {'keyword': 'HbA1c test za žene', 'title': 'HbA1c test: Šta govori o vašem šećeru u krvi', 'is_pillar': False},
            {'keyword': 'genski testovi za žensko zdravlje', 'title': 'Genski testovi: Šta mogu otkriti o vašem zdravlju', 'is_pillar': False},
        ],
    },
]

# ── Auto-generate slugs and flatten ────────────────────────────────────
ALL_POSTS = []
_seen_slugs = set()

for cluster_data in CLUSTERS:
    for post in cluster_data['posts']:
        slug = _slug(post['keyword'])
        base_slug = slug
        counter = 2
        while slug in _seen_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1
        _seen_slugs.add(slug)

        ALL_POSTS.append({
            'keyword': post['keyword'],
            'title': post['title'],
            'slug': slug,
            'cluster': cluster_data['cluster'],
            'is_pillar': post['is_pillar'],
        })

TOTAL_POSTS = len(ALL_POSTS)

PILLAR_BY_CLUSTER = {}
for entry in ALL_POSTS:
    if entry['is_pillar']:
        PILLAR_BY_CLUSTER[entry['cluster']] = entry

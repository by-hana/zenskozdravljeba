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
            {'keyword': 'hormoni i menstrualni ciklus', 'title': 'Hormoni i menstrualni ciklus: Kompletni vodic za svaku zenu', 'is_pillar': True},
            {'keyword': 'faze menstrualnog ciklusa', 'title': '4 faze menstrualnog ciklusa i sta se desava u svakoj', 'is_pillar': False},
            {'keyword': 'kako uravnoteziti hormone prirodno', 'title': 'Kako prirodno uravnoteziti hormone: 10 dokazanih metoda', 'is_pillar': False},
            {'keyword': 'estrogen i progesteron odnos', 'title': 'Estrogen i progesteron: Zasto je njihov odnos kljucan', 'is_pillar': False},
            {'keyword': 'PMS simptomi i olaksanje', 'title': 'PMS simptomi: Uzroci i prirodni nacini olaksanja', 'is_pillar': False},
            {'keyword': 'neredovne menstruacije uzroci', 'title': 'Zasto su tvoje menstruacije neredovne: 8 mogucih uzroka', 'is_pillar': False},
            {'keyword': 'obilna menstruacija sta raditi', 'title': 'Obilna menstruacija: Kada je normalna a kada treba reagovati', 'is_pillar': False},
            {'keyword': 'bolne menstruacije prirodni lijekovi', 'title': 'Bolne menstruacije: 12 prirodnih nacina za olaksanje bola', 'is_pillar': False},
            {'keyword': 'hormonske promjene tokom zivota zene', 'title': 'Hormonske promjene od puberteta do menopauze', 'is_pillar': False},
            {'keyword': 'kortizol i zenski hormoni', 'title': 'Kako kortizol utice na tvoje zenske hormone', 'is_pillar': False},
            {'keyword': 'luteinizujuci hormon LH kod zena', 'title': 'Luteinizujuci hormon (LH): Sta pokazuje o tvom zdravlju', 'is_pillar': False},
            {'keyword': 'folikulostimulirajuci hormon FSH', 'title': 'FSH hormon kod zena: Sve sto trebate znati', 'is_pillar': False},
            {'keyword': 'amenoreja uzroci i lijecenje', 'title': 'Amenoreja: Zasto je izostala menstruacija i sta to znaci', 'is_pillar': False},
            {'keyword': 'ciklicno zivljenje prema menstruaciji', 'title': 'Ciklicno zivljenje: Kako prilagoditi zivot fazama ciklusa', 'is_pillar': False},
            {'keyword': 'sindrom predmenstrualne disforije PMDD', 'title': 'PMDD: Kada je PMS mnogo vise od obicnog PMS-a', 'is_pillar': False},
            {'keyword': 'menstrualna higijena savjeti', 'title': 'Menstrualna higijena: Sta svaka zena treba znati', 'is_pillar': False},
            {'keyword': 'pracenje menstrualnog ciklusa', 'title': 'Zasto i kako pratiti svoj menstrualni ciklus', 'is_pillar': False},
            {'keyword': 'krvavi ugrusci tokom menstruacije', 'title': 'Krvavi ugrusci tokom menstruacije: Kada se zabrinuti', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'pcos-hormonski-poremecaji',
        'posts': [
            {'keyword': 'PCOS sindrom policisticnih jajnika', 'title': 'PCOS: Kompletni vodic o sindromu policisticnih jajnika', 'is_pillar': True},
            {'keyword': 'simptomi PCOS-a', 'title': '10 najcescih simptoma PCOS-a koje zene ignorisu', 'is_pillar': False},
            {'keyword': 'PCOS dijeta i ishrana', 'title': 'PCOS dijeta: Sta jesti a sta izbjegavati', 'is_pillar': False},
            {'keyword': 'inzulinska rezistencija i PCOS', 'title': 'Inzulinska rezistencija kod PCOS-a: Povezanost i rjesenja', 'is_pillar': False},
            {'keyword': 'PCOS i gubitak tezine', 'title': 'Kako mrsaviti sa PCOS-om: Strategije koje funkcionisu', 'is_pillar': False},
            {'keyword': 'hiperandrogenizam kod zena', 'title': 'Visak muskih hormona kod zena: Uzroci i lijecenje', 'is_pillar': False},
            {'keyword': 'PCOS i plodnost', 'title': 'PCOS i trudnoca: Kako povecati sanse za zacece', 'is_pillar': False},
            {'keyword': 'endometrioza simptomi i lijecenje', 'title': 'Endometrioza: Simptomi koje ne smijete ignorisati', 'is_pillar': False},
            {'keyword': 'hipotireoza kod zena', 'title': 'Hipotireoza kod zena: Simptomi i prirodno lijecenje', 'is_pillar': False},
            {'keyword': 'hipertireoza simptomi', 'title': 'Hipertireoza kod zena: Kako prepoznati i lijeciti', 'is_pillar': False},
            {'keyword': 'Hashimoto tireoiditis', 'title': 'Hashimoto bolest: Vodic za zene sa autoimunim tireoiditisom', 'is_pillar': False},
            {'keyword': 'dominacija estrogena', 'title': 'Dominacija estrogena: Simptomi i kako je smanjiti', 'is_pillar': False},
            {'keyword': 'nizak progesteron simptomi', 'title': 'Nizak progesteron: Znakovi i prirodni nacini podizanja', 'is_pillar': False},
            {'keyword': 'adrenalna iscrpljenost kod zena', 'title': 'Adrenalna iscrpljenost: Zasto si stalno umorna i sta pomoci', 'is_pillar': False},
            {'keyword': 'miomi materice prirodno lijecenje', 'title': 'Miomi materice: Simptomi i prirodni pristupi lijecenju', 'is_pillar': False},
            {'keyword': 'hormonski disbalans testovi', 'title': 'Koji testovi otkrivaju hormonski disbalans kod zena', 'is_pillar': False},
            {'keyword': 'PCOS suplementi koji pomazu', 'title': 'Najbolji suplementi za PCOS: Naucno dokazani', 'is_pillar': False},
            {'keyword': 'razlika PCOS i hipotireoza', 'title': 'PCOS ili hipotireoza: Kako razlikovati slicne simptome', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'ginekolosko-zdravlje',
        'posts': [
            {'keyword': 'ginekolosko zdravlje zena', 'title': 'Ginekolosko zdravlje: Sve sto svaka zena mora znati', 'is_pillar': True},
            {'keyword': 'redovni ginekoloski pregled znacaj', 'title': 'Zasto je redovni ginekoloski pregled neophodan', 'is_pillar': False},
            {'keyword': 'PAPA test sta pokazuje', 'title': 'PAPA test: Sta pokazuje i koliko cesto ga raditi', 'is_pillar': False},
            {'keyword': 'vaginalne infekcije vrste i lijecenje', 'title': 'Vaginalne infekcije: Vrste, simptomi i kako ih lijeciti', 'is_pillar': False},
            {'keyword': 'kandidijaza uzroci i prevencija', 'title': 'Kandidijaza: Uzroci, simptomi i kako je sprijeciti', 'is_pillar': False},
            {'keyword': 'bakterijska vaginoza', 'title': 'Bakterijska vaginoza: Simptomi i prirodno lijecenje', 'is_pillar': False},
            {'keyword': 'HPV virus kod zena', 'title': 'HPV virus: Sta svaka zena treba znati o prevenciji', 'is_pillar': False},
            {'keyword': 'vaginalna suhoca uzroci', 'title': 'Vaginalna suhoca: Uzroci i rjesenja za svaku dob', 'is_pillar': False},
            {'keyword': 'zdrava vaginalna flora', 'title': 'Vaginalna flora: Kako je odrzati zdravom', 'is_pillar': False},
            {'keyword': 'ciste na jajnicima', 'title': 'Ciste na jajnicima: Vrste, simptomi i kada lijeciti', 'is_pillar': False},
            {'keyword': 'intimna higijena savjeti', 'title': 'Intimna higijena: Greske koje vecina zena pravi', 'is_pillar': False},
            {'keyword': 'rak grlica materice prevencija', 'title': 'Rak grlica materice: Kako se zastititi i rano otkriti', 'is_pillar': False},
            {'keyword': 'bol tokom odnosa uzroci', 'title': 'Bol tokom intimnog odnosa: Uzroci i rjesenja', 'is_pillar': False},
            {'keyword': 'menopauza simptomi i savjeti', 'title': 'Menopauza: Simptomi, faze i kako lakse kroz nju proci', 'is_pillar': False},
            {'keyword': 'perimenopauza rani znakovi', 'title': 'Perimenopauza: 10 ranih znakova koje vecina zena ne prepoznaje', 'is_pillar': False},
            {'keyword': 'inkontinencija kod zena', 'title': 'Urinarna inkontinencija kod zena: Uzroci i vjezbe koje pomazu', 'is_pillar': False},
            {'keyword': 'kegel vjezbe pravilno izvodenje', 'title': 'Kegel vjezbe: Kako ih pravilno izvoditi za rezultate', 'is_pillar': False},
            {'keyword': 'cervikalna sluz i plodnost', 'title': 'Cervikalna sluz: Sta govori o plodnosti i zdravlju', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'ishrana-zensko-zdravlje',
        'posts': [
            {'keyword': 'ishrana za zensko zdravlje', 'title': 'Ishrana za zensko zdravlje: Kompletni vodic po fazama zivota', 'is_pillar': True},
            {'keyword': 'namirnice za balansiranje hormona', 'title': '15 namirnica koje prirodno balansiraju zenske hormone', 'is_pillar': False},
            {'keyword': 'antiinflamatorna ishrana za zene', 'title': 'Antiinflamatorna ishrana: Kljuc za zensko zdravlje', 'is_pillar': False},
            {'keyword': 'ishrana tokom menstruacije', 'title': 'Sta jesti tokom menstruacije za manje bolova i vise energije', 'is_pillar': False},
            {'keyword': 'ishrana za plodnost', 'title': 'Ishrana za plodnost: Namirnice koje povecavaju sanse za zacece', 'is_pillar': False},
            {'keyword': 'namirnice bogate zeljezom za zene', 'title': 'Namirnice bogate zeljezom: Prevencija anemije kod zena', 'is_pillar': False},
            {'keyword': 'omega 3 za zensko zdravlje', 'title': 'Omega 3 masne kiseline: Zasto su kljucne za zene', 'is_pillar': False},
            {'keyword': 'secer i hormoni kod zena', 'title': 'Kako secer utice na zenske hormone i sta raditi', 'is_pillar': False},
            {'keyword': 'glutenfree ishrana i hormoni', 'title': 'Bezglutenska ishrana: Da li pomaze kod hormonskih problema', 'is_pillar': False},
            {'keyword': 'probiotici za zensko zdravlje', 'title': 'Probiotici za zene: Koji su najbolji i zasto ih trebate', 'is_pillar': False},
            {'keyword': 'ishrana u menopauzi', 'title': 'Ishrana u menopauzi: Sta jesti za manje simptoma', 'is_pillar': False},
            {'keyword': 'adaptogene biljke za zene', 'title': 'Adaptogene biljke za zene: Ashwagandha, maca i druge', 'is_pillar': False},
            {'keyword': 'zeleni smoothie za hormone', 'title': 'Zeleni smoothie recepti za balansiranje hormona', 'is_pillar': False},
            {'keyword': 'ishrana za zdravu kozu zene', 'title': 'Ishrana za zdravu kozu: Namirnice za sjaj iznutra', 'is_pillar': False},
            {'keyword': 'post i zensko zdravlje', 'title': 'Intermitentni post i zene: Koristi, rizici i savjeti', 'is_pillar': False},
            {'keyword': 'kalcijum i zensko zdravlje', 'title': 'Kalcijum za zene: Koliko vam treba i odakle ga dobiti', 'is_pillar': False},
            {'keyword': 'fiber i probava kod zena', 'title': 'Vlakna u ishrani: Zasto su kljucna za probavu i hormone', 'is_pillar': False},
            {'keyword': 'hidratacija i zensko zdravlje', 'title': 'Hidratacija za zene: Koliko vode zaista trebate piti', 'is_pillar': False},
            {'keyword': 'namirnice za zdravu jetru zene', 'title': 'Namirnice za zdravu jetru: Podrska detoksikaciji hormona', 'is_pillar': False},
            {'keyword': 'proteini za zene koliko i odakle', 'title': 'Proteini za zene: Koliko trebate i najbolji izvori', 'is_pillar': False},
            {'keyword': 'zdrave masti za zenske hormone', 'title': 'Zdrave masti i zenski hormoni: Zasto ih ne izbjegavati', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'vitamini-suplementi-minerali',
        'posts': [
            {'keyword': 'vitamini i suplementi za zene', 'title': 'Vitamini i suplementi za zene: Kompletni vodic', 'is_pillar': True},
            {'keyword': 'vitamin D za zene', 'title': 'Vitamin D kod zena: Zasto je nedostatak tako cest i sta raditi', 'is_pillar': False},
            {'keyword': 'magnezijum za zene', 'title': 'Magnezijum za zene: Vrste, doziranje i koristi', 'is_pillar': False},
            {'keyword': 'cink za zenske hormone', 'title': 'Cink i zenski hormoni: Zasto je ovaj mineral kljucan', 'is_pillar': False},
            {'keyword': 'folna kiselina znacaj za zene', 'title': 'Folna kiselina: Nije samo za trudnocu', 'is_pillar': False},
            {'keyword': 'vitamin B12 nedostatak simptomi', 'title': 'Nedostatak vitamina B12: Simptomi koje zene cesto ignorisu', 'is_pillar': False},
            {'keyword': 'vitamin B kompleks za zene', 'title': 'Vitamin B kompleks: Zasto je bitan za energiju i hormone', 'is_pillar': False},
            {'keyword': 'zeljezo suplementacija zene', 'title': 'Zeljezo za zene: Kada i kako ga pravilno uzimati', 'is_pillar': False},
            {'keyword': 'selen za stitnu zlijezdu', 'title': 'Selen za stitnu zlijezdu: Doziranje i koristi za zene', 'is_pillar': False},
            {'keyword': 'inozitol za PCOS', 'title': 'Inozitol za PCOS: Kako djeluje i koliko uzimati', 'is_pillar': False},
            {'keyword': 'vitex za regulaciju ciklusa', 'title': 'Vitex (konopljika): Prirodni lijek za regulaciju ciklusa', 'is_pillar': False},
            {'keyword': 'kolagen za zene', 'title': 'Kolagen za zene: Koristi za kozu, kosu i zglobove', 'is_pillar': False},
            {'keyword': 'vitamin C za imunitet i kozu', 'title': 'Vitamin C za zene: Od imuniteta do ljepse koze', 'is_pillar': False},
            {'keyword': 'DIM suplement za estrogen', 'title': 'DIM suplement: Kako pomaze kod viska estrogena', 'is_pillar': False},
            {'keyword': 'vecernja jagorce vina ulje', 'title': 'Ulje vecernje jagorceevine: Koristi za zenske tegobe', 'is_pillar': False},
            {'keyword': 'berberine za inzulinsku rezistenciju', 'title': 'Berberin: Prirodna pomoc kod inzulinske rezistencije', 'is_pillar': False},
            {'keyword': 'NAC za PCOS i plodnost', 'title': 'NAC (N-acetilcistein): Suplement za PCOS i plodnost', 'is_pillar': False},
            {'keyword': 'vitamin E za reproduktivno zdravlje', 'title': 'Vitamin E: Zasto je vazan za reproduktivno zdravlje zena', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'mentalno-zdravlje-zena',
        'posts': [
            {'keyword': 'mentalno zdravlje zena', 'title': 'Mentalno zdravlje zena: Zasto je drukcije i kako ga cuvati', 'is_pillar': True},
            {'keyword': 'anksioznost kod zena', 'title': 'Anksioznost kod zena: Zasto je cesca i kako je smanjiti', 'is_pillar': False},
            {'keyword': 'depresija i hormoni', 'title': 'Depresija i hormoni: Povezanost koju zene moraju razumjeti', 'is_pillar': False},
            {'keyword': 'stres i zensko zdravlje', 'title': 'Kako stres utice na zensko tijelo: Od hormona do imuniteta', 'is_pillar': False},
            {'keyword': 'burnout kod zena', 'title': 'Burnout kod zena: Kako prepoznati i oporaviti se', 'is_pillar': False},
            {'keyword': 'emocionalno jedenje kod zena', 'title': 'Emocionalno jedenje: Kako prekinuti ciklus', 'is_pillar': False},
            {'keyword': 'hormoni i raspolozenje', 'title': 'Hormoni i raspolozenje: Zasto se osjecas kao na ringispilu', 'is_pillar': False},
            {'keyword': 'postporodajna depresija', 'title': 'Postporodajna depresija: Znakovi i kako potraziti pomoc', 'is_pillar': False},
            {'keyword': 'san i zensko zdravlje', 'title': 'San i zenski hormoni: Kako poboljsati kvalitet spavanja', 'is_pillar': False},
            {'keyword': 'meditacija za zene', 'title': 'Meditacija za zene: Tehnike za hormonski balans i mir', 'is_pillar': False},
            {'keyword': 'brain fog kod zena', 'title': 'Mozdana magla kod zena: Uzroci i kako je rijesiti', 'is_pillar': False},
            {'keyword': 'samopouzdanje i hormoni', 'title': 'Kako hormoni uticu na samopouzdanje zena', 'is_pillar': False},
            {'keyword': 'PMS i mentalno zdravlje', 'title': 'PMS i mentalno zdravlje: Strategije za teske dane', 'is_pillar': False},
            {'keyword': 'tehnika disanja za smirenje', 'title': 'Tehnike disanja za zene: Smirite hormone i um', 'is_pillar': False},
            {'keyword': 'menopauza i mentalno zdravlje', 'title': 'Mentalno zdravlje u menopauzi: Izazovi i rjesenja', 'is_pillar': False},
            {'keyword': 'journaling za zensko zdravlje', 'title': 'Dnevnik zdravlja: Kako pisanje pomaze zenskom zdravlju', 'is_pillar': False},
            {'keyword': 'digitalni detox za zene', 'title': 'Digitalni detox: Kako drustvene mreze uticu na zensko zdravlje', 'is_pillar': False},
            {'keyword': 'sindrom laznog ja kod zena', 'title': 'Sindrom laznog ja: Kada zene gube sebe ugadajuci drugima', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'plodnost-trudnoca',
        'posts': [
            {'keyword': 'plodnost i trudnoca vodic', 'title': 'Plodnost i trudnoca: Kompletni vodic za zene', 'is_pillar': True},
            {'keyword': 'kako povecati plodnost prirodno', 'title': 'Kako prirodno povecati plodnost: 15 dokazanih savjeta', 'is_pillar': False},
            {'keyword': 'ovulacija znakovi i pracenje', 'title': 'Ovulacija: Kako prepoznati znakove i pratiti plodne dane', 'is_pillar': False},
            {'keyword': 'bazalna temperatura pracenje', 'title': 'Pracenje bazalne temperature: Vodic za pocetnike', 'is_pillar': False},
            {'keyword': 'neplodnost uzroci kod zena', 'title': 'Neplodnost kod zena: Najcesci uzroci i opcije lijecenja', 'is_pillar': False},
            {'keyword': 'priprema za trudnocu', 'title': 'Priprema za trudnocu: Sta raditi 3-6 mjeseci prije zaceca', 'is_pillar': False},
            {'keyword': 'ishrana u trudnoci', 'title': 'Ishrana u trudnoci: Sta jesti trimester po trimester', 'is_pillar': False},
            {'keyword': 'suplementi u trudnoci', 'title': 'Suplementi u trudnoci: Koji su neophodni a koji opcionalni', 'is_pillar': False},
            {'keyword': 'rani znakovi trudnoce', 'title': 'Rani znakovi trudnoce: Simptomi prije izostanka menstruacije', 'is_pillar': False},
            {'keyword': 'mucnina u trudnoci savjeti', 'title': 'Mucnina u trudnoci: Prirodni nacini za olaksanje', 'is_pillar': False},
            {'keyword': 'spontani pobacaj uzroci i oporavak', 'title': 'Spontani pobacaj: Uzroci, oporavak i ponovna trudnoca', 'is_pillar': False},
            {'keyword': 'trudnoca nakon 35 godina', 'title': 'Trudnoca nakon 35: Rizici, savjeti i priprema', 'is_pillar': False},
            {'keyword': 'dojenje i ishrana majke', 'title': 'Dojenje i ishrana: Sta jesti za zdravo mlijeko', 'is_pillar': False},
            {'keyword': 'oporavak nakon poroda', 'title': 'Oporavak nakon poroda: Tijelo, hormoni i um', 'is_pillar': False},
            {'keyword': 'hormoni nakon poroda', 'title': 'Hormoni nakon poroda: Sta ocekivati i kako se nositi', 'is_pillar': False},
            {'keyword': 'IVF proces i priprema', 'title': 'IVF: Priprema, proces i sta ocekivati', 'is_pillar': False},
            {'keyword': 'plodnost i stres povezanost', 'title': 'Stres i plodnost: Kako stres smanjuje sanse za zacece', 'is_pillar': False},
            {'keyword': 'gestacijski dijabetes', 'title': 'Gestacijski dijabetes: Simptomi, ishrana i upravljanje', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'fitness-kretanje-zene',
        'posts': [
            {'keyword': 'fitness za zensko zdravlje', 'title': 'Fitness za zene: Kako vjezba ti u skladu sa tijelom', 'is_pillar': True},
            {'keyword': 'trening prema fazama ciklusa', 'title': 'Trening prema fazama ciklusa: Vodic za svaku fazu', 'is_pillar': False},
            {'keyword': 'trening snage za zene', 'title': 'Trening snage za zene: Zasto ne trebate izbjegavati tegove', 'is_pillar': False},
            {'keyword': 'yoga za hormonski balans', 'title': 'Yoga za hormone: Poze koje balansiraju zensko zdravlje', 'is_pillar': False},
            {'keyword': 'hodanje za zensko zdravlje', 'title': 'Hodanje za zdravlje: Najjednostavnija vjezba za zene', 'is_pillar': False},
            {'keyword': 'pilates za zene', 'title': 'Pilates za zene: Koristi za tijelo, hormone i um', 'is_pillar': False},
            {'keyword': 'vjezbanje i PCOS', 'title': 'Vjezbanje sa PCOS-om: Sta raditi a sta izbjegavati', 'is_pillar': False},
            {'keyword': 'vjezbanje u trudnoci', 'title': 'Vjezbanje u trudnoci: Sigurne vjezbe trimester po trimester', 'is_pillar': False},
            {'keyword': 'diastaza recti vjezbe', 'title': 'Diastaza recti: Vjezbe za oporavak trbusnih misica', 'is_pillar': False},
            {'keyword': 'vjezbanje u menopauzi', 'title': 'Vjezbanje u menopauzi: Najbolji treninzi za ovo razdoblje', 'is_pillar': False},
            {'keyword': 'kardio vs snaga za zene', 'title': 'Kardio ili snaga: Sta je bolje za zensko zdravlje', 'is_pillar': False},
            {'keyword': 'pretjerano vjezbanje i hormoni', 'title': 'Pretjerano vjezbanje: Kako previse treninga skodi hormonima', 'is_pillar': False},
            {'keyword': 'vjezbe za dno zdjelice', 'title': 'Vjezbe za dno zdjelice: Prevencija i lijecenje', 'is_pillar': False},
            {'keyword': 'jutarnja rutina vjezbi za zene', 'title': 'Jutarnja rutina: 15-minutni trening za energiju cijeli dan', 'is_pillar': False},
            {'keyword': 'stretching za zensko tijelo', 'title': 'Stretching za zene: Istezanje za fleksibilnost i opustanje', 'is_pillar': False},
            {'keyword': 'HIIT trening za zene', 'title': 'HIIT trening za zene: Kada je koristan a kada stetan', 'is_pillar': False},
            {'keyword': 'vjezbanje i gubitak tezine zene', 'title': 'Vjezbanje i mrsavljenje: Zasto zene trebaju drukciji pristup', 'is_pillar': False},
            {'keyword': 'osteoporoza prevencija vjezbama', 'title': 'Osteoporoza: Vjezbe koje jacaju kosti kod zena', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'prirodni-pristupi-zdravlju',
        'posts': [
            {'keyword': 'prirodni pristupi zenskom zdravlju', 'title': 'Prirodni pristupi zenskom zdravlju: Kompletni vodic', 'is_pillar': True},
            {'keyword': 'biljni cajevi za zenske tegobe', 'title': 'Biljni cajevi za zenske tegobe: 10 najdjelotvornijih', 'is_pillar': False},
            {'keyword': 'aromaterapija za zene', 'title': 'Aromaterapija za zene: Etericna ulja za hormonski balans', 'is_pillar': False},
            {'keyword': 'akupunktura za zensko zdravlje', 'title': 'Akupunktura za zene: Koristi za plodnost i hormone', 'is_pillar': False},
            {'keyword': 'detoksikacija estrogena prirodno', 'title': 'Detoksikacija estrogena: Prirodni nacini ciscenja viska', 'is_pillar': False},
            {'keyword': 'jetra i zenski hormoni', 'title': 'Jetra i hormoni: Zasto je ciscenje jetre vazno za zene', 'is_pillar': False},
            {'keyword': 'seed cycling za hormone', 'title': 'Seed cycling: Moze li rotacija sjemenki uravnoteziti hormone', 'is_pillar': False},
            {'keyword': 'kineska medicina za zene', 'title': 'Kineska medicina za zene: Principi i koristi', 'is_pillar': False},
            {'keyword': 'ayurveda za zensko zdravlje', 'title': 'Ayurveda za zene: Drevna mudrost za moderno zdravlje', 'is_pillar': False},
            {'keyword': 'kurkuma za upalu kod zena', 'title': 'Kurkuma za zene: Antiinflamatorno djelovanje i recepti', 'is_pillar': False},
            {'keyword': 'maca korijenje za hormone', 'title': 'Maca korijen: Koristi za energiju i hormonski balans', 'is_pillar': False},
            {'keyword': 'crvena djetelina za menopauzu', 'title': 'Crvena djetelina: Prirodna pomoc u menopauzi', 'is_pillar': False},
            {'keyword': 'upotreba magnezijumovih kupki', 'title': 'Magnezijumove kupke: Relaksacija i zdravlje za zene', 'is_pillar': False},
            {'keyword': 'endokrini disruptori u okolini', 'title': 'Endokrini disruptori: Hemikalije koje remete hormone', 'is_pillar': False},
            {'keyword': 'prirodna kozmetika i hormoni', 'title': 'Prirodna kozmetika: Zasto je vazna za hormonsko zdravlje', 'is_pillar': False},
            {'keyword': 'holisticko lijecenje zenskih tegoba', 'title': 'Holisticki pristup zenskom zdravlju: Tijelo, um i dusa', 'is_pillar': False},
            {'keyword': 'grounding i zensko zdravlje', 'title': 'Grounding (uzemljenje): Kako pomaze zenskom zdravlju', 'is_pillar': False},
            {'keyword': 'sok od celera za hormone', 'title': 'Sok od celera: Da li zaista pomaze hormonima', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'koza-kosa-hormoni',
        'posts': [
            {'keyword': 'koza kosa i hormoni vodic', 'title': 'Koza, kosa i hormoni: Kako su povezani i sta raditi', 'is_pillar': True},
            {'keyword': 'hormonski akne uzroci i lijecenje', 'title': 'Hormonski akne: Uzroci i kako ih lijeciti iznutra', 'is_pillar': False},
            {'keyword': 'akne na bradi i vilici hormoni', 'title': 'Akne na bradi i vilici: Sta govore o vasim hormonima', 'is_pillar': False},
            {'keyword': 'gubitak kose kod zena', 'title': 'Gubitak kose kod zena: Hormonski uzroci i rjesenja', 'is_pillar': False},
            {'keyword': 'hirzutizam visak dlaka zene', 'title': 'Hirzutizam: Visak dlacica kod zena i hormonski uzroci', 'is_pillar': False},
            {'keyword': 'suha koza i hormoni', 'title': 'Suha koza i hormoni: Uzroci i kako je prirodno hidratizirati', 'is_pillar': False},
            {'keyword': 'starenje koze i estrogen', 'title': 'Starenje koze i estrogen: Sta se desava u menopauzi', 'is_pillar': False},
            {'keyword': 'celulite i hormoni', 'title': 'Celulite i hormoni: Uzroci i prirodni pristupi smanjenju', 'is_pillar': False},
            {'keyword': 'koza i crijeva povezanost', 'title': 'Os crijeva-koza: Kako probava utice na izgled koze', 'is_pillar': False},
            {'keyword': 'rosacea i hormoni', 'title': 'Rozacea kod zena: Hormonski okidaci i prirodni tretmani', 'is_pillar': False},
            {'keyword': 'ekcemi i zenski hormoni', 'title': 'Ekcemi i hormoni: Zasto se pogorsavaju tokom ciklusa', 'is_pillar': False},
            {'keyword': 'pigmentacija koze hormoni', 'title': 'Hiperpigmentacija kod zena: Hormonski uzroci i rjesenja', 'is_pillar': False},
            {'keyword': 'njega koze prema fazi ciklusa', 'title': 'Njega koze prema fazi ciklusa: Prilagodite rutinu hormonima', 'is_pillar': False},
            {'keyword': 'lomljivi nokti i nedostatak minerala', 'title': 'Lomljivi nokti: Koji nedostaci minerala su uzrok', 'is_pillar': False},
            {'keyword': 'biotin za kosu i nokte', 'title': 'Biotin za kosu i nokte: Da li zaista funkcionise', 'is_pillar': False},
            {'keyword': 'kolagen i zenski hormoni', 'title': 'Kolagen i estrogen: Kako hormoni uticu na elasticnost koze', 'is_pillar': False},
            {'keyword': 'masna kosa i hormoni', 'title': 'Masna kosa i hormoni: Uzroci i prirodna rjesenja', 'is_pillar': False},
            {'keyword': 'tamni kolutovi oko ociju zene', 'title': 'Tamni kolutovi oko ociju: Hormonski i nutritivni uzroci', 'is_pillar': False},
        ],
    },
    {
        'cluster': 'medicinski-testovi-analize',
        'posts': [
            {'keyword': 'medicinski testovi za zene', 'title': 'Medicinski testovi za zene: Kompletni vodic po godinama', 'is_pillar': True},
            {'keyword': 'hormonski panel krvi sta testirati', 'title': 'Hormonski panel krvi: Koji testovi su neophodni za zene', 'is_pillar': False},
            {'keyword': 'analiza stitne zlijezde TSH T3 T4', 'title': 'Analiza stitne zlijezde: TSH, T3, T4 i sta znace rezultati', 'is_pillar': False},
            {'keyword': 'vitamin D testiranje', 'title': 'Testiranje vitamina D: Zasto je vazno i kako citati rezultate', 'is_pillar': False},
            {'keyword': 'kompletna krvna slika zene', 'title': 'Kompletna krvna slika: Sta svaki parametar znaci za zene', 'is_pillar': False},
            {'keyword': 'HOMA indeks inzulinska rezistencija', 'title': 'HOMA indeks: Rani pokazatelj inzulinske rezistencije', 'is_pillar': False},
            {'keyword': 'testosteron kod zena normalne vrijednosti', 'title': 'Testosteron kod zena: Normalne vrijednosti i sta pokazuje', 'is_pillar': False},
            {'keyword': 'DHEA-S hormon znacaj', 'title': 'DHEA-S hormon: Sta pokazuje i zasto je vazan za zene', 'is_pillar': False},
            {'keyword': 'prolaktin povisen uzroci', 'title': 'Povisen prolaktin: Uzroci, simptomi i lijecenje', 'is_pillar': False},
            {'keyword': 'AMH test rezerva jajnika', 'title': 'AMH test: Sta govori o rezervi jajnika', 'is_pillar': False},
            {'keyword': 'ultrazvuk zdjelice znacaj', 'title': 'Ultrazvuk zdjelice: Zasto je vazan i sta pokazuje', 'is_pillar': False},
            {'keyword': 'mamografija kada i zasto', 'title': 'Mamografija: Kada poceti i koliko cesto je raditi', 'is_pillar': False},
            {'keyword': 'CRP i upala u tijelu', 'title': 'CRP marker: Sta pokazuje o upali u zenskom tijelu', 'is_pillar': False},
            {'keyword': 'test intolerancije na hranu', 'title': 'Testovi intolerancije na hranu: Koji su pouzdani', 'is_pillar': False},
            {'keyword': 'gustoca kostiju DEXA sken', 'title': 'DEXA sken: Test gustoce kostiju za zene', 'is_pillar': False},
            {'keyword': 'lipidni profil zene', 'title': 'Lipidni profil: Holesterol i trigliceridi kod zena', 'is_pillar': False},
            {'keyword': 'HbA1c test za zene', 'title': 'HbA1c test: Sta govori o vasem seceru u krvi', 'is_pillar': False},
            {'keyword': 'genski testovi za zensko zdravlje', 'title': 'Genski testovi: Sta mogu otkriti o vasem zdravlju', 'is_pillar': False},
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

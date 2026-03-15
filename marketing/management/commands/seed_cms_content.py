from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from marketing.models import Page, Post, NavMenu, Footer, Category, Tag


def _editorjs_body(blocks):
    return {'blocks': blocks, 'version': '2.30.2'}


class Command(BaseCommand):
    help = 'Seed CMS sadržaj za ŽenskoZdravlje.ba: stranice, blog postovi, navigacija i footer'

    def handle(self, *args, **options):
        self._seed_categories_tags()
        self._seed_pages()
        self._seed_posts()
        self._seed_navigation()
        self._seed_footer()
        self.stdout.write(self.style.SUCCESS('CMS sadržaj uspješno kreiran.'))

    def _seed_categories_tags(self):
        categories_data = [
            ('Hormoni i menstrualni ciklus', 'hormoni-menstrualni-ciklus'),
            ('PCOS i hormonski poreme\u0107aji', 'pcos-i-hormonski-poremecaji'),
            ('Ginekolo\u0161ko zdravlje', 'ginekolosko-zdravlje'),
            ('Ishrana za \u017eensko zdravlje', 'ishrana-zensko-zdravlje'),
            ('Vitamini, suplementi i minerali', 'vitamini-suplementi-minerali'),
            ('Mentalno zdravlje \u017eena', 'mentalno-zdravlje-zena'),
            ('Plodnost i trudno\u0107a', 'plodnost-i-trudnoca'),
            ('Fitness i kretanje za \u017eene', 'fitness-kretanje-zene'),
            ('Prirodni pristupi zdravlju', 'prirodni-pristupi-zdravlju'),
            ('Ko\u017ea, kosa i hormoni', 'koza-kosa-i-hormoni'),
            ('Medicinski testovi i analize', 'medicinski-testovi-analize'),
        ]
        for name, slug in categories_data:
            Category.objects.update_or_create(slug=slug, defaults={'name': name})

        for name, slug in [
            ('Početnice', 'pocetnice'),
            ('PCOS', 'pcos'),
            ('Hormoni', 'hormoni'),
            ('Suplementi', 'suplementi'),
            ('Ishrana', 'ishrana'),
            ('Stres', 'stres'),
            ('Menstruacija', 'menstruacija-tag'),
            ('Trudnoća', 'trudnoca'),
        ]:
            Tag.objects.get_or_create(slug=slug, defaults={'name': name})
        self.stdout.write('  Kategorije i tagovi kreirani.')

    def _seed_pages(self):
        pages = [
            {
                'title': 'O Nama',
                'slug': 'o-nama',
                'status': 'published',
                'seo_title': 'O Nama — ŽenskoZdravlje.ba',
                'seo_description': 'Saznajte više o ŽenskoZdravlje.ba — našoj misiji, timu i zašto smo pokrenuli ovaj portal za žene u Bosni i Hercegovini.',
                'blocks_json': {
                    'blocks': [
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'header', 'data': {'text': 'Naša misija', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'ŽenskoZdravlje.ba je nastao iz jedne jednostavne potrebe: žene u Bosni i Hercegovini zaslužuju pouzdane, razumljive i besplatne informacije o svom zdravlju. Zdravstvene informacije na internetu uglavnom su na stranim jezicima, prepune medicinskog žargona ili nedovoljno prilagođene kontekstu žena u našoj regiji.'}},
                                {'type': 'paragraph', 'data': {'text': 'Naš portal pokriv a teme koje su najvažnije za žensko zdravlje: PCOS i hormonalni disbalans, menstrualni ciklus, trudnoću i plodnost, ishranu i suplemente, te mentalno zdravlje. Sve na bosanskom jeziku, jasno i pristupačno.'}},
                                {'type': 'header', 'data': {'text': 'Zašto smo pokrenuli ovaj portal', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Pokrenuli smo ŽenskoZdravlje.ba jer smo svjesni da mnoge žene godinama traže odgovore na pitanja o svom tijelu, a ne mogu naći pouzdane informacije na bosanskom jeziku. Naš cilj je popuniti tu prazninu — korak po korak, članak po članak.'}},
                                {'type': 'paragraph', 'data': {'text': 'Važna napomena: sav sadržaj na ovom portalu je isključivo informativan i edukativnog karaktera. Ne zamjenjuje savjet, dijagnozu niti liječenje od strane kvalificiranog zdravstvenog radnika. Uvijek se posavjetujte s liječnikom ili ginekologom za konkretne zdravstvene probleme.'}},
                            ]),
                        },
                        {
                            'type': 'feature_grid',
                            'items': [
                                {
                                    'title': 'PCOS i hormoni',
                                    'body': 'Sve o sindromu policističnih jajnika, hormonalnom disbalansu i načinima regulacije hormona prirodnim i medicinskim putem.',
                                },
                                {
                                    'title': 'Menstrualni ciklus',
                                    'body': 'Objašnjenja menstrualnog ciklusa, neredovite menstruacije, boli i svega što žene trebaju znati o svom ciklusu.',
                                },
                                {
                                    'title': 'Trudnoća i plodnost',
                                    'body': 'Informacije o planiranju trudnoće, plodnosti, prenatalnoj njezi i zdravlju tokom trudnoće.',
                                },
                                {
                                    'title': 'Ishrana i suplementi',
                                    'body': 'Preporuke za ishranu i suplemente koji podržavaju žensko zdravlje u različitim fazama života.',
                                },
                            ],
                        },
                        {
                            'type': 'callout',
                            'title': 'Medicinska napomena',
                            'body': 'Sadržaj na ŽenskoZdravlje.ba je isključivo informativan i edukativnog karaktera. Ne zamjenjuje savjet, dijagnozu niti liječenje od strane kvalificiranog zdravstvenog radnika. Za konkretne zdravstvene tegobe uvijek se obratite svom ginekologu ili liječniku.',
                        },
                    ]
                },
            },
            {
                'title': 'Preporučeni Suplementi',
                'slug': 'suplementi',
                'status': 'published',
                'seo_title': 'Preporučeni suplementi za žensko zdravlje — ŽenskoZdravlje.ba',
                'seo_description': 'Pregled najvažnijih suplemenata za žensko zdravlje: folna kiselina, magnezij, vitamin D, omega-3 i drugi. Informacije zasnovane na istraživanjima.',
                'blocks_json': {
                    'blocks': [
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'header', 'data': {'text': 'Suplementi za žensko zdravlje', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Pravilna ishrana je temelj zdravlja, ali u nekim slučajevima tijelo zahtijeva dodatnu podršku kroz suplemente. Žene su u posebno ranjivoj skupini kada je riječ o nedostatku određenih nutrijenata — zbog menstrualnog ciklusa, trudnoće, dojenja ili specifičnih zdravstvenih stanja kao što je PCOS.'}},
                                {'type': 'paragraph', 'data': {'text': 'Ovdje donosimo pregled suplemenata koji se najčešće preporučuju ženama, zajedno s objašnjenjem zašto su važni i na što treba obratiti pažnju pri kupnji.'}},
                            ]),
                        },
                        {
                            'type': 'callout',
                            'title': 'Napomena',
                            'body': 'Ovi suplementi su informativne prirode. Prije uvođenja bilo kojeg suplementa u svoju rutinu, posavjetujte se s liječnikom, posebno ako imate neko zdravstveno stanje, uzimate lijekove ili ste trudni.',
                        },
                        {
                            'type': 'feature_grid',
                            'items': [
                                {
                                    'title': 'Folna kiselina',
                                    'body': 'Esencijalna za žene u reproduktivnoj dobi, posebno tokom planiranja trudnoće i u prvom tromjesečju. Pomaže u prevenciji neuroloških defekata kod bebe. Preporučena doza: 400-800 mcg dnevno.',
                                },
                                {
                                    'title': 'Magnezij',
                                    'body': 'Magnezij je uključen u preko 300 enzimskih reakcija u tijelu. Pomaže kod menstrualnih bolova, PMS-a, migrena i anksioznosti. Žene s PCOS-om često imaju niže razine magnezija.',
                                },
                                {
                                    'title': 'Vitamin D',
                                    'body': 'Vitamin D je esencijalan za hormonalni balans, imunosni sustav i zdravlje kostiju. Nedostatak vitamina D je posebno čest u zimskim mjesecima i kod žena s PCOS-om. Preporučuje se redovna provjera razina.',
                                },
                                {
                                    'title': 'Omega-3 masne kiseline',
                                    'body': 'Omega-3 masne kiseline (EPA i DHA) imaju protuupalna svojstva i podržavaju hormonalni balans. Posebno korisne za žene s PCOS-om, endometriozom i menstrualnim bolovima.',
                                },
                            ],
                        },
                        {
                            'type': 'faq',
                            'items': [
                                {
                                    'question': 'Da li trebam uzimati suplemente svakodnevno?',
                                    'answer': 'Većina suplemenata je najefikasnija kada se uzima redovno. Međutim, važno je pratiti preporučene doze i ne prekoračivati ih. Uvijek se posavjetujte s liječnikom o optimalnom rasporedu.',
                                },
                                {
                                    'question': 'Mogu li uzimati više suplemenata istovremeno?',
                                    'answer': 'U principu da, ali neke kombinacije mogu smanjiti apsorpciju ili izazvati interakcije. Na primjer, kalcij i magnezij kompetiraju za apsorpciju pa ih je bolje uzimati u različito doba dana.',
                                },
                                {
                                    'question': 'Koliko dugo treba uzimati suplemente da se vide rezultati?',
                                    'answer': 'Ovisi o suplementu i o tome koliki je bio nedostatak. Obično su potrebne 4-12 sedmica redovne primjene da se osjete značajni rezultati. Vitamin D, na primjer, može uzeti nekoliko mjeseci da se razine normalizuju.',
                                },
                                {
                                    'question': 'Da li su prirodni suplementi sigurniji od sintetičkih?',
                                    'answer': 'Nije uvijek tako jednostavno. Važnija je kvaliteta i bioraspoloživost suplementa od toga je li prirodan ili sintetički. Birajte suplemente od provjerenih proizvođača koji provode testiranja trećih strana.',
                                },
                            ],
                        },
                    ]
                },
            },
            {
                'title': 'Kontakt',
                'slug': 'kontakt',
                'status': 'published',
                'seo_title': 'Kontakt — ŽenskoZdravlje.ba',
                'seo_description': 'Kontaktirajte tim ŽenskoZdravlje.ba. Rado ćemo odgovoriti na vaša pitanja.',
                'blocks_json': {
                    'blocks': [
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'header', 'data': {'text': 'Stupite u kontakt s nama', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Radujemo se vašim porukama! Bilo da imate pitanje o sadržaju koji smo objavili, prijedlog za novu temu, ispravku greške ili jednostavno želite reći zdravo — slobodno nam pišite.'}},
                                {'type': 'paragraph', 'data': {'text': 'Možete nas kontaktirati putem e-pošte na adresu: zdravlje@zenskozdravljeba.com'}},
                                {'type': 'header', 'data': {'text': 'O sadržaju i temama', 'level': 3}},
                                {'type': 'paragraph', 'data': {'text': 'Ako primijetite grešku u nekom od naših članaka, ili biste željeli predložiti temu koja vas zanima, slobodno nam javite. Trudimo se da naš sadržaj bude što tačniji i korisniji.'}},
                            ]),
                        },
                        {
                            'type': 'callout',
                            'title': 'Vrijeme odgovora',
                            'body': 'Nastojimo odgovoriti na sve upite u roku od 2-3 radna dana. Hvala vam na strpljenju!',
                        },
                    ]
                },
            },
        ]

        for page_data in pages:
            blocks_json = page_data.pop('blocks_json', None)
            page, created = Page.objects.update_or_create(
                slug=page_data['slug'],
                defaults={**page_data, 'blocks_json': blocks_json},
            )
            action = 'Kreirana' if created else 'Ažurirana'
            self.stdout.write(f'  {action} stranica: {page.title}')

    def _seed_posts(self):
        posts_data = [
            {
                'title': 'OVA Lab Inositol: Najkvalitetniji Myo-Inositol i D-Chiro Inositol suplement u Bosni i Hercegovini',
                'slug': 'ova-lab-inositol-myo-d-chiro-pcos-bih',
                'status': 'published',
                'publish_at': timezone.now(),
                'author_name': '\u017denskoZdravlje.ba Tim',
                'cover_image': '/static/images/ilustracija-ova-lab.svg',
                'excerpt': 'OVA Lab d.o.o. donosi u Bosnu i Hercegovinu premium Myo-Inositol i D-Chiro Inositol suplement u klinički prouvanom omjeru 40:1, proizveden u UK, bez štetnih punila.',
                'seo_title': 'OVA Lab Inositol za PCOS: Myo-Inositol i D-Chiro Inositol u BiH | \u017denskoZdravlje.ba',
                'seo_description': 'OVA Lab donosi najkvalitetniji Myo-Inositol i D-Chiro Inositol suplement u BiH. Klinički prouvan omjer 40:1, UK proizvodnja, bez štetnih punila. Posebno formuliran za žene s PCOS-om.',
                'categories': ['vitamini-suplementi-minerali', 'pcos-i-hormonski-poremecaji'],
                'tags': ['suplementi', 'pcos'],
                'blocks_json': {
                    'blocks': [
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'paragraph', 'data': {'text': 'U svijetu suplementacije za žensko zdravlje, inositol je jedna od najis tra\u017eivanijih supstanci posljednjih godina. Posebno za \u017eene s PCOS-om (sindromom polici\u0161ti\u010dnih jajnika), kombinacija Myo-Inositola i D-Chiro Inositola pokazala se iznimno efikasnom. Sada, zahvaljuju\u0107i OVA Lab d.o.o., \u017eene u Bosni i Hercegovini kona\u010dno imaju pristup suplementu koji ispunjava me\u0111unarodne standarde kvalitete.'}},
                                {'type': 'header', 'data': {'text': 'Šta je Myo-Inositol i D-Chiro Inositol?', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Inositol je prirodna supstanca koja se svrstava u vitamine B grupe. U tijelu postoji u vi\u0161e oblika, od kojih su Myo-Inositol i D-Chiro Inositol najva\u017eniji za \u017eensko reproduktivno zdravlje. Myo-Inositol podr\u017eava signalizaciju inzulina i promi\u010de zdravu ovulaciju, dok D-Chiro Inositol igra klju\u010dnu ulogu u metabolizmu androgena i osjetljivosti na inzulin.'}},
                                {'type': 'paragraph', 'data': {'text': 'Klini\u010dka istra\u017eivanja pokazuju da \u017eene s PCOS-om \u010desto imaju poreme\u0107en omjer ova dva oblika inositola u tijelu. Upravo tu nastupa suplementacija.'}},
                                {'type': 'header', 'data': {'text': 'Zašto je omjer 40:1 toliko važan?', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Klini\u010dki prouvan omjer Myo-Inositola i D-Chiro Inositola je ta\u010dno 40:1. Ovaj omjer odra\u017eava prirodnu ravnote\u017eu koja postoji u zdravom \u017eenskom tijelu. OVA Lab je precizno formulisan prema ovom omjeru, \u0161to zna\u010di da ne uzimate samo "ne\u0161to inositola" nego ta\u010dno onu kombinaciju koju va\u0161e tijelo treba. Mnogi suplementi na tr\u017ei\u0161tu sadr\u017ee samo Myo-Inositol ili imaju neta\u010dan omjer.'}},
                                {'type': 'header', 'data': {'text': 'Proizvodnja u Ujedinjenom Kraljevstvu', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'OVA Lab je proizveden u tvornici u Ujedinjenom Kraljevstvu koja sara\u0111uje s nekim od najpoznatijih svjetskih brendova suplementacije. To zna\u010di stroge standarde kontrole kvalitete, provjeru sirovina i precizno doziranje. Ovakav nivo kvalitete do sada nije bio dostupan na bh. tr\u017ei\u0161tu po pristupa\u010dnoj cijeni.'}},
                                {'type': 'header', 'data': {'text': 'Bez štetnih punila', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Jedan od najve\u0107ih problema s inositol suplementima dostupnim u BiH je prisustvo nepotrebnih ili \u0161tetnih punila, veziva i aditiva. OVA Lab je formulisan bez tih supstanci. Dobijate \u010distu kombinaciju aktivnih ingredijenata bez balasta koji mo\u017ee umanjiti efikasnost ili izazvati ne\u017eeljene reakcije.'}},
                            ]),
                        },
                        {
                            'type': 'callout',
                            'title': 'Za koga je OVA Lab Inositol?',
                            'body': 'OVA Lab je posebno koristan za žene s PCOS-om, hormonalnim disbalansom, neredovitom menstruacijom ili poteškoćama s plodnošću. Kao i uvijek, preporučujemo savjetovanje s liječnikom ili ginekologom prije uvođenja novog suplementa.',
                        },
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'header', 'data': {'text': 'Gdje kupiti OVA Lab Inositol?', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'OVA Lab Inositol mo\u017eete prona\u0107i na slu\u017ebenoj web stranici OVA Lab d.o.o. Posjetite ovalab.ba za vi\u0161e informacija o proizvodu, sastavu, doziranju i na\u010dinu narud\u017ebe s dostavom u Bosnu i Hercegovinu.'}},
                            ]),
                        },
                        {
                            'type': 'cta',
                            'title': 'Saznajte više o OVA Lab Inositolu',
                            'body': 'Posjetite zvaničnu stranicu OVA Lab d.o.o. i saznajte sve o ovom premium suplementu za žensko zdravlje.',
                            'button_label': 'Posjetite ovalab.ba',
                            'button_url': 'https://ovalab.ba',
                        },
                    ]
                },
            },
            {
                'title': 'PCOS: Šta je to i kako utiče na vaše zdravlje',
                'slug': 'pcos-sta-je-i-kako-utice-na-zdravlje',
                'status': 'published',
                'publish_at': timezone.now() - timedelta(days=2),
                'author_name': '\u017denskoZdravlje.ba Tim',
                'cover_image': '/static/images/ilustracija-pcos.svg',
                'excerpt': 'Sindrom policističnih jajnika (PCOS) jedan je od najčešćih hormonalnih poremećaja kod žena u reproduktivnoj dobi. Saznajte šta je PCOS, koji su simptomi i kako se dijagnosticira.',
                'seo_title': 'PCOS: Šta je to i kako utiče na vaše zdravlje | ŽenskoZdravlje.ba',
                'seo_description': 'Sve što trebate znati o sindromu policističnih jajnika (PCOS): simptomi, uzroci, dijagnoza i opcije liječenja. Stručni članak na bosanskom jeziku.',
                'categories': ['pcos-i-hormonski-poremecaji'],
                'tags': ['pcos', 'hormoni'],
                'blocks_json': {
                    'blocks': [
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'paragraph', 'data': {'text': 'Sindrom policističnih jajnika, poznat pod kraticom PCOS (od engleskog Polycystic Ovary Syndrome), jedan je od najčešćih hormonalnih poremećaja kod žena u reproduktivnoj dobi. Procjenjuje se da od PCOS-a boluje između 8 i 13% žena reproduktivne dobi širom svijeta, što ga čini jednim od vodećih uzroka neplodnosti.'}},
                                {'type': 'paragraph', 'data': {'text': 'Unatoč rasprostranjenosti, PCOS je često nedijagnosticiran ili pogrešno shvaćen. Mnoge žene žive godinama s simptomima ne znajući da imaju ovaj sindrom. Dobra vijest je da uz pravilnu dijagnozu i liječenje, većina žena s PCOS-om može uspješno upravljati simptomima i živjeti punim životom.'}},
                                {'type': 'header', 'data': {'text': 'Šta je zapravo PCOS?', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'PCOS je kompleksan endokrini poremećaj koji utječe na jajnike i hormonalnu ravnotežu u tijelu. Naziv "policistični" odnosi se na pojavu malih folikula (cista) na jajnicima koji se mogu vidjeti na ultrazvuku, iako nisu svi slučajevi PCOS-a praćeni cistama.'}},
                                {'type': 'paragraph', 'data': {'text': 'Tri ključna obilježja PCOS-a su: nepravilna ovulacija ili izostanak ovulacije, povišene razine androgena (muških hormona) i policistični izgled jajnika na ultrazvuku. Za dijagnozu PCOS-a, prema Rotterdamskim kriterijima, dovoljno je prisustvo dva od ova tri obilježja.'}},
                                {'type': 'header', 'data': {'text': 'Najčešći simptomi PCOS-a', 'level': 2}},
                                {'type': 'list', 'data': {'style': 'unordered', 'items': [
                                    'Neredovita menstruacija ili izostanak menstruacije',
                                    'Pojačana dlakavost na licu, grudima ili stomaku (hirzutizam)',
                                    'Akne i masna koža',
                                    'Gubitak kose ili stanjenje kose na glavi',
                                    'Poteškoće s gubitkom kilograma ili nepojašnjeno debljanje',
                                    'Otpornost na inzulin',
                                    'Poteškoće s začećem',
                                    'Tamnjenje kože u pregibima (akantoza nigrikans)',
                                ]}},
                            ]),
                        },
                        {
                            'type': 'callout',
                            'title': 'Važna činjenica',
                            'body': 'PCOS je najčešći uzrok anovulatorne neplodnosti — neplodnosti uzrokovane izostankom ovulacije. Međutim, uz odgovarajući tretman, mnoge žene s PCOS-om uspješno zatrudne.',
                        },
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'header', 'data': {'text': 'Uzroci PCOS-a', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Tačan uzrok PCOS-a još uvijek nije u potpunosti razjašnjen, ali istraživanja ukazuju na kombinaciju genetskih faktora i faktora okoliša. Neke od ključnih uloga igraju: genetska predispozicija (PCOS se češće javlja u porodicama), otpornost na inzulin, upalni procesi u tijelu i poremećaji u lučenju hormona iz mozga.'}},
                                {'type': 'header', 'data': {'text': 'Kako se dijagnosticira PCOS?', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Dijagnoza PCOS-a postavlja se na osnovu kombinacije kliničkih simptoma, laboratorijskih nalaza i ultrazvuka jajnika. Ljekar će obično naručiti analizu hormona (LH, FSH, testosteron, inzulin, šećer u krvi), ultrazvuk abdomena ili transvaginalni ultrazvuk, te isključiti druga stanja koja mogu imati slične simptome (kao što su bolesti štitnjače ili nadbubrežne žlijezde).'}},
                            ]),
                        },
                        {
                            'type': 'faq',
                            'items': [
                                {
                                    'question': 'Mogu li žene s PCOS-om zatrudnjeti?',
                                    'answer': 'Da, apsolutno! Mnoge žene s PCOS-om zatrudne, bilo prirodno ili uz medicinsku pomoć. PCOS je vodeći uzrok anovulatorne neplodnosti, ali uz pravilno liječenje i stimulaciju ovulacije, šanse za trudnoću su dobre. Posavjetujte se s ginekologom o opcijama koje su vam na raspolaganju.',
                                },
                                {
                                    'question': 'Da li gubitak tjelesne mase pomaže kod PCOS-a?',
                                    'answer': 'Za žene s PCOS-om koje imaju prekomjernu tjelesnu težinu, čak i umjereni gubitak kilograma (5-10% tjelesne težine) može značajno poboljšati hormonalni balans, regulisati menstrualni ciklus i povećati šanse za ovulaciju. Međutim, PCOS se javlja i kod žena normalne tjelesne težine.',
                                },
                                {
                                    'question': 'Da li PCOS nestaje s menopauzom?',
                                    'answer': 'Menopauza donosi kraj menstrualnog ciklusa i promjene u hormonalnom profilu, ali PCOS može i dalje utjecati na zdravlje žene u menopauzi, posebno u pogledu metaboličkog zdravlja i rizika od dijabetesa tipa 2 i kardiovaskularnih bolesti. Važno je nastaviti redovne kontrole i nakon menopauze.',
                                },
                            ],
                        },
                    ]
                },
            },
            {
                'title': 'Kako regulisati menstrualni ciklus prirodnim putem',
                'slug': 'kako-regulisati-menstrualni-ciklus',
                'status': 'published',
                'publish_at': timezone.now() - timedelta(days=1),
                'author_name': '\u017denskoZdravlje.ba Tim',
                'cover_image': '/static/images/ilustracija-menstrualni-ciklus.svg',
                'excerpt': 'Neredovita menstruacija može biti uzrokovana stresom, prehranom, hormonalnim disbalansom ili drugim faktorima. Saznajte šta je normalan ciklus i kako prirodno potaknuti njegovu regulaciju.',
                'seo_title': 'Kako regulisati menstrualni ciklus prirodnim putem | ŽenskoZdravlje.ba',
                'seo_description': 'Saznajte šta uzrokuje neredovitu menstruaciju i koje prirodne metode mogu pomoći u regulaciji menstrualnog ciklusa. Stručni savjeti za žene.',
                'categories': ['hormoni-menstrualni-ciklus'],
                'tags': ['menstruacija-tag', 'hormoni'],
                'blocks_json': {
                    'blocks': [
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'paragraph', 'data': {'text': 'Menstrualni ciklus je jedna od najvažnijih mjera zdravlja kod žena. Redovit ciklus ukazuje na to da su hormoni u ravnoteži, ovulacija se odvija normalno i reproduktivni sustav funkcionira kako treba. S druge strane, neredovita menstruacija može biti znak hormonalnog disbalansa ili nekog drugog zdravstvenog stanja koje zaslužuje pažnju.'}},
                                {'type': 'header', 'data': {'text': 'Šta je normalan menstrualni ciklus?', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Normalan menstrualni ciklus traje između 21 i 35 dana, pri čemu se kao "normalno" smatra svako trajanje unutar ovog raspona. Menstrualno krvarenje obično traje 2 do 7 dana. Važno je razumjeti da ono što je normalno za vas može se razlikovati od onoga što je normalno za drugu ženu — bitno je da je vaš ciklus relativno predvidiv i redovit.'}},
                                {'type': 'header', 'data': {'text': 'Uzroci neredovite menstruacije', 'level': 2}},
                                {'type': 'list', 'data': {'style': 'unordered', 'items': [
                                    'Stres (jedan od najčešćih uzroka)',
                                    'Prekomjerna fizička aktivnost ili nedovoljno kretanje',
                                    'Nagle promjene u tjelesnoj težini',
                                    'Nedovoljan unos kalorija ili poremećaji prehrane',
                                    'Hormonalni disbalans (PCOS, hipotireoza, hiperprolaktinemija)',
                                    'Perimenopauza',
                                    'Uzimanje određenih lijekova ili kontraceptiva',
                                ]}},
                                {'type': 'header', 'data': {'text': 'Prirodni pristupi za regulaciju ciklusa', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Prije nego što posegnete za hormonskim tretmanima, vrijedi razmotriti neke promjene životnog stila koje mogu prirodno podržati hormonalni balans i regularnost ciklusa.'}},
                                {'type': 'header', 'data': {'text': 'Upravljanje stresom', 'level': 3}},
                                {'type': 'paragraph', 'data': {'text': 'Stres direktno utječe na osi hipotalamus-hipofiza-jajnici i može poremetiti lučenje hormona koji reguliraju ovulaciju. Tehnike poput meditacije, joge, dubokog disanja i redovnih šetnji u prirodi mogu značajno smanjiti razine kortizola (hormona stresa) i poboljšati regularnost ciklusa.'}},
                                {'type': 'header', 'data': {'text': 'Prehrana i ishrana', 'level': 3}},
                                {'type': 'paragraph', 'data': {'text': 'Prehrana bogata vlaknima, zdravim mastima i antioksidansima podržava hormonalni balans. Posebno je korisno uključiti namirnice bogate omega-3 masnim kiselinama (masna riba, laneno sjeme), magnezijumom (tamna čokolada, orašasti plodovi, tamnozeleno povrće) i cink om (bundeva sjemenke, mahunarke).'}},
                                {'type': 'header', 'data': {'text': 'Umjeren trening', 'level': 3}},
                                {'type': 'paragraph', 'data': {'text': 'Pretjerana fizička aktivnost može poremetiti menstrualni ciklus (poznato kao atletska amenoreja). S druge strane, umjeren, redovan trening pomaže u regulaciji inzulina i smanjenju upale — što je korisno posebno za žene s PCOS-om. Cilj je umjerena aktivnost 150-300 minuta sedmično.'}},
                            ]),
                        },
                        {
                            'type': 'callout',
                            'title': 'Kada posjetiti ljekara?',
                            'body': 'Obratite se ginekologu ako menstruacija izostane tri ili više ciklusa, ako je menstruacija izuzetno bolna ili obilna, ako imate krvarenje između ciklusa, ili ako primijetite bilo kakvu drugu zabrinjavajuću promjenu u svom ciklusu.',
                        },
                    ]
                },
            },
            {
                'title': 'Vitamin D i žensko zdravlje: zašto je toliko važan',
                'slug': 'vitamin-d-zensko-zdravlje',
                'status': 'published',
                'publish_at': timezone.now() - timedelta(days=3),
                'author_name': '\u017denskoZdravlje.ba Tim',
                'cover_image': '/static/images/ilustracija-vitamin-d.svg',
                'excerpt': 'Nedostatak vitamina D je globalna epidemija, a žene su posebno ranjive. Saznajte zašto je vitamin D toliko važan za žensko zdravlje, koji su simptomi nedostatka i kako osigurati optimalne razine.',
                'seo_title': 'Vitamin D i žensko zdravlje: zašto je toliko važan | ŽenskoZdravlje.ba',
                'seo_description': 'Sve o vitaminu D i ženskom zdravlju: simptomi nedostatka, preporučene doze, hrana bogata vitaminom D i savjeti za suplementaciju.',
                'categories': ['vitamini-suplementi-minerali'],
                'tags': ['suplementi', 'ishrana'],
                'blocks_json': {
                    'blocks': [
                        {
                            'type': 'rich_text',
                            'content': _editorjs_body([
                                {'type': 'paragraph', 'data': {'text': 'Vitamin D nije samo vitamin — on djeluje kao hormon u tijelu i uključen je u gotovo svaki aspekt zdravlja: od jačanja kostiju i imunosnog sistema, do regulacije raspoloženja, hormonalne ravnoteže i zaštite od hroničnih bolesti. Nažalost, procjenjuje se da više od milijardu ljudi širom svijeta ima nedostatak vitamina D, a žene su posebno pogođene.'}},
                                {'type': 'header', 'data': {'text': 'Zašto su žene posebno ranjive?', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Nekoliko faktora čini žene posebno sklonim nedostatku vitamina D. Trudnoća i dojenje dramatično iscrpljuju zalihe vitamina D. Žene s PCOS-om imaju statistički niže razine vitamina D. Starenje smanjuje sposobnost kože da sintetiše vitamin D. Provođenje više vremena u zatvorenom prostoru i upotreba zaštitnih kremova (koje blokiraju UVB zrake) dodatno smanjuju prirodnu sintezu.'}},
                                {'type': 'header', 'data': {'text': 'Simptomi nedostatka vitamina D', 'level': 2}},
                                {'type': 'list', 'data': {'style': 'unordered', 'items': [
                                    'Umor i iscrpljenost bez jasnog uzroka',
                                    'Bolovi u kostima i mišićima',
                                    'Učestale infekcije i slab imunitet',
                                    'Depresivno raspoloženje i anksioznost',
                                    'Gubitak kose',
                                    'Poteškoće s koncentracijom i pamćenjem',
                                    'Polagano zarastanje rana',
                                ]}},
                                {'type': 'header', 'data': {'text': 'Optimalne razine vitamina D', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Razina vitamina D mjeri se krvnim testom (25-OH vitamin D). Prema većini stručnjaka, optimalne razine za opće zdravlje su između 50 i 80 ng/mL. Razine ispod 20 ng/mL se smatraju nedostatkom, a razine između 20 i 30 ng/mL insuficijencijom.'}},
                                {'type': 'header', 'data': {'text': 'Vitamin D i PCOS', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Istraživanja dosljedno pokazuju da žene s PCOS-om imaju statistički niže razine vitamina D u usporedbi sa ženama bez ovog sindroma. Suplementacija vitaminom D u studijama je pokazala pozitivan učinak na regulaciju menstrualnog ciklusa, osjetljivost na inzulin i razine androgena. Zbog toga se ženama s PCOS-om posebno preporučuje provjera i suplementacija vitaminom D.'}},
                                {'type': 'header', 'data': {'text': 'Preporučene doze suplementacije', 'level': 2}},
                                {'type': 'paragraph', 'data': {'text': 'Preporučena dnevna doza vitamina D ovisi o postojećim razinama u krvi i individualnim potrebama. Općenito se preporučuje:'}},
                                {'type': 'list', 'data': {'style': 'unordered', 'items': [
                                    'Preventivna suplementacija: 1000-2000 IU dnevno',
                                    'Kod nedostatka (20-30 ng/mL): 2000-4000 IU dnevno',
                                    'Kod teškog nedostatka (ispod 20 ng/mL): 4000-10000 IU dnevno pod nadzorom ljekara',
                                    'Tokom trudnoće: 1500-2000 IU dnevno (ili prema preporuci ginekologa)',
                                ]}},
                                {'type': 'paragraph', 'data': {'text': 'Vitamin D je topljiv u masti, što znači da ga je bolje uzimati s obrokom koji sadrži zdrave masti (avokado, orašasti plodovi, maslinovo ulje). Kombinacija s vitaminom K2 (posebno K2-MK7) pomaže usmjeravanju kalcija u kosti, a ne u krvne žile.'}},
                            ]),
                        },
                        {
                            'type': 'callout',
                            'title': 'Savjet',
                            'body': 'Prije nego što počnete uzimati visoke doze vitamina D, napravite krvnu analizu (25-OH vitamin D). Na osnovu nalaza, liječnik može preporučiti odgovarajuću dozu. Previsoke doze vitamina D mogu biti štetne.',
                        },
                    ]
                },
            },
        ]

        for post_data in posts_data:
            categories = post_data.pop('categories', [])
            tags = post_data.pop('tags', [])
            blocks_json = post_data.pop('blocks_json', None)

            post, created = Post.objects.update_or_create(
                slug=post_data['slug'],
                defaults={**post_data, 'blocks_json': blocks_json},
            )

            if categories:
                post.categories.set(Category.objects.filter(slug__in=categories))
            if tags:
                post.tags.set(Tag.objects.filter(slug__in=tags))

            action = 'Kreiran' if created else 'Ažuriran'
            self.stdout.write(f'  {action} post: {post.title}')

    def _seed_navigation(self):
        nav, _ = NavMenu.objects.update_or_create(
            name='Primary',
            defaults={
                'items_json': [
                    {'label': 'Početna', 'url': '/'},
                    {'label': 'Blog', 'url': '/blog/'},
                    {'label': 'PCOS', 'url': '/kategorija/pcos-i-hormonski-poremecaji/'},
                    {'label': 'Suplementi', 'url': '/kategorija/vitamini-suplementi-minerali/'},
                    {'label': 'O Nama', 'url': '/o-nama/'},
                    {'label': 'Kontakt', 'url': '/kontakt/'},
                ]
            }
        )
        self.stdout.write('  Navigacija kreirana.')

    def _seed_footer(self):
        Footer.objects.update_or_create(
            label='Default',
            defaults={
                'columns_json': [
                    {
                        'title': 'Zdravstvene teme',
                        'links': [
                            {'label': 'Hormoni i menstrualni ciklus', 'url': '/kategorija/hormoni-menstrualni-ciklus/'},
                            {'label': 'PCOS i hormonski poreme\u0107aji', 'url': '/kategorija/pcos-i-hormonski-poremecaji/'},
                            {'label': 'Ginekolo\u0161ko zdravlje', 'url': '/kategorija/ginekolosko-zdravlje/'},
                            {'label': 'Ishrana za \u017eensko zdravlje', 'url': '/kategorija/ishrana-zensko-zdravlje/'},
                            {'label': 'Vitamini, suplementi i minerali', 'url': '/kategorija/vitamini-suplementi-minerali/'},
                            {'label': 'Mentalno zdravlje \u017eena', 'url': '/kategorija/mentalno-zdravlje-zena/'},
                        ]
                    },
                    {
                        'title': 'Vi\u0161e tema',
                        'links': [
                            {'label': 'Plodnost i trudno\u0107a', 'url': '/kategorija/plodnost-i-trudnoca/'},
                            {'label': 'Fitness i kretanje za \u017eene', 'url': '/kategorija/fitness-kretanje-zene/'},
                            {'label': 'Prirodni pristupi zdravlju', 'url': '/kategorija/prirodni-pristupi-zdravlju/'},
                            {'label': 'Ko\u017ea, kosa i hormoni', 'url': '/kategorija/koza-kosa-i-hormoni/'},
                            {'label': 'Medicinski testovi i analize', 'url': '/kategorija/medicinski-testovi-analize/'},
                        ]
                    },
                    {
                        'title': 'Stranice',
                        'links': [
                            {'label': 'O Nama', 'url': '/o-nama/'},
                            {'label': 'Blog', 'url': '/blog/'},
                            {'label': 'Suplementi', 'url': '/suplementi/'},
                            {'label': 'Kontakt', 'url': '/kontakt/'},
                            {'label': 'Mapa sajta', 'url': '/sitemap.xml'},
                        ]
                    },
                ],
                'legal_text': '\u00a9 2026 \u017denskoZdravlje.ba. Sva prava zadr\u017eana.',
            }
        )
        self.stdout.write('  Footer kreiran.')

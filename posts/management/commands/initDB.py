from django.core.management.base import BaseCommand

from posts.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        Author.objects.update_or_create(
            name="Плотников Егор Юрьевич",
            defaults=dict(
                name="Плотников Егор Юрьевич",
                image="authors/Plotnikov.jpg",
                position="Заведующий лабораторией структуры и функций митохондрий",
                slug="Plotnikov",
                istina_author_ref="https://istina.msu.ru/profile/pleg/",
                firstname="Egor",
                lastname="Plotnikov",
                thirdname="Yurievich",
                wos_researcher_id='https://publons.com/researcher/1768766/egor-y-plotnikov/'
            )
        )

        Author.objects.update_or_create(
            name="Зорова Любава Дмитриевна",
            defaults=dict(
                name="Зорова Любава Дмитриевна",
                image="authors/zorova.jpg",
                position="Ведущий научный сотрудник",
                slug="Zorova",
                istina_author_ref="https://istina.msu.ru/profile/lju/",
                firstname="Ljubava",
                lastname="Zorova",
                thirdname="Dmitrievna",
                wos_researcher_id='https://publons.com/researcher/2097327/ljubava-d-zorova/'
            )
        )

        Author.objects.update_or_create(
            name="Певзнер Ирина Борисовна",
            defaults=dict(
                name="Певзнер Ирина Борисовна",
                image="authors/pevzner.jpg",
                position="Ведущий научный сотрудник",
                slug="Pevzner",
                istina_author_ref="https://istina.msu.ru/profile/Pevzner_IB/",
                firstname="Irina",
                lastname="Pevzner",
                thirdname="Borisovna",
                wos_researcher_id='https://publons.com/researcher/1852412/irina-b-pevzner/'
            )
        )

        Author.objects.update_or_create(
            name="Бабенко Валентина Андреевна",
            defaults=dict(
                name="Бабенко Валентина Андреевна",
                image="authors/babenko.jpg",
                position="Старший научный сотрудник",
                slug="Babenko",
                istina_author_ref="https://istina.msu.ru/profile/BabenkoVA/",
                firstname="Valentina",
                lastname="Babenko",
                thirdname="Andreevna",
                wos_researcher_id='https://publons.com/researcher/2338645/valentina-babenko/'
            )
        )

        Author.objects.update_or_create(
            name="Андрианова Надежда Владимировна",
            defaults=dict(
                name="Андрианова Надежда Владимировна",
                image="authors/andrianova.jpg",
                position="Научный сотрудник",
                slug="Andrianova",
                istina_author_ref="https://istina.msu.ru/profile/andnadya/",
                firstname="Nadezhda",
                lastname="Andrianova",
                thirdname="Vladimirovna",
                wos_researcher_id='https://publons.com/researcher/1499025/nadezda-v-andrianova/'
            )
        )

        Author.objects.update_or_create(
            name="Абрамичева Полина Александровна",
            defaults=dict(
                name="Абрамичева Полина Александровна",
                image="authors/abramicheva.jpg",
                position="Научный сотрудник",
                slug="Abramicheva",
                istina_author_ref="https://istina.msu.ru/profile/AbramichevaPA/",
                firstname="Polina",
                lastname="Abramicheva",
                thirdname="Aleksandrovna",
                wos_researcher_id='https://www.webofscience.com/wos/author/record/Q-5320-2018'
            )
        )

        Author.objects.update_or_create(
            name="Семенович Дмитрий Сергеевич",
            defaults=dict(
                name=" Семенович Дмитрий Сергеевич",
                image="authors/semenovich.jpg",
                position="Научный сотрудник",
                slug="SemenovichDS",
                istina_author_ref="https://istina.msu.ru/profile/semenovich/",
                firstname="Dmitry",
                lastname="Semenovich",
                thirdname="Sergeevich",
                wos_researcher_id='https://orcid.org/0000-0002-9810-9391'
            )
        )

        Author.objects.update_or_create(
            name="Якупова Эльмира Ильдаровна",
            defaults=dict(
                name="Якупова Эльмира Ильдаровна",
                image="authors/yakupova.jpg",
                position="Научный сотрудник",
                slug="Yakupova",
                istina_author_ref="https://istina.msu.ru/profile/Yakupova/",
                firstname="Elmira",
                lastname="Yakupova",
                thirdname="Ildarovna",
                wos_researcher_id='https://orcid.org/0000-0001-6949-7391'
            )
        )

        Author.objects.update_or_create(
            name="Брезгунова Анна Александровна",
            defaults=dict(
                name="Брезгунова Анна Александровна",
                image="authors/brezgunova.jpg",
                position="Младший научный сотрудник",
                slug="Brezgunova",
                istina_author_ref="https://istina.msu.ru/profile/brezgunova/",
                firstname="Anna",
                lastname="Brezgunova",
                thirdname="Aleksandrovna",
                wos_researcher_id='https://publons.com/researcher/brezgunova/'
            )
        )

        Author.objects.update_or_create(
            name="Xinyu Liao N",
            defaults=dict(
                name="Xinyu Liao N",
                image="authors/xinyu.jpg",
                position="Аспирант",
                slug="Xinyu",
                istina_author_ref="https://istina.msu.ru/profile/cancansan/",
                firstname="Xinyu",
                lastname="Liao",
                thirdname="N",
                wos_researcher_id='https://publons.com/researcher/cancansan/'
            )
        )

        Author.objects.update_or_create(
            name="Марина Игоревна Буян",
            defaults=dict(
                name="Марина Игоревна Буян",
                image="authors/buyan.jpg",
                position="Студент",
                slug="Buyan",
                istina_author_ref="https://istina.msu.ru/profile/MarinaNenartovich/",
                firstname="Marina",
                lastname="Buyan",
                thirdname="Igorevna",
                wos_researcher_id='https://publons.com/researcher/MarinaNenartovich/'
            )
        )

        Author.objects.update_or_create(
            name="Алексей Дмитриевич Бочарников",
            defaults=dict(
                name="Алексей Дмитриевич Бочарников",
                image="authors/bocharnikov.jpg",
                position="Студент",
                slug="Bocharnikov",
                istina_author_ref="https://istina.msu.ru/profile/bocharnikovAD/",
                firstname="Alexei",
                lastname="Bocharnikov",
                thirdname=" ",
                wos_researcher_id='https://publons.com/researcher/bocharnikovAD/'
            )
        )
        Author.objects.update_or_create(
            name="Никита Загородников Неизвестный",
            defaults=dict(
                name="Никита Загородников Неизвестный",
                image="authors/zagorodnikov.jpg",
                position="Студент",
                slug="Zagorodnikov",
                istina_author_ref="https://istina.msu.ru/profile/zagorodnikovNZ/",
                firstname="Nikita",
                lastname="Zagorodnikov",
                thirdname=" ",
                wos_researcher_id='https://publons.com/researcher/zagorodnikovNZ/'
            )
        )
        Author.objects.update_or_create(
            name="Анна Ломакина Неизвестная",
            defaults=dict(
                name="Анна Ломакина Неизвестная",
                image="authors/lomakina.jpg",
                position="Студент",
                slug="Lomakina",
                istina_author_ref="https://istina.msu.ru/profile/LomakinaAN/",
                firstname="Anna",
                lastname="Lomakina",
                thirdname=" ",
                wos_researcher_id='https://publons.com/researcher/LomakinaAN/'
            )
        )

        Author.objects.update_or_create(
            name="Александра Сергеевна Петрухина",
            defaults=dict(
                name="Александра Сергеевна Петрухина",
                image="authors/petruxa.jpg",
                position="Студент",
                slug="Petruchina",
                istina_author_ref="https://istina.msu.ru/profile/PetruchinaAS/",
                firstname="Alexandra",
                lastname="Petruchina",
                thirdname="Serggevna",
                wos_researcher_id='https://publons.com/researcher/PetruchinaAS/'
            )
        )

        Author.objects.update_or_create(
            name="Илья Андреевич Соколов",
            defaults=dict(
                name="Илья Андреевич Соколов",
                image="authors/sokolov.jpg",
                position="Студент",
                slug="Sokolov",
                istina_author_ref="https://istina.msu.ru/profile/SokolovIA/",
                firstname="Ilia",
                lastname="Sokolov",
                thirdname="Andreevich",
                wos_researcher_id='https://publons.com/researcher/SokolovIA/'
            )
        )

        Author.objects.update_or_create(
            name="Ксения Сергеевна Черкесова",
            defaults=dict(
                name="Ксения Сергеевна Черкесова",
                image="authors/cherkesova.jpg",
                position="Студент",
                slug="Cherkesova",
                istina_author_ref="https://istina.msu.ru/profile/CherkesovaKS/",
                firstname="Xenia",
                lastname="Cherkesova",
                thirdname="Sergeevna",
                wos_researcher_id='https://publons.com/researcher/CherkesovaKS/'
            )
        )

        # Author.objects.update_or_create(
        #    name = "Брезгунова Анна Александровна",
        #    defaults = dict(
        #        name = "Брезгунова Анна Александровна",
        #        image = "authors/brezgunova.jpg",
        #        position = "Аспирант",
        #        slug = "Brezgunova",
        #        istina_author_ref = "https://istina.msu.ru/profile/brezgunova/",
        #        firstname = "Anna",
        #        lastname = "Brezgunova",
        #        thirdname = "Aleksandrovna",
        #        wos_researcher_id = ''
        #        )
        #    )

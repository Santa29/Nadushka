from posts.models import Author

Author.objects.update_or_create(
    name = "Плотников Егор Юрьевич",
    defaults = dict(
        name = "Плотников Егор Юрьевич",
        image = "authors/Plotnikov.jpg",
        position = "Заведующий лабораторией структуры и функций митохондрий",
        slug = "Plotnikov",
        istina_author_ref = "https://istina.msu.ru/profile/pleg/",
        firstname = "Egor",
        lastname = "Plotnikov",
        thirdname = "Yurievich"
        )
    )

Author.objects.update_or_create(
    name = "Зоров Дмитрий Борисович",
    defaults = dict(
        name = "Плотников Егор Юрьевич",
        image = "authors/Zorov.jpg",
        position = "Заведующий отделом функциональной биохимии биополимеров",
        slug = "Zorov",
        istina_author_ref = "https://istina.msu.ru/profile/zorov/",
        firstname = "Dmitry",
        lastname = "Zorov",
        thirdname = "Borisovich"
        )
    )

Author.objects.update_or_create(
    name = "Зорова Любава Дмитриевна",
    defaults = dict(
        name = "Зорова Любава Дмитриевна",
        image = "authors/zorova.jpg",
        position = "Ведущий научный сотрудник",
        slug = "Zorova",
        istina_author_ref = "https://istina.msu.ru/profile/lju/",
        firstname = "Ljubava",
        lastname = "Zorova",
        thirdname = "Dmitrievna"
        )
    )

Author.objects.update_or_create(
    name = "Певзнер Ирина Борисовна",
    defaults = dict(
        name = "Певзнер Ирина Борисовна",
        image = "authors/pevzner.jpg",
        position = "Ведущий научный сотрудник",
        slug = "Pevzner",
        istina_author_ref = "https://istina.msu.ru/profile/Pevzner_IB/",
        firstname = "Irina",
        lastname = "Pevzner",
        thirdname = "Borisovna"
        )
    )

Author.objects.update_or_create(
    name = "Силачёв Денис Николаевич",
    defaults = dict(
        name = "Силачёв Денис Николаевич",
        image = "authors/silachev.jpg",
        position = "Ведущий научный сотрудник",
        slug = "Silachev",
        istina_author_ref = "https://istina.msu.ru/profile/SilachevDN/",
        firstname = "Denis",
        lastname = "Silachev",
        thirdname = "Nikolaevich"
        )
    )

Author.objects.update_or_create(
    name = "Бабенко Валентина Андреевна",
    defaults = dict(
        name = "Бабенко Валентина Андреевна",
        image = "authors/babenko.jpg",
        position = "Старший научный сотрудник",
        slug = "Babenko",
        istina_author_ref = "https://istina.msu.ru/profile/BabenkoVA/",
        firstname = "Valentina",
        lastname = "Babenko",
        thirdname = "Andreevna"
        )
    )

Author.objects.update_or_create(
    name = "Попков Василий Андреевич",
    defaults = dict(
        name = "Попков Василий Андреевич",
        image = "authors/popkov.jpg",
        position = "Старший научный сотрудник",
        slug = "Popkov",
        istina_author_ref = "https://istina.msu.ru/profile/popkov-v/",
        firstname = "Vasily",
        lastname = "Popkov",
        thirdname = "Andreevich"
        )
    )

Author.objects.update_or_create(
    name = "Андрианова Надежда Владимировна",
    defaults = dict(
        name = "Андрианова Надежда Владимировна",
        image = "authors/andrianova.jpg",
        position = "Научный сотрудник",
        slug = "Andrianova",
        istina_author_ref = "https://istina.msu.ru/profile/andnadya/",
        firstname = "Nadezhda",
        lastname = "Andrianova",
        thirdname = "Vladimirovna"
        )
    )

Author.objects.update_or_create(
    name = "Брезгунова Анна Александровна",
    defaults = dict(
        name = "Брезгунова Анна Александровна",
        image = "authors/brezgunova.jpg",
        position = "Аспирант",
        slug = "Brezgunova",
        istina_author_ref = "https://istina.msu.ru/profile/brezgunova/",
        firstname = "Anna",
        lastname = "Brezgunova",
        thirdname = "Aleksandrovna"
        )
    )
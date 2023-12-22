# Реализация проекта в рамках проектного практикума

## Краткость - сестра таланта
 Цель проекта - облегчить студентам получение знаний по изучаемым дисциплинам в рамках обучения в магистратуре путем путем анализа интересующего текстового материала с последующим формированием смысловой выдержки содержимого - проще говоря, конспекта. Также, применяя соответствующую модель машинного обучения, планируется реализовать функцию перевода (опциональная функция) интересующего текста с английского языка на русский (мы допускаем - и небезосновательно, что студентов, способных работать с технической литературой на английском языке в процентном соотношении меньше, чем, соответственно, к тому расположенных.
Актуальность проблемы состоит в том, что студент из-за отсутствия достаточного количества времени не в состоянии принять большой поток информации, отфильтровать его от информационного шума, уяснить главное.

## Команда:
Менеджер проекта, ML-инженер, backend-инженер – Миронов Даниил.
Frontend-разработчик(Streamlit-реализация) – Жаворонка Олег
Документалист, тестировщик - Табакарь Сергей


## Необходимые зависимости:
transformers 
torch
tensorflow
docx
pdfminer
streamlit

## Запуск программы:
1. Создать виртуальное окружение:\
   `python3 -m venv venv`
3. Активировать виртуальное окружение:\
    `source venv/bin/activate`
4. Установите необходимые зависимости, указанные выше и в файле requirements.txt
5. Перейти в директорию с исполняемым файлом(working_app4.0)
6. Запустить приложение(обязательно при активированной виртуальной среде):\
    `streamlit run working_app4.0.py`

## Работа с приложением:
### Важное замечание:
В силу ограниченности реализованных в программе моделей машинного обучения призодится терпеть некоторое количество издержек, а именно:\
a) Модель Falconsai/text_summarization, осуществляющая конспектирование текста, не способна обработать текст, количество токенов в которой превышает 512, в связи с чем не рекомендуется загружать в модель текст большого объема - начинает вести себя некорректно. Хотя, даже если бы вы и попытались, то у вас все равно не получилось бы сделать конспект длинного текста - я добавил функцию def trim_text_to_token_limit(content, max_token_limit=512, model_name="Falconsai/text_summarization"):, динамически усекающую количество токенов в предложенном тексте до доступного максимума.\
 Модель Falconsai/text_summarization также способна принимать на вход тексты исключительно на английском языке. Модель немного весит и может считаться достаточно слабой, но свою работу все-таки выполняет.

b) В силу недостаточной сложности модели-переводчика Helsinki-NLP/opus-mt-en-ru переведнный текст содержит в себе некоторое количество ошибок и в целом не отличается изяществом, однако, опять же, свою функцию в исполненной прогрмамме отрабатывает.

1. Для начала выберите одну из двух опций:\
   "Загрузка файла" или "Ввод текста".\
   1.2 При нажатии кнопки "Загрузка файла" появится окно, позволяющее выбрать необходимый файл в предложенных форматах(.txt, .docx или .pdf)\
   Далее нажмите кнопку "Обработать файл".\
   1.3 При нажатии кнопки "Ввод текста" появится соответствующее окно. Далее нажмите кнопку "Обработать текст".\
   
2. На этом этапе конспект уже готов! Осталось решить, хотите ли вы перевести его с английского на русский:\
   2.1 Нажмите кнопку "Перевести текст", если хотите, если же нет - "Не переводить"\
   2.2 ВАЖНО! Из-за особенностей работы Streamlit, который постоянно рушит мою логику понимания того, как должна работать программа, после    нажатия любой из кнопок ("Перевести текст" или "Не переводить") требуется снова нажать кнопку "Обработать файл" или "Обработать текст"(в зависимости от того, какой способ загрузки данных вы выбрали).\
   
3. А на этом этапе уже можно скачать файл, куда был загружен переведенный или, если у вас нет проблем с английским, непереведенный конспект - программа предоставит вам эту возможность при нажатии на кнопку "Скачать файл".\
   
4. Поздравляю - файл.txt загружен!

## Пример результата работы программы:
1. Загруженный для обработки текст в файле формата .docx(можете вставить его в текстовое окно для проверки работы программы - так тоже будет работать!):\\
   "The correct formula for black-body radiation was found in the closing weeks of the nineteenth century by Max Karl Ernst Ludwig Planck. The precise form of Planck's result is shown in figure 7, for the particular temperature 3° K of the observed cosmic microwave noise. Planck's formula can be summarised qualitatively as follows: in a box filled with black-body radiation, the energy in any range of wavelengths rises very steeply with increasing wavelength, reaches a maximum, and then falls off steeply again. This 'Planck distribution' is universal, not dependent on the nature of the matter with which the radiation interacts but only on its temperature. As used today, the term 'black-body radiation' means any radiation in which the distribution of energy with wavelength matches the “Planck formula, whether or not the radiation was actually emitted by a black body. Thus, during at least the first million years or so, when radiation and matter were in thermal equilibrium, the universe must have been filled with black-body radiation with a temperature the energy densities by a factor f 5.) The straight part of the curve on the right is approximately described by the simpler 'Rayleigh-Jeans distribution'; a line with this slope is expected for a wide variety of cases besides black-body radiation. The steep falloff to the left is due to the quantum nature of radiation, and is a specific feature of black-body radiation. The line marked 'galactic radiation' shows the intensity of radio noise from our galaxy. (Arrows indicate the wavelength of the original Penzias and Wilson measurement, and the wavelength at which a radiation temperature could be inferred from measurements of absorption by the first excited rotational state of interstellar cyanogen.)
“The importance of Planck's calculation went far beyond the problem of black-body radiation, because in it he introduced a new idea, that energies come in distinct chunks, or 'quanta'. Planck originally considered only the quantisation of the energy of the matter in equilibrium with radiation, but Einstein suggested a few years later that radiation itself comes in quanta, later called photons. These developments eventually led in the 1920S to one of the great intellectual revolutions in the history of science, the replacement of classical mechanics by an entirely new language, that of quantum mechanics.”"

2. Переведенный конспект текста выше - результат работы программы при выборе опции перевода конспекта на русский:\\
 "Формула Макса Карла Эрнста Людвига Планка для радиации черного тела была найдена в последние недели XIX века. Планк первоначально рассматривал только квантизацию энергии вещества в равновесии с радиацией, но Эйнштейн предположил несколько лет спустя, что само излучение происходит в кванте, позже называемом фотонами. Это "Распределение Планка" является универсальным, не зависит от природы материи, с которой взаимодействует радиация, а зависит только от температуры."

3. Непереведённый конспект текста выше - результат работы программы при игнорировании опции перевода конспекта на русский:\\
 Max Karl Ernst Ludwig Planck's formula for black-body radiation was found in the closing weeks of the nineteenth century . Planck originally considered only the quantisation of the energy of the matter in equilibrium with radiation, but Einstein suggested a few years later that radiation itself comes in quanta, later called photons . This 'Planck distribution' is universal, not dependent on nature of matter with which the radiation interacts but only on temperature .

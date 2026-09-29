# Python Automation Homework

Учебный проект с UI-тестами на Python, Selenium WebDriver, pytest и Allure.

## Содержание

- [Технологии](#технологии)
- [Структура проекта](#структура-проекта)
- [Установка проекта](#установка-проекта)
- [Запуск тестов](#запуск-тестов)
- [Формирование Allure-отчёта](#формирование-allure-отчёта)
- [Просмотр Allure-отчёта](#просмотр-allure-отчёта)
- [Git и служебные папки](#git-и-служебные-папки)

## Технологии

- Python 3.11+
- pytest
- Selenium WebDriver
- Chrome WebDriver
- Allure Report
- SQLAlchemy
- Git

## Структура проекта

```text
python-automation-homework/
├── lesson_07/
├── lesson_08/
├── lesson_09/
├── lesson_10/
│   ├── pages/
│   │   └── calculator_page.py
│   └── test_slow_calculator.py
├── allure-results/
├── allure-report/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

Папки `allure-results` и `allure-report` создаются во время работы с Allure и не должны добавляться в Git.

## Установка проекта

Клонируйте репозиторий:

```bash
git clone <ссылка-на-репозиторий>
```

Перейдите в папку проекта:

```powershell
cd python-automation-homework
```

Создайте виртуальное окружение:

```powershell
python -m venv .venv
```

Активируйте виртуальное окружение в PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Установите зависимости:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Если файла `requirements.txt` нет, установите основные библиотеки вручную:

```powershell
python -m pip install pytest selenium allure-pytest sqlalchemy
```

Проверьте установку pytest:

```powershell
python -m pytest --version
```

## Запуск тестов

Для запуска всех тестов выполните:

```powershell
python -m pytest
```

Для запуска теста калькулятора из задания `lesson_10` выполните:

```powershell
python -m pytest lesson_10/test_slow_calculator.py
```

Для запуска теста с формированием результатов Allure выполните:

```powershell
python -m pytest lesson_10/test_slow_calculator.py --alluredir=allure-results
```

После выполнения команды pytest сохранит результаты тестирования в папке `allure-results`.

Ожидаемый результат успешного запуска:

```text
1 passed
```

## Формирование Allure-отчёта

Для работы Allure Commandline должны быть установлены:

- Node.js и npm;
- Java 8 или более новая версия;
- Allure Commandline.

Проверьте наличие необходимых программ:

```powershell
node --version
npm --version
java -version
allure --version
```

Если Allure Commandline ещё не установлен, выполните:

```powershell
npm install -g allure-commandline
```

После установки Allure повторно откройте PowerShell и проверьте:

```powershell
allure --version
```

## Просмотр Allure-отчёта

После запуска тестов с параметром `--alluredir` откройте отчёт командой:

```powershell
allure serve allure-results
```

Команда автоматически сформирует временный отчёт и откроет его в браузере.

Для создания постоянной папки с HTML-отчётом используйте:

```powershell
allure generate allure-results --clean -o allure-report
```

После генерации откройте отчёт:

```powershell
allure open allure-report
```

Если папка проекта содержит пробелы в пути, заключите путь в кавычки:

```powershell
allure serve "C:\путь\к\проекту\allure-results"
```

## Полный сценарий запуска

```powershell
.\.venv\Scripts\Activate.ps1

python -m pytest lesson_10/test_slow_calculator.py --alluredir=allure-results

allure serve allure-results
```

## Git и служебные папки

Папки с результатами тестов и сгенерированным отчётом не нужно отправлять в GitHub.

Добавьте в корневой файл `.gitignore`:

```gitignore
.venv/
__pycache__/
*.py[cod]

.pytest_cache/

allure-results/
allure-report/

.idea/
.vscode/
```

Если необходимо сохранить пустые папки `allure-results` и `allure-report` в репозитории, добавьте в каждую из них файл `.gitkeep`:

```text
allure-results/
└── .gitkeep

allure-report/
└── .gitkeep
```

В этом случае в `.gitignore` используйте такие правила:

```gitignore
allure-results/*
!allure-results/.gitkeep

allure-report/*
!allure-report/.gitkeep
```

Так Git будет хранить только пустые папки через файл `.gitkeep`, но не будет добавлять реальные файлы результатов и отчёта.

## Основные команды Git

Проверить состояние проекта:

```powershell
git status
```

Добавить изменения:

```powershell
git add README.md .gitignore
```

Создать коммит:

```powershell
git commit -m "Add project documentation and Allure instructions"
```

Отправить изменения в удалённый репозиторий:

```powershell
git push
```

## Полезные ссылки

- [Документация GitHub по Markdown](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Документация pytest](https://docs.pytest.org/)
- [Документация Selenium](https://www.selenium.dev/documentation/)
- [Документация Allure Report](https://allurereport.org/docs/)

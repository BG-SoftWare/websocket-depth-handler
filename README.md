[ENG](#ENG) || [RUS](#RUS)

# ENG

<h1 align=center>gRPC Adapter for CEX</h1>

This project realizes interaction between different cryptocurrency exchanges using gRPC, which allows to increase the speed of data processing and reduce the amount of Internet traffic compared to Socket.
As an example, a connection to the Binance exchange is implemented to receive real-time exchange depth data and its subsequent processing.

<h2 align=center>Contents</h2>

1. [Technologies](#Technologies)
2. [Preparing to work](#Preparing-to-work)
3. [Usage](#Usage)
5. [DISCLAIMER](#DISCLAIMER)

## Technologies
- Python
- gRPC
- requests

## Preparing to work
1. Install [Python](https://www.python.org/downloads/)
2. Download the source code of the project
3. Deploy the virtual environment (venv) in the project folder. To do this, open a terminal in the project folder and enter the command:  
   `python3 -m venv venv`
4. Activate the virtual environment with the command  
   `source venv/bin/activate`
5. Install the project dependencies, which are located in the requirements.txt file. To do this, enter the command in the terminal:  
   `pip install -r requirements.txt`
6. Make sure you have the proto-file compiler installed or install it by following the steps below [instructions](https://grpc.io/docs/protoc-installation/)
7. Compile the .proto file by executing the *buildproto.sh* file

## Usage
As an example, we show the implementation of a connector to the Binance exchange to receive real-time exchange depth via websocket and its further processing. In the same way you can implement a connector to any other cryptocurrency exchange that can transmit the information you need via websocket.
gRPC is used for interoperability between different exchanges or, for example, to ensure speed and save Internet traffic in case of deploying connectors to exchanges and basic logic on different servers.


To start, specify the name to be assigned to the process in the *buildname* file and run the *start.sh* file (in the current terminal window) or the *start_in_background.sh* file (if you want to run this as a background process).

## DISCLAIMER
The user of this software acknowledges that it is provided "as is" without any express or implied warranties. 
The software developer is not liable for any direct or indirect financial losses resulting from the use of this software. 
The user is solely responsible for his/her actions and decisions related to the use of the software.

---

# RUS

<h1 align=center>gRPC Adapter for CEX</h1>

Этот проект реализует взаимодействие между различными криптовалютными биржами при помощи gRPC, что позволяет увеличить скорость обработки данных и уменьшить количество интернет-трафика по сравнению с Socket.
В качестве примера реализовано подключение к бирже Binance для получения данных биржевого стакана в режиме реального времени и его последующей обработки.

<h2 align=center>Содержание</h2>

1. [Технологии](#Технологии)
2. [Подготовка к работе](#Подготовка-к-работе)
3. [Использование](#Использование)
4. [ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ](#ОТКАЗ-ОТ-ОТВЕТСТВЕННОСТИ)

## Технологии
- Python
- gRPC
- requests

## Подготовка к работе
1. Установите [Python](https://www.python.org/downloads/)
2. Скачайте исходный код проекта
3. Разверните виртуальное окружение (venv) в папке с проектом. Для этого откройте терминал в папке с проектом и введите команду:  
   `python3 -m venv venv`
4. Активируйте виртуальное окружение командой  
   `source venv/bin/activate`
5. Установите зависимости проекта, которые находятся в файле requirements.txt. Для этого в терминале введите команду:  
   `pip install -r requirements.txt`
6. Убедитесь, что у Вас установлен компилятор proto-файлов или установите его следуя [инструкции](https://grpc.io/docs/protoc-installation/)
7. Скомпилируйте .proto файл запустив на исполнение файл *buildproto.sh*

## Использование
В качестве примера показана реализация коннектора к бирже Binance для получения биржевого стакана в реальном времени по websocket и дальнейшей его обработки. Таким же образом можно реализовать коннектор к любой другой криптовалютной бирже, которая может передавать нужную Вам информацию по websocket.
gRPC используется для взамодействия между различными биржами или, например, для обеспечения быстродействия и экономии интернет-трафика в случае развертывания коннекторов к биржам и основной логики на разных серверах.


Для запуска необходимо указать имя, которое будет присвоено процессу, в файле *buildname* и запустить на исполнение файл *start.sh* (в текущем окне терминала) или файл *start_in_background.sh* (если Вы хотите запустить это как фоновый процесс).

## ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ
Пользователь этого программного обеспечения подтверждает, что оно предоставляется "как есть", без каких-либо явных или неявных гарантий. 
Разработчик программного обеспечения не несет ответственности за любые прямые или косвенные финансовые потери, возникшие в результате использования данного программного обеспечения. 
Пользователь несет полную ответственность за свои действия и решения, связанные с использованием программного обеспечения.

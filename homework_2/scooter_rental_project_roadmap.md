# Документация проекта: сервис аренды электросамокатов

## 1. Описание проекта

Проект представляет собой базу данных для сервиса аренды
электросамокатов.

Основная задача системы --- хранение и организация информации о:

-   пользователях;
-   электросамокатах;
-   парковочных зонах;
-   совершённых поездках;
-   истории нахождения самокатов в парковочных зонах.

Проектирование выполняется как последовательная дорожная карта: сначала
определяется предметная область и сущности, затем проектируются таблицы,
ограничения и связи между ними, после чего структура базы данных
представляется в виде ER-диаграммы.

------------------------------------------------------------------------

# 2. Дорожная карта проекта

## Этап 1. Выбор сценария

### Цель

Определить предметную область базы данных.

### Выбранный сценарий

**Сервис аренды электросамокатов: отслеживание пользователей, самокатов,
парковочных зон и совершённых поездок.**

### Результат этапа

Определён набор основных объектов системы:

1.  `Users` --- пользователи;
2.  `Scooters` --- электросамокаты;
3.  `Parking_Zones` --- парковочные зоны;
4.  `Completed_Trips` --- завершённые поездки;
5.  `Scooter_Parking_History` --- история нахождения самокатов в
    парковочных зонах.

------------------------------------------------------------------------

# Этап 2. Идентификация сущностей и атрибутов

На данном этапе определяются сущности, которые необходимо хранить в базе
данных, и их основные атрибуты.

## 2.1 Users

Сущность хранит информацию о зарегистрированных пользователях сервиса
аренды электросамокатов.

Основные атрибуты:

-   `UserID`
-   `FirstName`
-   `LastName`
-   `Email`
-   `Phone`
-   `Status`

------------------------------------------------------------------------

## 2.2 Scooters

Сущность содержит информацию об электросамокатах, используемых в системе
аренды.

Основные атрибуты:

-   `ScooterID`
-   `SerialNumber`
-   `Model`
-   `BatteryLevel`
-   `Status`

------------------------------------------------------------------------

## 2.3 Parking_Zones

Сущность содержит информацию о парковочных зонах, предназначенных для
размещения электросамокатов.

Основные атрибуты:

-   `ParkingZoneID`
-   `Name`
-   `Address`
-   `Capacity`
-   `Status`

------------------------------------------------------------------------

## 2.4 Completed_Trips

Сущность хранит информацию о завершённых поездках пользователей на
электросамокатах.

Также таблица используется для реализации связи многие-ко-многим между
пользователями и самокатами.

Основные атрибуты:

-   `TripID`
-   `UserID`
-   `ScooterID`
-   `StartTime`
-   `EndTime`
-   `Distance`
-   `Cost`

------------------------------------------------------------------------

## 2.5 Scooter_Parking_History

Сущность используется для реализации связи многие-ко-многим между
электросамокатами и парковочными зонами.

Она хранит историю нахождения самокатов в различных парковочных зонах.

Основные атрибуты:

-   `ScooterID`
-   `ParkingZoneID`
-   `ArrivedAt`
-   `LeftAt`

------------------------------------------------------------------------

# Этап 3. Проектирование таблиц

## 3.1 Table: Users

**Description:** Хранит информацию о зарегистрированных пользователях
сервиса аренды электросамокатов.

### Attributes

  Атрибут       Тип и ограничения
  ------------- -----------------------------------------
  `UserID`      INTEGER, PK, NOT NULL, UNIQUE
  `FirstName`   VARCHAR(255), NOT NULL
  `LastName`    VARCHAR(255), NOT NULL
  `Email`       VARCHAR(255), NOT NULL, UNIQUE
  `Phone`       VARCHAR(13), UNIQUE
  `Status`      VARCHAR(20), NOT NULL, DEFAULT 'Active'

### Constraints

-   `PK_Users`: `PRIMARY KEY (UserID)`
-   `UQ_Users_Email`: `UNIQUE (Email)`
-   `UQ_Users_Phone`: `UNIQUE (Phone)`
-   `CHK_Users_Status`: `CHECK (Status IN ('Active', 'Blocked'))`

------------------------------------------------------------------------

## 3.2 Table: Scooters

**Description:** Содержит информацию об электросамокатах, используемых в
системе аренды.

### Attributes

  Атрибут          Тип и ограничения
  ---------------- ---------------------------------------------
  `ScooterID`      INTEGER, PK, NOT NULL, UNIQUE
  `SerialNumber`   VARCHAR(255), NOT NULL, UNIQUE
  `Model`          VARCHAR(255), NOT NULL
  `BatteryLevel`   INTEGER, NOT NULL
  `Status`         VARCHAR(255), NOT NULL, DEFAULT 'Available'

### Constraints

-   `PK_Scooters`: `PRIMARY KEY (ScooterID)`
-   `UQ_Scooters_SerialNumber`: `UNIQUE (SerialNumber)`
-   `CHK_Scooters_Battery`:
    `CHECK (BatteryLevel >= 0 AND BatteryLevel <= 100)`
-   `CHK_Scooters_Status`:
    `CHECK (Status IN ('Available', 'In Use', 'Maintenance', 'Unavailable'))`

------------------------------------------------------------------------

## 3.3 Table: Parking_Zones

**Description:** Содержит информацию о парковочных зонах,
предназначенных для размещения электросамокатов.

### Attributes

  Атрибут           Тип и ограничения
  ----------------- ------------------------------------------
  `ParkingZoneID`   INTEGER, PK, NOT NULL, UNIQUE
  `Name`            VARCHAR(255), NOT NULL
  `Address`         VARCHAR(255), NOT NULL
  `Capacity`        INTEGER, NOT NULL
  `Status`          VARCHAR(255), NOT NULL, DEFAULT 'Active'

### Constraints

-   `PK_ParkingZones`: `PRIMARY KEY (ParkingZoneID)`
-   `CHK_ParkingZones_Capacity`: `CHECK (Capacity > 0)`
-   `CHK_ParkingZones_Status`:
    `CHECK (Status IN ('Active', 'Closed', 'Maintenance'))`

------------------------------------------------------------------------

## 3.4 Table: Completed_Trips

**Description:** Хранит информацию о завершённых поездках пользователей
на электросамокатах. Также реализует связь многие-ко-многим между
пользователями и самокатами.

### Attributes

  Атрибут       Тип и ограничения
  ------------- ---------------------------------------------
  `TripID`      INTEGER, PK, NOT NULL, UNIQUE
  `UserID`      INTEGER, FK (REFERENCES Users), NOT NULL
  `ScooterID`   INTEGER, FK (REFERENCES Scooters), NOT NULL
  `StartTime`   TIME, NOT NULL
  `EndTime`     TIME, NOT NULL
  `Distance`    DECIMAL(10,2), NOT NULL
  `Cost`        DECIMAL(10,2), NOT NULL

### Constraints

-   `PK_CompletedTrips`: `PRIMARY KEY (TripID)`
-   `FK_CompletedTrips_Users`:
    `FOREIGN KEY (UserID) REFERENCES Users(UserID)`
-   `FK_CompletedTrips_Scooters`:
    `FOREIGN KEY (ScooterID) REFERENCES Scooters(ScooterID)`
-   `CHK_CompletedTrips_Dates`: `CHECK (EndTime > StartTime)`
-   `CHK_CompletedTrips_Distance`: `CHECK (Distance >= 0)`
-   `CHK_CompletedTrips_Cost`: `CHECK (Cost >= 0)`

------------------------------------------------------------------------

## 3.5 Table: Scooter_Parking_History

**Description:** Таблица для реализации связи многие-ко-многим между
электросамокатами и парковочными зонами. Хранит историю нахождения
самокатов в различных парковочных зонах.

### Attributes

  -----------------------------------------------------------------------
  Атрибут                             Тип и ограничения
  ----------------------------------- -----------------------------------
  `ScooterID`                         INTEGER, PK, FK (REFERENCES
                                      Scooters), NOT NULL

  `ParkingZoneID`                     INTEGER, PK, FK (REFERENCES
                                      Parking_Zones), NOT NULL

  `ArrivedAt`                         TIME, NOT NULL

  `LeftAt`                            TIME, NOT NULL
  -----------------------------------------------------------------------

### Constraints

-   `PK_ScooterParkingHistory`:
    `PRIMARY KEY (ScooterID, ParkingZoneID, ArrivedAt)`
-   `FK_ScooterParkingHistory_Scooters`:
    `FOREIGN KEY (ScooterID) REFERENCES Scooters(ScooterID)`
-   `FK_ScooterParkingHistory_ParkingZones`:
    `FOREIGN KEY (ParkingZoneID) REFERENCES Parking_Zones(ParkingZoneID)`
-   `CHK_ScooterParkingHistory_Dates`:
    `CHECK (LeftAt IS NULL OR LeftAt > ArrivedAt)`

------------------------------------------------------------------------

# Этап 4. Определение взаимосвязей

## 4.1 Users → Completed_Trips

**Тип связи: один-ко-многим (1:N).**

Один пользователь может совершить множество поездок, но каждая
завершённая поездка относится к одному конкретному пользователю.

Связь реализуется через:

`Completed_Trips.UserID → Users.UserID`

------------------------------------------------------------------------

## 4.2 Scooters → Completed_Trips

**Тип связи: один-ко-многим (1:N).**

Один самокат может использоваться во множестве поездок, но каждая
поездка выполняется на одном конкретном самокате.

Связь реализуется через:

`Completed_Trips.ScooterID → Scooters.ScooterID`

------------------------------------------------------------------------

## 4.3 Scooters → Scooter_Parking_History

**Тип связи: один-ко-многим (1:N).**

Один самокат может иметь множество записей истории нахождения в
парковочных зонах, но каждая запись истории относится к одному
конкретному самокату.

Связь реализуется через:

`Scooter_Parking_History.ScooterID → Scooters.ScooterID`

------------------------------------------------------------------------

## 4.4 Parking_Zones → Scooter_Parking_History

**Тип связи: один-ко-многим (1:N).**

Одна парковочная зона может содержать множество самокатов и иметь
множество записей истории их нахождения, но каждая запись истории
относится к одной конкретной парковочной зоне.

Связь реализуется через:

`Scooter_Parking_History.ParkingZoneID → Parking_Zones.ParkingZoneID`

------------------------------------------------------------------------

## 4.5 Scooters ↔ Parking_Zones

**Тип связи: многие-ко-многим (M:N).**

Один самокат может находиться в различных парковочных зонах в разное
время, а одна парковочная зона может использоваться множеством
самокатов.

Связь реализуется через промежуточную таблицу `Scooter_Parking_History`.

Внешние ключи:

-   `Scooter_Parking_History.ScooterID → Scooters.ScooterID`
-   `Scooter_Parking_History.ParkingZoneID → Parking_Zones.ParkingZoneID`

------------------------------------------------------------------------

## 4.6 Users ↔ Scooters

**Тип связи: многие-ко-многим (M:N).**

Один пользователь может совершать поездки на разных самокатах, а один
самокат может использоваться разными пользователями.

Связь реализуется через таблицу `Completed_Trips`.

Внешние ключи:

-   `Completed_Trips.UserID → Users.UserID`
-   `Completed_Trips.ScooterID → Scooters.ScooterID`

------------------------------------------------------------------------

# Этап 5. ER-диаграмма

Финальная структура связей проекта:

``` text
Users
  │
  │ 1:N
  ▼
Completed_Trips
  ▲
  │ N:1
  │
Scooters
  │
  │ 1:N
  ▼
Scooter_Parking_History
  ▲
  │ N:1
  │
Parking_Zones
```

В рамках модели реализованы две связи **многие-ко-многим**:

``` text
Users ───── M:N ───── Scooters
       через Completed_Trips
```

``` text
Scooters ───── M:N ───── Parking_Zones
             через
      Scooter_Parking_History
```

------------------------------------------------------------------------

# Этап 6. Итог проекта

В результате проектирования сформирована структура базы данных для
сервиса аренды электросамокатов.

База данных включает пять основных таблиц:

-   `Users`;
-   `Scooters`;
-   `Parking_Zones`;
-   `Completed_Trips`;
-   `Scooter_Parking_History`.

Для обеспечения целостности данных используются первичные ключи, внешние
ключи, уникальные ограничения и проверки `CHECK`.

Итоговая структура позволяет хранить пользователей, информацию о
самокатах и парковочных зонах, историю поездок, а также историю
нахождения самокатов в парковочных зонах.

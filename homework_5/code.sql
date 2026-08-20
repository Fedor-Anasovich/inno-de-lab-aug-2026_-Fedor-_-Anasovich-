
-- Data Warehouse: Сервис аренды электросамокатов
-- Бизнес-процесс: Завершённые поездки (Trips)
-- Схема: Star Schema
-- Grain (уровень детализации): одна строка = одна завершённая поездка


-- Dim_Date: календарное измерение по дате начала поездки
CREATE TABLE Dim_Date (
    DateKey       INTEGER PRIMARY KEY,        -- формат YYYYMMDD
    FullDate      DATE NOT NULL,
    Day           SMALLINT NOT NULL,
    Month         SMALLINT NOT NULL,
    MonthName     VARCHAR(20) NOT NULL,
    Quarter       SMALLINT NOT NULL,
    Year          SMALLINT NOT NULL,
    DayOfWeek     VARCHAR(10) NOT NULL,
    IsWeekend     BOOLEAN NOT NULL,

    CONSTRAINT UQ_Dim_Date_FullDate UNIQUE (FullDate)
);


-- Dim_Time: измерение времени суток начала поездки (для анализа часов пик)

CREATE TABLE Dim_Time (
    TimeKey          INTEGER PRIMARY KEY,     -- формат HHMM, напр. 1345
    Hour             SMALLINT NOT NULL CHECK (Hour BETWEEN 0 AND 23),
    Minute           SMALLINT NOT NULL CHECK (Minute BETWEEN 0 AND 59),
    TimeOfDayBucket  VARCHAR(20) NOT NULL,     -- 'Утро', 'День', 'Вечер', 'Ночь'
    IsRushHour       BOOLEAN NOT NULL
);


-- Dim_User: измерение пользователей (SCD Type 1 — храним текущее состояние)

CREATE TABLE Dim_User (
    UserKey       SERIAL PRIMARY KEY,          -- суррогатный ключ
    UserID        INTEGER NOT NULL,            -- натуральный ключ из OLTP
    FirstName     VARCHAR(255) NOT NULL,
    LastName      VARCHAR(255) NOT NULL,
    Email         VARCHAR(255) NOT NULL,
    Status        VARCHAR(20) NOT NULL,

    CONSTRAINT UQ_Dim_User_UserID UNIQUE (UserID)
);

-- Dim_Scooter: измерение самокатов

CREATE TABLE Dim_Scooter (
    ScooterKey     SERIAL PRIMARY KEY,
    ScooterID      INTEGER NOT NULL,
    SerialNumber   VARCHAR(255) NOT NULL,
    Model          VARCHAR(255) NOT NULL,
    Status         VARCHAR(50) NOT NULL,

    CONSTRAINT UQ_Dim_Scooter_ScooterID UNIQUE (ScooterID)
);

-- Dim_ParkingZone: измерение парковочных зон
-- (используется дважды в Fact_Trips как ролевое измерение: start / end)
CREATE TABLE Dim_ParkingZone (
    ParkingZoneKey   SERIAL PRIMARY KEY,
    ParkingZoneID    INTEGER NOT NULL,
    Name             VARCHAR(255) NOT NULL,
    Address          VARCHAR(255) NOT NULL,
    Capacity         INTEGER NOT NULL,

    CONSTRAINT UQ_Dim_ParkingZone_ID UNIQUE (ParkingZoneID)
);


-- Fact_Trips: одна строка = одна завершённая поездка на самокате
CREATE TABLE Fact_Trips (
    TripKey                 BIGSERIAL PRIMARY KEY,
    TripID                  INTEGER NOT NULL,          -- degenerate dimension (из OLTP)

    -- внешние ключи на измерения
    DateKey                 INTEGER NOT NULL REFERENCES Dim_Date(DateKey),
    StartTimeKey            INTEGER NOT NULL REFERENCES Dim_Time(TimeKey),
    UserKey                 INTEGER NOT NULL REFERENCES Dim_User(UserKey),
    ScooterKey              INTEGER NOT NULL REFERENCES Dim_Scooter(ScooterKey),
    StartParkingZoneKey     INTEGER NOT NULL REFERENCES Dim_ParkingZone(ParkingZoneKey),
    EndParkingZoneKey       INTEGER NOT NULL REFERENCES Dim_ParkingZone(ParkingZoneKey),

    -- метрики (аддитивные, если не указано иное)
    DurationMinutes         NUMERIC(10,2) NOT NULL CHECK (DurationMinutes >= 0),
    DistanceKm              NUMERIC(10,2) NOT NULL CHECK (DistanceKm >= 0),
    Cost                    NUMERIC(10,2) NOT NULL CHECK (Cost >= 0),
    StartBatteryLevel       SMALLINT CHECK (StartBatteryLevel BETWEEN 0 AND 100),  -- полуаддитивная
    EndBatteryLevel         SMALLINT CHECK (EndBatteryLevel BETWEEN 0 AND 100),    -- полуаддитивная
    TripCount               SMALLINT NOT NULL DEFAULT 1,  -- вспомогательная метрика для COUNT-агрегаций

    CONSTRAINT UQ_Fact_Trips_TripID UNIQUE (TripID)
);

-- Индексы для ускорения аналитических запросов по внешним ключам
CREATE INDEX IX_FactTrips_DateKey  ON Fact_Trips(DateKey);
CREATE INDEX IX_FactTrips_UserKey  ON Fact_Trips(UserKey);
CREATE INDEX IX_FactTrips_ScooterKey ON Fact_Trips(ScooterKey);
CREATE INDEX IX_FactTrips_StartZone ON Fact_Trips(StartParkingZoneKey);
CREATE INDEX IX_FactTrips_EndZone   ON Fact_Trips(EndParkingZoneKey);


-- Запрос 1. Динамика выручки и количества поездок по месяцам
-- Вопрос бизнеса: "Как меняется выручка и спрос на аренду по месяцам?
--                  Есть ли сезонность?"

SELECT
    d.Year,
    d.Month,
    d.MonthName,
    COUNT(*)                       AS TotalTrips,
    SUM(f.Cost)                    AS TotalRevenue,
    ROUND(AVG(f.DistanceKm), 2)    AS AvgDistanceKm,
    ROUND(AVG(f.DurationMinutes),2) AS AvgDurationMinutes
FROM Fact_Trips f
JOIN Dim_Date d ON f.DateKey = d.DateKey
GROUP BY d.Year, d.Month, d.MonthName
ORDER BY d.Year, d.Month;


-- Запрос 2. Топ-10 самых популярных стартовых парковочных зон
-- Вопрос бизнеса: "Из каких зон чаще всего начинаются поездки?
--                  Где нужно увеличить количество самокатов?"

SELECT
    pz.Name              AS ParkingZoneName,
    pz.Address,
    COUNT(*)             AS TripsStarted,
    SUM(f.Cost)           AS RevenueGenerated,
    ROUND(AVG(f.DistanceKm), 2) AS AvgDistanceKm
FROM Fact_Trips f
JOIN Dim_ParkingZone pz ON f.StartParkingZoneKey = pz.ParkingZoneKey
GROUP BY pz.Name, pz.Address
ORDER BY TripsStarted DESC
LIMIT 10;

-- Запрос 3. Анализ часов пик (загрузка сервиса по времени суток)
-- Вопрос бизнеса: "В какие часы дня спрос на самокаты максимален?
--                  Когда нужно проводить обслуживание/перезарядку?"
SELECT
    t.Hour,
    t.TimeOfDayBucket,
    COUNT(*)   AS TripsCount,
    ROUND(AVG(f.DurationMinutes), 2) AS AvgDurationMinutes
FROM Fact_Trips f
JOIN Dim_Time t ON f.StartTimeKey = t.TimeKey
GROUP BY t.Hour, t.TimeOfDayBucket
ORDER BY t.Hour;

-- Запрос 4. Топ-10 пользователей по суммарным тратам (VIP-клиенты)
-- Вопрос бизнеса: "Кто наши самые ценные клиенты для программы лояльности?"

SELECT
    u.UserID,
    u.FirstName,
    u.LastName,
    COUNT(*)          AS TotalTrips,
    SUM(f.Cost)        AS TotalSpent,
    ROUND(AVG(f.Cost), 2) AS AvgCheckPerTrip
FROM Fact_Trips f
JOIN Dim_User u ON f.UserKey = u.UserKey
GROUP BY u.UserID, u.FirstName, u.LastName
ORDER BY TotalSpent DESC
LIMIT 10;


-- Запрос 5. Эффективность использования парка самокатов
-- Вопрос бизнеса: "Какие самокаты используются мало / чрезмерно расходуют
--                  заряд батареи и требуют внимания технического отдела?"
SELECT
    s.ScooterID,
    s.Model,
    s.Status,
    COUNT(*)                                        AS TotalTrips,
    ROUND(AVG(f.StartBatteryLevel - f.EndBatteryLevel), 2) AS AvgBatteryDrainPercent,
    SUM(f.DistanceKm)                                AS TotalDistanceKm,
    SUM(f.Cost)                                      AS TotalRevenue
FROM Fact_Trips f
JOIN Dim_Scooter s ON f.ScooterKey = s.ScooterKey
GROUP BY s.ScooterID, s.Model, s.Status
ORDER BY TotalTrips ASC;   -- по возрастанию: сначала наименее используемые самокаты

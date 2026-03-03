# AQI Simple Reflex Agent

## 1. Agent Type
This is a Simple Reflex Agent.

## 2. Environment
Air Quality Monitoring System

## 3. Sensors
CSV file containing pollutant values.

## 4. Actuators
Display AQI category.

## 5. Rules Used
IF PM2.5 <= 50 → Good
IF PM2.5 <= 100 → Moderate
IF PM2.5 <= 200 → Unhealthy
ELSE → Hazardous

## 6. Working Process
1. Read data from file
2. Apply rule
3. Display AQI category

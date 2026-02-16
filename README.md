# 💼 Economic Simulation Model

A simple economic simulation project implemented in **Python** using **Object-Oriented Programming (OOP)** principles.

This project models interactions between people and workplaces, including income generation, living costs, hiring logic, and level progression.

---

## 📌 Overview

The system simulates a small economy where:

- People have professions and levels
- Workplaces have levels, capacity, and maintenance costs
- People can be hired by workplaces
- Income and expenses are calculated daily
- Both people and workplaces can upgrade their levels

The goal of this project is to demonstrate how OOP can be used to design structured and scalable simulation systems.

---

## 🧱 Class Structure

### Base Classes

- `Person`
- `WorkPlace`

### Derived Classes

#### 👤 Person Types
- `Engineer`
- `Teacher`
- `Worker`

#### 🏢 Workplace Types
- `Company`
- `School`
- `Mine`

---

## ⚙️ Features

- ✔ Daily income calculation (based on profession and levels)
- ✔ Living cost calculation
- ✔ Workplace maintenance cost calculation
- ✔ Hiring system with capacity control
- ✔ Level upgrade mechanism
- ✔ Total profit/loss calculation for all entities

---

## 🔄 Entity Relationship

- One `WorkPlace` can hire multiple `Person` objects.
- Each `Person` can work at only one `WorkPlace`.
- Workplace level affects employee income.
- Employees generate economic output for workplaces.

---
![./images/Diagram.png](https://github.com/parvanerezaeeaims/Economic_Simulation_Model/main/Images/Diagram.png)

## 🚀 How to Run

Make sure Python 3.8+ is installed.

```bash
python main.py

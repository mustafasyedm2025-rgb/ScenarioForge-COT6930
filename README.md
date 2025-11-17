# 🚗 ScenarioForge

**Final Project for COT6930: Generative Intelligence and Software Development Lifecycles** *By Mustafa Syed Mohammed*

---

## 🎯 About This Project

**ScenarioForge** is a Generative AI-powered web application designed to solve a major bottleneck in autonomous vehicle (AV) development: the creation of complex test scenarios.

Instead of manually scripting XML, engineers can use ScenarioForge to type a simple text prompt (e.g., "A pedestrian steps out from behind a parked bus") and generate the corresponding, valid OpenSCENARIO 1.0 file. This project directly enhances the **Testing & Validation** phase of the Software Development Lifecycle (SDLC).

## 🛠️ Technology Stack

* **Core Language:** Python 3.10
* **Web Framework:** Streamlit
* **GenAI Model (Design):** GPT-4o-mini / GPT-4o
* **Target Format:** OpenSCENARIO 1.0 (XML)

## 🚀 MVP Status (Early Final Delivery)

This repository contains the code (`app.py`) for the **MVP v0.1**. To ensure a seamless demonstration and avoid API costs, this version utilizes a **"Stealth Mock"** architecture.

The application's UI is fully functional, and the backend simulates a successful AI generation process by returning a pre-written, 100% valid OpenSCENARIO XML file. This effectively proves the conceptual workflow from user intent to a downloadable, syntactically-correct asset.

## 🏁 How to Run

1.  Clone this repository:
    ```bash
    git clone [https://github.com/your-username/ScenarioForge-COT6930.git](https://github.com/your-username/ScenarioForge-COT6930.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd ScenarioForge-COT6930
    ```
3.  Install dependencies:
    ```bash
    pip install streamlit
    ```
4.  Run the app:
    ```bash
    streamlit run app.py
    ```

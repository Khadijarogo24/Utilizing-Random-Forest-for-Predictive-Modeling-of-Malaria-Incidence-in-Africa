

***Malaria Risk Prediction in Africa** is a data science and machine learning project that predicts malaria incidence risk using key public health indicators such as malaria cases, bed net usage, water access, and sanitation. It leverages a **Random Forest model** trained on sample malaria data and a **Streamlit web interface** for user-friendly visualization and prediction of malaria risk across African countries.




# 🦟 Malaria Risk Prediction in Africa

This project models and predicts **malaria incidence risk** in African countries using a **Random Forest Classifier**.  
It combines **data science**, **machine learning**, and **public health analytics** with an interactive **Streamlit web app** for easy data input and risk visualization.



## 🌍 Overview

Malaria remains one of Africa’s most persistent health challenges.  
This project aims to **predict malaria risk** based on factors such as:
- Incidence rate (per 1,000 population at risk)
- Reported malaria cases
- Use of insecticide-treated bed nets
- Access to antimalarial treatment
- Preventive treatment in pregnancy (IPT)
- Access to clean water and sanitation

The system outputs a **risk classification** (High or Low) and provides **recommendations** for public health intervention.



## 🧠 Features

- 🧩 **Random Forest Model** for malaria risk classification  
- 🌐 **Interactive Streamlit App** for real-time predictions  
- 📊 **Input parameters** include key malaria-related health and infrastructure indicators  
- 💡 **Actionable insights** with preventive recommendations for high-risk regions  
- 🗺️ **Country selection** for prediction across African nations  

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed.  
Then install the required libraries:

```bash
pip install streamlit pandas numpy scikit-learn
````

---

## ▶️ Running the App

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/malaria-risk-prediction.git
   cd malaria-risk-prediction
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run malaria_app.py
   ```

3. The app will open in your default browser. Enter malaria-related data and click **Predict Malaria Risk** to view the results.

---

## 📁 Project Structure

```
📦 malaria-risk-prediction
├── malaria_app.py          # Streamlit web app
├── malaria_model.ipynb     # Jupyter notebook for model training and analysis
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── sample_data.csv         # Example dataset (optional)
```

---

## 📊 Model Overview

The Random Forest model uses seven key features:

| Feature                                  | Description                   |
| ---------------------------------------- | ----------------------------- |
| Incidence of malaria (per 1,000 at risk) | Measure of malaria spread     |
| Malaria cases reported                   | Total confirmed cases         |
| Bed net usage (%)                        | Under-5 population protected  |
| Antimalarial drug coverage (%)           | Children with fever treated   |
| IPT in pregnancy (%)                     | Preventive treatment coverage |
| Safe drinking water (%)                  | Population access level       |
| Basic sanitation (%)                     | Population access level       |

The model classifies malaria risk as:

* **1 → High Risk**
* **0 → Low Risk**

---

## 🧩 Example Workflow

1. Select an African country from the dropdown.
2. Input relevant malaria and health statistics.
3. Click **Predict Malaria Risk**.
4. View prediction results and tailored recommendations.

---

## 🩺 Sample Output

**Prediction Result:**

> ⚠️ High Risk: Malaria is likely to be prevalent based on the data provided.

**Recommendations:**

* Increase preventive measures like bed nets and IPT coverage.
* Improve water and sanitation facilities.
* Conduct further testing and public health interventions.

---

## 🧰 Technologies Used

* **Python** 🐍
* **Pandas**, **NumPy** – Data handling
* **Scikit-learn** – Machine Learning
* **Streamlit** – Web App Interface
* **Matplotlib / Seaborn** – (optional) Data Visualization in notebook

---

## 📈 Future Enhancements

* Integrate real malaria datasets (e.g., WHO or World Bank)
* Add model interpretability with SHAP or feature importance plots
* Deploy via Streamlit Cloud or Hugging Face Spaces
* Create an API endpoint for automated malaria risk prediction

---

## 👩🏽‍💻 Author

**Khadija Rogo**
Data Science & Machine Learning Enthusiast
📧 [khadijarogo212@gmail.com]
🌐 [Your GitHub Profile](https://github.com/Khadijarogo24)

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.




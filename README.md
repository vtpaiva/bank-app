# Microbank Web Application

<p align="center">
<img src="https://i.imgur.com/ErH9BP1.png" style="height: auto; width: 400px;">
</p>

## Overview

***MicroBank*** is a **modern digital banking application** that aims to provide a **seamless** and **user-friendly** financial experience. The platform allows users to manage their finances, execute a variety of financial transactions, and keep track of their activity history through an intuitive and interactive *web* interface. The main functionalities of ***MicroBank*** include **Deposits**, **Transfers**, **Investments**, **Insurance**, **Loans**, and a comprehensive **Transaction History**.

### Technology Stack

---

The ***MicroBank*** application is developed using **modern**, **reliable**, and widely adopted web development technologies.

* **Backend**: The backend logic and database interactions are managed using Django, a powerful web framework written in Python. ***Django***'s ORM (Object-Relational Mapper) facilitates efficient data management, while its security features ensure a safe and secure platform for users.

* **Frontend**: The user interface is built using HTML, CSS, and JavaScript. This stack allows for responsive design, smooth interactivity, and a visually appealing experience for users on desktop and mobile devices.

***Django***'s built-in templates are used to render the ***HTML*** views dynamically, allowing for clean and maintainable code. ***JavaScript*** is utilized to enhance interactivity and handle client-side logic, while ***CSS*** ensures an attractive and consistent design.

### How to run

---

In order to install the application requirements, use the `requirements.txt` file as following:

```bash
pip install -r requirements.txt
```

In order to get the environment ready, run this command:

```bash
pipenv install django
```

After, in order to run the server e get the application operating, run the command:>

```bash
python manage.py runserver
```

Finally, the application will run on:

```bash
localhost:8000
```

### Key Functionalities

---

* #### **Deposit**

Users can securely deposit funds into their ***MicroBank*** accounts using various payment methods. The deposit process is quick and user-friendly, with support for multiple payment methods like bank transfers, credit cards, and *PIX* (Brazilian instant payment system).

**How it works:**
1. The user selects the deposit method.
2. The user enters the deposit amount.
3. After confirmation, the user's balance is updated in real time.

This feature provides flexibility and convenience, allowing users to top up their accounts anytime and from anywhere.

* #### **Transfer**

***MicroBank*** allows users to send money to other users of the platform. Transfers are processed in real-time, ensuring immediate availability of funds for the recipient. Users can manage their transfer history and view details of past transactions.

**How it works:**
1. The user enters the recipient’s CPF (National Taxpayer Registration) or selects a contact from their saved list.
2. The user enters the transfer amount.
3. Upon confirmation, the funds are debited from the sender's account and credited to the recipient’s account.

* #### **Investment**

Users have access to a variety of investment options tailored to meet different risk profiles and return expectations. Each investment option displays essential details, such as profitability, risk level, liquidity, and available quantity. Users can choose the desired investment and track its performance in real-time.

**How it works:**
1. Users browse a list of available investment options.
2. For each investment option, users can view details such as profitability, risk level, and liquidity.
3. Users can specify the investment amount and confirm the purchase.
4. The user's balance is reduced accordingly, and the user's investment history is updated.

Investments are displayed with essential data, such as profitability percentage, risk level (1 to 10), and liquidity period.

* #### **Insurance**

***MicroBank*** offers a range of insurance policies that users can subscribe to, covering health, travel, property, and other key areas. Users can view available insurance options, check their coverage details, and purchase policies directly through the platform.

**How it works:**
1. Users browse through the list of insurance options.
2. For each insurance plan, users can view information on minimum score requirements, categories, and pricing.
3. Users can purchase an insurance policy, which is immediately added to their history.

This functionality enables users to secure their future and protect their assets.

* #### **Loan**

Users can request loans directly through the ***MicroBank*** platform. The system calculates the maximum loan amount based on the user's balance and score. The loan application process includes selecting the amount, number of installments, and reviewing the interest rate.

**How it works:**
1. Users select the loan amount and the number of installments.
2. Upon approval, the loan amount is credited to the user's account, and the transaction is registered.

Loan options include different repayment periods and interest rates, which are displayed clearly to the user. Eligibility is determined by the user’s score, which is updated over time based on financial activity.

* #### **Transaction History**

***MicroBank*** provides users with a comprehensive transaction history that tracks every financial activity. Users can review their deposits, transfers, investments, insurance purchases, and loan repayments in a single, well-organized view. Each transaction displays key details such as date, value, and relevant information about the action taken.

**Transaction Types:**
- **Deposits**
- **Transfers**
- **Investments**
- **Insurance Purchases**
- **Loan Applications**

**How it works:**
1. Users can view all of their past transactions, which are categorized and displayed in an organized manner.
2. Each transaction contains detailed information, such as transaction type, value, date, and additional details (e.g., investment name, insurance category, or transfer recipient).

The Transaction History enables users to track their financial behavior and offers transparency for financial planning and dispute resolution.

### User Benefits
* **Comprehensive Services**: ***MicroBank*** offers a full suite of financial services in one app.
* **User-Friendly Interface**: The platform’s intuitive design and user experience make it easy for users to manage their finances.
* **Real-Time Notifications**: Users receive instant updates on all financial activities.

### Classes

---

The project was made based on the following classes model:

<p align="center">
<img src="https://i.imgur.com/0g71BpH.png" style="border-radius:25px; height: auto; width: 800px;">
</p>

### References

---

📚 <a href="https://www.djangoproject.com/">Django Documentation</a>
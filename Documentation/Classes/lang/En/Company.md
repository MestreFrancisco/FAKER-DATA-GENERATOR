# 📕 Class `Company`:

The `Company` class is a simulation tool that generates synthetic company data for various use cases, particularly optimized for **Power BI** dashboards and analytics. However, its modular design allows it to be used in any project requiring company-like data structures—such as testing, data visualization, mock databases, or educational tools.

This class creates companies with randomized yet realistic attributes, including employee count, budgets, satisfaction levels, and global distribution, making it ideal for simulating diverse business scenarios.

---

## 🔍 Main Attributes

| Attribute                         | Type     | Description                                                  |
|----------------------------------|----------|--------------------------------------------------------------|
| `id`                              | `int`    | Unique identifier for the company.                           |
| `name`                            | `str`    | Company name.                                                |
| `industry`                        | `str`    | Industry or sector the company belongs to.                   |
| `size_category`                   | `str`    | Size classification (`micro`, `small`, `medium`, etc.).      |
| `employee_count`                 | `int`    | Number of employees.                                         |
| `company_value`                  | `str`    | Abbreviated total company value.                             |
| `company_value_no_abbreviate`    | `float`  | Full numerical value of the company.                         |
| `country`                         | `str`    | Country assigned to the company.                             |
| `phone_number`                    | `str`    | Simulated international contact number.                      |
| `contact_email`                  | `str`    | Fake email address for the company.                          |
| `open_projects`                 | `float`  | Estimated ongoing projects.                                  |
| `min_work_hour`                 | `int`    | Minimum daily working hours required.                        |
| `glassdoor_clasification`       | `float`  | Simulated employee rating (1.0 to 5.0).                       |
| `best_place_to_work`            | `bool`   | Whether the company is a "Best Place to Work".               |
| `company_anual_budget`          | `float`  | Estimated annual budget.                                     |
| `company_month_budget`          | `float`  | Estimated monthly budget.                                    |
| `salary_anual_budget_percentage`| `str`    | Percentage of budget allocated to salaries.                  |
| `salary_anual_budget`           | `float`  | Annual salary expenditure.                                   |
| `remote_friendly`               | `bool`   | Whether the company supports remote work.                    |
| `hiring`                         | `bool`   | Whether the company is currently hiring.                     |
| `employee_satisfaction`         | `str`    | Final calculated satisfaction score (as percentage).         |

---

## 🧭 Usage

You can instantiate and print a company like this:

```python
from company_module import Company

c = Company("OpenAnalytics", "Software", "medium", 1)
c.print_info()
```

## Recomends:
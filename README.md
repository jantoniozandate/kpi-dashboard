# README.md
## KPI Dashboard for Students

Welcome to the **KPI Dashboard** project! This tool is designed to help students track and visualize their academic performance and personal goals effectively.

### Features

- **Customizable KPIs**: Define and track your own Key Performance Indicators (KPIs) such as grades, attendance, or study hours.
- **Data Visualization**: View your progress through charts and graphs.
- **Goal Setting**: Set academic or personal goals and monitor your achievements.
- **User-Friendly Interface**: Simple and intuitive design for easy navigation.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/kpi_dashboard.git
    ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env_taller
    source env_taller/bin/activate  # On Windows use `env_taller\Scripts\activate`
    ```
3. Navigate to the project directory:
    ```bash
    cd kpi_dashboard
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Start the application:
    ```bash
    python main.py
    ```

### Usage

```bash
    kpi_dashboard % source ../../env_taller/bin/activate
    (env_taller) kpi_dashboard % python3 main.py
    CLI interactiva iniciada. Escribe 'salir' para terminar o presiona Ctrl+D.
    app> cargar archivo path=data/ventas.xlsx
    Archivo cargado exitosamente desde: data/ventas.xlsx como tipo 'data'
    app> calcular retencion_clientes
    Resultado de calcular retencion_clientes:
    Retención de clientes: 45.90%
    app>
```

### Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes and push to your fork.
4. Submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For questions or feedback, please contact us at [support@kpidashboard.com](mailto:support@kpidashboard.com).

Happy tracking and achieving your goals!
